# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AutofeExperimentConfigurationOdpsConfig(TeaModel):
    def __init__(self, odps_access_id=None, odps_access_key=None, odps_endpoint=None, odps_project_name=None,
                 odps_region_id=None, odps_role_arn=None):
        self.odps_access_id = odps_access_id  # type: str
        self.odps_access_key = odps_access_key  # type: str
        self.odps_endpoint = odps_endpoint  # type: str
        self.odps_project_name = odps_project_name  # type: str
        self.odps_region_id = odps_region_id  # type: str
        self.odps_role_arn = odps_role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AutofeExperimentConfigurationOdpsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.odps_access_id is not None:
            result['odps_access_id'] = self.odps_access_id
        if self.odps_access_key is not None:
            result['odps_access_key'] = self.odps_access_key
        if self.odps_endpoint is not None:
            result['odps_endpoint'] = self.odps_endpoint
        if self.odps_project_name is not None:
            result['odps_project_name'] = self.odps_project_name
        if self.odps_region_id is not None:
            result['odps_region_id'] = self.odps_region_id
        if self.odps_role_arn is not None:
            result['odps_role_arn'] = self.odps_role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('odps_access_id') is not None:
            self.odps_access_id = m.get('odps_access_id')
        if m.get('odps_access_key') is not None:
            self.odps_access_key = m.get('odps_access_key')
        if m.get('odps_endpoint') is not None:
            self.odps_endpoint = m.get('odps_endpoint')
        if m.get('odps_project_name') is not None:
            self.odps_project_name = m.get('odps_project_name')
        if m.get('odps_region_id') is not None:
            self.odps_region_id = m.get('odps_region_id')
        if m.get('odps_role_arn') is not None:
            self.odps_role_arn = m.get('odps_role_arn')
        return self


