# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConsumerGroup(TeaModel):
    def __init__(self, name=None, order=None, timeout=None):
        # consumerGroup
        self.name = name  # type: str
        # order
        self.order = order  # type: bool
        # timeout
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
        # enable
        self.enable = enable  # type: bool
        # 加密算法，只支持default和m4。当 enable 为 true 时，此项必选。
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
        # arn
        self.arn = arn  # type: str
        # cmk_key_id
        self.cmk_key_id = cmk_key_id  # type: str
        # region_id
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


class LogtailConfigOutputDetail(TeaModel):
    def __init__(self, endpoint=None, logstore_name=None, region=None):
        # endpoint
        self.endpoint = endpoint  # type: str
        # logstoreName
        self.logstore_name = logstore_name  # type: str
        # 地域
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
        # configName
        self.config_name = config_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: long
        # inputDetail
        self.input_detail = input_detail  # type: dict[str, any]
        # inputType
        self.input_type = input_type  # type: str
        # 修改时间
        self.last_modify_time = last_modify_time  # type: long
        # 日志样例
        self.log_sample = log_sample  # type: str
        # outputDetail
        self.output_detail = output_detail  # type: LogtailConfigOutputDetail
        # outputType
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


class SavedSearch(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        # displayName
        self.display_name = display_name  # type: str
        # logstore
        self.logstore = logstore  # type: str
        # savedsearchName
        self.savedsearch_name = savedsearch_name  # type: str
        # searchQuery
        self.search_query = search_query  # type: str
        # topic
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


class ChartDisplay(TeaModel):
    def __init__(self, height=None, width=None, x_axis=None, x_pos=None, y_axis=None, y_pos=None):
        # 高度
        self.height = height  # type: long
        # 宽度
        self.width = width  # type: long
        # x 轴
        self.x_axis = x_axis  # type: list[str]
        # x 坐标
        self.x_pos = x_pos  # type: long
        # y 轴
        self.y_axis = y_axis  # type: list[str]
        # y 坐标
        self.y_pos = y_pos  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChartDisplay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.x_axis is not None:
            result['xAxis'] = self.x_axis
        if self.x_pos is not None:
            result['xPos'] = self.x_pos
        if self.y_axis is not None:
            result['yAxis'] = self.y_axis
        if self.y_pos is not None:
            result['yPos'] = self.y_pos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('xAxis') is not None:
            self.x_axis = m.get('xAxis')
        if m.get('xPos') is not None:
            self.x_pos = m.get('xPos')
        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')
        if m.get('yPos') is not None:
            self.y_pos = m.get('yPos')
        return self


class ChartSearch(TeaModel):
    def __init__(self, end=None, logstore=None, query=None, start=None, topic=None):
        # 结束时间
        self.end = end  # type: str
        # logstore 名称
        self.logstore = logstore  # type: str
        # 查询语句
        self.query = query  # type: str
        # 开始时间
        self.start = start  # type: str
        # topic
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChartSearch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.query is not None:
            result['query'] = self.query
        if self.start is not None:
            result['start'] = self.start
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class Chart(TeaModel):
    def __init__(self, action=None, display=None, search=None, title=None, type=None):
        # action
        self.action = action  # type: dict[str, str]
        # 图表的显示配置
        self.display = display  # type: ChartDisplay
        # 查询配置
        self.search = search  # type: ChartSearch
        # 图表标题
        self.title = title  # type: str
        # 图标类型
        self.type = type  # type: str

    def validate(self):
        if self.display:
            self.display.validate()
        if self.search:
            self.search.validate()

    def to_map(self):
        _map = super(Chart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.display is not None:
            result['display'] = self.display.to_map()
        if self.search is not None:
            result['search'] = self.search.to_map()
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
            temp_model = ChartDisplay()
            self.display = temp_model.from_map(m['display'])
        if m.get('search') is not None:
            temp_model = ChartSearch()
            self.search = temp_model.from_map(m['search'])
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Dashboard(TeaModel):
    def __init__(self, attribute=None, charts=None, dashboard_name=None, description=None, display_name=None):
        # 属性值
        self.attribute = attribute  # type: dict[str, str]
        # 包含的图表
        self.charts = charts  # type: list[Chart]
        # 内部名称
        self.dashboard_name = dashboard_name  # type: str
        # 描述信息
        self.description = description  # type: str
        # 展示名称
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
        # 账户 id
        self.account_id = account_id  # type: str
        # endpoint
        self.endpoint = endpoint  # type: str
        # 函数名
        self.function_name = function_name  # type: str
        # 函数 provider
        self.function_provider = function_provider  # type: str
        # 地域
        self.region_name = region_name  # type: str
        # 角色授权
        self.role_arn = role_arn  # type: str
        # 服务名
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
        # endpoint
        self.endpoint = endpoint  # type: str
        # logstore 名称
        self.logstore_name = logstore_name  # type: str
        # project 名称
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
        # logstore 名称
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
        # 最大重试次数
        self.max_retry_time = max_retry_time  # type: int
        # 角色授权配置
        self.role_arn = role_arn  # type: str
        # 开始位置
        self.starting_position = starting_position  # type: str
        # 开始时间
        self.starting_unixtime = starting_unixtime  # type: long
        # 触发间隔
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
        # 是否启用
        self.enable = enable  # type: bool
        # 任务名称
        self.etl_job_name = etl_job_name  # type: str
        # 运行函数配置
        self.function_config = function_config  # type: EtlJobFunctionConfig
        # 参数列表
        self.function_parameter = function_parameter  # type: dict[str, str]
        # 日志配置
        self.log_config = log_config  # type: EtlJobLogConfig
        # 配置数据来源
        self.source_config = source_config  # type: EtlJobSourceConfig
        # 触发器配置
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
        # 是否启用
        self.enable = enable  # type: bool
        # key
        self.etl_meta_key = etl_meta_key  # type: str
        # 名字
        self.etl_meta_name = etl_meta_name  # type: str
        # tag
        self.etl_meta_tag = etl_meta_tag  # type: str
        # value
        self.etl_meta_value = etl_meta_value  # type: dict[str, str]

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


class ExternalStoreParameter(TeaModel):
    def __init__(self, db=None, host=None, instance_id=None, password=None, port=None, region=None, table=None,
                 username=None, vpc_id=None):
        # meta
        self.db = db  # type: str
        # 192.168.XX.XX
        self.host = host  # type: str
        # RDS MySQL实例ID。
        self.instance_id = instance_id  # type: str
        # sfdsfldsfksfls****\
        self.password = password  # type: str
        # 3306
        self.port = port  # type: str
        # cn-qingdao
        self.region = region  # type: str
        # join_meta
        self.table = table  # type: str
        # root
        self.username = username  # type: str
        # RDS MySQL实例所属的VPC ID。
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExternalStoreParameter, self).to_map()
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


class ExternalStore(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # 名称
        self.external_store_name = external_store_name  # type: str
        # 参数
        self.parameter = parameter  # type: ExternalStoreParameter
        # 类型
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(ExternalStore, self).to_map()
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
            temp_model = ExternalStoreParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class LoggingLoggingDetails(TeaModel):
    def __init__(self, logstore=None, type=None):
        # logstore 名称。
        self.logstore = logstore  # type: str
        # logging 类型。
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
        # logging 配置项
        self.logging_details = logging_details  # type: list[LoggingLoggingDetails]
        # project 名称。
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
                 hot_ttl=None, last_modify_time=None, logstore_name=None, max_split_shard=None, shard_count=None,
                 telemetry_type=None, ttl=None):
        # 接收日志后，自动添加客户端外网IP和日志到达时间
        self.append_meta = append_meta  # type: bool
        # 是否开启 shard 自动分裂。当写入数据量超过已有分区（Shard）写入服务能力且持续5分钟以上时，开启自动分裂功能可自动根据数据量增加分区数量
        self.auto_split = auto_split  # type: bool
        # 创建时间。
        self.create_time = create_time  # type: int
        # WebTracking功能支持快速采集各种浏览器以及iOS/Android/APP访问信息，默认关闭
        self.enable_tracking = enable_tracking  # type: bool
        # Encrypt configuration
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        # 必须在 (30, ttl) 之间
        self.hot_ttl = hot_ttl  # type: int
        # 最后修改时间。
        self.last_modify_time = last_modify_time  # type: int
        # logstore 的名称。
        self.logstore_name = logstore_name  # type: str
        # 最大 shard 数量。
        self.max_split_shard = max_split_shard  # type: int
        # shard 数量。
        self.shard_count = shard_count  # type: int
        # telemetryType
        self.telemetry_type = telemetry_type  # type: str
        # 数据保存的天数。
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
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
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
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class Machine(TeaModel):
    def __init__(self, ip=None, last_heartbeat_time=None, machine_uniqueid=None, userdefined_id=None):
        # ip 地址
        self.ip = ip  # type: str
        # 上次心跳时间
        self.last_heartbeat_time = last_heartbeat_time  # type: long
        # 机器的唯一标识
        self.machine_uniqueid = machine_uniqueid  # type: str
        # 用户自定义标识
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
        # 机器组所依赖的外部管理系统标识。
        self.external_name = external_name  # type: str
        # 机器组的日志主题。
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
        # 机器组属性。
        self.group_attribute = group_attribute  # type: MachineGroupGroupAttribute
        # 机器组名称。
        self.group_name = group_name  # type: str
        # 机器组种类。
        self.group_type = group_type  # type: str
        # 机器组标识种类，支持 IP 标识或者用户自定义标识，即 ip 、userdefined。
        self.machine_identify_type = machine_identify_type  # type: str
        # 机器组标识列表。
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


class OssExternalStoreParameter(TeaModel):
    def __init__(self, access_key=None, accessid=None, bucket=None, endpoint=None):
        # 您的AccessKey Secret。
        self.access_key = access_key  # type: str
        # 您的AccessKey ID。
        self.accessid = accessid  # type: str
        # oss 桶名称。
        self.bucket = bucket  # type: str
        # oss 的 endpoint 访问网址。
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OssExternalStoreParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.accessid is not None:
            result['accessid'] = self.accessid
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessid') is not None:
            self.accessid = m.get('accessid')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        return self


class OssExternalStore(TeaModel):
    def __init__(self, external_store_name=None, parameter=None, store_type=None):
        # 名称
        self.external_store_name = external_store_name  # type: str
        # 参数
        self.parameter = parameter  # type: OssExternalStoreParameter
        # 类型。这里固定为 oss
        self.store_type = store_type  # type: str

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super(OssExternalStore, self).to_map()
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
            temp_model = OssExternalStoreParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class Project(TeaModel):
    def __init__(self, create_time=None, description=None, last_modify_time=None, owner=None, project_name=None,
                 region=None, status=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 最后更新时间
        self.last_modify_time = last_modify_time  # type: str
        # owner
        self.owner = owner  # type: str
        # Project名称
        self.project_name = project_name  # type: str
        # 所在区域
        self.region = region  # type: str
        # 状态
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
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Shard(TeaModel):
    def __init__(self, create_time=None, exclusive_end_key=None, inclusive_begin_key=None, shard_id=None,
                 status=None):
        # Shard的创建时间。Unix时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        self.create_time = create_time  # type: int
        # 指定Shard范围的结束值，Shard范围中不包含该值。即 shard 包含MD5值在 [inclusiveBeginKey, exclusiveEndKey) 之间的日志。
        self.exclusive_end_key = exclusive_end_key  # type: str
        # 指定Shard范围的起始值，Shard范围中包含该值。即 shard 包含MD5值在 [inclusiveBeginKey, exclusiveEndKey) 之间的日志。
        self.inclusive_begin_key = inclusive_begin_key  # type: str
        # shard id
        self.shard_id = shard_id  # type: int
        # shard 的读写状态，readwrite 或者 readonly。
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


class CreateConsumerGroupRequest(TeaModel):
    def __init__(self, consumer_group=None, order=None, timeout=None):
        self.consumer_group = consumer_group  # type: str
        self.order = order  # type: bool
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


class CreateDomainRequest(TeaModel):
    def __init__(self, domain_name=None):
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
        # 大小写敏感
        self.case_sensitive = case_sensitive  # type: bool
        # 包含中文
        self.chn = chn  # type: bool
        # 排除的字段列表，不能与include_keys同时指定。
        self.exclude_keys = exclude_keys  # type: list[str]
        # 包含的字段列表，不能与exclude_keys同时指定。
        self.include_keys = include_keys  # type: list[str]
        # 分词符列表。可以设置一个分词参数，指定这个字段按照哪一种方式分词。
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
        self.keys = keys  # type: dict[str, KeysValue]
        # 配置全文索引
        self.line = line  # type: CreateIndexRequestLine
        # 开启日志聚类，开启后白名单与黑名单至多生效其中一个。
        self.log_reduce = log_reduce  # type: bool
        # 日志聚类的聚类字段黑名单
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # 日志聚类的聚类字段白名单
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # 统计字段的最大长度
        self.max_text_len = max_text_len  # type: int
        # 保存时间，单位为天
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
                 logstore_name=None, max_split_shard=None, shard_count=None, telemetry_type=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.enable_tracking = enable_tracking  # type: bool
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        self.hot_ttl = hot_ttl  # type: int
        self.logstore_name = logstore_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.shard_count = shard_count  # type: int
        self.telemetry_type = telemetry_type  # type: str
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
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
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
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
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
        # 该种类服务日志要保存到的 logstore 名称。
        self.logstore = logstore  # type: str
        # 服务日志的种类。可选 "consumergroup_log"、 "logtail_alarm"、"operation_log"、"logtail_profile"、"metering"、"logtail_status"、"scheduled_sql_alert"、 "etl_alert" 等。
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
        # 服务日志配置列表。
        self.logging_details = logging_details  # type: list[CreateLoggingRequestLoggingDetails]
        # 服务日志要保存到的 project 名称。
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


class CreateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(self, external_name=None, group_topic=None):
        # 机器组所依赖的外部管理系统标识。
        self.external_name = external_name  # type: str
        # 机器组的日志主题。
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
        # 机器组属性。
        self.group_attribute = group_attribute  # type: CreateMachineGroupRequestGroupAttribute
        # 机器组名称。
        self.group_name = group_name  # type: str
        # 机器组类型，可选值，默认为空。
        self.group_type = group_type  # type: str
        # 机器组标识种类，支持 ip 、userdefined 两种。
        self.machine_identify_type = machine_identify_type  # type: str
        # 机器列表。
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


class CreateProjectRequest(TeaModel):
    def __init__(self, description=None, project_name=None):
        self.description = description  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
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


class CreateSavedSearchRequest(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        self.display_name = display_name  # type: str
        self.logstore = logstore  # type: str
        self.savedsearch_name = savedsearch_name  # type: str
        self.search_query = search_query  # type: str
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


class GetAppliedConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, count=None):
        # Logtail配置名称列表。
        self.configs = configs  # type: list[str]
        # Logtail配置数量。
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


class GetCheckPointRequest(TeaModel):
    def __init__(self, shard=None):
        # Shard ID。
        # 如果指定的Shard不存在，则返回空列表。
        # 如果不指定Shard，则返回所有Shard的checkpoint。
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
        # shard id。
        self.shard = shard  # type: int
        # checkpoint 值。
        self.checkpoint = checkpoint  # type: str
        # checkpoint最后的更新时间。Unix时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        self.update_time = update_time  # type: long
        # 消费者。
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


class GetContextLogsRequest(TeaModel):
    def __init__(self, back_lines=None, forward_lines=None, pack_id=None, pack_meta=None, type=None):
        # 指定起始日志往前（上文）的日志条数，取值范围为(0,100]。
        self.back_lines = back_lines  # type: long
        # 指定起始日志往后（下文）的日志条数，取值范围为(0,100]。
        self.forward_lines = forward_lines  # type: long
        # 起始日志所属的LogGroup的唯一身份标识。
        self.pack_id = pack_id  # type: str
        # 起始日志在对应LogGroup内的唯一上下文结构标识。
        self.pack_meta = pack_meta  # type: str
        # Logstore中数据的类型。该接口中该参数固定为context_log。
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
        # 向前查询到的日志条数。
        self.back_lines = back_lines  # type: long
        # 向后查询到的日志条数。
        self.forward_lines = forward_lines  # type: long
        # 获取到的日志，按上下文顺序排列。当根据指定起始日志查询不到上下文日志时，此参数为空。
        self.logs = logs  # type: list[dict[str, any]]
        # 查询的结果是否完整。
        # Complete：查询已经完成，返回结果为完整结果。
        # Incomplete：查询已经完成，返回结果为不完整结果，需要重复请求以获得完整结果。
        self.progress = progress  # type: str
        # 返回的总日志条数，包含请求参数中所指定的起始日志。
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
    def __init__(self, from_=None, type=None):
        # 时间点（Unix时间戳）或者字符串begin、end。
        self.from_ = from_  # type: str
        # 这里固定为 cursor。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCursorResponseBody(TeaModel):
    def __init__(self, cursor=None):
        # 游标位置。
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
    def __init__(self, cursor=None, type=None):
        # 游标。
        self.cursor = cursor  # type: str
        # 固定为 cursor_time 。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCursorTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetCursorTimeResponseBody(TeaModel):
    def __init__(self, cursor_time=None):
        # Cursor的服务端时间。Unix时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
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


class GetHistogramsRequest(TeaModel):
    def __init__(self, from_=None, query=None, to=None, topic=None, type=None):
        # 查询开始时间点。UNIX时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        # 
        # 时间区间遵循“左闭右开”原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        self.from_ = from_  # type: long
        # 查询语句。仅支持查询语句，不支持分析语句。关于查询语句的详细语法，请参见查询语法。
        self.query = query  # type: str
        # 查询结束时间点。UNIX时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        # 
        # 时间区间遵循“左闭右开”原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        self.to = to  # type: long
        # 日志主题。
        self.topic = topic  # type: str
        # Logstore中数据的类型。该接口中固定取值为histogram。
        self.type = type  # type: str

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
        if self.type is not None:
            result['type'] = self.type
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
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(self, from_=None, to=None, count=None, progress=None):
        # 子时间区间的开始时间点。UNIX时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        # 
        # 时间区间遵循“左闭右开”原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        self.from_ = from_  # type: long
        # 子时间区间的结束时间点。UNIX时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        # 
        # 时间区间遵循“左闭右开”原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        self.to = to  # type: long
        # 该子时间区间内查询到的日志条数。
        self.count = count  # type: long
        # 当前查询结果在该子时间区间内的结果是否完整。
        # 
        # Complete：查询已经完成，返回结果为完整结果。
        # 
        # Incomplete：查询已经完成，返回结果为不完整结果，需要重复请求以获得完整结果。
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
        # 大小写敏感
        self.case_sensitive = case_sensitive  # type: bool
        # 是否包含中文。
        self.chn = chn  # type: bool
        # 排除的字段列表。
        self.exclude_keys = exclude_keys  # type: list[str]
        # 包含的字段列表。
        self.include_keys = include_keys  # type: list[str]
        # 分词符列表。
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
        # 索引模式
        self.index_mode = index_mode  # type: str
        # 字段索引配置。key为字段名称，value为索引配置。
        self.keys = keys  # type: dict[str, KeysValue]
        # 上次修改时间
        self.last_modify_time = last_modify_time  # type: long
        # 配置全文索引。
        self.line = line  # type: GetIndexResponseBodyLine
        # 是否开启日志聚类.
        self.log_reduce = log_reduce  # type: bool
        # 日志聚类的聚类字段过滤黑名单，仅当日志聚类开启时有效。
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # 日志聚类的聚类字段过滤白名单，仅当日志聚类开启时有效。
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # 日志服务默认字段值的最大长度为2048字节，即2 KB。如果您需要修改字段值的最大长度，可设置统计字段（text）最大长度，取值范围为64~16384字节。
        self.max_text_len = max_text_len  # type: int
        # 存储类型，目前固定取值为pg。
        self.storage = storage  # type: str
        # 索引文件生命周期，支持7天、30天、90天。
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
                 topic=None, type=None):
        # 查询开始时间点。该时间是指写入日志数据时指定的日志时间。
        # 
        # 请求参数from和to定义的时间区间遵循左闭右开原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        # Unix时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        self.from_ = from_  # type: long
        # 仅当query参数为查询语句时，该参数有效，表示请求返回的最大日志条数。最小值为0，最大值为100，默认值为100。
        self.line = line  # type: long
        # 仅当query参数为查询语句时，该参数有效，表示查询开始行。默认值为0。
        self.offset = offset  # type: long
        # 用于指定返回结果是否按日志时间戳降序返回日志，精确到分钟级别。
        # 
        # true：按照日志时间戳降序返回日志。
        # false（默认值）：按照日志时间戳升序返回日志。
        # 注意
        # 当query参数为查询语句时，参数reverse有效，用于指定返回日志排序方式。
        # 当query参数为查询和分析语句时，参数reverse无效，由SQL分析语句中order by语法指定排序方式。如果order by为asc（默认），则为升序；如果order by为desc，则为降序。
        self.power_sql = power_sql  # type: bool
        # 查询语句或者分析语句。更多信息，请参见查询概述和分析概述。
        # 
        # 在query参数的分析语句中加上set session parallel_sql=true;，表示使用SQL独享版。例如* | set session parallel_sql=true; select count(*) as pv 。
        # 
        # 说明 当query参数中有分析语句（SQL语句）时，该接口的line参数和offset参数无效，建议设置为0，需通过SQL语句的LIMIT语法实现翻页。更多信息，请参见分页显示查询分析结果。
        self.query = query  # type: str
        # 用于指定返回结果是否按日志时间戳降序返回日志，精确到分钟级别。
        # 
        # true：按照日志时间戳降序返回日志。
        # false（默认值）：按照日志时间戳升序返回日志。
        # 注意
        # 当query参数为查询语句时，参数reverse有效，用于指定返回日志排序方式。
        # 当query参数为查询和分析语句时，参数reverse无效，由SQL分析语句中order by语法指定排序方式。如果order by为asc（默认），则为升序；如果order by为desc，则为降序。
        self.reverse = reverse  # type: bool
        # 查询结束时间点。该时间是指写入日志数据时指定的日志时间。
        # 
        # 请求参数from和to定义的时间区间遵循左闭右开原则，即该时间区间包括区间开始时间点，但不包括区间结束时间点。如果from和to的值相同，则为无效区间，函数直接返回错误。
        # Unix时间戳格式，表示从1970-1-1 00:00:00 UTC计算起的秒数。
        self.to = to  # type: long
        # status: 401 | SELECT remote_addr,COUNT(*) as pv GROUP by remote_addr ORDER by pv desc limit 5
        self.topic = topic  # type: str
        # 查询Logstore数据的类型。在该接口中固定取值为log。
        self.type = type  # type: str

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
        if self.type is not None:
            result['type'] = self.type
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
        if m.get('type') is not None:
            self.type = m.get('type')
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
        # 是否使用SQL独享版。更多信息，请参见开启SQL独享版。
        # 
        # true：使用SQL独享版。
        # false（默认值）：使用SQL普通版。
        # 除通过powerSql参数配置SQL独享版外，您还可以使用query参数。
        self.power_sql = power_sql  # type: bool
        # 标准SQL语句。例如日志库名称为nginx-moni，查询时间区间在2022-03-01 10:41:40到2022-03-01 10:56:40之间的访问数量。
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


class ListDomainsRequest(TeaModel):
    def __init__(self, domain_name=None, offset=None, size=None):
        # 用于搜索匹配的自定义域名
        self.domain_name = domain_name  # type: str
        self.offset = offset  # type: int
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
        self.count = count  # type: long
        self.domains = domains  # type: list[str]
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


class ListLogStoresRequest(TeaModel):
    def __init__(self, logstore_name=None, offset=None, size=None, telemetry_type=None):
        self.logstore_name = logstore_name  # type: str
        self.offset = offset  # type: int
        self.size = size  # type: int
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
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        return self


class ListLogStoresResponseBody(TeaModel):
    def __init__(self, logstores=None, total=None):
        self.logstores = logstores  # type: list[str]
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogStoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstores is not None:
            result['logstores'] = self.logstores
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
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


class ListMachineGroupRequest(TeaModel):
    def __init__(self, group_name=None, offset=None, size=None):
        # 可将 groupName 作为 pattern 匹配名称，只会返回匹配的机器组。例如 test 可以匹配机器组 test-group。
        self.group_name = group_name  # type: str
        # 分页请求的起始位置。默认为0。
        self.offset = offset  # type: int
        # 分页查询时，设置的每页行数。最大值为500。
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
        # 当前页返回的机器组数量。
        self.count = count  # type: int
        # 机器组名称列表。
        self.machinegroups = machinegroups  # type: list[str]
        # 机器组总数量。
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
        # 查询开始行。默认值为0。
        self.offset = offset  # type: int
        # 分页查询时，设置的每页行数。默认值为100，最大值为500。
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
        # 当前页返回的机器数目。
        self.count = count  # type: int
        # 返回的机器信息列表。
        self.machines = machines  # type: list[Machine]
        # 机器总数。
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
    def __init__(self, offset=None, project_name=None, size=None):
        self.offset = offset  # type: int
        self.project_name = project_name  # type: str
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
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(self, count=None, projects=None, total=None):
        self.count = count  # type: long
        self.projects = projects  # type: list[Project]
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
        self.offset = offset  # type: int
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
        self.count = count  # type: int
        self.savedsearch_items = savedsearch_items  # type: list[SavedSearch]
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


class ListTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 精确过滤的标签的键。
        self.key = key  # type: str
        # 精确过滤的标签的值。
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
        # 查询的资源的 id 列表。resource id 与 tags 应至少存在一个。
        self.resource_id = resource_id  # type: list[str]
        # 资源类型。目前取值范围：project。
        self.resource_type = resource_type  # type: str
        # 精确查找时过滤的标签键值对。resource id 与 tags 应至少存在一个。
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
        # 查询的资源的 id 列表。resource id 与 tags 应至少存在一个。
        self.resource_id_shrink = resource_id_shrink  # type: str
        # 资源类型。目前取值范围：project。
        self.resource_type = resource_type  # type: str
        # 精确查找时过滤的标签键值对。resource id 与 tags 应至少存在一个。
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
        # 资源 id。
        self.resource_id = resource_id  # type: str
        # 资源类型。
        self.resource_type = resource_type  # type: str
        # 标签的键。
        self.tag_key = tag_key  # type: str
        # 标签的值。
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
        # 下一个查询开始Token。
        self.next_token = next_token  # type: str
        # 返回的标签列表。
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


class MergeShardsRequest(TeaModel):
    def __init__(self, action=None):
        # 固定为 merge。
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MergeShardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class MergeShardsResponse(TeaModel):
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
        _map = super(MergeShardsResponse, self).to_map()
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
    def __init__(self, action=None, key=None, shard_count=None):
        # 这里固定为 split。
        self.action = action  # type: str
        # 分裂的位置。
        self.key = key  # type: str
        # 要分裂成的 shard 数量，默认为 2。
        self.shard_count = shard_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SplitShardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.key is not None:
            result['key'] = self.key
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
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
        # 标签的 key。
        self.key = key  # type: str
        # 标签的 value。
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
        # 资源的 id 列表，可以一次为多个同类型资源打上相同的标签。
        self.resource_id = resource_id  # type: list[str]
        # 资源的类型。目前取值范围：project。
        self.resource_type = resource_type  # type: str
        # 标签列表。
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


class UnTagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tags=None):
        # 是否删除所有标签，默认为 false，表示仅删除 tags 列表中的标签项。值为 true 时删除资源上绑定的所有标签。
        self.all = all  # type: bool
        # 资源的 id 列表，可以一次为多个同类型资源删除相同的标签。当 all 为 false 时生效。
        self.resource_id = resource_id  # type: list[str]
        # 资源的类型。目前取值范围 ： project。
        self.resource_type = resource_type  # type: str
        # 标签 key 列表。当 all 为 false 时，仅删除列表中的标签。
        self.tags = tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesRequest, self).to_map()
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


class UnTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UnTagResourcesResponse, self).to_map()
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


class UpdateCheckPointRequest(TeaModel):
    def __init__(self, checkpoint=None, shard=None, consumer=None, force_success=None, type=None):
        # checkpoint值。
        self.checkpoint = checkpoint  # type: str
        # shard 的 id。
        self.shard = shard  # type: int
        # 消费者。
        self.consumer = consumer  # type: str
        # 当不指定消费者时，必须指定forceSuccess为true才能更新checkpoint。
        self.force_success = force_success  # type: bool
        # 固定为 checkpoint。
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCheckPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint
        if self.shard is not None:
            result['shard'] = self.shard
        if self.consumer is not None:
            result['consumer'] = self.consumer
        if self.force_success is not None:
            result['forceSuccess'] = self.force_success
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        if m.get('forceSuccess') is not None:
            self.force_success = m.get('forceSuccess')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateCheckPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UpdateCheckPointResponse, self).to_map()
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
        self.order = order  # type: bool
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


class UpdateIndexRequestLine(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, exclude_keys=None, include_keys=None, token=None):
        # 大小写敏感
        self.case_sensitive = case_sensitive  # type: bool
        # 包含中文
        self.chn = chn  # type: bool
        # 排除的字段列表，不能与include_keys同时指定。
        self.exclude_keys = exclude_keys  # type: list[str]
        # 包含的字段列表，不能与exclude_keys同时指定。
        self.include_keys = include_keys  # type: list[str]
        # 分词符列表。可以设置一个分词参数，指定这个字段按照哪一种方式分词。
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
        # 字段索引配置，key为字段名称，value为字段索引配置。
        self.keys = keys  # type: dict[str, KeysValue]
        # 配置全文索引。
        self.line = line  # type: UpdateIndexRequestLine
        # 开启日志聚类，开启后白名单与黑名单至多生效其中一个。
        self.log_reduce = log_reduce  # type: bool
        # 日志聚类的聚类字段黑名单
        self.log_reduce_black_list = log_reduce_black_list  # type: list[str]
        # 日志聚类的聚类字段白名单
        self.log_reduce_white_list = log_reduce_white_list  # type: list[str]
        # 统计字段的最大长度
        self.max_text_len = max_text_len  # type: int
        # 保存时间，单位为天
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
                 logstore_name=None, max_split_shard=None, shard_count=None, telemetry_type=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.enable_tracking = enable_tracking  # type: bool
        self.encrypt_conf = encrypt_conf  # type: EncryptConf
        self.hot_ttl = hot_ttl  # type: int
        self.logstore_name = logstore_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.shard_count = shard_count  # type: int
        self.telemetry_type = telemetry_type  # type: str
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
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
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
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
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


