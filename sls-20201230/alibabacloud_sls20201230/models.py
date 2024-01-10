# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConsumerGroup(TeaModel):
    def __init__(self, name=None, order=None, timeout=None):
        self.name = name  # type: str
        self.order = order  # type: bool
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConsumerGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class EncryptConf(TeaModel):
    def __init__(self, enable=None, encrypt_type=None, user_cmk_info=None):
        self.enable = enable  # type: bool
        self.encrypt_type = encrypt_type  # type: str
        self.user_cmk_info = user_cmk_info  # type: EncryptUserCmkConf

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        _map = super(EncryptConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.encrypt_type is not None:
            result['encrypt_type'] = self.encrypt_type
        if self.user_cmk_info is not None:
            result['user_cmk_info'] = self.user_cmk_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('encrypt_type') is not None:
            self.encrypt_type = m.get('encrypt_type')
        if m.get('user_cmk_info') is not None:
            temp_model = EncryptUserCmkConf()
            self.user_cmk_info = temp_model.from_map(m['user_cmk_info'])
        return self


class EncryptUserCmkConf(TeaModel):
    def __init__(self, arn=None, cmk_key_id=None, region_id=None):
        self.arn = arn  # type: str
        self.cmk_key_id = cmk_key_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptUserCmkConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.cmk_key_id is not None:
            result['cmk_key_id'] = self.cmk_key_id
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('cmk_key_id') is not None:
            self.cmk_key_id = m.get('cmk_key_id')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class Histogram(TeaModel):
    def __init__(self, count=None, from_=None, progress=None, to=None):
        self.count = count  # type: long
        self.from_ = from_  # type: int
        self.progress = progress  # type: str
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Histogram, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.from_ is not None:
            result['from'] = self.from_
        if self.progress is not None:
            result['progress'] = self.progress
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class LogContent(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogContent, self).to_map()
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


class LogGroup(TeaModel):
    def __init__(self, log_tags=None, logs=None, source=None, topic=None):
        self.log_tags = log_tags  # type: list[LogTag]
        self.logs = logs  # type: list[LogItem]
        self.source = source  # type: str
        self.topic = topic  # type: str

    def validate(self):
        if self.log_tags:
            for k in self.log_tags:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LogGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogTags'] = []
        if self.log_tags is not None:
            for k in self.log_tags:
                result['LogTags'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.source is not None:
            result['Source'] = self.source
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_tags = []
        if m.get('LogTags') is not None:
            for k in m.get('LogTags'):
                temp_model = LogTag()
                self.log_tags.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = LogItem()
                self.logs.append(temp_model.from_map(k))
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class LogItem(TeaModel):
    def __init__(self, contents=None, time=None):
        self.contents = contents  # type: list[LogContent]
        self.time = time  # type: int

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LogItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = LogContent()
                self.contents.append(temp_model.from_map(k))
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class LogTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogTag, self).to_map()
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


class LogtailConfigOutputDetail(TeaModel):
    def __init__(self, endpoint=None, logstore_name=None, region=None):
        self.endpoint = endpoint  # type: str
        self.logstore_name = logstore_name  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogtailConfigOutputDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class LogtailConfig(TeaModel):
    def __init__(self, config_name=None, create_time=None, input_detail=None, input_type=None,
                 last_modify_time=None, log_sample=None, output_detail=None, output_type=None):
        self.config_name = config_name  # type: str
        self.create_time = create_time  # type: long
        self.input_detail = input_detail  # type: dict[str, any]
        self.input_type = input_type  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.log_sample = log_sample  # type: str
        self.output_detail = output_detail  # type: LogtailConfigOutputDetail
        self.output_type = output_type  # type: str

    def validate(self):
        if self.output_detail:
            self.output_detail.validate()

    def to_map(self):
        _map = super(LogtailConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.input_detail is not None:
            result['inputDetail'] = self.input_detail
        if self.input_type is not None:
            result['inputType'] = self.input_type
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.output_detail is not None:
            result['outputDetail'] = self.output_detail.to_map()
        if self.output_type is not None:
            result['outputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('inputDetail') is not None:
            self.input_detail = m.get('inputDetail')
        if m.get('inputType') is not None:
            self.input_type = m.get('inputType')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('outputDetail') is not None:
            temp_model = LogtailConfigOutputDetail()
            self.output_detail = temp_model.from_map(m['outputDetail'])
        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')
        return self


class LogtailPipelineConfig(TeaModel):
    def __init__(self, aggregators=None, config_name=None, create_time=None, flushers=None, global_=None,
                 inputs=None, last_modify_time=None, log_sample=None, processors=None):
        self.aggregators = aggregators  # type: list[dict[str, any]]
        self.config_name = config_name  # type: str
        self.create_time = create_time  # type: long
        self.flushers = flushers  # type: list[dict[str, any]]
        self.global_ = global_  # type: dict[str, any]
        self.inputs = inputs  # type: list[dict[str, any]]
        self.last_modify_time = last_modify_time  # type: long
        self.log_sample = log_sample  # type: str
        self.processors = processors  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogtailPipelineConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class MLDataParam(TeaModel):
    def __init__(self, annotationdata_id=None, annotations=None, config=None, create_time=None, data_hash=None,
                 dataset_id=None, last_modify_time=None, predictions=None, value=None, value_type=None):
        self.annotationdata_id = annotationdata_id  # type: str
        self.annotations = annotations  # type: dict[str, MLDataParamAnnotationsValue]
        self.config = config  # type: dict[str, str]
        self.create_time = create_time  # type: long
        self.data_hash = data_hash  # type: str
        self.dataset_id = dataset_id  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.predictions = predictions  # type: dict[str, MLDataParamPredictionsValue]
        self.value = value  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        if self.annotations:
            for v in self.annotations.values():
                if v:
                    v.validate()
        if self.predictions:
            for v in self.predictions.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(MLDataParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id
        result['annotations'] = {}
        if self.annotations is not None:
            for k, v in self.annotations.items():
                result['annotations'][k] = v.to_map()
        if self.config is not None:
            result['config'] = self.config
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_hash is not None:
            result['dataHash'] = self.data_hash
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        result['predictions'] = {}
        if self.predictions is not None:
            for k, v in self.predictions.items():
                result['predictions'][k] = v.to_map()
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')
        self.annotations = {}
        if m.get('annotations') is not None:
            for k, v in m.get('annotations').items():
                temp_model = MLDataParamAnnotationsValue()
                self.annotations[k] = temp_model.from_map(v)
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataHash') is not None:
            self.data_hash = m.get('dataHash')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        self.predictions = {}
        if m.get('predictions') is not None:
            for k, v in m.get('predictions').items():
                temp_model = MLDataParamPredictionsValue()
                self.predictions[k] = temp_model.from_map(v)
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class MLDataSetParam(TeaModel):
    def __init__(self, create_by=None, create_time=None, data_type=None, dataset_id=None, description=None,
                 label_id=None, last_modify_time=None, name=None, setting_type=None):
        self.create_by = create_by  # type: str
        self.create_time = create_time  # type: long
        self.data_type = data_type  # type: str
        self.dataset_id = dataset_id  # type: str
        self.description = description  # type: str
        self.label_id = label_id  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.name = name  # type: str
        self.setting_type = setting_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLDataSetParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_by is not None:
            result['createBy'] = self.create_by
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.description is not None:
            result['description'] = self.description
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['name'] = self.name
        if self.setting_type is not None:
            result['settingType'] = self.setting_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createBy') is not None:
            self.create_by = m.get('createBy')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('settingType') is not None:
            self.setting_type = m.get('settingType')
        return self


class MLLabelParamSettings(TeaModel):
    def __init__(self, config=None, mode=None, type=None, version=None):
        self.config = config  # type: str
        self.mode = mode  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLLabelParamSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.mode is not None:
            result['mode'] = self.mode
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class MLLabelParam(TeaModel):
    def __init__(self, create_time=None, description=None, label_id=None, last_modify_time=None, name=None,
                 settings=None, type=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.label_id = label_id  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.name = name  # type: str
        self.settings = settings  # type: list[MLLabelParamSettings]
        self.type = type  # type: str

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MLLabelParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['name'] = self.name
        result['settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['settings'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.settings = []
        if m.get('settings') is not None:
            for k in m.get('settings'):
                temp_model = MLLabelParamSettings()
                self.settings.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MLServiceAnalysisParam(TeaModel):
    def __init__(self, input=None, parameter=None):
        self.input = input  # type: list[dict[str, str]]
        self.parameter = parameter  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLServiceAnalysisParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.parameter is not None:
            result['parameter'] = self.parameter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        return self


class MLServiceParamModel(TeaModel):
    def __init__(self, model_resource_id=None, model_resource_type=None):
        self.model_resource_id = model_resource_id  # type: str
        self.model_resource_type = model_resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLServiceParamModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_resource_id is not None:
            result['modelResourceId'] = self.model_resource_id
        if self.model_resource_type is not None:
            result['modelResourceType'] = self.model_resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('modelResourceId') is not None:
            self.model_resource_id = m.get('modelResourceId')
        if m.get('modelResourceType') is not None:
            self.model_resource_type = m.get('modelResourceType')
        return self


class MLServiceParamResource(TeaModel):
    def __init__(self, cpu_limit=None, gpu=None, memory_limit=None, replica=None):
        self.cpu_limit = cpu_limit  # type: int
        self.gpu = gpu  # type: int
        self.memory_limit = memory_limit  # type: int
        self.replica = replica  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLServiceParamResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.gpu is not None:
            result['gpu'] = self.gpu
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.replica is not None:
            result['replica'] = self.replica
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        return self


class MLServiceParam(TeaModel):
    def __init__(self, description=None, model=None, name=None, resource=None, service_type=None, status=None,
                 update_timestamp=None):
        self.description = description  # type: str
        self.model = model  # type: MLServiceParamModel
        self.name = name  # type: str
        self.resource = resource  # type: MLServiceParamResource
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.update_timestamp = update_timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super(MLServiceParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.model is not None:
            result['model'] = self.model.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('model') is not None:
            temp_model = MLServiceParamModel()
            self.model = temp_model.from_map(m['model'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resource') is not None:
            temp_model = MLServiceParamResource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class SavedSearch(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        self.display_name = display_name  # type: str
        self.logstore = logstore  # type: str
        self.savedsearch_name = savedsearch_name  # type: str
        self.search_query = search_query  # type: str
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SavedSearch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class Ticket(TeaModel):
    def __init__(self, caller_uid=None, create_date=None, expiration_time=None, expire_date=None, extra=None,
                 name=None, number=None, ticket=None, ticket_id=None, used_number=None, valid=None):
        self.caller_uid = caller_uid  # type: long
        self.create_date = create_date  # type: str
        self.expiration_time = expiration_time  # type: long
        self.expire_date = expire_date  # type: str
        self.extra = extra  # type: str
        self.name = name  # type: str
        self.number = number  # type: int
        self.ticket = ticket  # type: str
        self.ticket_id = ticket_id  # type: str
        self.used_number = used_number  # type: int
        self.valid = valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(Ticket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.create_date is not None:
            result['createDate'] = self.create_date
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.extra is not None:
            result['extra'] = self.extra
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.ticket is not None:
            result['ticket'] = self.ticket
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        if self.used_number is not None:
            result['usedNumber'] = self.used_number
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        if m.get('usedNumber') is not None:
            self.used_number = m.get('usedNumber')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class Chart(TeaModel):
    def __init__(self, action=None, display=None, search=None, title=None, type=None):
        self.action = action  # type: dict[str, any]
        self.display = display  # type: dict[str, any]
        self.search = search  # type: dict[str, any]
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Chart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.display is not None:
            result['display'] = self.display
        if self.search is not None:
            result['search'] = self.search
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Dashboard(TeaModel):
    def __init__(self, attribute=None, charts=None, dashboard_name=None, description=None, display_name=None):
        self.attribute = attribute  # type: dict[str, str]
        self.charts = charts  # type: list[Chart]
        self.dashboard_name = dashboard_name  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        if self.charts:
            for k in self.charts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Dashboard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute
        result['charts'] = []
        if self.charts is not None:
            for k in self.charts:
                result['charts'].append(k.to_map() if k else None)
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        self.charts = []
        if m.get('charts') is not None:
            for k in m.get('charts'):
                temp_model = Chart()
                self.charts.append(temp_model.from_map(k))
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class EtlJobFunctionConfig(TeaModel):
    def __init__(self, account_id=None, endpoint=None, function_name=None, function_provider=None, region_name=None,
                 role_arn=None, service_name=None):
        self.account_id = account_id  # type: str
        self.endpoint = endpoint  # type: str
        self.function_name = function_name  # type: str
        self.function_provider = function_provider  # type: str
        self.region_name = region_name  # type: str
        self.role_arn = role_arn  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EtlJobFunctionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.function_provider is not None:
            result['functionProvider'] = self.function_provider
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('functionProvider') is not None:
            self.function_provider = m.get('functionProvider')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class EtlJobLogConfig(TeaModel):
    def __init__(self, endpoint=None, logstore_name=None, project_name=None):
        self.endpoint = endpoint  # type: str
        self.logstore_name = logstore_name  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EtlJobLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class EtlJobSourceConfig(TeaModel):
    def __init__(self, logstore_name=None):
        self.logstore_name = logstore_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EtlJobSourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        return self


class EtlJobTriggerConfig(TeaModel):
    def __init__(self, max_retry_time=None, role_arn=None, starting_position=None, starting_unixtime=None,
                 trigger_interval=None):
        self.max_retry_time = max_retry_time  # type: int
        self.role_arn = role_arn  # type: str
        self.starting_position = starting_position  # type: str
        self.starting_unixtime = starting_unixtime  # type: long
        self.trigger_interval = trigger_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EtlJobTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_retry_time is not None:
            result['maxRetryTime'] = self.max_retry_time
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.starting_position is not None:
            result['startingPosition'] = self.starting_position
        if self.starting_unixtime is not None:
            result['startingUnixtime'] = self.starting_unixtime
        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxRetryTime') is not None:
            self.max_retry_time = m.get('maxRetryTime')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('startingPosition') is not None:
            self.starting_position = m.get('startingPosition')
        if m.get('startingUnixtime') is not None:
            self.starting_unixtime = m.get('startingUnixtime')
        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')
        return self


class EtlJob(TeaModel):
    def __init__(self, enable=None, etl_job_name=None, function_config=None, function_parameter=None,
                 log_config=None, source_config=None, trigger_config=None):
        self.enable = enable  # type: bool
        self.etl_job_name = etl_job_name  # type: str
        self.function_config = function_config  # type: EtlJobFunctionConfig
        self.function_parameter = function_parameter  # type: dict[str, any]
        self.log_config = log_config  # type: EtlJobLogConfig
        self.source_config = source_config  # type: EtlJobSourceConfig
        self.trigger_config = trigger_config  # type: EtlJobTriggerConfig

    def validate(self):
        if self.function_config:
            self.function_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        _map = super(EtlJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.etl_job_name is not None:
            result['etlJobName'] = self.etl_job_name
        if self.function_config is not None:
            result['functionConfig'] = self.function_config.to_map()
        if self.function_parameter is not None:
            result['functionParameter'] = self.function_parameter
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config.to_map()
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('etlJobName') is not None:
            self.etl_job_name = m.get('etlJobName')
        if m.get('functionConfig') is not None:
            temp_model = EtlJobFunctionConfig()
            self.function_config = temp_model.from_map(m['functionConfig'])
        if m.get('functionParameter') is not None:
            self.function_parameter = m.get('functionParameter')
        if m.get('logConfig') is not None:
            temp_model = EtlJobLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = EtlJobSourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        if m.get('triggerConfig') is not None:
            temp_model = EtlJobTriggerConfig()
            self.trigger_config = temp_model.from_map(m['triggerConfig'])
        return self


class EtlMeta(TeaModel):
    def __init__(self, enable=None, etl_meta_key=None, etl_meta_name=None, etl_meta_tag=None, etl_meta_value=None):
        self.enable = enable  # type: bool
        self.etl_meta_key = etl_meta_key  # type: str
        self.etl_meta_name = etl_meta_name  # type: str
        self.etl_meta_tag = etl_meta_tag  # type: str
        self.etl_meta_value = etl_meta_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EtlMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.etl_meta_key is not None:
            result['etlMetaKey'] = self.etl_meta_key
        if self.etl_meta_name is not None:
            result['etlMetaName'] = self.etl_meta_name
        if self.etl_meta_tag is not None:
            result['etlMetaTag'] = self.etl_meta_tag
        if self.etl_meta_value is not None:
            result['etlMetaValue'] = self.etl_meta_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('etlMetaKey') is not None:
            self.etl_meta_key = m.get('etlMetaKey')
        if m.get('etlMetaName') is not None:
            self.etl_meta_name = m.get('etlMetaName')
        if m.get('etlMetaTag') is not None:
            self.etl_meta_tag = m.get('etlMetaTag')
        if m.get('etlMetaValue') is not None:
            self.etl_meta_value = m.get('etlMetaValue')
        return self


class ExternalStore(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        self.external_store_name = external_store_name  # type: str
        self.parameter = parameter  # type: dict[str, any]
        self.store_type = store_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExternalStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class IndexLine(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, exclude_keys=None, include_keys=None, token=None):
        self.case_sensitive = case_sensitive  # type: bool
        self.chn = chn  # type: bool
        self.exclude_keys = exclude_keys  # type: list[str]
        self.include_keys = include_keys  # type: list[str]
        self.token = token  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class Index(TeaModel):
    def __init__(self, keys=None, last_modify_time=None, line=None, log_reduce=None, log_reduce_black_list=None,
                 log_reduce_white_list=None, max_text_len=None, ttl=None):
        self.keys = keys  # type: dict[str, IndexKeysValue]
        self.last_modify_time = last_modify_time  # type: long
        self.line = line  # type: IndexLine
        self.log_reduce = log_reduce  # type: bool
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        self.max_text_len = max_text_len  # type: int
        self.ttl = ttl  # type: int

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(Index, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = IndexKeysValue()
                self.keys[k] = temp_model.from_map(v)
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('line') is not None:
            temp_model = IndexLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class LoggingLoggingDetails(TeaModel):
    def __init__(self, logstore=None, type=None):
        self.logstore = logstore  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoggingLoggingDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Logging(TeaModel):
    def __init__(self, logging_details=None, logging_project=None):
        self.logging_details = logging_details  # type: list[LoggingLoggingDetails]
        self.logging_project = logging_project  # type: str

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Logging, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = LoggingLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class Logstore(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, create_time=None, enable_tracking=None, encrypt_conf=None,
                 hot_ttl=None, infrequent_access_ttl=None, last_modify_time=None, logstore_name=None, max_split_shard=None,
                 mode=None, product_type=None, shard_count=None, telemetry_type=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.create_time = create_time  # type: int
        self.enable_tracking = enable_tracking  # type: bool
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        self.hot_ttl = hot_ttl  # type: int
        self.infrequent_access_ttl = infrequent_access_ttl  # type: int
        self.last_modify_time = last_modify_time  # type: int
        self.logstore_name = logstore_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.mode = mode  # type: str
        self.product_type = product_type  # type: str
        self.shard_count = shard_count  # type: int
        self.telemetry_type = telemetry_type  # type: str
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(Logstore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class Machine(TeaModel):
    def __init__(self, ip=None, last_heartbeat_time=None, machine_uniqueid=None, userdefined_id=None):
        self.ip = ip  # type: str
        self.last_heartbeat_time = last_heartbeat_time  # type: long
        self.machine_uniqueid = machine_uniqueid  # type: str
        self.userdefined_id = userdefined_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Machine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.last_heartbeat_time is not None:
            result['lastHeartbeatTime'] = self.last_heartbeat_time
        if self.machine_uniqueid is not None:
            result['machine-uniqueid'] = self.machine_uniqueid
        if self.userdefined_id is not None:
            result['userdefined-id'] = self.userdefined_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('lastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('lastHeartbeatTime')
        if m.get('machine-uniqueid') is not None:
            self.machine_uniqueid = m.get('machine-uniqueid')
        if m.get('userdefined-id') is not None:
            self.userdefined_id = m.get('userdefined-id')
        return self


class MachineGroupGroupAttribute(TeaModel):
    def __init__(self, external_name=None, group_topic=None):
        self.external_name = external_name  # type: str
        self.group_topic = group_topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MachineGroupGroupAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class MachineGroup(TeaModel):
    def __init__(self, group_attribute=None, group_name=None, group_type=None, machine_identify_type=None,
                 machine_list=None):
        self.group_attribute = group_attribute  # type: MachineGroupGroupAttribute
        self.group_name = group_name  # type: str
        self.group_type = group_type  # type: str
        self.machine_identify_type = machine_identify_type  # type: str
        self.machine_list = machine_list  # type: list[str]

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super(MachineGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = MachineGroupGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class Project(TeaModel):
    def __init__(self, create_time=None, description=None, last_modify_time=None, owner=None, project_name=None,
                 region=None, resource_group_id=None, status=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.last_modify_time = last_modify_time  # type: str
        self.owner = owner  # type: str
        self.project_name = project_name  # type: str
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Project, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.owner is not None:
            result['owner'] = self.owner
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ServiceStatus(TeaModel):
    def __init__(self, enabled=None, status=None):
        self.enabled = enabled  # type: bool
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ServiceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Shard(TeaModel):
    def __init__(self, create_time=None, exclusive_end_key=None, inclusive_begin_key=None, shard_id=None,
                 status=None):
        self.create_time = create_time  # type: int
        self.exclusive_end_key = exclusive_end_key  # type: str
        self.inclusive_begin_key = inclusive_begin_key  # type: str
        self.shard_id = shard_id  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Shard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.exclusive_end_key is not None:
            result['exclusiveEndKey'] = self.exclusive_end_key
        if self.inclusive_begin_key is not None:
            result['inclusiveBeginKey'] = self.inclusive_begin_key
        if self.shard_id is not None:
            result['shardID'] = self.shard_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('exclusiveEndKey') is not None:
            self.exclusive_end_key = m.get('exclusiveEndKey')
        if m.get('inclusiveBeginKey') is not None:
            self.inclusive_begin_key = m.get('inclusiveBeginKey')
        if m.get('shardID') is not None:
            self.shard_id = m.get('shardID')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class MLDataParamAnnotationsValue(TeaModel):
    def __init__(self, annotated_by=None, update_time=None, results=None):
        self.annotated_by = annotated_by  # type: str
        self.update_time = update_time  # type: long
        self.results = results  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLDataParamAnnotationsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotated_by is not None:
            result['annotatedBy'] = self.annotated_by
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.results is not None:
            result['results'] = self.results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotatedBy') is not None:
            self.annotated_by = m.get('annotatedBy')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('results') is not None:
            self.results = m.get('results')
        return self


class MLDataParamPredictionsValue(TeaModel):
    def __init__(self, annotated_by=None, update_time=None, results=None):
        self.annotated_by = annotated_by  # type: str
        self.update_time = update_time  # type: long
        self.results = results  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(MLDataParamPredictionsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotated_by is not None:
            result['annotatedBy'] = self.annotated_by
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.results is not None:
            result['results'] = self.results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotatedBy') is not None:
            self.annotated_by = m.get('annotatedBy')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('results') is not None:
            self.results = m.get('results')
        return self


class IndexKeysValue(TeaModel):
    def __init__(self, chn=None, case_sensitive=None, token=None, alias=None, type=None, doc_value=None):
        self.chn = chn  # type: bool
        self.case_sensitive = case_sensitive  # type: bool
        self.token = token  # type: list[str]
        self.alias = alias  # type: str
        self.type = type  # type: str
        self.doc_value = doc_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexKeysValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chn is not None:
            result['chn'] = self.chn
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.token is not None:
            result['token'] = self.token
        if self.alias is not None:
            result['alias'] = self.alias
        if self.type is not None:
            result['type'] = self.type
        if self.doc_value is not None:
            result['doc_value'] = self.doc_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')
        return self


class KeysValue(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, type=None, alias=None, token=None, doc_value=None):
        # Specifies whether to enable case sensitivity. This parameter is required only when **type** is set to **text**. Valid values:
        # 
        # *   true
        # *   false (default)
        self.case_sensitive = case_sensitive  # type: bool
        # Specifies whether to include Chinese characters. This parameter is required only when **type** is set to **text**. Valid values:
        # 
        # *   true
        # *   false (default)
        self.chn = chn  # type: bool
        # The data type of the field value. Valid values: text, json, double, and long.
        self.type = type  # type: str
        # The alias of the field.
        self.alias = alias  # type: str
        # The delimiters that are used to split text.
        self.token = token  # type: list[str]
        # Specifies whether to turn on Enable Analytics for the field.
        self.doc_value = doc_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(KeysValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.type is not None:
            result['type'] = self.type
        if self.alias is not None:
            result['alias'] = self.alias
        if self.token is not None:
            result['token'] = self.token
        if self.doc_value is not None:
            result['doc_value'] = self.doc_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')
        return self


class ApplyConfigToMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(ApplyConfigToMachineGroupResponse, self).to_map()
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


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None, resource_id=None, resource_type=None):
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
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


class ConsumerGroupHeartBeatRequest(TeaModel):
    def __init__(self, body=None, consumer=None):
        self.body = body  # type: list[int]
        self.consumer = consumer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConsumerGroupHeartBeatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.consumer is not None:
            result['consumer'] = self.consumer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        return self


class ConsumerGroupHeartBeatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[int]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(ConsumerGroupHeartBeatResponse, self).to_map()
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


class CreateAnnotationDataSetRequest(TeaModel):
    def __init__(self, body=None, dataset_id=None):
        self.body = body  # type: MLDataSetParam
        self.dataset_id = dataset_id  # type: str

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAnnotationDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        return self


class CreateAnnotationDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateAnnotationDataSetResponse, self).to_map()
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


class CreateAnnotationLabelRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: MLLabelParam

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAnnotationLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAnnotationLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateAnnotationLabelResponse, self).to_map()
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


class CreateConfigRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: LogtailConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateConfigResponse, self).to_map()
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


class CreateConsumerGroupRequest(TeaModel):
    def __init__(self, consumer_group=None, order=None, timeout=None):
        # The name of the consumer group. The name must be unique in a project.
        self.consumer_group = consumer_group  # type: str
        # Specifies whether to consume data in sequence. Valid values:
        # 
        # *   true
        # 
        #     *   In a shard, data is consumed in ascending order based on the value of the \*\*\__tag\_\_:\__receive_time\_\_\*\* field.
        #     *   If a shard is split, data in the original shard is consumed first. Then, data in the new shards is consumed at the same time.
        #     *   If shards are merged, data in the original shards is consumed first. Then, data in the new shard is consumed.
        # 
        # *   false Data in all shards is consumed at the same time. If a new shard is generated after a shard is split or after shards are merged, data in the new shard is immediately consumed.
        self.order = order  # type: bool
        # The timeout period. If the server does not receive heartbeats from a consumer within the timeout period, the server deletes the consumer. Unit: seconds.
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['consumerGroup'] = self.consumer_group
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consumerGroup') is not None:
            self.consumer_group = m.get('consumerGroup')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateConsumerGroupResponse, self).to_map()
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


class CreateDashboardRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Dashboard

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDashboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Dashboard()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateDashboardResponse, self).to_map()
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


class CreateDomainRequest(TeaModel):
    def __init__(self, domain_name=None):
        # The domain name.
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateDomainResponse, self).to_map()
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


class CreateIndexRequestLine(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, exclude_keys=None, include_keys=None, token=None):
        # Specifies whether to enable case sensitivity. Valid values:
        # 
        # *   true
        # *   false (default)
        self.case_sensitive = case_sensitive  # type: bool
        # Specifies whether to include Chinese characters. Valid values:
        # 
        # *   true
        # *   false (default)
        self.chn = chn  # type: bool
        # The excluded fields. You cannot specify both include_keys and exclude_keys.
        self.exclude_keys = exclude_keys  # type: list[str]
        # The included fields. You cannot specify both include_keys and exclude_keys.
        self.include_keys = include_keys  # type: list[str]
        # The delimiters. You can specify a delimiter to delimit the content of a field value. For more information about delimiters, see Example.
        self.token = token  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexRequestLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(self, keys=None, line=None, log_reduce=None, log_reduce_black_list=None,
                 log_reduce_white_list=None, max_text_len=None, ttl=None):
        # The configuration of field indexes. A field index is a key-value pair in which the key specifies the name of the field and the value specifies the index configuration of the field. You must specify this parameter, the line parameter, or both parameters. For more information, see Example.
        self.keys = keys  # type: dict[str, KeysValue]
        # The configuration of full-text indexes. You must specify this parameter, the keys parameter, or both parameters. For more information, see Example.
        self.line = line  # type: CreateIndexRequestLine
        # Specifies whether to turn on LogReduce. After you turn on LogReduce, either the whitelist or blacklist takes effect.
        self.log_reduce = log_reduce  # type: bool
        # The fields in the blacklist that you want to use to cluster logs.
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # The fields in the whitelist that you want to use to cluster logs.
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # The maximum length of a field value that can be retained. Default value: 2048. Unit: bytes. The default value is equal to 2 KB. You can change the value of max_text_len. Valid values: 64 to 16384.
        self.max_text_len = max_text_len  # type: int
        # The retention period of logs. Unit: days. Valid values: 7, 30, and 90.
        self.ttl = ttl  # type: int

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(CreateIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = KeysValue()
                self.keys[k] = temp_model.from_map(v)
        if m.get('line') is not None:
            temp_model = CreateIndexRequestLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateIndexResponse, self).to_map()
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


class CreateLogStoreRequest(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, encrypt_conf=None, hot_ttl=None,
                 infrequent_access_ttl=None, logstore_name=None, max_split_shard=None, mode=None, shard_count=None, telemetry_type=None,
                 ttl=None):
        # Specifies whether to record public IP addresses. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta  # type: bool
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split  # type: bool
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking  # type: bool
        # The data structure of the encryption configuration.
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        # The retention period of data in the hot storage tier of the Logstore. Unit: days. You can specify a value that ranges from 30 to the value of ttl.
        # 
        # Hot data that is stored for longer than the period specified by hot_ttl is converted to cold data. For more information, see [Enable hot and cold-tiered storage for a Logstore](~~308645~~).
        self.hot_ttl = hot_ttl  # type: int
        self.infrequent_access_ttl = infrequent_access_ttl  # type: int
        # The name of the Logstore. The name must meet the following requirements:
        # 
        # *   The name must be unique in a project.
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (\_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.logstore_name = logstore_name  # type: str
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 64.
        # 
        # > If you set autoSplit to true, you must configure this parameter.
        self.max_split_shard = max_split_shard  # type: int
        # The type of the Logstore. Log Service provides the following types of Logstores: Standard Logstores and Query Logstores. Valid values:
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the amount of data is large, the log retention period is long, or log analysis is not required. Log retention periods of weeks or months are considered long.
        self.mode = mode  # type: str
        # The number of shards.
        # 
        # > You cannot call the CreateLogStore operation to change the number of shards. You can call the SplitShard or MergeShards operation to change the number of shards.
        self.shard_count = shard_count  # type: int
        # The type of the observable data. Valid values:
        # 
        # *   None: logs
        # *   Metrics: metrics
        self.telemetry_type = telemetry_type  # type: str
        # The retention period of data. Unit: days. Valid values: 1 to 3000. If you set this parameter to 3650, data is permanently stored.
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(CreateLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateLogStoreResponse, self).to_map()
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


class CreateLoggingRequestLoggingDetails(TeaModel):
    def __init__(self, logstore=None, type=None):
        # The name of the Logstore to which service logs of the type are stored.
        self.logstore = logstore  # type: str
        # The type of service logs. Valid values:
        # 
        # *   consumergroup_log: the consumption delay logs of consumer groups.
        # *   logtail_alarm: the alert logs of Logtail.
        # *   operation_log: the operation logs.
        # *   logtail_profile: the collection logs of Logtail.
        # *   metering: the metering logs.
        # *   logtail_status: the status logs of Logtail.
        # *   scheduledsqlalert: the run logs of Scheduled SQL jobs.
        # *   etl_alert: the run logs of data transformation jobs.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoggingRequestLoggingDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateLoggingRequest(TeaModel):
    def __init__(self, logging_details=None, logging_project=None):
        # The configurations of service logs.
        self.logging_details = logging_details  # type: list[CreateLoggingRequestLoggingDetails]
        # The name of the project to which service logs are stored.
        self.logging_project = logging_project  # type: str

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLoggingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = CreateLoggingRequestLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class CreateLoggingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateLoggingResponse, self).to_map()
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


class CreateLogtailPipelineConfigRequest(TeaModel):
    def __init__(self, aggregators=None, config_name=None, flushers=None, global_=None, inputs=None, log_sample=None,
                 processors=None):
        self.aggregators = aggregators  # type: list[dict[str, any]]
        self.config_name = config_name  # type: str
        self.flushers = flushers  # type: list[dict[str, any]]
        self.global_ = global_  # type: dict[str, any]
        self.inputs = inputs  # type: list[dict[str, any]]
        self.log_sample = log_sample  # type: str
        self.processors = processors  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogtailPipelineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class CreateLogtailPipelineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateLogtailPipelineConfigResponse, self).to_map()
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


class CreateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(self, external_name=None, group_topic=None):
        # The identifier of the external management system on which the machine group depends.
        self.external_name = external_name  # type: str
        # The log topic of the machine group.
        self.group_topic = group_topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMachineGroupRequestGroupAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class CreateMachineGroupRequest(TeaModel):
    def __init__(self, group_attribute=None, group_name=None, group_type=None, machine_identify_type=None,
                 machine_list=None):
        # The attributes of the machine group.
        self.group_attribute = group_attribute  # type: CreateMachineGroupRequestGroupAttribute
        # The name of the machine group. The name must meet the following requirements:
        # 
        # *   The name of each machine group in a project must be unique.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (\_).
        # *   It must start and end with a lowercase letter or a digit.
        # *   It must be 3 to 128 characters in length.
        self.group_name = group_name  # type: str
        # The type of the machine group. The parameter can be left empty.
        self.group_type = group_type  # type: str
        # The type of the machine group identifier. Valid values:
        # 
        # *   ip: The machine group uses IP addresses as identifiers.
        # *   userdefined: The machine group uses custom identifiers.
        self.machine_identify_type = machine_identify_type  # type: str
        # The identifiers of machine group.
        # 
        # *   If you set machineIdentifyType to ip, enter the IP address of the machine.
        # *   If you set machineIdentifyType to userdefined, enter a custom identifier.
        self.machine_list = machine_list  # type: list[str]

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super(CreateMachineGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = CreateMachineGroupRequestGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class CreateMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateMachineGroupResponse, self).to_map()
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


class CreateOssExternalStoreRequestParameterColumns(TeaModel):
    def __init__(self, name=None, type=None):
        # The name of the field.
        self.name = name  # type: str
        # The type of the field.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOssExternalStoreRequestParameterColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateOssExternalStoreRequestParameter(TeaModel):
    def __init__(self, accessid=None, accesskey=None, bucket=None, columns=None, endpoint=None, objects=None):
        # The AccessKey ID of your account.
        self.accessid = accessid  # type: str
        # The AccessKey secret of your account.
        self.accesskey = accesskey  # type: str
        # The name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The associated fields.
        self.columns = columns  # type: list[CreateOssExternalStoreRequestParameterColumns]
        # The OSS endpoint.
        self.endpoint = endpoint  # type: str
        # The associated objects.
        self.objects = objects  # type: list[str]

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOssExternalStoreRequestParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['accessid'] = self.accessid
        if self.accesskey is not None:
            result['accesskey'] = self.accesskey
        if self.bucket is not None:
            result['bucket'] = self.bucket
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.objects is not None:
            result['objects'] = self.objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessid') is not None:
            self.accessid = m.get('accessid')
        if m.get('accesskey') is not None:
            self.accesskey = m.get('accesskey')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = CreateOssExternalStoreRequestParameterColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('objects') is not None:
            self.objects = m.get('objects')
        return self


class CreateOssExternalStoreRequest(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # The name of the external store.
        self.external_store_name = external_store_name  # type: str
        # The parameters that are configured for the external store.
        self.parameter = parameter  # type: CreateOssExternalStoreRequestParameter
        # The type of the external store. Set the value to oss.
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(CreateOssExternalStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = CreateOssExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class CreateOssExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateOssExternalStoreResponse, self).to_map()
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


class CreateProjectRequest(TeaModel):
    def __init__(self, data_redundancy_type=None, description=None, project_name=None, resource_group_id=None):
        # Data redundancy type
        self.data_redundancy_type = data_redundancy_type  # type: str
        # The description of the project.
        self.description = description  # type: str
        # The name of the project. The name must be unique in a region. You cannot change the name after you create the project. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   It can contain only lowercase letters, digits, and hyphens (-).
        # *   It must start and end with a lowercase letter or a digit.
        # *   It must be 3 to 63 characters in length.
        self.project_name = project_name  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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


class CreateRdsExternalStoreRequestParameter(TeaModel):
    def __init__(self, db=None, host=None, instance_id=None, password=None, port=None, region=None, table=None,
                 username=None, vpc_id=None):
        # The name of the database in the ApsaraDB RDS for MySQL instance.
        self.db = db  # type: str
        # The internal or public endpoint of the ApsaraDB RDS for MySQL instance.
        self.host = host  # type: str
        # The ID of the ApsaraDB RDS for MySQL instance.
        self.instance_id = instance_id  # type: str
        # The password that is used to log on to the ApsaraDB RDS for MySQL instance.
        self.password = password  # type: str
        # The internal or public port of the ApsaraDB RDS for MySQL instance.
        self.port = port  # type: str
        # The region where the ApsaraDB RDS for MySQL instance resides. Valid values: cn-qingdao, cn-beijing, and cn-hangzhou.
        self.region = region  # type: str
        # The name of the database table in the ApsaraDB RDS for MySQL instance.
        self.table = table  # type: str
        # The username that is used to log on to the ApsaraDB RDS for MySQL instance.
        self.username = username  # type: str
        # The ID of the VPC to which the ApsaraDB RDS for MySQL instance belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRdsExternalStoreRequestParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['db'] = self.db
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instance-id'] = self.instance_id
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.region is not None:
            result['region'] = self.region
        if self.table is not None:
            result['table'] = self.table
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpc-id'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instance-id') is not None:
            self.instance_id = m.get('instance-id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpc-id') is not None:
            self.vpc_id = m.get('vpc-id')
        return self


class CreateRdsExternalStoreRequest(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # The name of the external store. The name must be unique in a project and must be different from Logstore names.
        self.external_store_name = external_store_name  # type: str
        # The parameter struct.
        self.parameter = parameter  # type: CreateRdsExternalStoreRequestParameter
        # The storage type. Set the value to rds-vpc, which indicates an ApsaraDB RDS for MySQL database in a virtual private cloud (VPC).
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(CreateRdsExternalStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = CreateRdsExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class CreateRdsExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateRdsExternalStoreResponse, self).to_map()
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


class CreateSavedSearchRequest(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        # The display name.
        self.display_name = display_name  # type: str
        # The name of the Logstore to which the saved search belongs.
        self.logstore = logstore  # type: str
        # The name of the saved search. The name must be 3 to 63 characters in length.
        self.savedsearch_name = savedsearch_name  # type: str
        # The query statement of the saved search. A query statement consists of a search statement and an analytic statement in the `Search statement|Analytic statement` format. For more information about search statements and analytic statements, see [Log search overview](~~43772~~) and [Log analysis overview](~~53608~~).
        self.search_query = search_query  # type: str
        # The topic of the log.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSavedSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class CreateSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CreateSavedSearchResponse, self).to_map()
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


class CreateTicketResponseBody(TeaModel):
    def __init__(self, ticket=None):
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTicketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAnnotationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteAnnotationDataResponse, self).to_map()
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


class DeleteAnnotationDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteAnnotationDataSetResponse, self).to_map()
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


class DeleteAnnotationLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteAnnotationLabelResponse, self).to_map()
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


class DeleteCollectionPolicyRequest(TeaModel):
    def __init__(self, data_code=None, product_code=None):
        self.data_code = data_code  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class DeleteCollectionPolicyResponseBody(TeaModel):
    def __init__(self, message=None):
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectionPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteCollectionPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCollectionPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCollectionPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCollectionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteConfigResponse, self).to_map()
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


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteConsumerGroupResponse, self).to_map()
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


class DeleteDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteDashboardResponse, self).to_map()
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


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteDomainResponse, self).to_map()
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


class DeleteExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteExternalStoreResponse, self).to_map()
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


class DeleteIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteIndexResponse, self).to_map()
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


class DeleteLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteLogStoreResponse, self).to_map()
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


class DeleteLoggingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteLoggingResponse, self).to_map()
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


class DeleteLogtailPipelineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteLogtailPipelineConfigResponse, self).to_map()
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


class DeleteMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteMachineGroupResponse, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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


class DeleteProjectPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteProjectPolicyResponse, self).to_map()
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


class DeleteSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteSavedSearchResponse, self).to_map()
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


class DeleteShipperResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteShipperResponse, self).to_map()
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


class GetAnnotationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MLDataParam

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAnnotationDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLDataParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnnotationDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MLDataSetParam

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAnnotationDataSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnnotationLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MLLabelParam

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAnnotationLabelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppliedConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, count=None):
        # The names of the Logtail configurations.
        self.configs = configs  # type: list[str]
        # The number of Logtail configurations.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppliedConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetAppliedConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppliedConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppliedConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppliedConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppliedMachineGroupsResponseBody(TeaModel):
    def __init__(self, count=None, machinegroups=None):
        # The number of returned machine groups.
        self.count = count  # type: int
        # The names of the returned machine groups.
        self.machinegroups = machinegroups  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppliedMachineGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.machinegroups is not None:
            result['machinegroups'] = self.machinegroups
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('machinegroups') is not None:
            self.machinegroups = m.get('machinegroups')
        return self


class GetAppliedMachineGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppliedMachineGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppliedMachineGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppliedMachineGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCheckPointRequest(TeaModel):
    def __init__(self, shard=None):
        # The shard ID.
        # 
        # *   If the specified shard does not exist, an empty list is returned.
        # *   If no shard ID is specified, the checkpoints of all shards are returned.
        self.shard = shard  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCheckPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shard is not None:
            result['shard'] = self.shard
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        return self