class AutofeExperimentConfigurationOssConfig(TeaModel):
    def __init__(self, oss_access_id=None, oss_access_key=None, oss_bucket=None, oss_endpoint=None,
                 oss_role_arn=None):
        self.oss_access_id = oss_access_id  # type: str
        self.oss_access_key = oss_access_key  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_role_arn = oss_role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AutofeExperimentConfigurationOssConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_access_id is not None:
            result['oss_access_id'] = self.oss_access_id
        if self.oss_access_key is not None:
            result['oss_access_key'] = self.oss_access_key
        if self.oss_bucket is not None:
            result['oss_bucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['oss_endpoint'] = self.oss_endpoint
        if self.oss_role_arn is not None:
            result['oss_role_arn'] = self.oss_role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('oss_access_id') is not None:
            self.oss_access_id = m.get('oss_access_id')
        if m.get('oss_access_key') is not None:
            self.oss_access_key = m.get('oss_access_key')
        if m.get('oss_bucket') is not None:
            self.oss_bucket = m.get('oss_bucket')
        if m.get('oss_endpoint') is not None:
            self.oss_endpoint = m.get('oss_endpoint')
        if m.get('oss_role_arn') is not None:
            self.oss_role_arn = m.get('oss_role_arn')
        return self


class AutofeExperimentConfigurationYmlConfig(TeaModel):
    def __init__(self, action=None, aggregate_only=None, analyze_exp_id=None, cpu=None, data_partition=None,
                 data_source=None, data_type=None, debug_mode=None, exclude_columns=None, feature_selection=None,
                 filter_thresh=None, iv_thresh=None, label=None, memory=None, output_config_oss_dir=None, pipeline_exp_id=None,
                 reuse_results=None, sample_ratio=None, sample_size=None, selection_exp_id=None, skip_select=None, workers=None,
                 workspace_name=None):
        self.action = action  # type: str
        self.aggregate_only = aggregate_only  # type: str
        self.analyze_exp_id = analyze_exp_id  # type: str
        self.cpu = cpu  # type: str
        self.data_partition = data_partition  # type: str
        self.data_source = data_source  # type: str
        self.data_type = data_type  # type: str
        self.debug_mode = debug_mode  # type: str
        self.exclude_columns = exclude_columns  # type: str
        self.feature_selection = feature_selection  # type: str
        self.filter_thresh = filter_thresh  # type: str
        self.iv_thresh = iv_thresh  # type: str
        self.label = label  # type: str
        self.memory = memory  # type: str
        self.output_config_oss_dir = output_config_oss_dir  # type: str
        self.pipeline_exp_id = pipeline_exp_id  # type: str
        self.reuse_results = reuse_results  # type: str
        self.sample_ratio = sample_ratio  # type: str
        self.sample_size = sample_size  # type: str
        self.selection_exp_id = selection_exp_id  # type: str
        self.skip_select = skip_select  # type: str
        self.workers = workers  # type: str
        self.workspace_name = workspace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AutofeExperimentConfigurationYmlConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.aggregate_only is not None:
            result['aggregate_only'] = self.aggregate_only
        if self.analyze_exp_id is not None:
            result['analyze_exp_id'] = self.analyze_exp_id
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.data_partition is not None:
            result['data_partition'] = self.data_partition
        if self.data_source is not None:
            result['data_source'] = self.data_source
        if self.data_type is not None:
            result['data_type'] = self.data_type
        if self.debug_mode is not None:
            result['debug_mode'] = self.debug_mode
        if self.exclude_columns is not None:
            result['exclude_columns'] = self.exclude_columns
        if self.feature_selection is not None:
            result['feature_selection'] = self.feature_selection
        if self.filter_thresh is not None:
            result['filter_thresh'] = self.filter_thresh
        if self.iv_thresh is not None:
            result['iv_thresh'] = self.iv_thresh
        if self.label is not None:
            result['label'] = self.label
        if self.memory is not None:
            result['memory'] = self.memory
        if self.output_config_oss_dir is not None:
            result['output_config_oss_dir'] = self.output_config_oss_dir
        if self.pipeline_exp_id is not None:
            result['pipeline_exp_id'] = self.pipeline_exp_id
        if self.reuse_results is not None:
            result['reuse_results'] = self.reuse_results
        if self.sample_ratio is not None:
            result['sample_ratio'] = self.sample_ratio
        if self.sample_size is not None:
            result['sample_size'] = self.sample_size
        if self.selection_exp_id is not None:
            result['selection_exp_id'] = self.selection_exp_id
        if self.skip_select is not None:
            result['skip_select'] = self.skip_select
        if self.workers is not None:
            result['workers'] = self.workers
        if self.workspace_name is not None:
            result['workspace_name'] = self.workspace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('aggregate_only') is not None:
            self.aggregate_only = m.get('aggregate_only')
        if m.get('analyze_exp_id') is not None:
            self.analyze_exp_id = m.get('analyze_exp_id')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('data_partition') is not None:
            self.data_partition = m.get('data_partition')
        if m.get('data_source') is not None:
            self.data_source = m.get('data_source')
        if m.get('data_type') is not None:
            self.data_type = m.get('data_type')
        if m.get('debug_mode') is not None:
            self.debug_mode = m.get('debug_mode')
        if m.get('exclude_columns') is not None:
            self.exclude_columns = m.get('exclude_columns')
        if m.get('feature_selection') is not None:
            self.feature_selection = m.get('feature_selection')
        if m.get('filter_thresh') is not None:
            self.filter_thresh = m.get('filter_thresh')
        if m.get('iv_thresh') is not None:
            self.iv_thresh = m.get('iv_thresh')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('output_config_oss_dir') is not None:
            self.output_config_oss_dir = m.get('output_config_oss_dir')
        if m.get('pipeline_exp_id') is not None:
            self.pipeline_exp_id = m.get('pipeline_exp_id')
        if m.get('reuse_results') is not None:
            self.reuse_results = m.get('reuse_results')
        if m.get('sample_ratio') is not None:
            self.sample_ratio = m.get('sample_ratio')
        if m.get('sample_size') is not None:
            self.sample_size = m.get('sample_size')
        if m.get('selection_exp_id') is not None:
            self.selection_exp_id = m.get('selection_exp_id')
        if m.get('skip_select') is not None:
            self.skip_select = m.get('skip_select')
        if m.get('workers') is not None:
            self.workers = m.get('workers')
        if m.get('workspace_name') is not None:
            self.workspace_name = m.get('workspace_name')
        return self


class AutofeExperimentConfiguration(TeaModel):
    def __init__(self, odps_config=None, oss_config=None, yml_config=None):
        self.odps_config = odps_config  # type: AutofeExperimentConfigurationOdpsConfig
        self.oss_config = oss_config  # type: AutofeExperimentConfigurationOssConfig
        self.yml_config = yml_config  # type: AutofeExperimentConfigurationYmlConfig

    def validate(self):
        if self.odps_config:
            self.odps_config.validate()
        if self.oss_config:
            self.oss_config.validate()
        if self.yml_config:
            self.yml_config.validate()

    def to_map(self):
        _map = super(AutofeExperimentConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.odps_config is not None:
            result['odps_config'] = self.odps_config.to_map()
        if self.oss_config is not None:
            result['oss_config'] = self.oss_config.to_map()
        if self.yml_config is not None:
            result['yml_config'] = self.yml_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('odps_config') is not None:
            temp_model = AutofeExperimentConfigurationOdpsConfig()
            self.odps_config = temp_model.from_map(m['odps_config'])
        if m.get('oss_config') is not None:
            temp_model = AutofeExperimentConfigurationOssConfig()
            self.oss_config = temp_model.from_map(m['oss_config'])
        if m.get('yml_config') is not None:
            temp_model = AutofeExperimentConfigurationYmlConfig()
            self.yml_config = temp_model.from_map(m['yml_config'])
        return self


class HpoExperimentConfigDlcConfig(TeaModel):
    def __init__(self, access_id=None, access_key=None, endpoint=None, protocol=None, region=None):
        self.access_id = access_id  # type: str
        self.access_key = access_key  # type: str
        self.endpoint = endpoint  # type: str
        self.protocol = protocol  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigDlcConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['access_id'] = self.access_id
        if self.access_key is not None:
            result['access_key'] = self.access_key
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_id') is not None:
            self.access_id = m.get('access_id')
        if m.get('access_key') is not None:
            self.access_key = m.get('access_key')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class HpoExperimentConfigK8sConfig(TeaModel):
    def __init__(self, nni_container_cpu_limit=None, nni_container_memory_limit=None,
                 nni_container_requested_cpu=None, nni_container_requested_memory=None):
        self.nni_container_cpu_limit = nni_container_cpu_limit  # type: str
        self.nni_container_memory_limit = nni_container_memory_limit  # type: str
        self.nni_container_requested_cpu = nni_container_requested_cpu  # type: str
        self.nni_container_requested_memory = nni_container_requested_memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigK8sConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nni_container_cpu_limit is not None:
            result['nni_container_cpu_limit'] = self.nni_container_cpu_limit
        if self.nni_container_memory_limit is not None:
            result['nni_container_memory_limit'] = self.nni_container_memory_limit
        if self.nni_container_requested_cpu is not None:
            result['nni_container_requested_cpu'] = self.nni_container_requested_cpu
        if self.nni_container_requested_memory is not None:
            result['nni_container_requested_memory'] = self.nni_container_requested_memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nni_container_cpu_limit') is not None:
            self.nni_container_cpu_limit = m.get('nni_container_cpu_limit')
        if m.get('nni_container_memory_limit') is not None:
            self.nni_container_memory_limit = m.get('nni_container_memory_limit')
        if m.get('nni_container_requested_cpu') is not None:
            self.nni_container_requested_cpu = m.get('nni_container_requested_cpu')
        if m.get('nni_container_requested_memory') is not None:
            self.nni_container_requested_memory = m.get('nni_container_requested_memory')
        return self


class HpoExperimentConfigMetricConfig(TeaModel):
    def __init__(self, final_mode=None, metric_dict=None, metric_source=None, metric_type=None,
                 source_list_final_mode=None):
        self.final_mode = final_mode  # type: str
        self.metric_dict = metric_dict  # type: dict[str, any]
        self.metric_source = metric_source  # type: list[str]
        self.metric_type = metric_type  # type: str
        self.source_list_final_mode = source_list_final_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigMetricConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.final_mode is not None:
            result['final_mode'] = self.final_mode
        if self.metric_dict is not None:
            result['metric_dict'] = self.metric_dict
        if self.metric_source is not None:
            result['metric_source'] = self.metric_source
        if self.metric_type is not None:
            result['metric_type'] = self.metric_type
        if self.source_list_final_mode is not None:
            result['source_list_final_mode'] = self.source_list_final_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('final_mode') is not None:
            self.final_mode = m.get('final_mode')
        if m.get('metric_dict') is not None:
            self.metric_dict = m.get('metric_dict')
        if m.get('metric_source') is not None:
            self.metric_source = m.get('metric_source')
        if m.get('metric_type') is not None:
            self.metric_type = m.get('metric_type')
        if m.get('source_list_final_mode') is not None:
            self.source_list_final_mode = m.get('source_list_final_mode')
        return self


class HpoExperimentConfigMonitorConfig(TeaModel):
    def __init__(self, at_mobiles=None, at_user_ids=None, is_at_all=None, keyword=None, url=None):
        self.at_mobiles = at_mobiles  # type: str
        self.at_user_ids = at_user_ids  # type: str
        self.is_at_all = is_at_all  # type: str
        self.keyword = keyword  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigMonitorConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_mobiles is not None:
            result['at_mobiles'] = self.at_mobiles
        if self.at_user_ids is not None:
            result['at_user_ids'] = self.at_user_ids
        if self.is_at_all is not None:
            result['is_at_all'] = self.is_at_all
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('at_mobiles') is not None:
            self.at_mobiles = m.get('at_mobiles')
        if m.get('at_user_ids') is not None:
            self.at_user_ids = m.get('at_user_ids')
        if m.get('is_at_all') is not None:
            self.is_at_all = m.get('is_at_all')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class HpoExperimentConfigOdpsConfig(TeaModel):
    def __init__(self, access_id=None, access_key=None, end_point=None, log_view_host=None, project_name=None,
                 region=None, role_arn=None):
        self.access_id = access_id  # type: str
        self.access_key = access_key  # type: str
        self.end_point = end_point  # type: str
        self.log_view_host = log_view_host  # type: str
        self.project_name = project_name  # type: str
        self.region = region  # type: str
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigOdpsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['access_id'] = self.access_id
        if self.access_key is not None:
            result['access_key'] = self.access_key
        if self.end_point is not None:
            result['end_point'] = self.end_point
        if self.log_view_host is not None:
            result['log_view_host'] = self.log_view_host
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.region is not None:
            result['region'] = self.region
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_id') is not None:
            self.access_id = m.get('access_id')
        if m.get('access_key') is not None:
            self.access_key = m.get('access_key')
        if m.get('end_point') is not None:
            self.end_point = m.get('end_point')
        if m.get('log_view_host') is not None:
            self.log_view_host = m.get('log_view_host')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        return self


class HpoExperimentConfigOssConfig(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, endpoint=None, role_arn=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.endpoint = endpoint  # type: str
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigOssConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyID'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.role_arn is not None:
            result['role_arn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyID') is not None:
            self.access_key_id = m.get('accessKeyID')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('role_arn') is not None:
            self.role_arn = m.get('role_arn')
        return self


class HpoExperimentConfigOutputConfig(TeaModel):
    def __init__(self, model_path=None, summary_path=None):
        self.model_path = model_path  # type: str
        self.summary_path = summary_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigOutputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['model_path'] = self.model_path
        if self.summary_path is not None:
            result['summary_path'] = self.summary_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('model_path') is not None:
            self.model_path = m.get('model_path')
        if m.get('summary_path') is not None:
            self.summary_path = m.get('summary_path')
        return self


class HpoExperimentConfigPaiflowConfig(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None, workspace_id=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.region_id = region_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigPaiflowConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.access_key_secret is not None:
            result['access_key_secret'] = self.access_key_secret
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.workspace_id is not None:
            result['workspace_id'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('access_key_secret') is not None:
            self.access_key_secret = m.get('access_key_secret')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('workspace_id') is not None:
            self.workspace_id = m.get('workspace_id')
        return self


class HpoExperimentConfigParamsConfig(TeaModel):
    def __init__(self, params_src_dst_filepath=None):
        self.params_src_dst_filepath = params_src_dst_filepath  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigParamsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params_src_dst_filepath is not None:
            result['params_src_dst_filepath'] = self.params_src_dst_filepath
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params_src_dst_filepath') is not None:
            self.params_src_dst_filepath = m.get('params_src_dst_filepath')
        return self


class HpoExperimentConfigPlatformConfig(TeaModel):
    def __init__(self, cmd=None, name=None, resume=None):
        self.cmd = cmd  # type: list[str]
        self.name = name  # type: str
        self.resume = resume  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigPlatformConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.name is not None:
            result['name'] = self.name
        if self.resume is not None:
            result['resume'] = self.resume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resume') is not None:
            self.resume = m.get('resume')
        return self


class HpoExperimentConfigScheduleConfig(TeaModel):
    def __init__(self, day=None, end_time=None, start_time=None):
        self.day = day  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigScheduleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['day'] = self.day
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.start_time is not None:
            result['start_time'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('day') is not None:
            self.day = m.get('day')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        return self


class HpoExperimentConfigTsConfig(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, endpoint=None, region_id=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.endpoint = endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigTsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.access_key_secret is not None:
            result['access_key_secret'] = self.access_key_secret
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('access_key_secret') is not None:
            self.access_key_secret = m.get('access_key_secret')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class HpoExperimentConfigYmlConfigAssessorClassArgs(TeaModel):
    def __init__(self, earlystop=None, moving_avg=None, optimize_mode=None, proportion=None, start_step=None):
        self.earlystop = earlystop  # type: bool
        self.moving_avg = moving_avg  # type: str
        self.optimize_mode = optimize_mode  # type: str
        self.proportion = proportion  # type: float
        self.start_step = start_step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigYmlConfigAssessorClassArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.earlystop is not None:
            result['earlystop'] = self.earlystop
        if self.moving_avg is not None:
            result['moving_avg'] = self.moving_avg
        if self.optimize_mode is not None:
            result['optimize_mode'] = self.optimize_mode
        if self.proportion is not None:
            result['proportion'] = self.proportion
        if self.start_step is not None:
            result['start_step'] = self.start_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('earlystop') is not None:
            self.earlystop = m.get('earlystop')
        if m.get('moving_avg') is not None:
            self.moving_avg = m.get('moving_avg')
        if m.get('optimize_mode') is not None:
            self.optimize_mode = m.get('optimize_mode')
        if m.get('proportion') is not None:
            self.proportion = m.get('proportion')
        if m.get('start_step') is not None:
            self.start_step = m.get('start_step')
        return self


class HpoExperimentConfigYmlConfigAssessor(TeaModel):
    def __init__(self, class_args=None, name=None):
        self.class_args = class_args  # type: HpoExperimentConfigYmlConfigAssessorClassArgs
        self.name = name  # type: str

    def validate(self):
        if self.class_args:
            self.class_args.validate()

    def to_map(self):
        _map = super(HpoExperimentConfigYmlConfigAssessor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_args is not None:
            result['class_args'] = self.class_args.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('class_args') is not None:
            temp_model = HpoExperimentConfigYmlConfigAssessorClassArgs()
            self.class_args = temp_model.from_map(m['class_args'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HpoExperimentConfigYmlConfigTuner(TeaModel):
    def __init__(self, class_args=None, name=None):
        self.class_args = class_args  # type: dict[str, any]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HpoExperimentConfigYmlConfigTuner, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_args is not None:
            result['class_args'] = self.class_args
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('class_args') is not None:
            self.class_args = m.get('class_args')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HpoExperimentConfigYmlConfig(TeaModel):
    def __init__(self, assessor=None, debug=None, experiment_name=None, log_level=None, max_trial_number=None,
                 trial_concurrency=None, tuner=None):
        self.assessor = assessor  # type: HpoExperimentConfigYmlConfigAssessor
        self.debug = debug  # type: bool
        self.experiment_name = experiment_name  # type: str
        self.log_level = log_level  # type: str
        self.max_trial_number = max_trial_number  # type: int
        self.trial_concurrency = trial_concurrency  # type: int
        self.tuner = tuner  # type: HpoExperimentConfigYmlConfigTuner

    def validate(self):
        if self.assessor:
            self.assessor.validate()
        if self.tuner:
            self.tuner.validate()

    def to_map(self):
        _map = super(HpoExperimentConfigYmlConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assessor is not None:
            result['assessor'] = self.assessor.to_map()
        if self.debug is not None:
            result['debug'] = self.debug
        if self.experiment_name is not None:
            result['experiment_name'] = self.experiment_name
        if self.log_level is not None:
            result['log_level'] = self.log_level
        if self.max_trial_number is not None:
            result['max_trial_number'] = self.max_trial_number
        if self.trial_concurrency is not None:
            result['trial_concurrency'] = self.trial_concurrency
        if self.tuner is not None:
            result['tuner'] = self.tuner.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assessor') is not None:
            temp_model = HpoExperimentConfigYmlConfigAssessor()
            self.assessor = temp_model.from_map(m['assessor'])
        if m.get('debug') is not None:
            self.debug = m.get('debug')
        if m.get('experiment_name') is not None:
            self.experiment_name = m.get('experiment_name')
        if m.get('log_level') is not None:
            self.log_level = m.get('log_level')
        if m.get('max_trial_number') is not None:
            self.max_trial_number = m.get('max_trial_number')
        if m.get('trial_concurrency') is not None:
            self.trial_concurrency = m.get('trial_concurrency')
        if m.get('tuner') is not None:
            temp_model = HpoExperimentConfigYmlConfigTuner()
            self.tuner = temp_model.from_map(m['tuner'])
        return self


class HpoExperimentConfig(TeaModel):
    def __init__(self, dlc_config=None, k_8s_config=None, metric_config=None, monitor_config=None, odps_config=None,
                 oss_config=None, output_config=None, paiflow_config=None, params_config=None, platform_config=None,
                 schedule_config=None, search_space=None, ts_config=None, yml_config=None):
        self.dlc_config = dlc_config  # type: HpoExperimentConfigDlcConfig
        self.k_8s_config = k_8s_config  # type: HpoExperimentConfigK8sConfig
        self.metric_config = metric_config  # type: HpoExperimentConfigMetricConfig
        self.monitor_config = monitor_config  # type: HpoExperimentConfigMonitorConfig
        self.odps_config = odps_config  # type: HpoExperimentConfigOdpsConfig
        self.oss_config = oss_config  # type: HpoExperimentConfigOssConfig
        self.output_config = output_config  # type: HpoExperimentConfigOutputConfig
        self.paiflow_config = paiflow_config  # type: HpoExperimentConfigPaiflowConfig
        self.params_config = params_config  # type: HpoExperimentConfigParamsConfig
        self.platform_config = platform_config  # type: HpoExperimentConfigPlatformConfig
        self.schedule_config = schedule_config  # type: HpoExperimentConfigScheduleConfig
        self.search_space = search_space  # type: dict[str, any]
        self.ts_config = ts_config  # type: HpoExperimentConfigTsConfig
        self.yml_config = yml_config  # type: HpoExperimentConfigYmlConfig

    def validate(self):
        if self.dlc_config:
            self.dlc_config.validate()
        if self.k_8s_config:
            self.k_8s_config.validate()
        if self.metric_config:
            self.metric_config.validate()
        if self.monitor_config:
            self.monitor_config.validate()
        if self.odps_config:
            self.odps_config.validate()
        if self.oss_config:
            self.oss_config.validate()
        if self.output_config:
            self.output_config.validate()
        if self.paiflow_config:
            self.paiflow_config.validate()
        if self.params_config:
            self.params_config.validate()
        if self.platform_config:
            self.platform_config.validate()
        if self.schedule_config:
            self.schedule_config.validate()
        if self.ts_config:
            self.ts_config.validate()
        if self.yml_config:
            self.yml_config.validate()

    def to_map(self):
        _map = super(HpoExperimentConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlc_config is not None:
            result['dlc_config'] = self.dlc_config.to_map()
        if self.k_8s_config is not None:
            result['k8s_config'] = self.k_8s_config.to_map()
        if self.metric_config is not None:
            result['metric_config'] = self.metric_config.to_map()
        if self.monitor_config is not None:
            result['monitor_config'] = self.monitor_config.to_map()
        if self.odps_config is not None:
            result['odps_config'] = self.odps_config.to_map()
        if self.oss_config is not None:
            result['oss_config'] = self.oss_config.to_map()
        if self.output_config is not None:
            result['output_config'] = self.output_config.to_map()
        if self.paiflow_config is not None:
            result['paiflow_config'] = self.paiflow_config.to_map()
        if self.params_config is not None:
            result['params_config'] = self.params_config.to_map()
        if self.platform_config is not None:
            result['platform_config'] = self.platform_config.to_map()
        if self.schedule_config is not None:
            result['schedule_config'] = self.schedule_config.to_map()
        if self.search_space is not None:
            result['search_space'] = self.search_space
        if self.ts_config is not None:
            result['ts_config'] = self.ts_config.to_map()
        if self.yml_config is not None:
            result['yml_config'] = self.yml_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dlc_config') is not None:
            temp_model = HpoExperimentConfigDlcConfig()
            self.dlc_config = temp_model.from_map(m['dlc_config'])
        if m.get('k8s_config') is not None:
            temp_model = HpoExperimentConfigK8sConfig()
            self.k_8s_config = temp_model.from_map(m['k8s_config'])
        if m.get('metric_config') is not None:
            temp_model = HpoExperimentConfigMetricConfig()
            self.metric_config = temp_model.from_map(m['metric_config'])
        if m.get('monitor_config') is not None:
            temp_model = HpoExperimentConfigMonitorConfig()
            self.monitor_config = temp_model.from_map(m['monitor_config'])
        if m.get('odps_config') is not None:
            temp_model = HpoExperimentConfigOdpsConfig()
            self.odps_config = temp_model.from_map(m['odps_config'])
        if m.get('oss_config') is not None:
            temp_model = HpoExperimentConfigOssConfig()
            self.oss_config = temp_model.from_map(m['oss_config'])
        if m.get('output_config') is not None:
            temp_model = HpoExperimentConfigOutputConfig()
            self.output_config = temp_model.from_map(m['output_config'])
        if m.get('paiflow_config') is not None:
            temp_model = HpoExperimentConfigPaiflowConfig()
            self.paiflow_config = temp_model.from_map(m['paiflow_config'])
        if m.get('params_config') is not None:
            temp_model = HpoExperimentConfigParamsConfig()
            self.params_config = temp_model.from_map(m['params_config'])
        if m.get('platform_config') is not None:
            temp_model = HpoExperimentConfigPlatformConfig()
            self.platform_config = temp_model.from_map(m['platform_config'])
        if m.get('schedule_config') is not None:
            temp_model = HpoExperimentConfigScheduleConfig()
            self.schedule_config = temp_model.from_map(m['schedule_config'])
        if m.get('search_space') is not None:
            self.search_space = m.get('search_space')
        if m.get('ts_config') is not None:
            temp_model = HpoExperimentConfigTsConfig()
            self.ts_config = temp_model.from_map(m['ts_config'])
        if m.get('yml_config') is not None:
            temp_model = HpoExperimentConfigYmlConfig()
            self.yml_config = temp_model.from_map(m['yml_config'])
        return self


class CreateHpoExperimentRequest(TeaModel):
    def __init__(self, accessibility=None, description=None, hpo_experiment_configuration=None, name=None,
                 workspace_id=None):
        self.accessibility = accessibility  # type: str
        self.description = description  # type: str
        self.hpo_experiment_configuration = hpo_experiment_configuration  # type: HpoExperimentConfig
        self.name = name  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.hpo_experiment_configuration:
            self.hpo_experiment_configuration.validate()

    def to_map(self):
        _map = super(CreateHpoExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.hpo_experiment_configuration is not None:
            result['HpoExperimentConfiguration'] = self.hpo_experiment_configuration.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HpoExperimentConfiguration') is not None:
            temp_model = HpoExperimentConfig()
            self.hpo_experiment_configuration = temp_model.from_map(m['HpoExperimentConfiguration'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateHpoExperimentResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, experiment_id=None, message=None, request_id=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.experiment_id = experiment_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHpoExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHpoExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHpoExperimentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHpoExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHpoExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHpoExperimentResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, message=None, request_id=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHpoExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHpoExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHpoExperimentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHpoExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHpoExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHpoExperimentResponseBody(TeaModel):
    def __init__(self, accessibility=None, code=None, config_ini=None, config_yml=None, creator=None, deleted=None,
                 description=None, detail=None, experiment_id=None, gmt_create_time=None, gmt_modified_time=None,
                 hpo_experiment_configuration=None, job_type=None, message=None, name=None, request_id=None, search_space=None, status=None,
                 trial_count=None, trial_status=None, workspace_id=None):
        self.accessibility = accessibility  # type: str
        self.code = code  # type: str
        self.config_ini = config_ini  # type: str
        self.config_yml = config_yml  # type: str
        self.creator = creator  # type: str
        self.deleted = deleted  # type: bool
        self.description = description  # type: str
        self.detail = detail  # type: dict[str, any]
        self.experiment_id = experiment_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.hpo_experiment_configuration = hpo_experiment_configuration  # type: dict[str, any]
        self.job_type = job_type  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.search_space = search_space  # type: str
        self.status = status  # type: str
        self.trial_count = trial_count  # type: int
        self.trial_status = trial_status  # type: dict[str, str]
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHpoExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.code is not None:
            result['Code'] = self.code
        if self.config_ini is not None:
            result['ConfigIni'] = self.config_ini
        if self.config_yml is not None:
            result['ConfigYml'] = self.config_yml
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.hpo_experiment_configuration is not None:
            result['HpoExperimentConfiguration'] = self.hpo_experiment_configuration
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_space is not None:
            result['SearchSpace'] = self.search_space
        if self.status is not None:
            result['Status'] = self.status
        if self.trial_count is not None:
            result['TrialCount'] = self.trial_count
        if self.trial_status is not None:
            result['TrialStatus'] = self.trial_status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigIni') is not None:
            self.config_ini = m.get('ConfigIni')
        if m.get('ConfigYml') is not None:
            self.config_yml = m.get('ConfigYml')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('HpoExperimentConfiguration') is not None:
            self.hpo_experiment_configuration = m.get('HpoExperimentConfiguration')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchSpace') is not None:
            self.search_space = m.get('SearchSpace')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrialCount') is not None:
            self.trial_count = m.get('TrialCount')
        if m.get('TrialStatus') is not None:
            self.trial_status = m.get('TrialStatus')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetHpoExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHpoExperimentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHpoExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHpoExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHpoTrialResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, experiment_id=None, final_metric=None, gmt_create_time=None,
                 gmt_modified_time=None, hyperparam=None, job_meta=None, message=None, metric=None, metric_name=None, model=None,
                 parameter_id=None, request_id=None, status=None, trial_id=None, user_comment=None, user_score=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.experiment_id = experiment_id  # type: str
        self.final_metric = final_metric  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.hyperparam = hyperparam  # type: str
        self.job_meta = job_meta  # type: str
        self.message = message  # type: str
        self.metric = metric  # type: str
        self.metric_name = metric_name  # type: str
        self.model = model  # type: str
        self.parameter_id = parameter_id  # type: int
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.trial_id = trial_id  # type: str
        self.user_comment = user_comment  # type: str
        self.user_score = user_score  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHpoTrialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.final_metric is not None:
            result['FinalMetric'] = self.final_metric
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.hyperparam is not None:
            result['Hyperparam'] = self.hyperparam
        if self.job_meta is not None:
            result['JobMeta'] = self.job_meta
        if self.message is not None:
            result['Message'] = self.message
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.model is not None:
            result['Model'] = self.model
        if self.parameter_id is not None:
            result['ParameterId'] = self.parameter_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.trial_id is not None:
            result['TrialId'] = self.trial_id
        if self.user_comment is not None:
            result['UserComment'] = self.user_comment
        if self.user_score is not None:
            result['UserScore'] = self.user_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FinalMetric') is not None:
            self.final_metric = m.get('FinalMetric')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Hyperparam') is not None:
            self.hyperparam = m.get('Hyperparam')
        if m.get('JobMeta') is not None:
            self.job_meta = m.get('JobMeta')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ParameterId') is not None:
            self.parameter_id = m.get('ParameterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrialId') is not None:
            self.trial_id = m.get('TrialId')
        if m.get('UserComment') is not None:
            self.user_comment = m.get('UserComment')
        if m.get('UserScore') is not None:
            self.user_score = m.get('UserScore')
        return self


class GetHpoTrialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHpoTrialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHpoTrialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHpoTrialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoExperimentLogsRequest(TeaModel):
    def __init__(self, log_name=None, page_number=None, page_size=None):
        self.log_name = log_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoExperimentLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHpoExperimentLogsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, logs=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, any]
        self.logs = logs  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoExperimentLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHpoExperimentLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoExperimentLogsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoExperimentLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoExperimentLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoExperimentsRequest(TeaModel):
    def __init__(self, accessibility=None, creator=None, include_config_data=None, max_create_time=None,
                 min_create_time=None, name=None, order=None, page_number=None, page_size=None, sort_by=None, status=None,
                 workspace_id=None):
        self.accessibility = accessibility  # type: str
        self.creator = creator  # type: str
        self.include_config_data = include_config_data  # type: str
        self.max_create_time = max_create_time  # type: str
        self.min_create_time = min_create_time  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoExperimentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.include_config_data is not None:
            result['IncludeConfigData'] = self.include_config_data
        if self.max_create_time is not None:
            result['MaxCreateTime'] = self.max_create_time
        if self.min_create_time is not None:
            result['MinCreateTime'] = self.min_create_time
        if self.name is not None:
            result['Name'] = self.name
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
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('IncludeConfigData') is not None:
            self.include_config_data = m.get('IncludeConfigData')
        if m.get('MaxCreateTime') is not None:
            self.max_create_time = m.get('MaxCreateTime')
        if m.get('MinCreateTime') is not None:
            self.min_create_time = m.get('MinCreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListHpoExperimentsResponseBodyExperiments(TeaModel):
    def __init__(self, accessibility=None, config_ini=None, config_yml=None, creator=None, deleted=None,
                 description=None, experiment_id=None, gmt_create_time=None, gmt_modified_time=None, job_type=None, name=None,
                 search_space=None, status=None, trial_count=None, trial_status=None, workspace_id=None):
        self.accessibility = accessibility  # type: str
        self.config_ini = config_ini  # type: str
        self.config_yml = config_yml  # type: str
        self.creator = creator  # type: str
        self.deleted = deleted  # type: bool
        self.description = description  # type: str
        self.experiment_id = experiment_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.job_type = job_type  # type: str
        self.name = name  # type: str
        self.search_space = search_space  # type: str
        self.status = status  # type: str
        self.trial_count = trial_count  # type: int
        self.trial_status = trial_status  # type: dict[str, str]
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoExperimentsResponseBodyExperiments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.config_ini is not None:
            result['ConfigIni'] = self.config_ini
        if self.config_yml is not None:
            result['ConfigYml'] = self.config_yml
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.name is not None:
            result['Name'] = self.name
        if self.search_space is not None:
            result['SearchSpace'] = self.search_space
        if self.status is not None:
            result['Status'] = self.status
        if self.trial_count is not None:
            result['TrialCount'] = self.trial_count
        if self.trial_status is not None:
            result['TrialStatus'] = self.trial_status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ConfigIni') is not None:
            self.config_ini = m.get('ConfigIni')
        if m.get('ConfigYml') is not None:
            self.config_yml = m.get('ConfigYml')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SearchSpace') is not None:
            self.search_space = m.get('SearchSpace')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrialCount') is not None:
            self.trial_count = m.get('TrialCount')
        if m.get('TrialStatus') is not None:
            self.trial_status = m.get('TrialStatus')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListHpoExperimentsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, experiments=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.experiments = experiments  # type: list[ListHpoExperimentsResponseBodyExperiments]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHpoExperimentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListHpoExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHpoExperimentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoExperimentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoExperimentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoTrialCommandsResponseBodyCommands(TeaModel):
    def __init__(self, command=None, id=None, output=None):
        self.command = command  # type: str
        self.id = id  # type: int
        self.output = output  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialCommandsResponseBodyCommands, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.id is not None:
            result['Id'] = self.id
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListHpoTrialCommandsResponseBody(TeaModel):
    def __init__(self, code=None, commands=None, detail=None, message=None, request_id=None):
        self.code = code  # type: str
        self.commands = commands  # type: list[ListHpoTrialCommandsResponseBodyCommands]
        self.detail = detail  # type: dict[str, str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHpoTrialCommandsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = ListHpoTrialCommandsResponseBodyCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHpoTrialCommandsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoTrialCommandsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoTrialCommandsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoTrialCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoTrialLogNamesResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, log_names=None, message=None, request_id=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.log_names = log_names  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialLogNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.log_names is not None:
            result['LogNames'] = self.log_names
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('LogNames') is not None:
            self.log_names = m.get('LogNames')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHpoTrialLogNamesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoTrialLogNamesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoTrialLogNamesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoTrialLogNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoTrialLogsRequest(TeaModel):
    def __init__(self, log_name=None, page_number=None, page_size=None):
        self.log_name = log_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHpoTrialLogsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, logs=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, any]
        self.logs = logs  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHpoTrialLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoTrialLogsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoTrialLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoTrialLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHpoTrialsRequest(TeaModel):
    def __init__(self, order=None, page_number=None, page_size=None, sort_by=None):
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListHpoTrialsResponseBodyTrials(TeaModel):
    def __init__(self, experiment_id=None, final_metric=None, gmt_create_time=None, gmt_modified_time=None,
                 hyperparam=None, job_meta=None, metric=None, metric_name=None, model=None, parameter_id=None, status=None,
                 trial_id=None, user_comment=None, user_score=None):
        self.experiment_id = experiment_id  # type: str
        self.final_metric = final_metric  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.hyperparam = hyperparam  # type: str
        self.job_meta = job_meta  # type: str
        self.metric = metric  # type: str
        self.metric_name = metric_name  # type: str
        self.model = model  # type: str
        self.parameter_id = parameter_id  # type: int
        self.status = status  # type: str
        self.trial_id = trial_id  # type: str
        self.user_comment = user_comment  # type: str
        self.user_score = user_score  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHpoTrialsResponseBodyTrials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.final_metric is not None:
            result['FinalMetric'] = self.final_metric
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.hyperparam is not None:
            result['Hyperparam'] = self.hyperparam
        if self.job_meta is not None:
            result['JobMeta'] = self.job_meta
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.model is not None:
            result['Model'] = self.model
        if self.parameter_id is not None:
            result['ParameterId'] = self.parameter_id
        if self.status is not None:
            result['Status'] = self.status
        if self.trial_id is not None:
            result['TrialId'] = self.trial_id
        if self.user_comment is not None:
            result['UserComment'] = self.user_comment
        if self.user_score is not None:
            result['UserScore'] = self.user_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FinalMetric') is not None:
            self.final_metric = m.get('FinalMetric')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Hyperparam') is not None:
            self.hyperparam = m.get('Hyperparam')
        if m.get('JobMeta') is not None:
            self.job_meta = m.get('JobMeta')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ParameterId') is not None:
            self.parameter_id = m.get('ParameterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrialId') is not None:
            self.trial_id = m.get('TrialId')
        if m.get('UserComment') is not None:
            self.user_comment = m.get('UserComment')
        if m.get('UserScore') is not None:
            self.user_score = m.get('UserScore')
        return self


class ListHpoTrialsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, message=None, request_id=None, total_count=None, trials=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.trials = trials  # type: list[ListHpoTrialsResponseBodyTrials]

    def validate(self):
        if self.trials:
            for k in self.trials:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHpoTrialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Trials'] = []
        if self.trials is not None:
            for k in self.trials:
                result['Trials'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trials = []
        if m.get('Trials') is not None:
            for k in m.get('Trials'):
                temp_model = ListHpoTrialsResponseBodyTrials()
                self.trials.append(temp_model.from_map(k))
        return self


class ListHpoTrialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHpoTrialsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHpoTrialsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHpoTrialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartHpoTrialsRequest(TeaModel):
    def __init__(self, trial_hyper_parameters=None, trial_ids=None):
        self.trial_hyper_parameters = trial_hyper_parameters  # type: str
        self.trial_ids = trial_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartHpoTrialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trial_hyper_parameters is not None:
            result['TrialHyperParameters'] = self.trial_hyper_parameters
        if self.trial_ids is not None:
            result['TrialIds'] = self.trial_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrialHyperParameters') is not None:
            self.trial_hyper_parameters = m.get('TrialHyperParameters')
        if m.get('TrialIds') is not None:
            self.trial_ids = m.get('TrialIds')
        return self


class RestartHpoTrialsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, message=None, request_id=None, results=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.results = results  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartHpoTrialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class RestartHpoTrialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartHpoTrialsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartHpoTrialsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartHpoTrialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopHpoExperimentResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, exp_id=None, message=None, request_id=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.exp_id = exp_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopHpoExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.exp_id is not None:
            result['ExpId'] = self.exp_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ExpId') is not None:
            self.exp_id = m.get('ExpId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopHpoExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopHpoExperimentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopHpoExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopHpoExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopHpoTrialsRequest(TeaModel):
    def __init__(self, trial_ids=None):
        self.trial_ids = trial_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopHpoTrialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trial_ids is not None:
            result['TrialIds'] = self.trial_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrialIds') is not None:
            self.trial_ids = m.get('TrialIds')
        return self


class StopHpoTrialsResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, message=None, request_id=None, results=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.results = results  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopHpoTrialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class StopHpoTrialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopHpoTrialsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopHpoTrialsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopHpoTrialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHpoExperimentRequest(TeaModel):
    def __init__(self, accessibility=None, description=None, hpo_experiment_configuration=None, name=None,
                 workspace_id=None):
        self.accessibility = accessibility  # type: str
        self.description = description  # type: str
        self.hpo_experiment_configuration = hpo_experiment_configuration  # type: HpoExperimentConfig
        self.name = name  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.hpo_experiment_configuration:
            self.hpo_experiment_configuration.validate()

    def to_map(self):
        _map = super(UpdateHpoExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.hpo_experiment_configuration is not None:
            result['HpoExperimentConfiguration'] = self.hpo_experiment_configuration.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HpoExperimentConfiguration') is not None:
            temp_model = HpoExperimentConfig()
            self.hpo_experiment_configuration = temp_model.from_map(m['HpoExperimentConfiguration'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateHpoExperimentResponseBody(TeaModel):
    def __init__(self, code=None, detail=None, message=None, request_id=None):
        self.code = code  # type: str
        self.detail = detail  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHpoExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateHpoExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHpoExperimentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHpoExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHpoExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


