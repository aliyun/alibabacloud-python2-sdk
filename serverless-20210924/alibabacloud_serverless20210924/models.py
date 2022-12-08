# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApplicationRepoSource(TeaModel):
    def __init__(self, owner=None, provider=None, repo=None):
        self.owner = owner  # type: str
        self.provider = provider  # type: str
        self.repo = repo  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplicationRepoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['owner'] = self.owner
        if self.provider is not None:
            result['provider'] = self.provider
        if self.repo is not None:
            result['repo'] = self.repo
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        return self


class ApplicationTrigger(TeaModel):
    def __init__(self, branch=None, commit=None, on=None):
        self.branch = branch  # type: str
        self.commit = commit  # type: str
        self.on = on  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplicationTrigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit is not None:
            result['commit'] = self.commit
        if self.on is not None:
            result['on'] = self.on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        if m.get('on') is not None:
            self.on = m.get('on')
        return self


class Application(TeaModel):
    def __init__(self, auto_deploy=None, created_time=None, description=None, env_vars=None, last_release=None,
                 name=None, output=None, parameters=None, repo_source=None, role_arn=None, template=None, trigger=None,
                 updated_time=None, work_dir=None):
        self.auto_deploy = auto_deploy  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.env_vars = env_vars  # type: dict[str, any]
        self.last_release = last_release  # type: dict[str, any]
        self.name = name  # type: str
        self.output = output  # type: dict[str, any]
        self.parameters = parameters  # type: dict[str, any]
        self.repo_source = repo_source  # type: ApplicationRepoSource
        self.role_arn = role_arn  # type: str
        self.template = template  # type: str
        self.trigger = trigger  # type: ApplicationTrigger
        self.updated_time = updated_time  # type: str
        self.work_dir = work_dir  # type: str

    def validate(self):
        if self.repo_source:
            self.repo_source.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super(Application, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.env_vars is not None:
            result['envVars'] = self.env_vars
        if self.last_release is not None:
            result['lastRelease'] = self.last_release
        if self.name is not None:
            result['name'] = self.name
        if self.output is not None:
            result['output'] = self.output
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.repo_source is not None:
            result['repoSource'] = self.repo_source.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.work_dir is not None:
            result['workDir'] = self.work_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')
        if m.get('lastRelease') is not None:
            self.last_release = m.get('lastRelease')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('repoSource') is not None:
            temp_model = ApplicationRepoSource()
            self.repo_source = temp_model.from_map(m['repoSource'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('trigger') is not None:
            temp_model = ApplicationTrigger()
            self.trigger = temp_model.from_map(m['trigger'])
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('workDir') is not None:
            self.work_dir = m.get('workDir')
        return self


class Condition(TeaModel):
    def __init__(self, expression=None):
        self.expression = expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Condition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['expression'] = self.expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        return self


class Context(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(Context, self).to_map()
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


class ContextSchema(TeaModel):
    def __init__(self, description=None, hint=None, name=None, required=None, type=None):
        self.description = description  # type: str
        self.hint = hint  # type: str
        self.name = name  # type: str
        self.required = required  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContextSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.hint is not None:
            result['hint'] = self.hint
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hint') is not None:
            self.hint = m.get('hint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Environment(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 name=None, spec=None, status=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.name = name  # type: str
        self.spec = spec  # type: EnvironmentSpec
        self.status = status  # type: EnvironmentStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Environment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class EnvironmentRevision(TeaModel):
    def __init__(self, created_time=None, environment_generation=None, environment_name=None, kind=None, spec=None,
                 status=None, uid=None):
        self.created_time = created_time  # type: str
        self.environment_generation = environment_generation  # type: int
        self.environment_name = environment_name  # type: str
        self.kind = kind  # type: str
        self.spec = spec  # type: EnvironmentSpec
        self.status = status  # type: EnvironmentStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(EnvironmentRevision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.environment_generation is not None:
            result['environmentGeneration'] = self.environment_generation
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('environmentGeneration') is not None:
            self.environment_generation = m.get('environmentGeneration')
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('spec') is not None:
            temp_model = EnvironmentSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class EnvironmentSpec(TeaModel):
    def __init__(self, region=None, role_arn=None, template=None, template_variables=None, template_version=None):
        self.region = region  # type: str
        self.role_arn = role_arn  # type: str
        self.template = template  # type: str
        self.template_variables = template_variables  # type: dict[str, any]
        self.template_version = template_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnvironmentSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.template_variables is not None:
            result['templateVariables'] = self.template_variables
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('templateVariables') is not None:
            self.template_variables = m.get('templateVariables')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class EnvironmentStatus(TeaModel):
    def __init__(self, message=None, observed_generation=None, observed_time=None, output=None, phase=None):
        self.message = message  # type: str
        self.observed_generation = observed_generation  # type: int
        self.observed_time = observed_time  # type: str
        self.output = output  # type: dict[str, any]
        self.phase = phase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnvironmentStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        if self.output is not None:
            result['output'] = self.output
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class InputVariable(TeaModel):
    def __init__(self, default_json=None, description=None, name=None, nullable=None, sensitive=None, type=None):
        self.default_json = default_json  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.nullable = nullable  # type: bool
        self.sensitive = sensitive  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InputVariable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_json is not None:
            result['defaultJson'] = self.default_json
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('defaultJson') is not None:
            self.default_json = m.get('defaultJson')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OutputValue(TeaModel):
    def __init__(self, description=None, name=None, sensitive=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.sensitive = sensitive  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OutputValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        return self


class Pipeline(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 labels=None, name=None, resource_version=None, spec=None, status=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.labels = labels  # type: dict[str, str]
        self.name = name  # type: str
        self.resource_version = resource_version  # type: int
        self.spec = spec  # type: PipelineSpec
        self.status = status  # type: PipelineStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Pipeline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PipelineStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PipelineSpec(TeaModel):
    def __init__(self, context=None, template_name=None):
        self.context = context  # type: Context
        self.template_name = template_name  # type: str

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super(PipelineSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class PipelineStatus(TeaModel):
    def __init__(self, phase=None):
        self.phase = phase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PipelineStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class PipelineTemplate(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 labels=None, name=None, resource_version=None, spec=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.labels = labels  # type: dict[str, str]
        self.name = name  # type: str
        self.resource_version = resource_version  # type: int
        self.spec = spec  # type: PipelineTemplateSpec
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(PipelineTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = PipelineTemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PipelineTemplateSpec(TeaModel):
    def __init__(self, context=None, context_schema=None, tasks=None):
        self.context = context  # type: Context
        self.context_schema = context_schema  # type: dict[str, any]
        self.tasks = tasks  # type: list[TaskExec]

    def validate(self):
        if self.context:
            self.context.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PipelineTemplateSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.context_schema is not None:
            result['contextSchema'] = self.context_schema
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('contextSchema') is not None:
            self.context_schema = m.get('contextSchema')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = TaskExec()
                self.tasks.append(temp_model.from_map(k))
        return self


class ReleaseCodeVersion(TeaModel):
    def __init__(self, branch=None, commit=None):
        self.branch = branch  # type: str
        self.commit = commit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseCodeVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit is not None:
            result['commit'] = self.commit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        return self


class Release(TeaModel):
    def __init__(self, app_config=None, code_version=None, created_time=None, description=None, output=None,
                 status=None, version_id=None):
        self.app_config = app_config  # type: dict[str, any]
        self.code_version = code_version  # type: ReleaseCodeVersion
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.output = output  # type: dict[str, any]
        self.status = status  # type: str
        self.version_id = version_id  # type: long

    def validate(self):
        if self.code_version:
            self.code_version.validate()

    def to_map(self):
        _map = super(Release, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_config is not None:
            result['appConfig'] = self.app_config
        if self.code_version is not None:
            result['codeVersion'] = self.code_version.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.output is not None:
            result['output'] = self.output
        if self.status is not None:
            result['status'] = self.status
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appConfig') is not None:
            self.app_config = m.get('appConfig')
        if m.get('codeVersion') is not None:
            temp_model = ReleaseCodeVersion()
            self.code_version = temp_model.from_map(m['codeVersion'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class RepoSource(TeaModel):
    def __init__(self, owner=None, provider=None, repo=None):
        self.owner = owner  # type: str
        self.provider = provider  # type: str
        self.repo = repo  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RepoSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['owner'] = self.owner
        if self.provider is not None:
            result['provider'] = self.provider
        if self.repo is not None:
            result['repo'] = self.repo
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        return self


class RunAfter(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunAfter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class Service(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 name=None, spec=None, status=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.name = name  # type: str
        self.spec = spec  # type: ServiceSpec
        self.status = status  # type: ServiceStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Service, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = ServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ServiceStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceRevision(TeaModel):
    def __init__(self, created_time=None, kind=None, service_generation=None, service_name=None, spec=None,
                 status=None, uid=None):
        self.created_time = created_time  # type: str
        self.kind = kind  # type: str
        self.service_generation = service_generation  # type: int
        self.service_name = service_name  # type: str
        self.spec = spec  # type: ServiceSpec
        self.status = status  # type: EnvironmentStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(ServiceRevision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.kind is not None:
            result['kind'] = self.kind
        if self.service_generation is not None:
            result['serviceGeneration'] = self.service_generation
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('serviceGeneration') is not None:
            self.service_generation = m.get('serviceGeneration')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('spec') is not None:
            temp_model = ServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = EnvironmentStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ServiceSpec(TeaModel):
    def __init__(self, environment=None, role_arn=None, template=None, template_variables=None,
                 template_version=None):
        self.environment = environment  # type: str
        self.role_arn = role_arn  # type: str
        self.template = template  # type: str
        self.template_variables = template_variables  # type: dict[str, any]
        self.template_version = template_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ServiceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['environment'] = self.environment
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.template_variables is not None:
            result['templateVariables'] = self.template_variables
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('templateVariables') is not None:
            self.template_variables = m.get('templateVariables')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class ServiceStatus(TeaModel):
    def __init__(self, message=None, observed_generation=None, observed_time=None, output=None, phase=None):
        self.message = message  # type: str
        self.observed_generation = observed_generation  # type: int
        self.observed_time = observed_time  # type: str
        self.output = output  # type: dict[str, any]
        self.phase = phase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ServiceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        if self.output is not None:
            result['output'] = self.output
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class Status(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(Status, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StsCredentials(TeaModel):
    def __init__(self, access_key_id=None, expiration_time=None, kind=None, secret_access_key=None, token=None):
        self.access_key_id = access_key_id  # type: str
        self.expiration_time = expiration_time  # type: str
        self.kind = kind  # type: str
        self.secret_access_key = secret_access_key  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StsCredentials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.kind is not None:
            result['kind'] = self.kind
        if self.secret_access_key is not None:
            result['secretAccessKey'] = self.secret_access_key
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('secretAccessKey') is not None:
            self.secret_access_key = m.get('secretAccessKey')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class Task(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 labels=None, name=None, resource_version=None, spec=None, status=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.labels = labels  # type: dict[str, str]
        self.name = name  # type: str
        self.resource_version = resource_version  # type: int
        self.spec = spec  # type: TaskSpec
        self.status = status  # type: TaskStatus
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Task, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = TaskSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TaskStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TaskExec(TeaModel):
    def __init__(self, context=None, name=None, run_afters=None, task_template=None):
        self.context = context  # type: Context
        self.name = name  # type: str
        self.run_afters = run_afters  # type: list[RunAfter]
        self.task_template = task_template  # type: str

    def validate(self):
        if self.context:
            self.context.validate()
        if self.run_afters:
            for k in self.run_afters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskExec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['runAfters'] = []
        if self.run_afters is not None:
            for k in self.run_afters:
                result['runAfters'].append(k.to_map() if k else None)
        if self.task_template is not None:
            result['taskTemplate'] = self.task_template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.run_afters = []
        if m.get('runAfters') is not None:
            for k in m.get('runAfters'):
                temp_model = RunAfter()
                self.run_afters.append(temp_model.from_map(k))
        if m.get('taskTemplate') is not None:
            self.task_template = m.get('taskTemplate')
        return self


class TaskSpec(TeaModel):
    def __init__(self, context=None, template_name=None):
        self.context = context  # type: Context
        self.template_name = template_name  # type: str

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super(TaskSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class TaskStatus(TeaModel):
    def __init__(self, execution_details=None, phase=None, status_generation=None):
        self.execution_details = execution_details  # type: list[str]
        self.phase = phase  # type: str
        self.status_generation = status_generation  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details
        if self.phase is not None:
            result['phase'] = self.phase
        if self.status_generation is not None:
            result['statusGeneration'] = self.status_generation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('executionDetails') is not None:
            self.execution_details = m.get('executionDetails')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('statusGeneration') is not None:
            self.status_generation = m.get('statusGeneration')
        return self


class TaskTemplate(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 labels=None, name=None, resource_version=None, spec=None, uid=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.labels = labels  # type: dict[str, str]
        self.name = name  # type: str
        self.resource_version = resource_version  # type: int
        self.spec = spec  # type: TaskTemplateSpec
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(TaskTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('spec') is not None:
            temp_model = TaskTemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TaskTemplateSpec(TeaModel):
    def __init__(self, context=None, context_schema=None, description=None, execute_condition=None, worker=None):
        self.context = context  # type: Context
        self.context_schema = context_schema  # type: dict[str, any]
        self.description = description  # type: str
        self.execute_condition = execute_condition  # type: Condition
        self.worker = worker  # type: TaskWorker

    def validate(self):
        if self.context:
            self.context.validate()
        if self.execute_condition:
            self.execute_condition.validate()
        if self.worker:
            self.worker.validate()

    def to_map(self):
        _map = super(TaskTemplateSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.context_schema is not None:
            result['contextSchema'] = self.context_schema
        if self.description is not None:
            result['description'] = self.description
        if self.execute_condition is not None:
            result['executeCondition'] = self.execute_condition.to_map()
        if self.worker is not None:
            result['worker'] = self.worker.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = Context()
            self.context = temp_model.from_map(m['context'])
        if m.get('contextSchema') is not None:
            self.context_schema = m.get('contextSchema')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executeCondition') is not None:
            temp_model = Condition()
            self.execute_condition = temp_model.from_map(m['executeCondition'])
        if m.get('worker') is not None:
            temp_model = TaskWorker()
            self.worker = temp_model.from_map(m['worker'])
        return self


class TaskWorker(TeaModel):
    def __init__(self, preset_worker=None):
        self.preset_worker = preset_worker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskWorker, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preset_worker is not None:
            result['presetWorker'] = self.preset_worker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('presetWorker') is not None:
            self.preset_worker = m.get('presetWorker')
        return self


class Template(TeaModel):
    def __init__(self, created_time=None, deletion_time=None, description=None, generation=None, kind=None,
                 name=None, spec=None, status=None, uid=None, version=None):
        self.created_time = created_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.description = description  # type: str
        self.generation = generation  # type: int
        self.kind = kind  # type: str
        self.name = name  # type: str
        self.spec = spec  # type: TemplateSpec
        self.status = status  # type: TemplateStatus
        self.uid = uid  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Template, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.deletion_time is not None:
            result['deletionTime'] = self.deletion_time
        if self.description is not None:
            result['description'] = self.description
        if self.generation is not None:
            result['generation'] = self.generation
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('deletionTime') is not None:
            self.deletion_time = m.get('deletionTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = TemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TemplateStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class TemplateRevision(TeaModel):
    def __init__(self, created_time=None, kind=None, spec=None, status=None, template_generation=None,
                 template_name=None, template_version=None, uid=None):
        self.created_time = created_time  # type: str
        self.kind = kind  # type: str
        self.spec = spec  # type: TemplateSpec
        self.status = status  # type: TemplateStatus
        self.template_generation = template_generation  # type: int
        self.template_name = template_name  # type: str
        self.template_version = template_version  # type: int
        self.uid = uid  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(TemplateRevision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.kind is not None:
            result['kind'] = self.kind
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.template_generation is not None:
            result['templateGeneration'] = self.template_generation
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('spec') is not None:
            temp_model = TemplateSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = TemplateStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('templateGeneration') is not None:
            self.template_generation = m.get('templateGeneration')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class TemplateSpec(TeaModel):
    def __init__(self, content=None, content_type=None, ram_policy=None, type=None):
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        self.ram_policy = ram_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TemplateSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.ram_policy is not None:
            result['ramPolicy'] = self.ram_policy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('ramPolicy') is not None:
            self.ram_policy = m.get('ramPolicy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TemplateStatus(TeaModel):
    def __init__(self, message=None, observed_generation=None, observed_time=None, outputs=None, phase=None,
                 variables=None):
        self.message = message  # type: str
        self.observed_generation = observed_generation  # type: int
        self.observed_time = observed_time  # type: str
        self.outputs = outputs  # type: list[OutputValue]
        self.phase = phase  # type: str
        self.variables = variables  # type: list[InputVariable]

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.observed_time is not None:
            result['observedTime'] = self.observed_time
        result['outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['outputs'].append(k.to_map() if k else None)
        if self.phase is not None:
            result['phase'] = self.phase
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('observedTime') is not None:
            self.observed_time = m.get('observedTime')
        self.outputs = []
        if m.get('outputs') is not None:
            for k in m.get('outputs'):
                temp_model = OutputValue()
                self.outputs.append(temp_model.from_map(k))
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = InputVariable()
                self.variables.append(temp_model.from_map(k))
        return self


class TriggerConfig(TeaModel):
    def __init__(self, branch=None, commit=None, on=None):
        self.branch = branch  # type: str
        self.commit = commit  # type: str
        self.on = on  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commit is not None:
            result['commit'] = self.commit
        if self.on is not None:
            result['on'] = self.on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commit') is not None:
            self.commit = m.get('commit')
        if m.get('on') is not None:
            self.on = m.get('on')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, auto_deploy=None, description=None, env_vars=None, name=None, parameters=None,
                 repo_source=None, role_arn=None, template=None, trigger=None):
        self.auto_deploy = auto_deploy  # type: bool
        self.description = description  # type: str
        self.env_vars = env_vars  # type: dict[str, str]
        self.name = name  # type: str
        self.parameters = parameters  # type: dict[str, str]
        self.repo_source = repo_source  # type: RepoSource
        self.role_arn = role_arn  # type: str
        self.template = template  # type: str
        self.trigger = trigger  # type: TriggerConfig

    def validate(self):
        if self.repo_source:
            self.repo_source.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.description is not None:
            result['description'] = self.description
        if self.env_vars is not None:
            result['envVars'] = self.env_vars
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.repo_source is not None:
            result['repoSource'] = self.repo_source.to_map()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.template is not None:
            result['template'] = self.template
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('repoSource') is not None:
            temp_model = RepoSource()
            self.repo_source = temp_model.from_map(m['repoSource'])
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('trigger') is not None:
            temp_model = TriggerConfig()
            self.trigger = temp_model.from_map(m['trigger'])
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Application

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Pipeline

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Pipeline

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTemplateRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: PipelineTemplate

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PipelineTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelineTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReleaseRequest(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReleaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateReleaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Release

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReleaseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Release()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Task

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskTemplateRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: TaskTemplate

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(DeleteApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteEnvironmentResponse, self).to_map()
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


class DeletePipelineTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelineTemplateResponseBody, self).to_map()
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


class DeletePipelineTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePipelineTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePipelineTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePipelineTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTaskTemplateResponseBody, self).to_map()
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


class DeleteTaskTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTaskTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTaskTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Status

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Status()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Application

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Environment

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Pipeline

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PipelineTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReleaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Release

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReleaseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Release()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Service

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Template

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Template()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentRevisionsRequest(TeaModel):
    def __init__(self, environment_name=None):
        self.environment_name = environment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentRevisionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        return self


class ListEnvironmentRevisionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[EnvironmentRevision]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentRevisionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = EnvironmentRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Environment]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Environment()
                self.body.append(temp_model.from_map(k))
        return self


class ListPipelineTemplatesRequest(TeaModel):
    def __init__(self, label_selector=None):
        self.label_selector = label_selector  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListPipelineTemplatesShrinkRequest(TeaModel):
    def __init__(self, label_selector_shrink=None):
        self.label_selector_shrink = label_selector_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineTemplatesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListPipelineTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[PipelineTemplate]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = PipelineTemplate()
                self.body.append(temp_model.from_map(k))
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(self, label_selector=None):
        self.label_selector = label_selector  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListPipelinesShrinkRequest(TeaModel):
    def __init__(self, label_selector_shrink=None):
        self.label_selector_shrink = label_selector_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Pipeline]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Pipeline()
                self.body.append(temp_model.from_map(k))
        return self


class ListServiceRevisionsRequest(TeaModel):
    def __init__(self, service_name=None):
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceRevisionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListServiceRevisionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[ServiceRevision]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceRevisionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ServiceRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Service]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Service()
                self.body.append(temp_model.from_map(k))
        return self


class ListTaskTemplatesRequest(TeaModel):
    def __init__(self, label_selector=None):
        self.label_selector = label_selector  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListTaskTemplatesShrinkRequest(TeaModel):
    def __init__(self, label_selector_shrink=None):
        self.label_selector_shrink = label_selector_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskTemplatesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListTaskTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[TaskTemplate]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaskTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = TaskTemplate()
                self.body.append(temp_model.from_map(k))
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, label_selector=None):
        self.label_selector = label_selector  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(self, label_selector_shrink=None):
        self.label_selector_shrink = label_selector_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector_shrink is not None:
            result['labelSelector'] = self.label_selector_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector_shrink = m.get('labelSelector')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Task]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Task()
                self.body.append(temp_model.from_map(k))
        return self


class ListTemplateRevisionsRequest(TeaModel):
    def __init__(self, template_name=None, template_version=None):
        self.template_name = template_name  # type: str
        self.template_version = template_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplateRevisionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_version is not None:
            result['templateVersion'] = self.template_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')
        return self


class ListTemplateRevisionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[TemplateRevision]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplateRevisionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = TemplateRevision()
                self.body.append(temp_model.from_map(k))
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
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


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Template]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Template()
                self.body.append(temp_model.from_map(k))
        return self


class PutEnvironmentRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Environment

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Environment

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Environment()
            self.body = temp_model.from_map(m['body'])
        return self


class PutPipelineStatusRequest(TeaModel):
    def __init__(self, body=None, force=None):
        self.body = body  # type: Pipeline
        self.force = force  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutPipelineStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutPipelineStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Pipeline

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutPipelineStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class PutPipelineTemplateRequest(TeaModel):
    def __init__(self, body=None, force=None):
        self.body = body  # type: PipelineTemplate
        self.force = force  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutPipelineTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutPipelineTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PipelineTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutPipelineTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PipelineTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class PutServiceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Service

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class PutServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Service

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTaskStatusRequest(TeaModel):
    def __init__(self, body=None, force=None):
        self.body = body  # type: Task
        self.force = force  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTaskTemplateRequest(TeaModel):
    def __init__(self, body=None, force=None):
        self.body = body  # type: TaskTemplate
        self.force = force  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTaskTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class PutTaskTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskTemplate

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTaskTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TaskTemplate()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTemplateRequest(TeaModel):
    def __init__(self, body=None, version=None):
        self.body = body  # type: Template
        self.version = version  # type: int

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Template()
            self.body = temp_model.from_map(m['body'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PutTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Template

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Template()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPipelineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Pipeline

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartPipelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Pipeline()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Task

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Task()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Application

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Application

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Application()
            self.body = temp_model.from_map(m['body'])
        return self