class GetCheckPointResponseBody(TeaModel):
    def __init__(self, shard=None, checkpoint=None, update_time=None, consumer=None):
        # The shard ID.
        self.shard = shard  # type: int
        # The value of the checkpoint.
        self.checkpoint = checkpoint  # type: str
        # The time when the checkpoint was last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time  # type: long
        # The consumer at the checkpoint.
        self.consumer = consumer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCheckPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shard is not None:
            result['shard'] = self.shard
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.consumer is not None:
            result['consumer'] = self.consumer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        return self


class GetCheckPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[GetCheckPointResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCheckPointResponse, self).to_map()
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
                temp_model = GetCheckPointResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetCollectionPolicyRequest(TeaModel):
    def __init__(self, data_code=None, product_code=None):
        self.data_code = data_code  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCollectionPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyAttribute(TeaModel):
    def __init__(self, app=None, policy_group=None):
        self.app = app  # type: str
        self.policy_group = policy_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCollectionPolicyResponseBodyCollectionPolicyAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['app'] = self.app
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app') is not None:
            self.app = m.get('app')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig(TeaModel):
    def __init__(self, dest_logstore=None, dest_project=None, dest_region=None, dest_ttl=None):
        self.dest_logstore = dest_logstore  # type: str
        self.dest_project = dest_project  # type: str
        self.dest_region = dest_region  # type: str
        self.dest_ttl = dest_ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig(TeaModel):
    def __init__(self, instance_ids=None, regions=None, resource_mode=None, resource_tags=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.regions = regions  # type: list[str]
        self.resource_mode = resource_mode  # type: str
        self.resource_tags = resource_tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicy(TeaModel):
    def __init__(self, attribute=None, centralize_config=None, centralize_enabled=None, data_code=None,
                 enabled=None, policy_config=None, policy_name=None, product_code=None):
        self.attribute = attribute  # type: GetCollectionPolicyResponseBodyCollectionPolicyAttribute
        self.centralize_config = centralize_config  # type: GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig
        self.centralize_enabled = centralize_enabled  # type: bool
        self.data_code = data_code  # type: str
        self.enabled = enabled  # type: str
        self.policy_config = policy_config  # type: GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig
        self.policy_name = policy_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        if self.attribute:
            self.attribute.validate()
        if self.centralize_config:
            self.centralize_config.validate()
        if self.policy_config:
            self.policy_config.validate()

    def to_map(self):
        _map = super(GetCollectionPolicyResponseBodyCollectionPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute.to_map()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyAttribute()
            self.attribute = temp_model.from_map(m['attribute'])
        if m.get('centralizeConfig') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('policyConfig') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class GetCollectionPolicyResponseBody(TeaModel):
    def __init__(self, collection_policy=None):
        self.collection_policy = collection_policy  # type: GetCollectionPolicyResponseBodyCollectionPolicy

    def validate(self):
        if self.collection_policy:
            self.collection_policy.validate()

    def to_map(self):
        _map = super(GetCollectionPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_policy is not None:
            result['collectionPolicy'] = self.collection_policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('collectionPolicy') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicy()
            self.collection_policy = temp_model.from_map(m['collectionPolicy'])
        return self


class GetCollectionPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCollectionPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCollectionPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCollectionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogtailConfig

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContextLogsRequest(TeaModel):
    def __init__(self, back_lines=None, forward_lines=None, pack_id=None, pack_meta=None, type=None):
        # The number of logs that you want to obtain and are generated before the generation time of the start log. Valid values: (0,100].
        self.back_lines = back_lines  # type: long
        # The number of logs that you want to obtain and are generated after the generation time of the start log. Valid values: (0,100].
        self.forward_lines = forward_lines  # type: long
        # The unique identifier of the log group to which the start log belongs.
        self.pack_id = pack_id  # type: str
        # The unique context identifier of the start log in the log group.
        self.pack_meta = pack_meta  # type: str
        # The type of the data in the Logstore. Set the value to context_log.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContextLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines
        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines
        if self.pack_id is not None:
            result['pack_id'] = self.pack_id
        if self.pack_meta is not None:
            result['pack_meta'] = self.pack_meta
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')
        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')
        if m.get('pack_id') is not None:
            self.pack_id = m.get('pack_id')
        if m.get('pack_meta') is not None:
            self.pack_meta = m.get('pack_meta')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetContextLogsResponseBody(TeaModel):
    def __init__(self, back_lines=None, forward_lines=None, logs=None, progress=None, total_lines=None):
        # The number of logs that are generated before the generation time of the start log.
        self.back_lines = back_lines  # type: long
        # The number of logs that are generated after the generation time of the start log.
        self.forward_lines = forward_lines  # type: long
        # The logs that are returned.
        self.logs = logs  # type: list[dict[str, any]]
        # Indicates whether the query and analysis results are complete. Valid values:
        # 
        # *   Complete: The query is successful, and the complete query and analysis results are returned.
        # *   Incomplete: The query is successful, but the query and analysis results are incomplete. To obtain the complete results, you must repeat the request.
        self.progress = progress  # type: str
        # The total number of logs that are returned. The logs include the start log that is specified in the request.
        self.total_lines = total_lines  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContextLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines
        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines
        if self.logs is not None:
            result['logs'] = self.logs
        if self.progress is not None:
            result['progress'] = self.progress
        if self.total_lines is not None:
            result['total_lines'] = self.total_lines
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')
        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')
        if m.get('logs') is not None:
            self.logs = m.get('logs')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('total_lines') is not None:
            self.total_lines = m.get('total_lines')
        return self


class GetContextLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetContextLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetContextLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetContextLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCursorRequest(TeaModel):
    def __init__(self, from_=None):
        # The point in time that you want to use to query a cursor. Set the value to a UNIX timestamp or a string such as `begin` and `end`.
        self.from_ = from_  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        return self


class GetCursorResponseBody(TeaModel):
    def __init__(self, cursor=None):
        # The value of the cursor.
        self.cursor = cursor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class GetCursorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCursorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCursorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCursorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCursorTimeRequest(TeaModel):
    def __init__(self, cursor=None):
        # The cursor.
        self.cursor = cursor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class GetCursorTimeResponseBody(TeaModel):
    def __init__(self, cursor_time=None):
        # The server time that is queried based on the cursor. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.cursor_time = cursor_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor_time is not None:
            result['cursor_time'] = self.cursor_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor_time') is not None:
            self.cursor_time = m.get('cursor_time')
        return self


class GetCursorTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCursorTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCursorTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCursorTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Dashboard

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDashboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Dashboard()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExternalStore

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExternalStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExternalStore()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistogramsRequest(TeaModel):
    def __init__(self, from_=None, query=None, to=None, topic=None):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: long
        # The search statement. Only search statements are supported. Analytic statements are not supported. For more information about the syntax of search statements, see [Log search overview](~~43772~~).
        self.query = query  # type: str
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: long
        # The topic of the logs.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.query is not None:
            result['query'] = self.query
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(self, from_=None, to=None, count=None, progress=None):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.from_ = from_  # type: long
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.to = to  # type: long
        # The number of logs that are generated within the subinterval.
        self.count = count  # type: long
        # Indicates whether the query and analysis results in the subinterval is complete. Valid values:
        # 
        # Complete: The query is successful, and the complete query and analysis results are returned.
        # 
        # Incomplete: The query is successful, but the query and analysis results are incomplete. To obtain the complete results, you must repeat the request.
        self.progress = progress  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.to is not None:
            result['to'] = self.to
        if self.count is not None:
            result['count'] = self.count
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class GetHistogramsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[GetHistogramsResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHistogramsResponse, self).to_map()
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
                temp_model = GetHistogramsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetIndexResponseBodyLine(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, exclude_keys=None, include_keys=None, token=None):
        # Indicates whether case sensitivity is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.case_sensitive = case_sensitive  # type: bool
        # Indicates whether Chinese characters are included. Valid values:
        # 
        # *   true
        # *   false
        self.chn = chn  # type: bool
        # The excluded fields.
        self.exclude_keys = exclude_keys  # type: list[str]
        # The included fields.
        self.include_keys = include_keys  # type: list[str]
        # The delimiters.
        self.token = token  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexResponseBodyLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetIndexResponseBody(TeaModel):
    def __init__(self, index_mode=None, keys=None, last_modify_time=None, line=None, log_reduce=None,
                 log_reduce_black_list=None, log_reduce_white_list=None, max_text_len=None, storage=None, ttl=None):
        # The type of the index.
        self.index_mode = index_mode  # type: str
        # The configurations of field indexes. A field index is in the key-value format in which the key specifies the name of the field and the value specifies the index configuration of the field.
        self.keys = keys  # type: dict[str, KeysValue]
        # The time when the index configurations were last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time  # type: long
        # The configurations of full-text indexes.
        self.line = line  # type: GetIndexResponseBodyLine
        # Indicates whether the log clustering feature is enabled.
        self.log_reduce = log_reduce  # type: bool
        # The fields in the blacklist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # The fields in the whitelist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # The maximum length of a field value that can be retained. Default value: 2048. Unit: bytes. The default value is equal to 2 KB. You can change the value of the max_text_len parameter. Valid values: 64 to 16384. Unit: bytes.
        self.max_text_len = max_text_len  # type: int
        # The storage type. The value is fixed as pg.
        self.storage = storage  # type: str
        # The lifecycle of the index file. Valid values: 7, 30, and 90. Unit: day.
        self.ttl = ttl  # type: int

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(GetIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_mode is not None:
            result['index_mode'] = self.index_mode
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        if self.storage is not None:
            result['storage'] = self.storage
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('index_mode') is not None:
            self.index_mode = m.get('index_mode')
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = KeysValue()
                self.keys[k] = temp_model.from_map(v)
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('line') is not None:
            temp_model = GetIndexResponseBodyLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class GetIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIndexResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIndexResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Logstore

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Logstore()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStoreMeteringModeResponseBody(TeaModel):
    def __init__(self, metering_mode=None):
        self.metering_mode = metering_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogStoreMeteringModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class GetLogStoreMeteringModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLogStoreMeteringModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogStoreMeteringModeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLogStoreMeteringModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoggingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Logging

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoggingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Logging()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsRequest(TeaModel):
    def __init__(self, from_=None, line=None, offset=None, power_sql=None, query=None, reverse=None, to=None,
                 topic=None):
        # The beginning of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you specify the same value for the **from** and **to** parameters, the interval is invalid, and an error message is returned.
        # *   The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To ensure that full data can be queried, specify a query time range that is accurate to the minute. If you also specify a time range in an analytic statement, Simple Log Service uses the time range specified in the analytic statement for query and analysis.
        # 
        # If you want to specify a time range that is accurate to the second in your analytic statement, you must use the from_unixtime or to_unixtime function to convert the time format. For more information about the functions, see [from_unixtime function](~~63451~~) and [to_unixtime function](~~63451~~). Examples:
        # 
        # *   `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # *   `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\"2022-10-19 15:46:05\", \"%Y-%m-%d %H:%i:%s\")) AND __time__ < to_unixtime(now())`
        self.from_ = from_  # type: int
        # The maximum number of logs to return for the request. This parameter takes effect only when the query parameter is set to a search statement. Minimum value: 0. Maximum value: 100. Default value: 100.
        self.line = line  # type: long
        # The line from which the query starts. This parameter takes effect only when the query parameter is set to a search statement. Default value: 0.
        self.offset = offset  # type: long
        # Specifies whether to enable the Dedicated SQL feature. For more information, see [Enable Dedicated SQL](~~223777~~). Valid values:
        # 
        # *   true: enables the Dedicated SQL feature.
        # *   false (default): enables the Standard SQL feature.
        # 
        # You can use the powerSql or **query** parameter to configure Dedicated SQL.
        self.power_sql = power_sql  # type: bool
        # The search statement or the query statement. For more information, see [Log search overview](~~43772~~) and [Log analysis overview](~~53608~~). If you add `set session parallel_sql=true;` to the analytic statement in the query parameter, Dedicated SQL is used. For example, you can set the query parameter to `* | set session parallel_sql=true; select count(*) as pv`. For more information about common errors that may occur during log query and analysis, see [How do I resolve common errors that occur when I query and analyze logs?](~~61628~~)
        # 
        # > If you specify an analytic statement in the value of the query parameter, the line and offset parameters do not take effect. In this case, we recommend that you set the line and offset parameters to 0 and use the LIMIT clause to limit the number of logs to return on each page. For more information, see [Paged query](~~89994~~).
        self.query = query  # type: str
        # Specifies whether to return logs in reverse chronological order of log timestamps. The log timestamps are accurate to the minute. Valid values:
        # 
        # *   true: returns logs in reverse chronological order of log timestamps.
        # *   false (default): returns logs in chronological order of log timestamps.
        # 
        # > 
        # 
        # *   The reverse parameter takes effect only when the query parameter is set to a search statement. The reverse parameter specifies the method used to sort returned logs.
        # *   If the query parameter is set to a query statement, the reverse parameter does not take effect. The method used to sort returned logs is specified by the ORDER BY clause in the analytic statement. If you use the keyword asc in the ORDER BY clause, the logs are sorted in chronological order. If you use the keyword desc in the ORDER BY clause, the logs are sorted in reverse chronological order. By default, asc is used in the ORDER BY clause.
        self.reverse = reverse  # type: bool
        # The end of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you specify the same value for the **from** and **to** parameters, the interval is invalid, and an error message is returned.
        # *   The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To ensure that full data can be queried, specify a query time range that is accurate to the minute. If you also specify a time range in an analytic statement, Simple Log Service uses the time range specified in the analytic statement for query and analysis.
        # 
        # If you want to specify a time range that is accurate to the second in your analytic statement, you must use the from_unixtime or to_unixtime function to convert the time format. For more information about the functions, see [from_unixtime function](~~63451~~) and [to_unixtime function](~~63451~~). Examples:
        # 
        # *   `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # *   `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\"2022-10-19 15:46:05\", \"%Y-%m-%d %H:%i:%s\")) AND __time__ < to_unixtime(now())`
        self.to = to  # type: int
        # The topic of the logs. The default value is double quotation marks (""). For more information, see [Topic](~~48881~~).
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.line is not None:
            result['line'] = self.line
        if self.offset is not None:
            result['offset'] = self.offset
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.reverse is not None:
            result['reverse'] = self.reverse
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('line') is not None:
            self.line = m.get('line')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[dict[str, any]]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetLogsResponse, self).to_map()
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


class GetLogsV2Headers(TeaModel):
    def __init__(self, common_headers=None, accept_encoding=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The compression method.
        self.accept_encoding = accept_encoding  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsV2Headers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.accept_encoding is not None:
            result['Accept-Encoding'] = self.accept_encoding
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Accept-Encoding') is not None:
            self.accept_encoding = m.get('Accept-Encoding')
        return self


class GetLogsV2Request(TeaModel):
    def __init__(self, forward=None, from_=None, line=None, offset=None, power_sql=None, query=None, reverse=None,
                 session=None, shard=None, to=None, topic=None):
        # Specifies whether to page forward or backward for the scan-based query or the phrase query.
        self.forward = forward  # type: bool
        # The beginning of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range specified by the from and to parameters is a left-closed and right-open interval. Each interval includes the specified start time but does not include the specified end time. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: int
        # The maximum number of logs to return for the request. This parameter takes effect only when the query parameter is set to a search statement. Valid values: 0 to 100. Default value: 100.
        self.line = line  # type: long
        # The row from which the query starts. This parameter takes effect only when the query parameter is set to a search statement. Default value: 0.
        self.offset = offset  # type: long
        # Specifies whether to enable the SQL enhancement feature. By default, the feature is disabled.
        self.power_sql = power_sql  # type: bool
        # The search statement or the query statement. For more information, see the "Log search overview" and "Log analysis overview" topics.
        # 
        # If you add set session parallel_sql=true; to the analytic statement in the query parameter, the dedicated SQL feature is enabled. Example: \* | set session parallel_sql=true; select count(\*) as pv.
        # 
        # Note: If you specify an analytic statement in the query parameter, the line and offset parameters are invalid for this operation. In this case, we recommend that you set the line and offset parameters to 0 and use a LIMIT clause to limit the number of entries to return on each page. For more information, see the "Perform paged queries" topic.
        self.query = query  # type: str
        # Specifies whether to return logs in reverse chronological order of log timestamps. The log timestamps are accurate to the minute. Valid values:
        # 
        # true: returns logs in reverse chronological order of log timestamps. false (default): returns logs in chronological order of log timestamps. Note The reverse parameter takes effect only when the query parameter is set to a search statement. The reverse parameter specifies the method used to sort the returned logs. If the query parameter is set to a query statement, which consists of a search statement and an analytic statement, the reverse parameter does not take effect. The method used to sort the returned logs is specified by the ORDER BY clause in the analytic statement. If you use the keyword asc in the ORDER BY clause, the logs are sorted in chronological order. If you use the keyword desc in the ORDER BY clause, the logs are sorted in reverse chronological order. By default, asc is used in the ORDER BY clause.
        self.reverse = reverse  # type: bool
        self.session = session  # type: str
        # The ID of the shard.
        self.shard = shard  # type: int
        # The end of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range specified by the from and to parameters is a left-closed and right-open interval. Each interval includes the specified start time but does not include the specified end time. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: int
        # The topic of the logs. Default value: double quotation marks ("").
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward is not None:
            result['forward'] = self.forward
        if self.from_ is not None:
            result['from'] = self.from_
        if self.line is not None:
            result['line'] = self.line
        if self.offset is not None:
            result['offset'] = self.offset
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.reverse is not None:
            result['reverse'] = self.reverse
        if self.session is not None:
            result['session'] = self.session
        if self.shard is not None:
            result['shard'] = self.shard
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('forward') is not None:
            self.forward = m.get('forward')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('line') is not None:
            self.line = m.get('line')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')
        if m.get('session') is not None:
            self.session = m.get('session')
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetLogsV2ResponseBodyMeta(TeaModel):
    def __init__(self, agg_query=None, count=None, elapsed_millisecond=None, has_sql=None, is_accurate=None,
                 keys=None, processed_bytes=None, processed_rows=None, progress=None, telementry_type=None, terms=None,
                 where_query=None):
        # The SQL statement after | in the query statement.
        self.agg_query = agg_query  # type: str
        # The number of rows that are returned.
        self.count = count  # type: int
        # The amount of time that is consumed by the request. Unit: milliseconds.
        self.elapsed_millisecond = elapsed_millisecond  # type: long
        # Indicates whether the query is an SQL query.
        self.has_sql = has_sql  # type: bool
        # Indicates whether the returned result is accurate.
        self.is_accurate = is_accurate  # type: bool
        # All keys in the query result.
        self.keys = keys  # type: list[str]
        # The number of logs that are processed in the request.
        self.processed_bytes = processed_bytes  # type: long
        # The number of rows that are processed in the request.
        self.processed_rows = processed_rows  # type: int
        # Indicates whether the query result is complete. Valid values:
        # 
        # *   Complete: The query was successful, and the complete result is returned.
        # *   Incomplete: The query was successful, but the query result is incomplete. To obtain the complete result, you must call the operation again.
        self.progress = progress  # type: str
        # The type of observable data.
        self.telementry_type = telementry_type  # type: str
        # All terms in the query statement.
        self.terms = terms  # type: list[dict[str, any]]
        # The part before | in the query statement.
        self.where_query = where_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsV2ResponseBodyMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_query is not None:
            result['aggQuery'] = self.agg_query
        if self.count is not None:
            result['count'] = self.count
        if self.elapsed_millisecond is not None:
            result['elapsedMillisecond'] = self.elapsed_millisecond
        if self.has_sql is not None:
            result['hasSQL'] = self.has_sql
        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate
        if self.keys is not None:
            result['keys'] = self.keys
        if self.processed_bytes is not None:
            result['processedBytes'] = self.processed_bytes
        if self.processed_rows is not None:
            result['processedRows'] = self.processed_rows
        if self.progress is not None:
            result['progress'] = self.progress
        if self.telementry_type is not None:
            result['telementryType'] = self.telementry_type
        if self.terms is not None:
            result['terms'] = self.terms
        if self.where_query is not None:
            result['whereQuery'] = self.where_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aggQuery') is not None:
            self.agg_query = m.get('aggQuery')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('elapsedMillisecond') is not None:
            self.elapsed_millisecond = m.get('elapsedMillisecond')
        if m.get('hasSQL') is not None:
            self.has_sql = m.get('hasSQL')
        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        if m.get('processedBytes') is not None:
            self.processed_bytes = m.get('processedBytes')
        if m.get('processedRows') is not None:
            self.processed_rows = m.get('processedRows')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('telementryType') is not None:
            self.telementry_type = m.get('telementryType')
        if m.get('terms') is not None:
            self.terms = m.get('terms')
        if m.get('whereQuery') is not None:
            self.where_query = m.get('whereQuery')
        return self


class GetLogsV2ResponseBody(TeaModel):
    def __init__(self, data=None, meta=None):
        # The returned result.
        self.data = data  # type: list[dict[str, str]]
        # The metadata that is returned.
        self.meta = meta  # type: GetLogsV2ResponseBodyMeta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super(GetLogsV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('meta') is not None:
            temp_model = GetLogsV2ResponseBodyMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class GetLogsV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLogsV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogsV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLogsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogtailPipelineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogtailPipelineConfig

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogtailPipelineConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogtailPipelineConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMLServiceResultsRequest(TeaModel):
    def __init__(self, allow_builtin=None, body=None):
        self.allow_builtin = allow_builtin  # type: bool
        self.body = body  # type: MLServiceAnalysisParam

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMLServiceResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_builtin is not None:
            result['allowBuiltin'] = self.allow_builtin
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allowBuiltin') is not None:
            self.allow_builtin = m.get('allowBuiltin')
        if m.get('body') is not None:
            temp_model = MLServiceAnalysisParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMLServiceResultsResponseBody(TeaModel):
    def __init__(self, data=None, status=None):
        self.data = data  # type: list[dict[str, str]]
        self.status = status  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMLServiceResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetMLServiceResultsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMLServiceResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMLServiceResultsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMLServiceResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MachineGroup

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MachineGroup()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Project

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectLogsRequest(TeaModel):
    def __init__(self, power_sql=None, query=None):
        # Specifies whether to enable the Dedicated SQL feature. For more information, see [Enable Dedicated SQL](~~223777~~). Valid values:
        # 
        # *   true
        # *   false (default): enables the Standard SQL feature.
        # 
        # You can use the powerSql or **query** parameter to configure Dedicated SQL.
        self.power_sql = power_sql  # type: bool
        # The standard SQL statement. In this example, the SQL statement queries the number of page views (PVs) from 2022-03-01 10:41:40 to 2022-03-01 10:56:40 in a Logstore whose name is nginx-moni.
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class GetProjectLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[dict[str, str]]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetProjectLogsResponse, self).to_map()
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


class GetProjectPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super(GetProjectPolicyResponse, self).to_map()
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


class GetSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SavedSearch

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SavedSearch()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShipperStatusRequest(TeaModel):
    def __init__(self, from_=None, offset=None, size=None, status=None, to=None):
        # The start time of the log shipping job. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: long
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Default value: 100. Maximum value: 500.
        self.size = size  # type: int
        # The status of the log shipping job. This parameter is empty by default, which indicates that log shipping jobs in all states are returned. Valid values: success, fail, and running.
        self.status = status  # type: str
        # The end time of the log shipping job. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShipperStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetShipperStatusResponseBodyStatistics(TeaModel):
    def __init__(self, fail=None, running=None, success=None):
        # The number of log shipping jobs that are in the fail state.
        self.fail = fail  # type: long
        # The number of log shipping jobs that are in the running state.
        self.running = running  # type: long
        # The number of log shipping jobs that are in the success state.
        self.success = success  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShipperStatusResponseBodyStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail is not None:
            result['fail'] = self.fail
        if self.running is not None:
            result['running'] = self.running
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fail') is not None:
            self.fail = m.get('fail')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetShipperStatusResponseBodyTasks(TeaModel):
    def __init__(self, id=None, task_code=None, task_create_time=None, task_data_lines=None, task_finish_time=None,
                 task_last_data_receive_time=None, task_message=None, task_status=None):
        # The ID of the log shipping job.
        self.id = id  # type: str
        # The error code of the log shipping job.
        self.task_code = task_code  # type: str
        # The start time of the log shipping job. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.task_create_time = task_create_time  # type: long
        # The number of logs that are shipped in the log shipping job.
        self.task_data_lines = task_data_lines  # type: int
        # The end time of the log shipping job. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.task_finish_time = task_finish_time  # type: long
        # The time when Simple Log Service receives the most recent log of the log shipping job. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.task_last_data_receive_time = task_last_data_receive_time  # type: long
        # The error message of the log shipping job.
        self.task_message = task_message  # type: str
        # The status of the log shipping job. Valid values: running, success, and fail.
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShipperStatusResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.task_code is not None:
            result['taskCode'] = self.task_code
        if self.task_create_time is not None:
            result['taskCreateTime'] = self.task_create_time
        if self.task_data_lines is not None:
            result['taskDataLines'] = self.task_data_lines
        if self.task_finish_time is not None:
            result['taskFinishTime'] = self.task_finish_time
        if self.task_last_data_receive_time is not None:
            result['taskLastDataReceiveTime'] = self.task_last_data_receive_time
        if self.task_message is not None:
            result['taskMessage'] = self.task_message
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('taskCode') is not None:
            self.task_code = m.get('taskCode')
        if m.get('taskCreateTime') is not None:
            self.task_create_time = m.get('taskCreateTime')
        if m.get('taskDataLines') is not None:
            self.task_data_lines = m.get('taskDataLines')
        if m.get('taskFinishTime') is not None:
            self.task_finish_time = m.get('taskFinishTime')
        if m.get('taskLastDataReceiveTime') is not None:
            self.task_last_data_receive_time = m.get('taskLastDataReceiveTime')
        if m.get('taskMessage') is not None:
            self.task_message = m.get('taskMessage')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class GetShipperStatusResponseBody(TeaModel):
    def __init__(self, count=None, statistics=None, tasks=None, total=None):
        # The number of log shipping jobs returned on the current page.
        self.count = count  # type: long
        # The statistics about log shipping jobs.
        self.statistics = statistics  # type: GetShipperStatusResponseBodyStatistics
        # The details of log shipping jobs.
        self.tasks = tasks  # type: GetShipperStatusResponseBodyTasks
        # The total number of log shipping jobs.
        self.total = total  # type: long

    def validate(self):
        if self.statistics:
            self.statistics.validate()
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(GetShipperStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.statistics is not None:
            result['statistics'] = self.statistics.to_map()
        if self.tasks is not None:
            result['tasks'] = self.tasks.to_map()
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('statistics') is not None:
            temp_model = GetShipperStatusResponseBodyStatistics()
            self.statistics = temp_model.from_map(m['statistics'])
        if m.get('tasks') is not None:
            temp_model = GetShipperStatusResponseBodyTasks()
            self.tasks = temp_model.from_map(m['tasks'])
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetShipperStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetShipperStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetShipperStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetShipperStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationDataRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        self.offset = offset  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnnotationDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationDataResponseBody(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[MLDataParam]
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnnotationDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLDataParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAnnotationDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnnotationDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationDataSetsRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        self.offset = offset  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnnotationDataSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationDataSetsResponseBody(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[MLDataSetParam]
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnnotationDataSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLDataSetParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationDataSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAnnotationDataSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnnotationDataSetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationDataSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationLabelsRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        self.offset = offset  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnnotationLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationLabelsResponseBody(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[MLLabelParam]
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnnotationLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLLabelParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAnnotationLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnnotationLabelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionPoliciesRequestAttribute(TeaModel):
    def __init__(self, app=None, policy_group=None):
        self.app = app  # type: str
        self.policy_group = policy_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionPoliciesRequestAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['app'] = self.app
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app') is not None:
            self.app = m.get('app')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        return self


class ListCollectionPoliciesRequest(TeaModel):
    def __init__(self, attribute=None, data_code=None, instance_id=None, page_num=None, page_size=None,
                 policy_name=None, product_code=None):
        self.attribute = attribute  # type: ListCollectionPoliciesRequestAttribute
        self.data_code = data_code  # type: str
        self.instance_id = instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.policy_name = policy_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        _map = super(ListCollectionPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute.to_map()
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            temp_model = ListCollectionPoliciesRequestAttribute()
            self.attribute = temp_model.from_map(m['attribute'])
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class ListCollectionPoliciesShrinkRequest(TeaModel):
    def __init__(self, attribute_shrink=None, data_code=None, instance_id=None, page_num=None, page_size=None,
                 policy_name=None, product_code=None):
        self.attribute_shrink = attribute_shrink  # type: str
        self.data_code = data_code  # type: str
        self.instance_id = instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.policy_name = policy_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionPoliciesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_shrink is not None:
            result['attribute'] = self.attribute_shrink
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute_shrink = m.get('attribute')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class ListCollectionPoliciesResponseBodyDataAttribute(TeaModel):
    def __init__(self, app=None, policy_group=None):
        self.app = app  # type: str
        self.policy_group = policy_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionPoliciesResponseBodyDataAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['app'] = self.app
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app') is not None:
            self.app = m.get('app')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        return self


class ListCollectionPoliciesResponseBodyDataCentralizeConfig(TeaModel):
    def __init__(self, dest_logstore=None, dest_project=None, dest_region=None, dest_ttl=None):
        self.dest_logstore = dest_logstore  # type: str
        self.dest_project = dest_project  # type: str
        self.dest_region = dest_region  # type: str
        self.dest_ttl = dest_ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionPoliciesResponseBodyDataCentralizeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class ListCollectionPoliciesResponseBodyDataPolicyConfig(TeaModel):
    def __init__(self, instance_ids=None, regions=None, resource_mode=None, resource_tags=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.regions = regions  # type: list[str]
        self.resource_mode = resource_mode  # type: str
        self.resource_tags = resource_tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectionPoliciesResponseBodyDataPolicyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class ListCollectionPoliciesResponseBodyData(TeaModel):
    def __init__(self, attribute=None, centralize_config=None, centralize_enabled=None, data_code=None,
                 enabled=None, policy_config=None, policy_name=None, product_code=None):
        self.attribute = attribute  # type: ListCollectionPoliciesResponseBodyDataAttribute
        self.centralize_config = centralize_config  # type: ListCollectionPoliciesResponseBodyDataCentralizeConfig
        self.centralize_enabled = centralize_enabled  # type: bool
        self.data_code = data_code  # type: str
        self.enabled = enabled  # type: bool
        self.policy_config = policy_config  # type: ListCollectionPoliciesResponseBodyDataPolicyConfig
        self.policy_name = policy_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        if self.attribute:
            self.attribute.validate()
        if self.centralize_config:
            self.centralize_config.validate()
        if self.policy_config:
            self.policy_config.validate()

    def to_map(self):
        _map = super(ListCollectionPoliciesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute.to_map()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataAttribute()
            self.attribute = temp_model.from_map(m['attribute'])
        if m.get('centralizeConfig') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('policyConfig') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class ListCollectionPoliciesResponseBody(TeaModel):
    def __init__(self, current_count=None, data=None, total_count=None):
        self.current_count = current_count  # type: int
        self.data = data  # type: list[ListCollectionPoliciesResponseBodyData]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCollectionPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['currentCount'] = self.current_count
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currentCount') is not None:
            self.current_count = m.get('currentCount')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListCollectionPoliciesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListCollectionPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCollectionPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCollectionPoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCollectionPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRequest(TeaModel):
    def __init__(self, config_name=None, logstore_name=None, offset=None, size=None):
        self.config_name = config_name  # type: str
        self.logstore_name = logstore_name  # type: str
        self.offset = offset  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListConfigResponseBody(TeaModel):
    def __init__(self, configs=None, count=None, total=None):
        self.configs = configs  # type: list[str]
        self.count = count  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[ConsumerGroup]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConsumerGroupResponse, self).to_map()
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
                temp_model = ConsumerGroup()
                self.body.append(temp_model.from_map(k))
        return self


class ListDashboardRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        self.offset = offset  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDashboardResponseBodyDashboardItems(TeaModel):
    def __init__(self, dashboard_name=None, display_name=None):
        self.dashboard_name = dashboard_name  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardResponseBodyDashboardItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListDashboardResponseBody(TeaModel):
    def __init__(self, dashboard_items=None, dashboards=None):
        self.dashboard_items = dashboard_items  # type: list[ListDashboardResponseBodyDashboardItems]
        self.dashboards = dashboards  # type: list[str]

    def validate(self):
        if self.dashboard_items:
            for k in self.dashboard_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDashboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dashboardItems'] = []
        if self.dashboard_items is not None:
            for k in self.dashboard_items:
                result['dashboardItems'].append(k.to_map() if k else None)
        if self.dashboards is not None:
            result['dashboards'] = self.dashboards
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dashboard_items = []
        if m.get('dashboardItems') is not None:
            for k in m.get('dashboardItems'):
                temp_model = ListDashboardResponseBodyDashboardItems()
                self.dashboard_items.append(temp_model.from_map(k))
        if m.get('dashboards') is not None:
            self.dashboards = m.get('dashboards')
        return self


class ListDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDashboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDashboardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(self, domain_name=None, offset=None, size=None):
        # The domain name that is used to match custom domain names. For example, if you set domainName to `example.com`, the matched domain names are `a.example.com` and `b.example.com`.
        self.domain_name = domain_name  # type: str
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Default value: 500. Maximum value: 500.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(self, count=None, domains=None, total=None):
        # The number of domain names that are returned on the current page.
        self.count = count  # type: long
        # The domain names.
        self.domains = domains  # type: list[str]
        # The total number of domain names that are returned.
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.domains is not None:
            result['domains'] = self.domains
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExternalStoreRequest(TeaModel):
    def __init__(self, external_store_name=None, offset=None, sizs=None):
        # The name of the external store. You can query external stores that contain a specified string.
        self.external_store_name = external_store_name  # type: str
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Maximum value: 500.
        self.sizs = sizs  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExternalStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.sizs is not None:
            result['sizs'] = self.sizs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('sizs') is not None:
            self.sizs = m.get('sizs')
        return self


class ListExternalStoreResponseBody(TeaModel):
    def __init__(self, count=None, externalstores=None, total=None):
        # The number of external stores returned on the current page.
        self.count = count  # type: int
        # The names of the external stores.
        self.externalstores = externalstores  # type: list[ExternalStore]
        # The number of external stores that meet the query conditions.
        self.total = total  # type: int

    def validate(self):
        if self.externalstores:
            for k in self.externalstores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExternalStoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['externalstores'] = []
        if self.externalstores is not None:
            for k in self.externalstores:
                result['externalstores'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.externalstores = []
        if m.get('externalstores') is not None:
            for k in m.get('externalstores'):
                temp_model = ExternalStore()
                self.externalstores.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExternalStoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExternalStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExternalStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogStoresRequest(TeaModel):
    def __init__(self, logstore_name=None, mode=None, offset=None, size=None, telemetry_type=None):
        # The name of the Logstore. Fuzzy match is supported. For example, if you enter test, Logstores whose name contains test are returned.
        self.logstore_name = logstore_name  # type: str
        # The type of the Logstore. Valid values: standard and query.
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the volume of data is large, the log retention period is long, or log analysis is not required. Log retention periods of weeks or months are considered long.
        self.mode = mode  # type: str
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.size = size  # type: int
        # The type of the data that you want to query. Valid values:
        # 
        # *   None: logs
        # *   Metrics: metrics
        self.telemetry_type = telemetry_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogStoresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.mode is not None:
            result['mode'] = self.mode
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        return self


class ListLogStoresResponseBody(TeaModel):
    def __init__(self, count=None, logstores=None, total=None):
        # The number of entries that are returned on the current page.
        self.count = count  # type: int
        # The Logstores that meet the query conditions.
        self.logstores = logstores  # type: list[str]
        # The number of the Logstores that meet the query conditions.
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogStoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.logstores is not None:
            result['logstores'] = self.logstores
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('logstores') is not None:
            self.logstores = m.get('logstores')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListLogStoresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLogStoresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogStoresResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogtailPipelineConfigRequest(TeaModel):
    def __init__(self, config_name=None, logstore_name=None, offset=None, size=None):
        self.config_name = config_name  # type: str
        self.logstore_name = logstore_name  # type: str
        self.offset = offset  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogtailPipelineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListLogtailPipelineConfigResponseBody(TeaModel):
    def __init__(self, configs=None, count=None, total=None):
        self.configs = configs  # type: list[str]
        self.count = count  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogtailPipelineConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListLogtailPipelineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLogtailPipelineConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogtailPipelineConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogtailPipelineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachineGroupRequest(TeaModel):
    def __init__(self, group_name=None, offset=None, size=None):
        # The name of the machine group. This parameter is used to filter machine groups. Partial match is supported.
        self.group_name = group_name  # type: str
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Maximum value: 500.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMachineGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMachineGroupResponseBody(TeaModel):
    def __init__(self, count=None, machinegroups=None, total=None):
        # The number of machine groups that are returned on the current page.
        self.count = count  # type: int
        # The machine groups that meet the query conditions.
        self.machinegroups = machinegroups  # type: list[str]
        # The total number of machine groups that meet the query conditions.
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMachineGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.machinegroups is not None:
            result['machinegroups'] = self.machinegroups
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('machinegroups') is not None:
            self.machinegroups = m.get('machinegroups')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMachineGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMachineGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachinesRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Default value: 100. Maximum value: 500.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMachinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMachinesResponseBody(TeaModel):
    def __init__(self, count=None, machines=None, total=None):
        # The number of machines that are returned on the current page.
        self.count = count  # type: int
        # The machines that are returned.
        self.machines = machines  # type: list[Machine]
        # The total number of machines.
        self.total = total  # type: int

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMachinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = Machine()
                self.machines.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMachinesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMachinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMachinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMachinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(self, offset=None, project_name=None, resource_group_id=None, size=None):
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The name of the project.
        self.project_name = project_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The number of entries per page. Default value: 100. This operation can return up to 500 projects.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(self, count=None, projects=None, total=None):
        # The number of returned projects on the current page.
        self.count = count  # type: long
        # The projects that meet the query conditions.
        self.projects = projects  # type: list[Project]
        # The total number of projects that meet the query conditions.
        self.total = total  # type: long

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavedSearchRequest(TeaModel):
    def __init__(self, offset=None, size=None):
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Maximum value: 500.
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSavedSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSavedSearchResponseBody(TeaModel):
    def __init__(self, count=None, savedsearch_items=None, total=None):
        # The number of saved searches returned on the current page.
        self.count = count  # type: int
        # The saved searches.
        self.savedsearch_items = savedsearch_items  # type: list[SavedSearch]
        # The total number of saved searches that meet the query conditions.
        self.total = total  # type: int

    def validate(self):
        if self.savedsearch_items:
            for k in self.savedsearch_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSavedSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['savedsearchItems'] = []
        if self.savedsearch_items is not None:
            for k in self.savedsearch_items:
                result['savedsearchItems'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.savedsearch_items = []
        if m.get('savedsearchItems') is not None:
            for k in m.get('savedsearchItems'):
                temp_model = SavedSearch()
                self.savedsearch_items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSavedSearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSavedSearchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSavedSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Shard]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListShardsResponse, self).to_map()
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
                temp_model = Shard()
                self.body.append(temp_model.from_map(k))
        return self


class ListShipperResponseBody(TeaModel):
    def __init__(self, count=None, shipper=None, total=None):
        # The number of log shipping jobs returned.
        self.count = count  # type: long
        # The names of the log shipping jobs.
        self.shipper = shipper  # type: list[str]
        # The total number of log shipping jobs.
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListShipperResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.shipper is not None:
            result['shipper'] = self.shipper
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('shipper') is not None:
            self.shipper = m.get('shipper')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListShipperResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListShipperResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListShipperResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListShipperResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag that you want to use to filter resources. For example, if you set the key to `"test-key"`, only resources to which the key is added are returned.``
        self.key = key  # type: str
        # The value of the tag that you want to use to filter resources. If you set the value to null, resources are filtered based only on the key of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTags, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tags=None):
        # The IDs of the resources for which you want to query tags. You must specify at least one of resourceId and tags.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Set the value to project.
        self.resource_type = resource_type  # type: str
        # The tags that you want to use to filter resources based on exact match. Each tag is a key-value pair. You must specify at least one of resourceId and tags.
        # 
        # You can enter up to 20 tags.
        self.tags = tags  # type: list[ListTagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(self, resource_id_shrink=None, resource_type=None, tags_shrink=None):
        # The IDs of the resources for which you want to query tags. You must specify at least one of resourceId and tags.
        self.resource_id_shrink = resource_id_shrink  # type: str
        # The type of the resource. Set the value to project.
        self.resource_type = resource_type  # type: str
        # The tags that you want to use to filter resources based on exact match. Each tag is a key-value pair. You must specify at least one of resourceId and tags.
        # 
        # You can enter up to 20 tags.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, tag_resources=None):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The returned tags.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['tagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['tagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.tag_resources = []
        if m.get('tagResources') is not None:
            for k in m.get('tagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAnnotationDataRequest(TeaModel):
    def __init__(self, annotationdata_id=None, ml_data_param=None, raw_log=None):
        self.annotationdata_id = annotationdata_id  # type: str
        self.ml_data_param = ml_data_param  # type: MLDataParam
        self.raw_log = raw_log  # type: list[dict[str, str]]

    def validate(self):
        if self.ml_data_param:
            self.ml_data_param.validate()

    def to_map(self):
        _map = super(PutAnnotationDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id
        if self.ml_data_param is not None:
            result['mlDataParam'] = self.ml_data_param.to_map()
        if self.raw_log is not None:
            result['rawLog'] = self.raw_log
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')
        if m.get('mlDataParam') is not None:
            temp_model = MLDataParam()
            self.ml_data_param = temp_model.from_map(m['mlDataParam'])
        if m.get('rawLog') is not None:
            self.raw_log = m.get('rawLog')
        return self


class PutAnnotationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(PutAnnotationDataResponse, self).to_map()
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


class PutProjectPolicyRequest(TeaModel):
    def __init__(self, body=None):
        # The project policy.
        self.body = body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProjectPolicyRequest, self).to_map()
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


class PutProjectPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(PutProjectPolicyResponse, self).to_map()
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


class PutProjectTransferAccelerationRequest(TeaModel):
    def __init__(self, enabled=None):
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProjectTransferAccelerationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class PutProjectTransferAccelerationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(PutProjectTransferAccelerationResponse, self).to_map()
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


class PutWebtrackingRequest(TeaModel):
    def __init__(self, logs=None, source=None, tags=None, topic=None):
        self.logs = logs  # type: list[dict[str, str]]
        self.source = source  # type: str
        self.tags = tags  # type: dict[str, str]
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutWebtrackingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['__logs__'] = self.logs
        if self.source is not None:
            result['__source__'] = self.source
        if self.tags is not None:
            result['__tags__'] = self.tags
        if self.topic is not None:
            result['__topic__'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('__logs__') is not None:
            self.logs = m.get('__logs__')
        if m.get('__source__') is not None:
            self.source = m.get('__source__')
        if m.get('__tags__') is not None:
            self.tags = m.get('__tags__')
        if m.get('__topic__') is not None:
            self.topic = m.get('__topic__')
        return self


class PutWebtrackingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(PutWebtrackingResponse, self).to_map()
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


class QueryMLServiceResultsRequest(TeaModel):
    def __init__(self, allow_builtin=None, body=None):
        self.allow_builtin = allow_builtin  # type: bool
        self.body = body  # type: MLServiceAnalysisParam

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMLServiceResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_builtin is not None:
            result['allowBuiltin'] = self.allow_builtin
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allowBuiltin') is not None:
            self.allow_builtin = m.get('allowBuiltin')
        if m.get('body') is not None:
            temp_model = MLServiceAnalysisParam()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMLServiceResultsResponseBody(TeaModel):
    def __init__(self, data=None, status=None):
        self.data = data  # type: list[dict[str, str]]
        self.status = status  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMLServiceResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryMLServiceResultsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMLServiceResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMLServiceResultsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMLServiceResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveConfigFromMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(RemoveConfigFromMachineGroupResponse, self).to_map()
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


class SplitShardRequest(TeaModel):
    def __init__(self, key=None, shard_count=None):
        # The position where the shard is split.
        self.key = key  # type: str
        # The number of new shards that are generated after splitting.
        self.shard_count = shard_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SplitShardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        return self


class SplitShardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[Shard]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SplitShardResponse, self).to_map()
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
                temp_model = Shard()
                self.body.append(temp_model.from_map(k))
        return self


class TagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. The key must meet the following requirements:
        # 
        # *   The key must be `1 to 128` characters in length.
        # *   The key cannot contain `"http://"` or `"https://"`.
        # *   The key cannot start with `"acs:"` or `"aliyun"`.
        self.key = key  # type: str
        # The value of the tag. The value must meet the following requirements:
        # 
        # *   The value must be `1 to 128` characters in length.
        # *   The value cannot contain `"http://"` or `"https://"`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTags, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tags=None):
        # The resource IDs. You can specify only one resource and add tags to the resource.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Set the value to project.
        self.resource_type = resource_type  # type: str
        # The tags that you want to add to the resource. Up to 20 tags are supported at a time. Each tag is a key-value pair.
        self.tags = tags  # type: list[TagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tags=None):
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tags = tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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


class UpdateAnnotationDataSetRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: MLDataSetParam

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAnnotationDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnnotationDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateAnnotationDataSetResponse, self).to_map()
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


class UpdateAnnotationLabelRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: MLLabelParam

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAnnotationLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnnotationLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateAnnotationLabelResponse, self).to_map()
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


class UpdateConfigRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: LogtailConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateConfigResponse, self).to_map()
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


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(self, order=None, timeout=None):
        # Specifies whether to consume data in sequence. Valid values:
        # 
        # *   true: If a shard is split, the data in the original shard is consumed first. Then, the data in the new shards is consumed at the same time. If shards are merged, the data in the original shards is consumed first. Then, the data in the new shard is consumed.
        # *   false: The data in all shards is consumed at the same time. If a new shard is generated after a shard is split or shards are merged, the data in the new shard is immediately consumed.
        self.order = order  # type: bool
        # The timeout period. If Simple Log Service does not receive heartbeats from a consumer within the timeout period, Simple Log Service deletes the consumer. Unit: seconds.
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConsumerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateConsumerGroupResponse, self).to_map()
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


class UpdateDashboardRequest(TeaModel):
    def __init__(self, attribute=None, charts=None, dashboard_name=None, description=None, display_name=None):
        self.attribute = attribute  # type: dict[str, str]
        self.charts = charts  # type: list[Chart]
        self.dashboard_name = dashboard_name  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        if self.charts:
            for k in self.charts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateDashboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute
        result['charts'] = []
        if self.charts is not None:
            for k in self.charts:
                result['charts'].append(k.to_map() if k else None)
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        self.charts = []
        if m.get('charts') is not None:
            for k in m.get('charts'):
                temp_model = Chart()
                self.charts.append(temp_model.from_map(k))
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class UpdateDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateDashboardResponse, self).to_map()
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


class UpdateIndexRequestLine(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, exclude_keys=None, include_keys=None, token=None):
        # Specifies whether to enable case sensitivity. Valid values:
        # 
        # *   true
        # *   false
        self.case_sensitive = case_sensitive  # type: bool
        # Specifies whether to include Chinese characters. Valid values:
        # 
        # *   true
        # *   false
        self.chn = chn  # type: bool
        # The excluded fields. You cannot specify both include_keys and exclude_keys.
        self.exclude_keys = exclude_keys  # type: list[str]
        # The included fields. You cannot specify both include_keys and exclude_keys.
        self.include_keys = include_keys  # type: list[str]
        # The delimiters that are used to split text.
        self.token = token  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIndexRequestLine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class UpdateIndexRequest(TeaModel):
    def __init__(self, keys=None, line=None, log_reduce=None, log_reduce_black_list=None,
                 log_reduce_white_list=None, max_text_len=None, ttl=None):
        # The configuration of field indexes. A field index is a key-value pair in which the key specifies the name of the field and the value specifies the index configuration of the field.
        self.keys = keys  # type: dict[str, KeysValue]
        # The configuration of full-text indexes.
        self.line = line  # type: UpdateIndexRequestLine
        # Specifies whether to turn on LogReduce. If you turn on LogReduce, only one of `log_reduce_white_list` and `log_reduce_black_list` takes effect.
        self.log_reduce = log_reduce  # type: bool
        # The fields in the blacklist that you want to use to cluster logs.
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # The fields in the whitelist that you want to use to cluster logs.
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # The maximum length of a field value that can be retained.
        self.max_text_len = max_text_len  # type: int
        # The retention period of data. Unit: days. Valid values: 7, 30, and 90.
        self.ttl = ttl  # type: int

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super(UpdateIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = KeysValue()
                self.keys[k] = temp_model.from_map(v)
        if m.get('line') is not None:
            temp_model = UpdateIndexRequestLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateIndexResponse, self).to_map()
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


class UpdateLogStoreRequest(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, encrypt_conf=None, hot_ttl=None,
                 infrequent_access_ttl=None, logstore_name=None, max_split_shard=None, mode=None, shard_count=None, telemetry_type=None,
                 ttl=None):
        # Specifies whether to record public IP addresses. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta  # type: bool
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split  # type: bool
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking  # type: bool
        # The data structure of the encryption configuration.
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        # The retention period of data in the hot storage tier of the Logstore. Minimum value: 30. Unit: day. You can specify a value that ranges from 30 to the value of ttl. Hot data that is stored for longer than the period specified by hot_ttl is converted to cold data. For more information, see [Enable hot and cold-tiered storage for a Logstore](~~308645~~).
        self.hot_ttl = hot_ttl  # type: int
        self.infrequent_access_ttl = infrequent_access_ttl  # type: int
        # The name of the Logstore.
        self.logstore_name = logstore_name  # type: str
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 64.
        # 
        # > If you set autoSplit to true, you must specify maxSplitShard.
        self.max_split_shard = max_split_shard  # type: int
        # The type of the Logstore. Simple Log Service provides two types of Logstores: Standard Logstores and Query Logstores.
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the volume of data is large, the log retention period is long, or log analysis is not required. Log retention periods of weeks or months are considered long.
        self.mode = mode  # type: str
        # The number of shards.
        # 
        # > You cannot call the UpdateLogstore operation to change the number of shards. You can call the SplitShard or MergeShards operation to change the number of shards.
        self.shard_count = shard_count  # type: int
        # The type of the log that you want to query. Valid values:
        # 
        # *   None: all types of logs.
        # *   Metrics: metrics.
        self.telemetry_type = telemetry_type  # type: str
        # The retention period of data. Unit: day. Valid values: 1 to 3650. If you set ttl to 3650, data is permanently stored.
        self.ttl = ttl  # type: int

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super(UpdateLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateLogStoreResponse, self).to_map()
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


class UpdateLogStoreMeteringModeRequest(TeaModel):
    def __init__(self, metering_mode=None):
        self.metering_mode = metering_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogStoreMeteringModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class UpdateLogStoreMeteringModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateLogStoreMeteringModeResponse, self).to_map()
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


class UpdateLoggingRequestLoggingDetails(TeaModel):
    def __init__(self, logstore=None, type=None):
        # The name of the Logstore to which you want to save service logs.
        self.logstore = logstore  # type: str
        # The type of service logs. Valid values:
        # 
        # *   consumergroup_log: the consumption delay logs of consumer groups.
        # *   logtail_alarm: the alert logs of Logtail.
        # *   operation_log: the operation logs.
        # *   logtail_profile: the collection logs of Logtail.
        # *   metering: the metering logs.
        # *   logtail_status: the status logs of Logtail.
        # *   scheduledsqlalert: the operational logs of Scheduled SQL jobs.
        # *   etl_alert: the operational logs of data transformation jobs.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoggingRequestLoggingDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateLoggingRequest(TeaModel):
    def __init__(self, logging_details=None, logging_project=None):
        # The configurations of service logs.
        self.logging_details = logging_details  # type: list[UpdateLoggingRequestLoggingDetails]
        # The name of the project to which you want to save service logs.
        self.logging_project = logging_project  # type: str

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateLoggingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = UpdateLoggingRequestLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class UpdateLoggingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateLoggingResponse, self).to_map()
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


class UpdateLogtailPipelineConfigRequest(TeaModel):
    def __init__(self, aggregators=None, config_name=None, flushers=None, global_=None, inputs=None, log_sample=None,
                 processors=None):
        self.aggregators = aggregators  # type: list[dict[str, any]]
        self.config_name = config_name  # type: str
        self.flushers = flushers  # type: list[dict[str, any]]
        self.global_ = global_  # type: dict[str, any]
        self.inputs = inputs  # type: list[dict[str, any]]
        self.log_sample = log_sample  # type: str
        self.processors = processors  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogtailPipelineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class UpdateLogtailPipelineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateLogtailPipelineConfigResponse, self).to_map()
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


class UpdateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(self, external_name=None, group_topic=None):
        # The identifier of the external management system on which the machine group depends. This parameter is empty by default.
        self.external_name = external_name  # type: str
        # The topic of the machine group. This parameter is empty by default.
        self.group_topic = group_topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMachineGroupRequestGroupAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class UpdateMachineGroupRequest(TeaModel):
    def __init__(self, group_attribute=None, group_name=None, group_type=None, machine_identify_type=None,
                 machine_list=None):
        # The attribute of the machine group. This parameter is empty by default.
        self.group_attribute = group_attribute  # type: UpdateMachineGroupRequestGroupAttribute
        # The name of the machine group.
        self.group_name = group_name  # type: str
        # The type of the machine group. Set the value to an empty string.
        self.group_type = group_type  # type: str
        # The identifier type of the machine group. Valid values:
        # 
        # *   ip: The machine group uses IP addresses as identifiers.
        # *   userdefined: The machine group uses custom identifiers.
        self.machine_identify_type = machine_identify_type  # type: str
        # The identifiers of the machines in the machine group.
        # 
        # *   If you set machineIdentifyType to ip, enter the IP addresses of the machines.
        # *   If you set machineIdentifyType to userdefined, enter a custom identifier.
        self.machine_list = machine_list  # type: list[str]

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super(UpdateMachineGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = UpdateMachineGroupRequestGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class UpdateMachineGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateMachineGroupResponse, self).to_map()
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


class UpdateMachineGroupMachineRequest(TeaModel):
    def __init__(self, action=None, body=None):
        # The operation on the machine. Valid values: add and delete. A value of add specifies to add the machine to the machine group. A value of delete specifies to remove the machine from the machine group.
        self.action = action  # type: str
        # The machines to be added or removed.
        self.body = body  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMachineGroupMachineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateMachineGroupMachineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateMachineGroupMachineResponse, self).to_map()
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


class UpdateOssExternalStoreRequestParameterColumns(TeaModel):
    def __init__(self, name=None, type=None):
        # The key of the field.
        self.name = name  # type: str
        # The type of the field.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssExternalStoreRequestParameterColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateOssExternalStoreRequestParameter(TeaModel):
    def __init__(self, accessid=None, accesskey=None, bucket=None, columns=None, endpoint=None, objects=None):
        # The AccessKey ID of your account.
        self.accessid = accessid  # type: str
        # The AccessKey secret of your account.
        self.accesskey = accesskey  # type: str
        # The name of the OSS bucket.
        self.bucket = bucket  # type: str
        # The associated fields.
        self.columns = columns  # type: list[UpdateOssExternalStoreRequestParameterColumns]
        # The OSS endpoint.
        self.endpoint = endpoint  # type: str
        # The associated objects.
        self.objects = objects  # type: list[str]

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateOssExternalStoreRequestParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['accessid'] = self.accessid
        if self.accesskey is not None:
            result['accesskey'] = self.accesskey
        if self.bucket is not None:
            result['bucket'] = self.bucket
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.objects is not None:
            result['objects'] = self.objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessid') is not None:
            self.accessid = m.get('accessid')
        if m.get('accesskey') is not None:
            self.accesskey = m.get('accesskey')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = UpdateOssExternalStoreRequestParameterColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('objects') is not None:
            self.objects = m.get('objects')
        return self


class UpdateOssExternalStoreRequest(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # The name of the external store.
        self.external_store_name = external_store_name  # type: str
        # The parameters that are configured for the external store.
        self.parameter = parameter  # type: UpdateOssExternalStoreRequestParameter
        # The type of the external store. Set the value to oss.
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(UpdateOssExternalStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = UpdateOssExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class UpdateOssExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateOssExternalStoreResponse, self).to_map()
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


class UpdateProjectRequest(TeaModel):
    def __init__(self, description=None):
        # The description of the project. The default value is an empty string.
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
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


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
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


class UpdateRdsExternalStoreRequestParameter(TeaModel):
    def __init__(self, db=None, host=None, instance_id=None, password=None, port=None, region=None, table=None,
                 username=None, vpc_id=None):
        # The name of the database in the ApsaraDB RDS for MySQL instance.
        self.db = db  # type: str
        # The internal or public endpoint of the ApsaraDB RDS for MySQL instance.
        self.host = host  # type: str
        # The ID of the ApsaraDB RDS for MySQL instance.
        self.instance_id = instance_id  # type: str
        # The password that is used to log on to the ApsaraDB RDS for MySQL instance.
        self.password = password  # type: str
        # The internal or public port of the ApsaraDB RDS for MySQL instance.
        self.port = port  # type: str
        # The region where the ApsaraDB RDS for MySQL instance resides. Valid values: cn-qingdao, cn-beijing, and cn-hangzhou.
        self.region = region  # type: str
        # The name of the database table in the ApsaraDB RDS for MySQL instance.
        self.table = table  # type: str
        # The username that is used to log on to the ApsaraDB RDS for MySQL instance.
        self.username = username  # type: str
        # The ID of the VPC to which the ApsaraDB RDS for MySQL instance belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRdsExternalStoreRequestParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['db'] = self.db
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instance-id'] = self.instance_id
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.region is not None:
            result['region'] = self.region
        if self.table is not None:
            result['table'] = self.table
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpc-id'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instance-id') is not None:
            self.instance_id = m.get('instance-id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpc-id') is not None:
            self.vpc_id = m.get('vpc-id')
        return self


class UpdateRdsExternalStoreRequest(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # The name of the external store.
        self.external_store_name = external_store_name  # type: str
        # The parameter struct.
        self.parameter = parameter  # type: UpdateRdsExternalStoreRequestParameter
        # The storage type. Set the value to rds-vpc, which indicates an ApsaraDB RDS for MySQL database in a virtual private cloud (VPC).
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(UpdateRdsExternalStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = UpdateRdsExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class UpdateRdsExternalStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateRdsExternalStoreResponse, self).to_map()
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


class UpdateSavedSearchRequest(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        # The display name.
        self.display_name = display_name  # type: str
        # The name of the Logstore to which the saved search belongs.
        self.logstore = logstore  # type: str
        # The name of the saved search. The name must be 3 to 63 characters in length.
        self.savedsearch_name = savedsearch_name  # type: str
        # The search statement or the query statement of the saved search. A query statement consists of a search statement and an analytic statement in the Search statement|Analytic statement format.
        # 
        # For more information, see Log search overview and Log analysis overview.
        self.search_query = search_query  # type: str
        # The topic of the logs.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSavedSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class UpdateSavedSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateSavedSearchResponse, self).to_map()
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


class UpsertCollectionPolicyRequestAttribute(TeaModel):
    def __init__(self, app=None, policy_group=None):
        self.app = app  # type: str
        self.policy_group = policy_group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionPolicyRequestAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['app'] = self.app
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app') is not None:
            self.app = m.get('app')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        return self


class UpsertCollectionPolicyRequestCentralizeConfig(TeaModel):
    def __init__(self, dest_logstore=None, dest_project=None, dest_region=None, dest_ttl=None):
        self.dest_logstore = dest_logstore  # type: str
        self.dest_project = dest_project  # type: str
        self.dest_region = dest_region  # type: str
        self.dest_ttl = dest_ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionPolicyRequestCentralizeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class UpsertCollectionPolicyRequestPolicyConfig(TeaModel):
    def __init__(self, instance_ids=None, regions=None, resource_mode=None, resource_tags=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.regions = regions  # type: list[str]
        self.resource_mode = resource_mode  # type: str
        self.resource_tags = resource_tags  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionPolicyRequestPolicyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class UpsertCollectionPolicyRequest(TeaModel):
    def __init__(self, attribute=None, centralize_config=None, centralize_enabled=None, data_code=None,
                 enabled=None, policy_config=None, policy_name=None, product_code=None):
        self.attribute = attribute  # type: UpsertCollectionPolicyRequestAttribute
        self.centralize_config = centralize_config  # type: UpsertCollectionPolicyRequestCentralizeConfig
        self.centralize_enabled = centralize_enabled  # type: bool
        self.data_code = data_code  # type: str
        self.enabled = enabled  # type: bool
        self.policy_config = policy_config  # type: UpsertCollectionPolicyRequestPolicyConfig
        self.policy_name = policy_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        if self.attribute:
            self.attribute.validate()
        if self.centralize_config:
            self.centralize_config.validate()
        if self.policy_config:
            self.policy_config.validate()

    def to_map(self):
        _map = super(UpsertCollectionPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute.to_map()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attribute') is not None:
            temp_model = UpsertCollectionPolicyRequestAttribute()
            self.attribute = temp_model.from_map(m['attribute'])
        if m.get('centralizeConfig') is not None:
            temp_model = UpsertCollectionPolicyRequestCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('policyConfig') is not None:
            temp_model = UpsertCollectionPolicyRequestPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class UpsertCollectionPolicyResponseBody(TeaModel):
    def __init__(self, message=None):
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpsertCollectionPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpsertCollectionPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpsertCollectionPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpsertCollectionPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpsertCollectionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