class UpdateLoggingRequestLoggingDetails(TeaModel):
    def __init__(self, logstore=None, type=None):
        # 该种类服务日志要保存到的 logstore 名称。
        self.logstore = logstore  # type: str
        # 服务日志的种类。可选 "consumergroup_log"、 "logtail_alarm"、"operation_log"、"logtail_profile"、"metering"、"logtail_status"、"scheduled_sql_alert"、 "etl_alert" 等。
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
        # 服务日志配置列表。
        self.logging_details = logging_details  # type: list[UpdateLoggingRequestLoggingDetails]
        # 服务日志要保存到的 project 名称。
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


class UpdateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(self, external_name=None, group_topic=None):
        # 机器组所依赖的外部管理系统标识。
        self.external_name = external_name  # type: str
        # 机器组的日志主题。
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
        # 机器组属性。
        self.group_attribute = group_attribute  # type: UpdateMachineGroupRequestGroupAttribute
        # 机器组名称。
        self.group_name = group_name  # type: str
        # 机器组类型，可选值，默认为空。
        self.group_type = group_type  # type: str
        # 机器组标识种类，支持 ip 、userdefined 两种。
        self.machine_identify_type = machine_identify_type  # type: str
        # 机器列表。
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


class UpdateProjectRequest(TeaModel):
    def __init__(self, description=None):
        # Project description
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


class UpdateSavedSearchRequest(TeaModel):
    def __init__(self, display_name=None, logstore=None, savedsearch_name=None, search_query=None, topic=None):
        self.display_name = display_name  # type: str
        self.logstore = logstore  # type: str
        self.savedsearch_name = savedsearch_name  # type: str
        self.search_query = search_query  # type: str
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


class KeysValue(TeaModel):
    def __init__(self, case_sensitive=None, chn=None, type=None, alias=None, token=None, doc_value=None):
        # 大小写敏感
        self.case_sensitive = case_sensitive  # type: bool
        # 包含中文
        self.chn = chn  # type: bool
        # 字段的索引类型
        self.type = type  # type: str
        # 别名
        self.alias = alias  # type: str
        # 分词符列表。仅当type参数取值为text时，必须设置。
        self.token = token  # type: list[str]
        # 开启统计
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


