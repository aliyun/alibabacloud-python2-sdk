# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ABTestExperiment(TeaModel):
    def __init__(self, name=None, online=None, params=None, serial_number=None, traffic=None):
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: dict[str, str]
        self.serial_number = serial_number  # type: int
        self.traffic = traffic  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ABTestExperiment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.traffic is not None:
            result['traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        return self


class ABTestGroup(TeaModel):
    def __init__(self, name=None, status=None):
        self.name = name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ABTestGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ABTestScene(TeaModel):
    def __init__(self, name=None, status=None, values=None):
        self.name = name  # type: str
        self.status = status  # type: int
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ABTestScene, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class AppCluster(TeaModel):
    def __init__(self, max_query_clause_length=None, max_timeout_ms=None):
        self.max_query_clause_length = max_query_clause_length  # type: int
        self.max_timeout_ms = max_timeout_ms  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_query_clause_length is not None:
            result['maxQueryClauseLength'] = self.max_query_clause_length
        if self.max_timeout_ms is not None:
            result['maxTimeoutMS'] = self.max_timeout_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxQueryClauseLength') is not None:
            self.max_query_clause_length = m.get('maxQueryClauseLength')
        if m.get('maxTimeoutMS') is not None:
            self.max_timeout_ms = m.get('maxTimeoutMS')
        return self


class App(TeaModel):
    def __init__(self, auto_switch=None, cluster=None, data_sources=None, description=None, domain=None,
                 fetch_fields=None, first_ranks=None, network_type=None, query_processors=None, quota=None, realtime_shared=None,
                 schema=None, schemas=None, second_ranks=None, summaries=None, type=None):
        self.auto_switch = auto_switch  # type: bool
        self.cluster = cluster  # type: AppCluster
        self.data_sources = data_sources  # type: list[DataSource]
        self.description = description  # type: str
        self.domain = domain  # type: Domain
        self.fetch_fields = fetch_fields  # type: list[str]
        self.first_ranks = first_ranks  # type: list[FirstRank]
        self.network_type = network_type  # type: str
        self.query_processors = query_processors  # type: list[QueryProcessor]
        self.quota = quota  # type: Quota
        self.realtime_shared = realtime_shared  # type: bool
        self.schema = schema  # type: Schema
        self.schemas = schemas  # type: list[Schema]
        self.second_ranks = second_ranks  # type: list[SecondRank]
        self.summaries = summaries  # type: list[Summary]
        self.type = type  # type: str

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.domain:
            self.domain.validate()
        if self.first_ranks:
            for k in self.first_ranks:
                if k:
                    k.validate()
        if self.query_processors:
            for k in self.query_processors:
                if k:
                    k.validate()
        if self.quota:
            self.quota.validate()
        if self.schema:
            self.schema.validate()
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()
        if self.second_ranks:
            for k in self.second_ranks:
                if k:
                    k.validate()
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(App, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster is not None:
            result['cluster'] = self.cluster.to_map()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        result['firstRanks'] = []
        if self.first_ranks is not None:
            for k in self.first_ranks:
                result['firstRanks'].append(k.to_map() if k else None)
        if self.network_type is not None:
            result['networkType'] = self.network_type
        result['queryProcessors'] = []
        if self.query_processors is not None:
            for k in self.query_processors:
                result['queryProcessors'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.realtime_shared is not None:
            result['realtimeShared'] = self.realtime_shared
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        result['schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['schemas'].append(k.to_map() if k else None)
        result['secondRanks'] = []
        if self.second_ranks is not None:
            for k in self.second_ranks:
                result['secondRanks'].append(k.to_map() if k else None)
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cluster') is not None:
            temp_model = AppCluster()
            self.cluster = temp_model.from_map(m['cluster'])
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = DataSource()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = Domain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        self.first_ranks = []
        if m.get('firstRanks') is not None:
            for k in m.get('firstRanks'):
                temp_model = FirstRank()
                self.first_ranks.append(temp_model.from_map(k))
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        self.query_processors = []
        if m.get('queryProcessors') is not None:
            for k in m.get('queryProcessors'):
                temp_model = QueryProcessor()
                self.query_processors.append(temp_model.from_map(k))
        if m.get('quota') is not None:
            temp_model = Quota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('realtimeShared') is not None:
            self.realtime_shared = m.get('realtimeShared')
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        self.schemas = []
        if m.get('schemas') is not None:
            for k in m.get('schemas'):
                temp_model = Schema()
                self.schemas.append(temp_model.from_map(k))
        self.second_ranks = []
        if m.get('secondRanks') is not None:
            for k in m.get('secondRanks'):
                temp_model = SecondRank()
                self.second_ranks.append(temp_model.from_map(k))
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = Summary()
                self.summaries.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AppGroup(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, description=None, domain=None, name=None, quota=None,
                 type=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: str
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.name = name  # type: str
        self.quota = quota  # type: Quota
        self.type = type  # type: str

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(AppGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = Quota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DataSource(TeaModel):
    def __init__(self, fields=None, key_field=None, parameters=None, plugins=None, schema_name=None, table_name=None,
                 type=None):
        self.fields = fields  # type: list[dict[str, str]]
        self.key_field = key_field  # type: str
        self.parameters = parameters  # type: dict[str, any]
        self.plugins = plugins  # type: dict[str, DataSourcePluginsValue]
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.plugins:
            for v in self.plugins.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(DataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.key_field is not None:
            result['keyField'] = self.key_field
        if self.parameters is not None:
            result['parameters'] = self.parameters
        result['plugins'] = {}
        if self.plugins is not None:
            for k, v in self.plugins.items():
                result['plugins'][k] = v.to_map()
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        self.plugins = {}
        if m.get('plugins') is not None:
            for k, v in m.get('plugins').items():
                temp_model = DataSourcePluginsValue()
                self.plugins[k] = temp_model.from_map(v)
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Domain(TeaModel):
    def __init__(self, category=None, functions=None, name=None):
        self.category = category  # type: str
        self.functions = functions  # type: dict[str, list[str]]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Domain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            self.functions = m.get('functions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class FirstRank(TeaModel):
    def __init__(self, active=None, description=None, meta=None, name=None, type=None):
        self.active = active  # type: bool
        self.description = description  # type: str
        self.meta = meta  # type: any
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FirstRank, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PrepayOrderInfo(TeaModel):
    def __init__(self, auto_renew=None, duration=None, pricing_cycle=None):
        self.auto_renew = auto_renew  # type: bool
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrepayOrderInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class QueryProcessor(TeaModel):
    def __init__(self, active=None, category=None, domain=None, indexes=None, name=None, processors=None):
        self.active = active  # type: bool
        self.category = category  # type: str
        self.domain = domain  # type: str
        self.indexes = indexes  # type: list[str]
        self.name = name  # type: str
        self.processors = processors  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProcessor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class Quota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, order_type=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.order_type = order_type  # type: str
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Quota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ScheduledTaskFilter(TeaModel):
    def __init__(self, days=None, expression=None, field=None, unit=None):
        self.days = days  # type: int
        self.expression = expression  # type: str
        self.field = field  # type: str
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScheduledTaskFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['days'] = self.days
        if self.expression is not None:
            result['expression'] = self.expression
        if self.field is not None:
            result['field'] = self.field
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class ScheduledTask(TeaModel):
    def __init__(self, auto_switch=None, cron=None, enabled=None, filter=None, forked_app_id=None, permanent=None,
                 run_now=None, type=None, version=None):
        self.auto_switch = auto_switch  # type: bool
        self.cron = cron  # type: str
        self.enabled = enabled  # type: bool
        self.filter = filter  # type: ScheduledTaskFilter
        self.forked_app_id = forked_app_id  # type: str
        self.permanent = permanent  # type: bool
        self.run_now = run_now  # type: bool
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super(ScheduledTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cron is not None:
            result['cron'] = self.cron
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        if self.forked_app_id is not None:
            result['forkedAppId'] = self.forked_app_id
        if self.permanent is not None:
            result['permanent'] = self.permanent
        if self.run_now is not None:
            result['runNow'] = self.run_now
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('filter') is not None:
            temp_model = ScheduledTaskFilter()
            self.filter = temp_model.from_map(m['filter'])
        if m.get('forkedAppId') is not None:
            self.forked_app_id = m.get('forkedAppId')
        if m.get('permanent') is not None:
            self.permanent = m.get('permanent')
        if m.get('runNow') is not None:
            self.run_now = m.get('runNow')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class SchemaIndexSortConfig(TeaModel):
    def __init__(self, direction=None, field=None):
        self.direction = direction  # type: str
        self.field = field  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SchemaIndexSortConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.field is not None:
            result['field'] = self.field
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('field') is not None:
            self.field = m.get('field')
        return self


class SchemaIndexes(TeaModel):
    def __init__(self, filter_fields=None, search_fields=None):
        self.filter_fields = filter_fields  # type: list[str]
        self.search_fields = search_fields  # type: dict[str, SchemaIndexesSearchFieldsValue]

    def validate(self):
        if self.search_fields:
            for v in self.search_fields.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SchemaIndexes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_fields is not None:
            result['filterFields'] = self.filter_fields
        result['searchFields'] = {}
        if self.search_fields is not None:
            for k, v in self.search_fields.items():
                result['searchFields'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filterFields') is not None:
            self.filter_fields = m.get('filterFields')
        self.search_fields = {}
        if m.get('searchFields') is not None:
            for k, v in m.get('searchFields').items():
                temp_model = SchemaIndexesSearchFieldsValue()
                self.search_fields[k] = temp_model.from_map(v)
        return self


class SchemaTtlField(TeaModel):
    def __init__(self, name=None, ttl=None):
        self.name = name  # type: str
        self.ttl = ttl  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SchemaTtlField, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class Schema(TeaModel):
    def __init__(self, index_sort_config=None, indexes=None, name=None, route_field=None, route_field_values=None,
                 second_route_field=None, tables=None, ttl_field=None):
        self.index_sort_config = index_sort_config  # type: list[SchemaIndexSortConfig]
        self.indexes = indexes  # type: SchemaIndexes
        self.name = name  # type: str
        self.route_field = route_field  # type: str
        self.route_field_values = route_field_values  # type: list[str]
        self.second_route_field = second_route_field  # type: str
        self.tables = tables  # type: dict[str, SchemaTablesValue]
        self.ttl_field = ttl_field  # type: SchemaTtlField

    def validate(self):
        if self.index_sort_config:
            for k in self.index_sort_config:
                if k:
                    k.validate()
        if self.indexes:
            self.indexes.validate()
        if self.tables:
            for v in self.tables.values():
                if v:
                    v.validate()
        if self.ttl_field:
            self.ttl_field.validate()

    def to_map(self):
        _map = super(Schema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexSortConfig'] = []
        if self.index_sort_config is not None:
            for k in self.index_sort_config:
                result['indexSortConfig'].append(k.to_map() if k else None)
        if self.indexes is not None:
            result['indexes'] = self.indexes.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.route_field is not None:
            result['routeField'] = self.route_field
        if self.route_field_values is not None:
            result['routeFieldValues'] = self.route_field_values
        if self.second_route_field is not None:
            result['secondRouteField'] = self.second_route_field
        result['tables'] = {}
        if self.tables is not None:
            for k, v in self.tables.items():
                result['tables'][k] = v.to_map()
        if self.ttl_field is not None:
            result['ttlField'] = self.ttl_field.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.index_sort_config = []
        if m.get('indexSortConfig') is not None:
            for k in m.get('indexSortConfig'):
                temp_model = SchemaIndexSortConfig()
                self.index_sort_config.append(temp_model.from_map(k))
        if m.get('indexes') is not None:
            temp_model = SchemaIndexes()
            self.indexes = temp_model.from_map(m['indexes'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeField') is not None:
            self.route_field = m.get('routeField')
        if m.get('routeFieldValues') is not None:
            self.route_field_values = m.get('routeFieldValues')
        if m.get('secondRouteField') is not None:
            self.second_route_field = m.get('secondRouteField')
        self.tables = {}
        if m.get('tables') is not None:
            for k, v in m.get('tables').items():
                temp_model = SchemaTablesValue()
                self.tables[k] = temp_model.from_map(v)
        if m.get('ttlField') is not None:
            temp_model = SchemaTtlField()
            self.ttl_field = temp_model.from_map(m['ttlField'])
        return self


class SearchStrategyMergeConfig(TeaModel):
    def __init__(self, doc_count=None, rank_name=None):
        self.doc_count = doc_count  # type: int
        self.rank_name = rank_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchStrategyMergeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_count is not None:
            result['docCount'] = self.doc_count
        if self.rank_name is not None:
            result['rankName'] = self.rank_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docCount') is not None:
            self.doc_count = m.get('docCount')
        if m.get('rankName') is not None:
            self.rank_name = m.get('rankName')
        return self


class SearchStrategySearchConfigs(TeaModel):
    def __init__(self, first_rank_name=None, merge_proportion=None, query_type=None, second_rank_name=None):
        self.first_rank_name = first_rank_name  # type: str
        self.merge_proportion = merge_proportion  # type: int
        self.query_type = query_type  # type: str
        self.second_rank_name = second_rank_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchStrategySearchConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_rank_name is not None:
            result['firstRankName'] = self.first_rank_name
        if self.merge_proportion is not None:
            result['mergeProportion'] = self.merge_proportion
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.second_rank_name is not None:
            result['secondRankName'] = self.second_rank_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('firstRankName') is not None:
            self.first_rank_name = m.get('firstRankName')
        if m.get('mergeProportion') is not None:
            self.merge_proportion = m.get('mergeProportion')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('secondRankName') is not None:
            self.second_rank_name = m.get('secondRankName')
        return self


class SearchStrategy(TeaModel):
    def __init__(self, description=None, is_default=None, merge_config=None, name=None, search_configs=None):
        self.description = description  # type: str
        self.is_default = is_default  # type: bool
        self.merge_config = merge_config  # type: SearchStrategyMergeConfig
        self.name = name  # type: str
        self.search_configs = search_configs  # type: list[SearchStrategySearchConfigs]

    def validate(self):
        if self.merge_config:
            self.merge_config.validate()
        if self.search_configs:
            for k in self.search_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.merge_config is not None:
            result['mergeConfig'] = self.merge_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['searchConfigs'] = []
        if self.search_configs is not None:
            for k in self.search_configs:
                result['searchConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('mergeConfig') is not None:
            temp_model = SearchStrategyMergeConfig()
            self.merge_config = temp_model.from_map(m['mergeConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.search_configs = []
        if m.get('searchConfigs') is not None:
            for k in m.get('searchConfigs'):
                temp_model = SearchStrategySearchConfigs()
                self.search_configs.append(temp_model.from_map(k))
        return self


class SecondRank(TeaModel):
    def __init__(self, active=None, description=None, meta=None, name=None):
        self.active = active  # type: bool
        self.description = description  # type: str
        self.meta = meta  # type: any
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SecondRank, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SummaryMeta(TeaModel):
    def __init__(self, element=None, ellipsis=None, field=None, len=None, snippet=None):
        self.element = element  # type: str
        self.ellipsis = ellipsis  # type: str
        self.field = field  # type: str
        self.len = len  # type: int
        self.snippet = snippet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SummaryMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class Summary(TeaModel):
    def __init__(self, active=None, meta=None, name=None):
        self.active = active  # type: bool
        self.meta = meta  # type: SummaryMeta
        self.name = name  # type: str

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super(Summary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('meta') is not None:
            temp_model = SummaryMeta()
            self.meta = temp_model.from_map(m['meta'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DataSourcePluginsValue(TeaModel):
    def __init__(self, name=None, from_fields=None, parameters=None):
        self.name = name  # type: str
        self.from_fields = from_fields  # type: str
        self.parameters = parameters  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSourcePluginsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.from_fields is not None:
            result['fromFields'] = self.from_fields
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fromFields') is not None:
            self.from_fields = m.get('fromFields')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class SchemaIndexesSearchFieldsValue(TeaModel):
    def __init__(self, analyzer=None, analyzer_type=None, analyzer_generation=None, fields=None, label=None):
        self.analyzer = analyzer  # type: str
        self.analyzer_type = analyzer_type  # type: str
        self.analyzer_generation = analyzer_generation  # type: str
        self.fields = fields  # type: list[str]
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SchemaIndexesSearchFieldsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.analyzer_generation is not None:
            result['analyzerGeneration'] = self.analyzer_generation
        if self.fields is not None:
            result['fields'] = self.fields
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('analyzerGeneration') is not None:
            self.analyzer_generation = m.get('analyzerGeneration')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class SchemaTablesValue(TeaModel):
    def __init__(self, name=None, primary_table=None, fields=None):
        self.name = name  # type: str
        self.primary_table = primary_table  # type: bool
        self.fields = fields  # type: dict[str, SchemaTablesValueFieldsValue]

    def validate(self):
        if self.fields:
            for v in self.fields.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SchemaTablesValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.primary_table is not None:
            result['primaryTable'] = self.primary_table
        result['fields'] = {}
        if self.fields is not None:
            for k, v in self.fields.items():
                result['fields'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryTable') is not None:
            self.primary_table = m.get('primaryTable')
        self.fields = {}
        if m.get('fields') is not None:
            for k, v in m.get('fields').items():
                temp_model = SchemaTablesValueFieldsValue()
                self.fields[k] = temp_model.from_map(v)
        return self


class SchemaTablesValueFieldsValue(TeaModel):
    def __init__(self, name=None, primary_key=None, type=None, join_with=None, label=None):
        self.name = name  # type: str
        self.primary_key = primary_key  # type: bool
        self.type = type  # type: str
        self.join_with = join_with  # type: list[str]
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SchemaTablesValueFieldsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.type is not None:
            result['type'] = self.type
        if self.join_with is not None:
            result['joinWith'] = self.join_with
        if self.label is not None:
            result['label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('joinWith') is not None:
            self.join_with = m.get('joinWith')
        if m.get('label') is not None:
            self.label = m.get('label')
        return self


class BindESUserAnalyzerRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindESUserAnalyzerRequest, self).to_map()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindESUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEsInstanceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindEsInstanceRequest, self).to_map()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindEsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompileSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CompileSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CompileSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestExperimentRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body.
        self.body = body  # type: ABTestExperiment
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestExperiment()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        # The time when the experiment was created.
        self.created = created  # type: int
        # The experiment ID.
        self.id = id  # type: str
        # The experiment alias.
        self.name = name  # type: str
        # Indicates whether the experiment is in effect. Valid values:
        # 
        # *   true
        # *   false
        self.online = online  # type: bool
        # The experiment parameters.
        self.params = params  # type: dict[str, any]
        # The percentage of traffic that is routed to the experiment.
        self.traffic = traffic  # type: int
        # The time when the experiment was last modified.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The experiment details.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestGroupRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: ABTestGroup
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestGroup()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        # The time when the test group was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test group was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestSceneRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: ABTestScene
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestScene()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        # The time when the test scenario was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test scenario. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test scenario was last modified.
        self.updated = updated  # type: int
        # The tag of the test scenario.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body.
        self.body = body  # type: App
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = App()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned results.
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
    def __init__(self, body=None):
        self.body = body  # type: AppGroup

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AppGroup()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
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
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type  # type: str
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        self.domain = domain  # type: str
        # The expiration time.
        self.expire_on = expire_on  # type: str
        # The ID of the created rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The ID of the application.
        self.id = id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is not complete for the instance. For example, an order is one that is initiated to create the instance or change the quotas or billing method.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The information about the quotas of the application.
        self.quota = quota  # type: CreateAppGroupResponseBodyResultQuota
        # The ID of the created fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type  # type: str
        # The timestamp when the application was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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


class CreateFirstRankRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body that contains the parameters of the rough sort expression.
        self.body = body  # type: FirstRank
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFirstRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = FirstRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        # The parameters that are used by a function in the expression.
        self.arg = arg  # type: str
        # The attribute, feature functions, or field to be searched for.
        self.attribute = attribute  # type: str
        # The weight. Valid values: \[-100000,100000]. The value cannot be 0.
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
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The content of the expression.
        self.meta = meta  # type: list[CreateFirstRankResponseBodyResultMeta]
        # The name of the expression.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the rough sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters  # type: list[CreateFunctionInstanceRequestCreateParameters]
        # The cron expression used to schedule periodic training, in the format of (Minutes Hours DayofMonth Month DayofWeek). The default value is empty, which indicates that no periodic training is performed. DayofWeek 0 indicates Sunday.
        self.cron = cron  # type: str
        # The description.
        self.description = description  # type: str
        # The type of the feature. Valid values:
        # 
        # *   PAAS: This is the default value. Training is required before you can use the feature.
        self.function_type = function_type  # type: str
        # The name of the instance. The name must be 1 to 30 characters in length and can contain letters, digits, and underscores (\_). The name is case-sensitive and must start with a letter.
        self.instance_name = instance_name  # type: str
        # The type of the model. The following features correspond to different model types:
        # 
        # *   click-through rate (CTR) model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Shading model: offline_inference
        # *   Drop-down suggestion model: offline_inference
        # *   Word segmentation model: text
        # *   Term weight model: tf_checkpoint
        self.model_type = model_type  # type: str
        # The parameters that are used to use the instance.
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message. If no error occurs, this parameter is left empty.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionResourceRequestDataGeneratorsInputFeatures(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionResourceRequestDataGeneratorsInputFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFunctionResourceRequestDataGeneratorsInput(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[CreateFunctionResourceRequestDataGeneratorsInputFeatures]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFunctionResourceRequestDataGeneratorsInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = CreateFunctionResourceRequestDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class CreateFunctionResourceRequestDataGenerators(TeaModel):
    def __init__(self, generator=None, input=None, output=None):
        self.generator = generator  # type: str
        self.input = input  # type: CreateFunctionResourceRequestDataGeneratorsInput
        self.output = output  # type: str

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(CreateFunctionResourceRequestDataGenerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = CreateFunctionResourceRequestDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class CreateFunctionResourceRequestData(TeaModel):
    def __init__(self, content=None, generators=None):
        self.content = content  # type: str
        self.generators = generators  # type: list[CreateFunctionResourceRequestDataGenerators]

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFunctionResourceRequestData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = CreateFunctionResourceRequestDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class CreateFunctionResourceRequest(TeaModel):
    def __init__(self, data=None, description=None, resource_name=None, resource_type=None):
        self.data = data  # type: CreateFunctionResourceRequestData
        self.description = description  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateFunctionResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateFunctionResourceRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateFunctionResourceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionResourceResponseBody, self).to_map()
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


class CreateFunctionResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionTaskResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInterventionDictionaryRequest(TeaModel):
    def __init__(self, analyzer_type=None, name=None, type=None, dry_run=None):
        # The type of the analyzer. Valid values:
        # 
        # *   MODEL: model-based custom analyzer.
        # *   SYSTEM: system analyzer.
        # *   USER: custom analyzer.
        self.analyzer_type = analyzer_type  # type: str
        # The name of the intervention dictionary.
        self.name = name  # type: str
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering.
        # *   synonym: an intervention dictionary for synonym configuration.
        # *   correction: an intervention dictionary for spelling correction.
        # *   category_prediction: an intervention dictionary for category prediction.
        # *   ner: an intervention dictionary for named entity recognition (NER).
        # *   term_weighting: an intervention dictionary for term weight analysis.
        # *   suggest_allowlist: a drop-down suggestion whitelist.
        # *   suggest_denylist: a drop-down suggestion blacklist.
        # *   hot_allowlist: a top search whitelist.
        # *   hot_denylist: a top search blacklist.
        # *   hint_allowlist: a hint whitelist.
        # *   hint_denylist: a hint blacklist.
        self.type = type  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInterventionDictionaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        # Creates an intervention dictionary.
        self.analyzer = analyzer  # type: str
        # The name of the intervention dictionary.
        self.created = created  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        # CreateInterventionDictionary
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
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        # *   suggest_allowlist: a drop-down suggestion whitelist
        # *   suggest_denylist: a drop-down suggestion blacklist
        # *   hot_allowlist: a top search whitelist
        # *   hot_denylist: a top search blacklist
        # *   hint_allowlist: a shading whitelist
        # *   hint_denylist: a shading blacklist
        self.request_id = request_id  # type: str
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueryProcessorRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body.
        self.body = body  # type: any
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueryProcessorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        # Indicates whether the query analysis rule is the default one.
        self.active = active  # type: bool
        # The time when the query analysis rule was created.
        self.created = created  # type: int
        # The type of the industry to which the query analysis rule was applied. Valid values:
        # 
        # *   GENERAL: general.
        # *   ECOMMERCE: e-commerce.
        # *   IT_CONTENT: IT content.
        self.domain = domain  # type: str
        # The indexes to which the query analysis rule was applied.
        self.indexes = indexes  # type: list[str]
        # The name of the query analysis rule.
        self.name = name  # type: str
        # The features that are used in the query analysis rule.
        # 
        # For more information, see [QueryProcessor](~~170014~~).
        self.processors = processors  # type: list[dict[str, any]]
        # The time when the query analysis rule was last modified.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the query analysis rule.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskRequest(TeaModel):
    def __init__(self, body=None):
        # 请求体
        self.body = body  # type: ScheduledTask

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScheduledTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ScheduledTask()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the scheduled task.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSearchStrategyRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: SearchStrategy

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSearchStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SearchStrategy()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecondRankRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: SecondRank
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecondRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SecondRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the fine sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSortScriptRequest(TeaModel):
    def __init__(self, scope=None, script_name=None, type=None):
        # 脚本的作用范围
        self.scope = scope  # type: str
        # 脚本名称
        self.script_name = script_name  # type: str
        # 脚本的类型，目前只支持cava_script
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSortScriptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSortScriptResponseBodyResult(TeaModel):
    def __init__(self, scope=None, script_name=None, type=None):
        # 脚本的作用范围
        self.scope = scope  # type: str
        # 脚本名称
        self.script_name = script_name  # type: str
        # 脚本的类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSortScriptResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # 返回结果
        self.result = result  # type: CreateSortScriptResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateSortScriptResponseBody, self).to_map()
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
            temp_model = CreateSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateSortScriptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAnalyzerRequest(TeaModel):
    def __init__(self, business=None, business_app_group_id=None, business_type=None, name=None, type=None,
                 dry_run=None):
        self.business = business  # type: str
        self.business_app_group_id = business_app_group_id  # type: str
        self.business_type = business_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserAnalyzerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['business'] = self.business
        if self.business_app_group_id is not None:
            result['businessAppGroupId'] = self.business_app_group_id
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('business') is not None:
            self.business = m.get('business')
        if m.get('businessAppGroupId') is not None:
            self.business_app_group_id = m.get('businessAppGroupId')
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The custom analyzer.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned results.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message. If no error occurs, this parameter is left empty.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request. Valid values:
        # 
        # *   OK: The request is successful.
        # *   FAIL: The request fails.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionResourceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionResourceResponseBody, self).to_map()
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


class DeleteFunctionResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFunctionResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFunctionResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionTaskResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestExperimentResponseBodyResultParams(TeaModel):
    def __init__(self, first_formula_name=None):
        # The name of the rough sort policy.
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
        # The time when the test was created.
        self.created = created  # type: int
        # The ID of the test.
        self.id = id  # type: str
        # The name of the test.
        self.name = name  # type: str
        # The status of the test. Valid values:
        # 
        # *   true: in effect
        # *   false: not in effect
        self.online = online  # type: bool
        # The parameters of the test.
        self.params = params  # type: DescribeABTestExperimentResponseBodyResultParams
        # The percentage of traffic that is routed to the test.
        self.traffic = traffic  # type: int
        # The time when the test was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the test.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        # The time when the test group was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test group was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the test group.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        # The time when the test scenario was created.
        self.created = created  # type: int
        # The ID of the test scenario.
        self.id = id  # type: str
        # The name of the test scenario.
        self.name = name  # type: str
        # The status of the test scenario. Valid values:
        # 
        # *   0: The test is stopped.
        # *   1: The test is started.
        self.status = status  # type: int
        # The time when the test was last modified.
        self.updated = updated  # type: int
        # The indicators of the test scenarios.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The details of the test scenario.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The number of search requests per second. You are charged based on the number of search requests per second in the earlier billing model.
        self.qps = qps  # type: int
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
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
        # The ID of the created rough sort expression.
        self.algo_deployment_id = algo_deployment_id  # type: int
        # Indicates whether the version is automatically published to the online environment.
        self.auto_switch = auto_switch  # type: bool
        self.cluster_name = cluster_name  # type: str
        # The timestamp when the version was created.
        self.created = created  # type: int
        # The description of the version.
        self.description = description  # type: str
        self.domain = domain  # type: DescribeAppResponseBodyResultDomain
        # The default display fields.
        self.fetch_fields = fetch_fields  # type: list[str]
        # The ID of the version.
        self.id = id  # type: str
        # The progress of data import, in percentage. For example, a value of 83 indicates 83%.
        self.progress_percent = progress_percent  # type: int
        # The quota information about the version.
        self.quota = quota  # type: DescribeAppResponseBodyResultQuota
        # The application schema.
        self.schema = schema  # type: dict[str, any]
        # The status of the version. Valid values:
        # 
        # *   ok
        # *   stopped
        # *   frozen
        # *   initializing
        # *   unavailable
        # *   data_waiting
        # *   data_preparing
        self.status = status  # type: str
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the version.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
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


class DescribeAppGroupResponseBodyResultTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupResponseBodyResultTags, self).to_map()
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


class DescribeAppGroupResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None, resource_group_id=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, tags=None, type=None, updated=None):
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type  # type: str
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        self.domain = domain  # type: str
        # The expiration time.
        self.expire_on = expire_on  # type: str
        # The ID of the created rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The ID of the application.
        self.id = id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is not complete for the instance. For example, an order is one that is initiated to create the instance or change the quotas or billing method.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The information about the quotas of the application.
        self.quota = quota  # type: DescribeAppGroupResponseBodyResultQuota
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the created fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        self.tags = tags  # type: list[DescribeAppGroupResponseBodyResultTags]
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type  # type: str
        # The timestamp when the application was last updated.
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeAppGroupResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the application.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The statistics.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCollctionResponseBodyResult(TeaModel):
    def __init__(self, created=None, data_collection_type=None, id=None, industry_name=None, name=None, status=None,
                 sundial_id=None, type=None, updated=None):
        # The time when the data collection task was created.
        self.created = created  # type: int
        # The type of the data that is collected by the task. Valid values:
        # 
        # *   behavior: behavioral data
        # *   item_info: project data
        # *   industry_specific: industry-specific data
        self.data_collection_type = data_collection_type  # type: str
        # The ID of the data collection task.
        self.id = id  # type: str
        # The industry to which the data collection task applies. Valid values:
        # 
        # *   general
        # *   ecommerce
        self.industry_name = industry_name  # type: str
        # The name of the data collection task.
        self.name = name  # type: str
        # The status of the data collection task. Valid values:
        # 
        # *   0: disabled
        # *   1: being enabled
        # *   2: enabled
        # *   3: failed to be enabled
        self.status = status  # type: int
        # The ID of the sundial.
        self.sundial_id = sundial_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   server
        # 
        # *   web
        # 
        # *   app
        # 
        #     Note: Only server is supported.
        self.type = type  # type: str
        # The time when the data collection task was updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the data collection task.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataCollctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataCollctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        # The parameters that are used by a function in the expression.
        self.arg = arg  # type: str
        # The attribute, feature function, or field to be searched for.
        self.attribute = attribute  # type: str
        # The weight.
        # 
        # Valid values: \[-100000,100000] (excluding 0).
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
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The description of the expression.
        self.description = description  # type: str
        # The content of the expression.
        self.meta = meta  # type: list[DescribeFirstRankResponseBodyResultMeta]
        # The name of the expression.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the rough sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        # The custom analyzer.
        self.analyzer = analyzer  # type: str
        # The time when the intervention dictionary was created.
        self.created = created  # type: str
        # The name of the intervention dictionary.
        self.name = name  # type: str
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type  # type: str
        # The time when the intervention dictionary was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information the intervention dictionary.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        # Indicates whether the query analysis rule is the default one.
        self.active = active  # type: bool
        # The time when the query analysis rule was created.
        self.created = created  # type: int
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain  # type: str
        # The indexes to which the query analysis rule applies.
        self.indexes = indexes  # type: list[str]
        # The name of the query analysis rule.
        self.name = name  # type: str
        # The features that are used in the query analysis rule.
        self.processors = processors  # type: list[dict[str, any]]
        # The time when the query analysis rule was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the query analysis rule.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(self, console_url=None, endpoint=None, local_name=None, region_id=None):
        # The URL of the OpenSearch console.
        self.console_url = console_url  # type: str
        # The endpoint of the region.
        self.endpoint = endpoint  # type: str
        # The name of the region.
        self.local_name = local_name  # type: str
        # The ID of the region.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result that was returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the scheduled task.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecondRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The time when the expression was created.
        self.created = created  # type: int
        # The description of the expression.
        self.description = description  # type: str
        # The ID of the expression. This parameter appears only in the response.
        self.id = id  # type: str
        # Indicates whether the expression is the default one. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default  # type: str
        # Indicates whether the expression is a system expression. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_sys = is_sys  # type: str
        # The content of the fine sort expression.
        # 
        # You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta  # type: str
        # The name of the expression.
        self.name = name  # type: str
        # The time when the expression was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the fine sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryStatusResponseBodyResult(TeaModel):
    def __init__(self, app_group_id=None, region=None, status=None):
        # The ID of the application.
        self.app_group_id = app_group_id  # type: str
        # The network type of the slow query optimization service. Valid values:
        # 
        # *   outer: the Internet
        # *   internal: the internal network
        self.region = region  # type: str
        # The status of the slow query optimization service. Valid values:
        # 
        # *   enabled
        # *   disabled
        # *   n/a
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlowQueryStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowQueryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAnalyzerRequest(TeaModel):
    def __init__(self, with_=None):
        # all
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the custom analyzer.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSlowQueryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableSlowQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSlowQueryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableSlowQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateMergedTableRequest(TeaModel):
    def __init__(self, body=None, spec=None):
        self.body = body  # type: Schema
        # \-\
        self.spec = spec  # type: str

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateMergedTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Schema()
            self.body = temp_model.from_map(m['body'])
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateMergedTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateMergedTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(self, app_group_identity=None):
        # my_app_group_name
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return results.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCurrentVersionRequest(TeaModel):
    def __init__(self, category=None, domain=None, function_type=None, model_type=None):
        # The category. By default, this parameter is left empty.
        self.category = category  # type: str
        # The industry. By default, this parameter is left empty, which indicates General-purpose Edition.
        self.domain = domain  # type: str
        # The type of the feature. Valid values:
        # 
        # *   PAAS. This is the default value.
        # *   SAAS.
        self.function_type = function_type  # type: str
        # The type of the model. The following features correspond to different model types:
        # 
        # *   CTR model: tf_checkpoint
        # *   Popularity model: pop
        # *   Category model: offline_inference
        # *   Hotword model: offline_inference
        # *   Shading model: offline_inference
        # *   Drop-down suggestion model: offline_inference
        # *   Word segmentation model: text
        # *   Word weight model: tf_checkpoint
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
        # The name of the parameter.
        self.name = name  # type: str
        # Indicates whether the parameter is required.
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
        # The condition.
        self.condition = condition  # type: str
        # The dependency.
        self.dependency = dependency  # type: str
        # The description.
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
        # The name of the parameter.
        self.name = name  # type: str
        # Indicates whether the parameter is required.
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
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters  # type: list[GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters]
        # The dependencies of the instance.
        self.depends = depends  # type: list[GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends]
        # The parameters that are used to use the instance online.
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
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The type of the feature. Valid values:
        # 
        # *   PAAS
        # *   SAAS
        self.function_type = function_type  # type: str
        # The type of the model.
        self.model_type = model_type  # type: str
        # The configuration information about the instance.
        self.version_config = version_config  # type: GetFunctionCurrentVersionResponseBodyResultVersionConfig
        # The ID of the version.
        self.version_id = version_id  # type: long
        # The name of the version.
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the request.
        self.result = result  # type: GetFunctionCurrentVersionResponseBodyResult
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionCurrentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionCurrentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionDefaultInstanceResponseBodyResult(TeaModel):
    def __init__(self, instance_name=None):
        # The default instance name.
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
        # The error code.
        self.code = code  # type: str
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The default running time.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the request.
        self.result = result  # type: GetFunctionDefaultInstanceResponseBodyResult
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionDefaultInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionInstanceRequest(TeaModel):
    def __init__(self, output=None):
        # Specifies the richness of returned information. Valid values:
        # 
        # *   simple: displays only the basic information.
        # *   normal: displays information such as createParameters and cron. This is the default value.
        # *   detail: returns the details of the training task.
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
        # The category.
        self.category = category  # type: str
        # The industry.
        self.domain = domain  # type: str
        # The abbreviation of the language that applies.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The status of the task. Valid values:
        # 
        # *   success: succeeded
        # *   failed: failed
        # *   untrained: to be trained
        # *   pending: being scheduled
        # *   running: being trained
        self.dag_status = dag_status  # type: str
        # The time consumed for the most recent run, in milliseconds.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The information about the instance.
        self.belongs = belongs  # type: GetFunctionInstanceResponseBodyResultBelongs
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters  # type: list[GetFunctionInstanceResponseBodyResultCreateParameters]
        # The time when the task was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron  # type: str
        # The description of the instance.
        self.description = description  # type: str
        # The extended information, which is a JSON string.
        self.extend_info = extend_info  # type: str
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The type of the feature.
        self.function_type = function_type  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The type of the model.
        self.model_type = model_type  # type: str
        # How the instance is created. Valid values:
        # 
        # *   user: The instance is created by user.
        # *   builtin: The instance is created by the system.
        self.source = source  # type: str
        # The status of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status  # type: str
        # The information about the training task. This parameter is not displayed if no task is available.
        self.task = task  # type: GetFunctionInstanceResponseBodyResultTask
        # The parameters that are used.
        self.usage_parameters = usage_parameters  # type: list[GetFunctionInstanceResponseBodyResultUsageParameters]
        # The ID of the version.
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
        # The error code. If no error occurs, this parameter is left empty.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the instance.
        self.result = result  # type: GetFunctionInstanceResponseBodyResult
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionResourceRequest(TeaModel):
    def __init__(self, output=None):
        self.output = output  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionResourceRequest, self).to_map()
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


class GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFunctionResourceResponseBodyResultDataGeneratorsInput(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponseBodyResultDataGeneratorsInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = GetFunctionResourceResponseBodyResultDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class GetFunctionResourceResponseBodyResultDataGenerators(TeaModel):
    def __init__(self, generator=None, input=None, output=None):
        self.generator = generator  # type: str
        self.input = input  # type: GetFunctionResourceResponseBodyResultDataGeneratorsInput
        self.output = output  # type: str

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponseBodyResultDataGenerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = GetFunctionResourceResponseBodyResultDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class GetFunctionResourceResponseBodyResultData(TeaModel):
    def __init__(self, content=None, generators=None):
        self.content = content  # type: str
        self.generators = generators  # type: list[GetFunctionResourceResponseBodyResultDataGenerators]

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = GetFunctionResourceResponseBodyResultDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class GetFunctionResourceResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, data=None, description=None, function_name=None, modify_time=None,
                 referenced_instances=None, resource_name=None, resource_type=None):
        self.create_time = create_time  # type: long
        self.data = data  # type: GetFunctionResourceResponseBodyResultData
        self.description = description  # type: str
        self.function_name = function_name  # type: str
        self.modify_time = modify_time  # type: long
        self.referenced_instances = referenced_instances  # type: list[str]
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.referenced_instances is not None:
            result['ReferencedInstances'] = self.referenced_instances
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = GetFunctionResourceResponseBodyResultData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ReferencedInstances') is not None:
            self.referenced_instances = m.get('ReferencedInstances')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetFunctionResourceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionResourceResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponseBody, self).to_map()
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
            temp_model = GetFunctionResourceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionTaskResponseBodyResult(TeaModel):
    def __init__(self, end_time=None, extend_info=None, function_name=None, generation=None, progress=None,
                 run_id=None, start_time=None, status=None):
        # The timestamp that indicates the end time of the task. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The extended information, which is a JSON string.
        self.extend_info = extend_info  # type: str
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The number of iterations.
        self.generation = generation  # type: str
        # The progress. 90 indicates 90%.
        self.progress = progress  # type: long
        # The ID of the task.
        self.run_id = run_id  # type: str
        # The timestamp that indicates the start time of the task. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the request.
        self.result = result  # type: GetFunctionTaskResponseBodyResult
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionVersionResponseBodyResultVersionConfigCreateParameters(TeaModel):
    def __init__(self, name=None, required=None):
        # The name of the parameter.
        self.name = name  # type: str
        # Indicates whether the parameter is required.
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
        # The condition.
        self.condition = condition  # type: str
        # The dependency.
        self.dependency = dependency  # type: str
        # The description.
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
        # The name of the instance.
        self.name = name  # type: str
        # Indicates whether the parameter is required.
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
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters  # type: list[GetFunctionVersionResponseBodyResultVersionConfigCreateParameters]
        # The dependencies of the instance.
        self.depends = depends  # type: list[GetFunctionVersionResponseBodyResultVersionConfigDepends]
        # The parameters that are used during online use of the instance.
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
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The type of the feature. Valid values:
        # 
        # *   PAAS
        # *   SAAS
        self.function_type = function_type  # type: str
        # The type of the model.
        self.model_type = model_type  # type: str
        # The configuration information.
        self.version_config = version_config  # type: GetFunctionVersionResponseBodyResultVersionConfig
        # The ID of the version.
        self.version_id = version_id  # type: long
        # The name of the version.
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The maximum duration for which a task can be executed.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result body.
        self.result = result  # type: GetFunctionVersionResponseBodyResult
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScriptFileNamesResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, file_name=None, modify_time=None, path_name=None):
        # The time when the script file was created.
        self.create_time = create_time  # type: str
        # The name of the script file.
        self.file_name = file_name  # type: str
        # The time when the script file was last modified.
        self.modify_time = modify_time  # type: str
        self.path_name = path_name  # type: str

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
        if self.path_name is not None:
            result['pathName'] = self.path_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('pathName') is not None:
            self.path_name = m.get('pathName')
        return self


class GetScriptFileNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The files of the script.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScriptFileNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScriptFileNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, modify_time=None, scope=None, script_name=None, status=None, type=None):
        # The time when the script was created.
        self.create_time = create_time  # type: str
        # The time when the script was last modified.
        self.modify_time = modify_time  # type: str
        # The sort phase to which the script applies.
        self.scope = scope  # type: str
        self.script_name = script_name  # type: str
        # The status of the script. For more information, see the Script status table.
        self.status = status  # type: str
        # The type of the script.
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


class GetSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the script
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptFileResponseBodyResult(TeaModel):
    def __init__(self, content=None, create_time=None, modify_time=None, version=None):
        # The script content that is encoded in the Base64 format.
        self.content = content  # type: str
        # The time when the script was created.
        self.create_time = create_time  # type: str
        # The last time when the script was last modified.
        self.modify_time = modify_time  # type: str
        # The version of the script.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The content of the sort script.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestExperimentsResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        # The time when the test was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test. Valid values:
        # 
        # *   true: in effect
        # *   false: not in effect
        self.online = online  # type: bool
        # The parameters of the test.
        self.params = params  # type: dict[str, any]
        # The percentage of traffic that is routed to the test.
        # 
        # Valid values: \[0,100].
        self.traffic = traffic  # type: int
        # The time when the test was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the tests.
        # 
        # For more information, see [ABTestExperiment](~~173617~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListABTestExperimentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The queried whitelists.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListABTestFixedFlowDividersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestGroupsResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        # The time when the test group was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test group was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The test groups.
        # 
        # For more information, see [ABTestGroup](~~178935~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListABTestGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestScenesResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        # The time when the test scenario was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test scenario. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test scenario was last modified.
        self.updated = updated  # type: int
        # The name of the test scenario.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the test scenarios.
        # 
        # For more information, see [ABTestScene](~~173618~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListABTestScenesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListABTestScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupsRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupsRequestTags, self).to_map()
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


class ListAppGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, page_number=None, page_size=None, resource_group_id=None,
                 sort_by=None, tags=None, type=None):
        # ops-cn-xxxx
        self.instance_id = instance_id  # type: str
        # my_name
        self.name = name  # type: str
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # ""
        self.resource_group_id = resource_group_id  # type: str
        # 0
        self.sort_by = sort_by  # type: int
        self.tags = tags  # type: list[ListAppGroupsRequestTags]
        # standard
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListAppGroupsRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAppGroupsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, page_number=None, page_size=None, resource_group_id=None,
                 sort_by=None, tags_shrink=None, type=None):
        # ops-cn-xxxx
        self.instance_id = instance_id  # type: str
        # my_name
        self.name = name  # type: str
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # ""
        self.resource_group_id = resource_group_id  # type: str
        # 0
        self.sort_by = sort_by  # type: int
        self.tags_shrink = tags_shrink  # type: str
        # standard
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupsShrinkRequest, self).to_map()
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
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
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
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAppGroupsResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
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


class ListAppGroupsResponseBodyResultTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupsResponseBodyResultTags, self).to_map()
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


class ListAppGroupsResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, tags=None, type=None, updated=None):
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type  # type: str
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        # domain
        self.domain = domain  # type: str
        # The expiration time.
        self.expire_on = expire_on  # type: str
        # The ID of the created rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The ID of the application.
        self.id = id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        # Indicates whether the instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is not complete for the instance. For example, an order is one that is initiated to create the instance or change the quotas or billing method.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The information about the quotas of the application.
        # 
        # For more information, see [Quota](https://www.alibabacloud.com/help/doc-detail/170001.htm).
        self.quota = quota  # type: ListAppGroupsResponseBodyResultQuota
        # The ID of the created fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        self.tags = tags  # type: list[ListAppGroupsResponseBodyResultTags]
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type  # type: str
        # The timestamp when the application was last updated.
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListAppGroupsResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListAppGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each application.
        # 
        # For more information, see [AppGroup](~~170000~~).
        self.result = result  # type: list[ListAppGroupsResponseBodyResult]
        # The total number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataCollectionsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 1
        self.page_number = page_number  # type: int
        # 10
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
        # The time when the data collection task was created.
        self.created = created  # type: int
        # The type of the data that is collected by the task. Valid values:
        # 
        # *   behavior: behavioral data
        # *   item_info: project data
        # *   industry_specific: industry-specific data
        self.data_collection_type = data_collection_type  # type: str
        # The ID of the data collection task.
        self.id = id  # type: str
        # The industry to which the data collection task applies. Valid values:
        # 
        # *   general
        # *   ecommerce
        self.industry_name = industry_name  # type: str
        # The name of the data collection task.
        self.name = name  # type: str
        # The status of the data collection task. Valid values:
        # 
        # *   0: disabled
        # *   1: being enabled
        # *   2: enabled
        # *   3: failed to be enabled
        self.status = status  # type: int
        # The ID of the sundial.
        self.sundial_id = sundial_id  # type: str
        # The type of the data source. Valid values:
        # 
        # *   server
        # *   web
        # *   app
        # 
        # Note: Only server is supported.
        self.type = type  # type: str
        # The time when the data collection task was updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the data collection tasks.
        # 
        # For more information, see [DataCollection](~~173605~~).
        self.result = result  # type: list[ListDataCollectionsResponseBodyResult]
        # The total number of the returned data collection tasks.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataCollectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTableFieldsRequest(TeaModel):
    def __init__(self, params=None, raw_type=None):
        # The parameters of the data source. The value of the params parameter is a JSON string. The value must be URL-encoded.
        # 
        # Different types of data sources use different parameters. For more information, see the following sections of the "DataSource" topic:
        # 
        # *   [rds](~~170005~~)
        # *   [polardb](~~170005~~)
        # *   [odps](~~170005~~)
        # *   [mysql](~~173627~~)
        # *   [drds](~~173627~~)
        self.params = params  # type: str
        # Whether to return the original field type of the data source
        self.raw_type = raw_type  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTableFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.raw_type is not None:
            result['rawType'] = self.raw_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('rawType') is not None:
            self.raw_type = m.get('rawType')
        return self


class ListDataSourceTableFieldsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceTableFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTableFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTablesRequest(TeaModel):
    def __init__(self, params=None):
        # N/A
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The data tables.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFirstRanksResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        # The parameters that are used by a function in the expression.
        # 
        # For more information, see [Rough sort functions](~~180765~~).
        self.arg = arg  # type: str
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see [Rough sort functions](~~180765~~).
        self.attribute = attribute  # type: str
        # The weight.
        # 
        # Valid values: \[-100000,100000] (excluding 0).
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
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        self.created = created  # type: int
        # The description of the expression.
        self.description = description  # type: str
        # The content of the expression.
        self.meta = meta  # type: list[ListFirstRanksResponseBodyResultMeta]
        # The name of the expression.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each rough sort expression.
        # 
        # For more information, see [FirstRank](~~170007~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFirstRanksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFirstRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionInstancesRequest(TeaModel):
    def __init__(self, function_type=None, model_type=None, output=None, page_number=None, page_size=None,
                 source=None):
        # The type of the feature.
        self.function_type = function_type  # type: str
        # The type of the model.
        self.model_type = model_type  # type: str
        # The richness of the returned information. Valid values:
        # 
        # *   normal: displays information such as createParameters and cron. This is the default value.
        # *   simple: displays only the basic information.
        # *   detail: returns the details of the training task.
        self.output = output  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size  # type: int
        # How the instance is created. Valid values:
        # 
        # *   builtin: The instance is created by system.
        # *   user: The instance is created by user. This is the default value.
        # *   all: all instances
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
        # The category.
        self.category = category  # type: str
        # The industry.
        self.domain = domain  # type: str
        # The abbreviation of the language that applies.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The information about the instance.
        self.belongs = belongs  # type: ListFunctionInstancesResponseBodyResultBelongs
        # The parameters of the instance.
        self.create_parameters = create_parameters  # type: list[ListFunctionInstancesResponseBodyResultCreateParameters]
        # The time when the instance was created.
        self.create_time = create_time  # type: long
        # The cron expression used to schedule training, in the format of (Minutes Hours DayofMonth Month DayofWeek). If the value is empty, it indicates that no periodic training is performed.
        self.cron = cron  # type: str
        # The description.
        self.description = description  # type: str
        # The extended information, which is a JSON string. It includes model evaluation information and error information.
        self.extend_info = extend_info  # type: str
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The type of the feature.
        self.function_type = function_type  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The type of the model.
        self.model_type = model_type  # type: str
        # How the instance is created. Valid values:
        # 
        # *   user: The instance is created by user.
        # *   builtin: The instance is created by system.
        self.source = source  # type: str
        # The state of the instance. Valid values:
        # 
        # 1.  unavailable: No model is available. Models must be trained before you can use them.
        # 2.  available: Models can be used.
        self.status = status  # type: str
        # The parameters that are used.
        self.usage_parameters = usage_parameters  # type: list[ListFunctionInstancesResponseBodyResultUsageParameters]
        # The ID of the version.
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
        # The error code. If no error occurs, the parameter is left empty.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message. If no error occurs, the parameter is left empty.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the instances.
        self.result = result  # type: list[ListFunctionInstancesResponseBodyResult]
        # The status of the request.
        self.status = status  # type: str
        # The total number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionResourcesRequest(TeaModel):
    def __init__(self, output=None, page_number=None, page_size=None, resource_type=None):
        self.output = output  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFunctionResourcesResponseBodyResultDataGeneratorsInput(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBodyResultDataGeneratorsInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = ListFunctionResourcesResponseBodyResultDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class ListFunctionResourcesResponseBodyResultDataGenerators(TeaModel):
    def __init__(self, generator=None, input=None, output=None):
        self.generator = generator  # type: str
        self.input = input  # type: ListFunctionResourcesResponseBodyResultDataGeneratorsInput
        self.output = output  # type: str

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBodyResultDataGenerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = ListFunctionResourcesResponseBodyResultDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListFunctionResourcesResponseBodyResultData(TeaModel):
    def __init__(self, content=None, generators=None):
        self.content = content  # type: str
        self.generators = generators  # type: list[ListFunctionResourcesResponseBodyResultDataGenerators]

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = ListFunctionResourcesResponseBodyResultDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class ListFunctionResourcesResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, data=None, description=None, function_name=None, modify_time=None,
                 referenced_instances=None, resource_name=None, resource_type=None):
        self.create_time = create_time  # type: long
        self.data = data  # type: ListFunctionResourcesResponseBodyResultData
        self.description = description  # type: str
        self.function_name = function_name  # type: str
        self.modify_time = modify_time  # type: long
        self.referenced_instances = referenced_instances  # type: list[str]
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.referenced_instances is not None:
            result['ReferencedInstances'] = self.referenced_instances
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            temp_model = ListFunctionResourcesResponseBodyResultData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ReferencedInstances') is not None:
            self.referenced_instances = m.get('ReferencedInstances')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListFunctionResourcesResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None, total_count=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListFunctionResourcesResponseBodyResult]
        self.status = status  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponseBody, self).to_map()
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
                temp_model = ListFunctionResourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionTasksRequest(TeaModel):
    def __init__(self, end_time=None, page_number=None, page_size=None, start_time=None, status=None):
        # The end time is less than the specified time. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 1.
        self.page_size = page_size  # type: int
        # The start time is greater than the specified time. Specify the time in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
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
        # The timestamp that indicates the end time. Unit: milliseconds. 0 indicates that the task has not ended.
        self.end_time = end_time  # type: long
        # The value is a JSON string. It includes model evaluation information and training error information.
        self.extend_info = extend_info  # type: str
        # The name of the feature.
        self.function_name = function_name  # type: str
        # The number of iterations.
        self.generation = generation  # type: str
        # The progress. 90 indicates 90%.
        self.progress = progress  # type: long
        # The ID of the task.
        self.run_id = run_id  # type: str
        # The timestamp that indicates the start time. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the task. Valid values:
        # 
        # *   success
        # *   failed
        # *   running
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The returned result.
        self.result = result  # type: list[ListFunctionTasksResponseBodyResult]
        # The status of the request.
        self.status = status  # type: str
        # The total number of records that meet the requirements.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionariesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, types=None):
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # \-\
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
        # The custom analyzer.
        self.analyzer = analyzer  # type: str
        # The time when the intervention dictionary was created.
        self.created = created  # type: int
        # The ID of the intervention dictionary.
        self.id = id  # type: int
        # The name of the intervention dictionary.
        self.name = name  # type: str
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type  # type: str
        # The time when the intervention dictionary was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each intervention dictionary.
        # 
        # For more information, see [InterventionDictionary](~~173608~~).
        self.result = result  # type: list[ListInterventionDictionariesResponseBodyResult]
        # The total number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterventionDictionariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, word=None):
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # Test
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
        # The sequence number.
        self.order = order  # type: int
        # The internal name of the identified entity type. Valid values:
        # 
        # *   brand
        # *   category
        # *   material
        # *   element
        # *   style
        # *   color
        # *   function
        # *   scenario
        # *   people
        # *   season
        # *   model
        # *   region
        # *   name
        # *   adjective
        # *   category-modifier
        # *   size
        # *   quality
        # *   suit
        # *   new-release
        # *   series
        # *   marketing
        # *   entertainment
        # *   organization
        # *   movie
        # *   game
        # *   number
        # *   unit
        # *   common
        # *   new-word
        # *   proper-noun
        # *   symbol
        # *   prefix
        # *   suffix
        # *   gift
        # *   negative
        # *   agent
        self.tag = tag  # type: str
        # The description of the internal name of the identified entity type.
        self.tag_label = tag_label  # type: str
        # The entity.
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
        # The action. Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd  # type: str
        # The timestamp when the intervention entry was created.
        self.created = created  # type: long
        # The content of an intervention entry for category prediction.
        # 
        # The parameter returns key-value pairs. The key in a key-value pair indicates the ID of the category. The value in a key-value pair indicates the relevance value of the category. A value of 0 indicates irrelevant. A value of 1 indicates slightly relevant. A value of 2 indicates relevant.
        # 
        # Example: {"2":1, "100":0}
        self.relevance = relevance  # type: dict[str, any]
        # The status of the intervention entry. Valid value:
        # 
        # *   ACTIVE: The intervention entry takes effect.
        self.status = status  # type: str
        # The content of an intervention entry for term weight analysis.
        self.tokens = tokens  # type: list[ListInterventionDictionaryEntriesResponseBodyResultTokens]
        # The timestamp when the intervention entry was last updated.
        self.updated = updated  # type: long
        # The intervention query in the intervention entry.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each intervention entry.
        # 
        # For more information, see [InterventionDictionaryEntry](~~173606~~).
        self.result = result  # type: list[ListInterventionDictionaryEntriesResponseBodyResult]
        # The total number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterventionDictionaryEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryNerResultsRequest(TeaModel):
    def __init__(self, query=None):
        # Soymilk
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
        # The sequence number.
        self.order = order  # type: int
        # The internal name of the identified entity type. Valid values:
        # 
        # *   brand
        # *   category
        # *   material
        # *   element
        # *   style
        # *   color
        # *   function
        # *   scenario
        # *   people
        # *   season
        # *   model
        # *   region
        # *   name
        # *   adjective
        # *   category-modifier
        # *   size
        # *   quality
        # *   suit
        # *   new-release
        # *   series
        # *   marketing
        # *   entertainment
        # *   organization
        # *   movie
        # *   game
        # *   number
        # *   unit
        # *   common
        # *   new-word
        # *   proper-noun
        # *   symbol
        # *   prefix
        # *   suffix
        # *   gift
        # *   negative
        # *   agent
        self.tag = tag  # type: str
        # The description of the internal name of the identified entity type.
        self.tag_label = tag_label  # type: str
        # The entity.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The NER result.
        # 
        # For more information, see [InterventionDictionaryEntry](~~173606~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterventionDictionaryNerResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryNerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryRelatedEntitiesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each application and each query analysis rule. If no query analysis rule references the intervention dictionary, the value of the result parameter is an empty list.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterventionDictionaryRelatedEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInterventionDictionaryRelatedEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProceedingsRequest(TeaModel):
    def __init__(self, filter_finished=None):
        # Specifies whether the filtering is complete.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProceedingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProceedingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorAnalyzerResultsRequest(TeaModel):
    def __init__(self, text=None):
        # The text to be tested.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The data returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueryProcessorAnalyzerResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorAnalyzerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorNersRequest(TeaModel):
    def __init__(self, domain=None):
        # ECOMMERCE
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
        # The name of the entity type.
        self.label = label  # type: str
        # The priority of an entity type among entity types that have the same priority level.
        # 
        # A smaller value indicates a higher priority. Default value: 0.
        self.order = order  # type: int
        # The priority level of the entity type.
        # 
        # *   HIGH
        # *   MIDDLE
        # *   LOW
        self.priority = priority  # type: str
        # The internal name of the entity type.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The priority settings of entity types.
        # 
        # For more information, see [Priority settings of entity types](~~173616~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueryProcessorNersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorNersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorsRequest(TeaModel):
    def __init__(self, is_active=None):
        # 0
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
        # Indicates whether the query analysis rule is the default one.
        self.active = active  # type: bool
        # The time when the query analysis rule was created.
        self.created = created  # type: int
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain  # type: str
        # The indexes to which the query analysis rule applies.
        self.indexes = indexes  # type: list[str]
        # The name of the query analysis rule.
        self.name = name  # type: str
        # The features that are used in the query analysis rule.
        # 
        # For more information, see the ["Processor"](~~170014~~) section of the QueryProcessor topic.
        self.processors = processors  # type: list[dict[str, any]]
        # The time when the query analysis rule was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each query analysis rule.
        # 
        # For more information, see [QueryProcessor](~~170014~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueryProcessorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueryProcessorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaReviewTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # 1
        self.page_number = page_number  # type: int
        # 10
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
        # The ID of the application.
        self.app_group_id = app_group_id  # type: int
        # The name of the application.
        self.app_group_name = app_group_name  # type: str
        # The type of the application.
        self.app_group_type = app_group_type  # type: str
        # Indicates whether the ticket is approved.
        self.approved = approved  # type: bool
        # Indicates whether the model is available.
        self.available = available  # type: bool
        # The time when the ticket was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the ticket was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the ticket.
        self.id = id  # type: int
        # The remarks of the ticket.
        self.memo = memo  # type: str
        # The computing resource quota that is applied for.
        self.new_compute_resource = new_compute_resource  # type: int
        # The storage capacity quota that is applied for.
        self.new_soc_size = new_soc_size  # type: int
        # The application specifications that are applied for.
        self.new_spec = new_spec  # type: str
        # The original quota of computing resources.
        self.old_compute_resource = old_compute_resource  # type: int
        # The original quota of storage capacity.
        self.old_doc_size = old_doc_size  # type: int
        # The original application specifications.
        self.old_spec = old_spec  # type: str
        # Indicates whether the ticket is pending.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the ticket for application quota approval.
        # 
        # For more information, see [QuotaReviewTask](~~173609~~).
        self.result = result  # type: list[ListQuotaReviewTasksResponseBodyResult]
        # The total number of the returned tickets.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuotaReviewTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaReviewTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, type=None):
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # wipe
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the scheduled tasks.
        # 
        # For more information, see [ScheduledTask](~~173610~~).
        self.result = result  # type: list[dict[str, any]]
        # The total number of the returned scheduled tasks.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListScheduledTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchStrategiesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSearchStrategiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSearchStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecondRanksResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The time when the expression was created.
        self.created = created  # type: int
        # The description of the expression.
        self.description = description  # type: str
        # The ID of the expression. This parameter appears only in the response.
        self.id = id  # type: str
        # Indicates whether the expression is the default one. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default  # type: str
        # Indicates whether the expression is a system expression. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_sys = is_sys  # type: str
        # The content of the fine sort expression.
        # 
        # You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta  # type: str
        # The name of the expression.
        self.name = name  # type: str
        # The time when the expression was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about each fine sort expression.
        # 
        # For more information, see [SecondRank](~~170008~~).
        self.result = result  # type: list[ListSecondRanksResponseBodyResult]
        # The total number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecondRanksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSecondRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryCategoriesResponseBodyResult(TeaModel):
    def __init__(self, analyze_status=None, end=None, start=None):
        # The status of the analysis. Valid values:
        # 
        # *   PENDING: preparing
        # *   SUCCESS: succeeded
        # *   RUNNING: running
        # *   FAILED: failed
        # *   N/A: unknown
        self.analyze_status = analyze_status  # type: str
        # The timestamp that indicates the end of the time range to query.
        self.end = end  # type: int
        # The timestamp that indicates the beginning of the time range to query.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The data returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSlowQueryCategoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlowQueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryQueriesResponseBodyResult(TeaModel):
    def __init__(self, app_query=None, end=None, index=None, start=None):
        # The content of the optimization suggestion for the query.
        self.app_query = app_query  # type: str
        # The end of the time range that was queried.
        self.end = end  # type: int
        # The ID of the optimization suggestion.
        self.index = index  # type: int
        # The beginning of the time range that was queried.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSlowQueryQueriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlowQueryQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortExpressionsResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, name=None, updated=None):
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The time when the expression was created.
        self.created = created  # type: int
        # The description of the expression.
        self.description = description  # type: str
        # The name of the expression.
        self.name = name  # type: str
        # The time when the expression was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the rough sort or fine sort expressions that were returned.
        # 
        # For more information, see [FirstRank](~~170007~~) and [SecondRank](~~170008~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSortExpressionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSortExpressionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortScriptsResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, modify_time=None, scope=None, script_name=None, status=None, type=None):
        # The time when the script was created.
        self.create_time = create_time  # type: str
        # The time when the script was last modified.
        self.modify_time = modify_time  # type: str
        # The sort phase to which the script applies.
        self.scope = scope  # type: str
        # The name of the script.
        self.script_name = script_name  # type: str
        # The status of the script. Valid values:
        # 
        # *   configurable: The script is created, but no script files are uploaded.
        # *   not compiled: The script is not compiled.
        # *   compile failed: The compilation of the script failed.
        # *   compile successful: The script is compiled.
        # *   released: The script is published.
        self.status = status  # type: str
        # The type of the script.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The scripts of the application version.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSortScriptsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSortScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticLogsRequest(TeaModel):
    def __init__(self, columns=None, distinct=None, page_number=None, page_size=None, query=None, sort_by=None,
                 start_time=None, stop_time=None):
        # The fields to query. Example: columns=wordsTopPv.
        # 
        # For more information, see [Metrics in statistical reports](https://www.alibabacloud.com/help/en/opensearch/latest/statistical-report).
        self.columns = columns  # type: str
        # The content of the query clause.
        self.distinct = distinct  # type: bool
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size  # type: int
        # The content of the query clause.
        self.query = query  # type: str
        # The content of the sort clause.
        self.sort_by = sort_by  # type: str
        # The beginning of the time range to query. The default value is the timestamp of 00:00:00 on the current day.
        self.start_time = start_time  # type: int
        # The end of the time range to query. The default value is the timestamp of 24:00:00 on the current day.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The return result. For more information, see:
        # 
        # *   [Parameters of hotwords rankings](~~421248~~)
        self.result = result  # type: list[dict[str, any]]
        # The total number of the queried logs.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListStatisticLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatisticLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticReportRequest(TeaModel):
    def __init__(self, columns=None, end_time=None, page_number=None, page_size=None, query=None, start_time=None):
        # pv,uv
        self.columns = columns  # type: str
        # 1582646399
        self.end_time = end_time  # type: int
        # 1
        self.page_number = page_number  # type: int
        # 10
        self.page_size = page_size  # type: int
        # bizType:test,sceneTag:myTag
        self.query = query  # type: str
        # 1582214400
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The queried reports. Valid values:
        # 
        # For more information about the metrics in data quality reports, see the Upload behavioral data section of [Data collection 2.0](~~131547~~).
        # 
        # For more information about the metrics in application and A/B test reports, see the Core metrics section of [Metrics of statistical reports](~~187654~~).
        # 
        # For more information about the metrics in query analysis reports, see the Query analysis metrics section of [Metrics of statistical reports](~~187654~~).
        self.result = result  # type: list[dict[str, any]]
        # The total number of the queried reports.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListStatisticReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatisticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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
    def __init__(self, next_token=None, resource_id=None, resource_type=None, tag=None):
        # The token that is used to retrieve the next page.
        self.next_token = next_token  # type: str
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The tags. You can specify a maximum number of 20 tags.
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(self, next_token=None, resource_id_shrink=None, resource_type=None, tag_shrink=None):
        # The token that is used to retrieve the next page.
        self.next_token = next_token  # type: str
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id_shrink = resource_id_shrink  # type: str
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The tags. You can specify a maximum number of 20 tags.
        self.tag_shrink = tag_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListTagResourcesResponseBodyResult(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyResult, self).to_map()
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
    def __init__(self, next_token=None, request_id=None, result=None):
        # The token that is used to retrieve the next page.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The resources.
        self.result = result  # type: list[ListTagResourcesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListTagResourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
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


class ListUserAnalyzerEntriesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, word=None):
        # The page number. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Default value: 10.
        self.page_size = page_size  # type: int
        # The key to be used to query entries.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The entries of the custom analyzer. For more information, see UserAnalyzerEntry.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserAnalyzerEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: 10.
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
        # Indicates whether the application is available.
        self.available = available  # type: bool
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The number of intervention entries.
        self.entries_count = entries_count  # type: int
        # The maximum number of intervention entries that can be created in the dictionary.
        self.entries_limit = entries_limit  # type: int
        # The ID of the dictionary.
        self.id = id  # type: str
        # The type. Valid value:
        # 
        # *   segment
        self.type = type  # type: str
        # The timestamp when the application was last updated.
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
        # Indicates whether the application is available.
        self.available = available  # type: bool
        # The basic analyzer. Valid values:
        # 
        # *   chn_standard: [a common analyzer in Chinese](~~179424~~)
        # *   chn_scene_name: an analyzer for person names in Chinese
        # *   chn_ecommerce: [an analyzer for E-commerce in Chinese](~~179424~~)
        # *   chn_it_content: [an analyzer for IT content in Chinese](~~179424~~)
        # *   en_min: a small-granularity analyzer in English
        # *   th_standard: a common analyzer in Thai
        # *   th_ecommerce: an analyzer for E-commerce in Thai
        # *   vn_standard: a common analyzer in Vietnamese
        # *   chn_community_it: an analyzer for IT community content in Chinese
        # *   chn_ecommerce_general: a common analyzer for the E-commerce industry in Chinese
        # *   chn_esports_general: a common analyzer for the gaming industry in Chinese
        # *   chn_edu_question: an analyzer for question search of the education industry in Chinese
        self.business = business  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The dictionaries that are used by the custom analyzer.
        # 
        # For more information, see [UserDict](~~178933~~).
        self.dicts = dicts  # type: list[ListUserAnalyzersResponseBodyResultDicts]
        # The ID of the custom analyzer.
        self.id = id  # type: str
        # The name of the custom analyzer.
        self.name = name  # type: str
        # The timestamp when the application was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The custom analyzer.
        # 
        # For more information, see [UserAnalyzer](~~178934~~).
        self.result = result  # type: list[ListUserAnalyzersResponseBodyResult]
        # The total number.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserAnalyzersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserAnalyzersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupRequest(TeaModel):
    def __init__(self, current_version=None, description=None, domain=None, resource_group_id=None, dry_run=None):
        # The online version of the application.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The type of the industry. Valid values:
        # 
        # *   general: general.
        # *   ecommerce: e-commerce.
        # *   education: education.
        # *   esports: electronic sports.
        # *   community: content community.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # Specifies whether to verify the application before modification. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The computing resources. Unit: logical computing unit (LCU).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The specifications. Valid values:
        # 
        # *   opensearch.share.junior: basic.
        # *   opensearch.share.common: shared general-purpose.
        # *   opensearch.share.compute: shared computing.
        # *   opensearch.share.storage: shared storage.
        # *   opensearch.private.common: exclusive general-purpose.
        # *   opensearch.private.compute: exclusive computing.
        # *   opensearch.private.storage: exclusive storage.
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
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type  # type: str
        # The billable item. Valid values:
        # 
        # *   1: computing resources.
        # *   2: QPS.
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The type of the industry. Valid values:
        # 
        # *   GENERAL: general.
        # *   ECOMMERCE: e-commerce.
        # *   IT_CONTENT: IT content.
        self.domain = domain  # type: str
        # The time when the application expired.
        self.expire_on = expire_on  # type: str
        # The ID of the rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval status of the quotas. Valid values:
        # 
        # *   0: normal.
        # *   1: being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The application ID.
        self.id = id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The lock status. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        # Indicates whether the instance expires and is automatically locked. Valid values:
        # 
        # *   0: no.
        # *   1: yes.
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is not complete for the instance.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The information about the quotas of the application.
        self.quota = quota  # type: ModifyAppGroupResponseBodyResultQuota
        # The ID of the fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The state of the application. Valid values:
        # 
        # *   producing: being produced.
        # *   review_pending: being approved.
        # *   config_pending: to be configured.
        # *   normal: normal.
        # *   frozen: frozen.
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        # The type of the application. Valid values:
        # 
        # *   standard: a standard edition application.
        # *   advance: an advanced edition application of an old version. New versions are not supported for this edition.
        # *   enhanced: an advanced edition application of a new version.
        self.type = type  # type: str
        # The timestamp when the application was last modified.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned data.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupQuotaRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: Quota
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppGroupQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Quota()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyAppGroupQuotaResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The computing resources. Unit: logical computing units (LCUs).
        self.compute_resource = compute_resource  # type: int
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The specifications of the application. Valid values:
        # 
        # *   opensearch.share.junior: basic
        # *   opensearch.share.common: shared general-purpose
        # *   opensearch.share.compute: shared computing
        # *   opensearch.share.storage: shared storage
        # *   opensearch.private.common: exclusive general-purpose
        # *   opensearch.private.compute: exclusive computing
        # *   opensearch.private.storage: exclusive storage
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
        # The billing method of the application. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type  # type: str
        # The billing model. Valid values:
        # 
        # *   1: computing resources
        # *   2: queries per second (QPS)
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The expiration time.
        self.expire_on = expire_on  # type: str
        # The ID of the created rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval status of the quotas. Valid values:
        # 
        # *   0: The quotas are approved.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The ID of the application.
        self.id = id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The lock mode of the instance. Valid values:
        # 
        # *   Unlock: The instance is not locked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the application.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is not complete for the instance. For example, an order is one that is initiated to create the instance or change the quotas or billing method.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is complete. Valid values:
        # 
        # *   0: The order is in progress.
        # *   1: The order is complete.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The information about the quotas of the application.
        self.quota = quota  # type: ModifyAppGroupQuotaResponseBodyResultQuota
        # The ID of the created fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The status of the application. Valid values:
        # 
        # *   producing
        # *   review_pending
        # *   config_pending
        # *   normal
        # *   frozen
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        # The type of the application. Valid values:
        # 
        # *   standard: a standard application.
        # *   advance: an advanced application which is of an old application type. New applications cannot be of this type.
        # *   enhanced: an advanced application which is of a new application type.
        self.type = type  # type: str
        # The timestamp when the application was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the application.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppGroupQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppGroupQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirstRankRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: FirstRank
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFirstRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = FirstRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        # The parameters that are used by a function in the expression.
        self.arg = arg  # type: str
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see Rough sort functions.
        self.attribute = attribute  # type: str
        # The weight.
        # 
        # Valid values: \[-100000,100000] (excluding 0).
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
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The description of the expression.
        self.description = description  # type: str
        # The content of the expression.
        self.meta = meta  # type: list[ModifyFirstRankResponseBodyResultMeta]
        # The name of the expression.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the rough sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQueryProcessorRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: any
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyQueryProcessorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        # Indicates whether the query analysis rule is the default one.
        self.active = active  # type: bool
        # The time when the rule was created.
        self.created = created  # type: int
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain  # type: str
        # The indexes to which the query analysis rule applies.
        self.indexes = indexes  # type: list[str]
        # The name of the query analysis rule.
        self.name = name  # type: str
        # The analysis rule.
        self.processors = processors  # type: list[dict[str, any]]
        # The most recent update time.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the query analysis rule.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskRequest(TeaModel):
    def __init__(self, body=None):
        # 请求参数。
        self.body = body  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyScheduledTaskRequest, self).to_map()
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


class ModifyScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the scheduled task.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecondRankRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: SecondRank
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecondRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SecondRank()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifySecondRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        self.created = created  # type: int
        # The description of the expression.
        self.description = description  # type: str
        # The ID of the expression. This parameter appears only in the response.
        self.id = id  # type: str
        # Indicates whether the expression is the default one. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default  # type: str
        # Indicates whether the expression is a system expression. This parameter appears only in the response. Valid values:
        # 
        # *   true
        # *   false
        self.is_sys = is_sys  # type: str
        # The content of the fine sort expression.
        # 
        # You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta  # type: str
        # The name of the expression.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the fine sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: list[dict[str, any]]
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushInterventionDictionaryEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushInterventionDictionaryEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushUserAnalyzerEntriesRequestEntries(TeaModel):
    def __init__(self, cmd=None, key=None, split_enabled=None, value=None):
        # The operation to be performed on the entries.
        # 
        # Valid values:
        # 
        # *   add
        # *   delete
        self.cmd = cmd  # type: str
        # The key to be used to query entries.
        self.key = key  # type: str
        # Specifies whether to further analyze the terms that are generated after the search query is analyzed.
        # 
        # Default value: true.
        self.split_enabled = split_enabled  # type: bool
        # The analysis result.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushUserAnalyzerEntriesRequestEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.key is not None:
            result['key'] = self.key
        if self.split_enabled is not None:
            result['splitEnabled'] = self.split_enabled
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('splitEnabled') is not None:
            self.split_enabled = m.get('splitEnabled')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PushUserAnalyzerEntriesRequest(TeaModel):
    def __init__(self, entries=None, dry_run=None):
        # The entries of the custom analyzer.
        self.entries = entries  # type: list[PushUserAnalyzerEntriesRequestEntries]
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PushUserAnalyzerEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['entries'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entries = []
        if m.get('entries') is not None:
            for k in m.get('entries'):
                temp_model = PushUserAnalyzerEntriesRequestEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class PushUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The result returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushUserAnalyzerEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RankPreviewQueryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RankPreviewQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RankPreviewQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveDataCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        # The parameters that are used by a function in the expression.
        # 
        # For more information, see Rough sort functions.
        self.arg = arg  # type: str
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see Rough sort functions.
        self.attribute = attribute  # type: str
        # The weight.
        # 
        # Valid values: \[-100000,100000] (excluding 0).
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
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The description of the expression.
        self.description = description  # type: str
        # The content of the expression.
        self.meta = meta  # type: list[RemoveFirstRankResponseBodyResultMeta]
        # The name of the expression.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the rough sort expression.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        # The custom analyzer.
        self.analyzer = analyzer  # type: str
        # The time when the intervention dictionary was created.
        self.created = created  # type: str
        # The name of the intervention dictionary.
        self.name = name  # type: str
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering
        # *   synonym: an intervention dictionary for synonym configuration
        # *   correction: an intervention dictionary for spelling correction
        # *   category_prediction: an intervention dictionary for category prediction
        # *   ner: an intervention dictionary for named entity recognition (NER)
        # *   term_weighting: an intervention dictionary for term weight analysis
        self.type = type  # type: str
        # The time when the intervention dictionary was last updated.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the intervention dictionary.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveQueryProcessorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppGroupRequest(TeaModel):
    def __init__(self, body=None, client_token=None):
        # The renewal request body.
        self.body = body  # type: PrepayOrderInfo
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token  # type: str

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PrepayOrderInfo()
            self.body = temp_model.from_map(m['body'])
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the application was renewed.
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppGroupResponseBody, self).to_map()
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


class RenewAppGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        # The number of computing resources configured.
        self.compute_resource = compute_resource  # type: int
        # The storage capacity.
        self.doc_size = doc_size  # type: int
        # The specifications configured.
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
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type  # type: str
        # The billing type. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way  # type: int
        # The code of the commodity.
        self.commodity_code = commodity_code  # type: str
        # The timestamp when the application was created.
        self.created = created  # type: int
        # The ID of the current online version.
        self.current_version = current_version  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The expiration time.
        self.expire_on = expire_on  # type: str
        # The ID of the rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The approval status is normal.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        # The application ID.
        self.id = id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode  # type: str
        # Indicates whether the instance is automatically locked after it expires. Valid values:
        # 
        # *   0: The instance is not automatically locked after it expires.
        # *   1: The instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration  # type: int
        # The name of the order.
        self.name = name  # type: str
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        # The ID of the order that is in progress.
        self.processing_order_id = processing_order_id  # type: str
        # Indicates whether the order is produced.
        self.produced = produced  # type: int
        # The name of the A/B test group.
        self.project_id = project_id  # type: str
        # The configuration information.
        self.quota = quota  # type: ReplaceAppGroupCommodityCodeResponseBodyResultQuota
        # The ID of the fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        # The status of the application.
        self.status = status  # type: str
        # The timestamp when the current online version was published.
        self.switched_time = switched_time  # type: int
        # The type of the application.
        self.type = type  # type: str
        # The timestamp when the application was updated.
        self.updated = updated  # type: int
        # The versions.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned result.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReplaceAppGroupCommodityCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSortScriptFileRequest(TeaModel):
    def __init__(self, content=None, version=None):
        self.content = content  # type: str
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSortScriptFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class SaveSortScriptFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSlowQueryAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # N/A
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartSlowQueryAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartSlowQueryAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # The resource IDs. You can specify a maximum number of 50 resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The tags. You can specify a maximum number of 20 tags.
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
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
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindESUserAnalyzerRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindESUserAnalyzerRequest, self).to_map()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindESUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEsInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The data returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindEsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the specified one or more resources. This parameter takes effect only if the tagKey parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all  # type: bool
        # The resource IDs. You can specify a maximum number of 50 IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The keys of tags. You can specify a maximum number of 20 keys.
        self.tag_key = tag_key  # type: list[str]

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
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(self, all=None, resource_id_shrink=None, resource_type=None, tag_key_shrink=None):
        # Specifies whether to remove all tags from the specified one or more resources. This parameter takes effect only if the tagKey parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all  # type: bool
        # The resource IDs. You can specify a maximum number of 50 IDs.
        self.resource_id_shrink = resource_id_shrink  # type: str
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The keys of tags. You can specify a maximum number of 20 keys.
        self.tag_key_shrink = tag_key_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['tagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key_shrink = m.get('tagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, tequest_id=None):
        # The ID of the request.
        self.tequest_id = tequest_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tequest_id is not None:
            result['tequestId'] = self.tequest_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tequestId') is not None:
            self.tequest_id = m.get('tequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestExperimentRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: ABTestExperiment
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestExperiment()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        # The time when the test was created.
        self.created = created  # type: int
        # The ID of the test.
        self.id = id  # type: str
        # The name of the test.
        self.name = name  # type: str
        # The status of the test. Valid values:
        # 
        # *   true: in effect
        # *   false: not in effect
        self.online = online  # type: bool
        # The parameters of the test.
        self.params = params  # type: dict[str, any]
        # The percentage of traffic that is routed to the test.
        # 
        # Value values: 0 to 100.
        self.traffic = traffic  # type: int
        # The time when the test was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the test.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestFixedFlowDividersRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateABTestFixedFlowDividersRequest, self).to_map()
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


class UpdateABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The whitelists after the update.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateABTestFixedFlowDividersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestGroupRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: ABTestGroup
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestGroup()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        # The time when the test group was created.
        self.created = created  # type: int
        # The ID of the test group.
        self.id = id  # type: str
        # The name of the test group.
        self.name = name  # type: str
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status  # type: int
        # The time when the test group was last modified.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the test group.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestSceneRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body.
        self.body = body  # type: ABTestScene
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ABTestScene()
            self.body = temp_model.from_map(m['body'])
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        # The time when the test scenario was created.
        self.created = created  # type: int
        # The ID of the test scenario.
        self.id = id  # type: str
        # The name of the test scenario.
        self.name = name  # type: str
        # The status of the test. Valid values:
        # 
        # *   true: The test is started.
        # *   false: The test is stopped.
        self.online = online  # type: bool
        # The parameters of the A/B test.
        self.params = params  # type: dict[str, any]
        # The percentage of traffic that is allocated to the A/B test. Valid values: 0 to 100.
        self.traffic = traffic  # type: int
        # The time when the test scenario was last modified.
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
        # The request ID.
        self.request_id = request_id  # type: str
        # The details of the test scenario. For more information, see [ABTestScene](~~173618~~).
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFetchFieldsRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: list[str]
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFetchFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateFetchFieldsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFetchFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFetchFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionDefaultInstanceRequest(TeaModel):
    def __init__(self, instance_name=None):
        # The name of the instance.
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFunctionDefaultInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The name of the parameter.
        self.name = name  # type: str
        # The value of the parameter.
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
        # The parameters that are used to create the instance.
        self.create_parameters = create_parameters  # type: list[UpdateFunctionInstanceRequestCreateParameters]
        # The cron expression used to schedule periodic training, in the format of (Minutes Hours DayofMonth Month DayofWeek). The default value is empty, which indicates that no periodic training is performed. DayofWeek 0 indicates Sunday.
        self.cron = cron  # type: str
        # The description of the instance.
        self.description = description  # type: str
        # The parameters that are used.
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
        # The error code.
        self.code = code  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: long
        # The time consumed for the request, in milliseconds.
        self.latency = latency  # type: long
        # The error message.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The status of the request. Valid values:
        # 
        # *       OK: The request was successful.
        # *       FAIL: The request failed.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionResourceRequestDataGeneratorsInputFeatures(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionResourceRequestDataGeneratorsInputFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFunctionResourceRequestDataGeneratorsInput(TeaModel):
    def __init__(self, features=None):
        self.features = features  # type: list[UpdateFunctionResourceRequestDataGeneratorsInputFeatures]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateFunctionResourceRequestDataGeneratorsInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = UpdateFunctionResourceRequestDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k))
        return self


class UpdateFunctionResourceRequestDataGenerators(TeaModel):
    def __init__(self, generator=None, input=None, output=None):
        self.generator = generator  # type: str
        self.input = input  # type: UpdateFunctionResourceRequestDataGeneratorsInput
        self.output = output  # type: str

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(UpdateFunctionResourceRequestDataGenerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generator is not None:
            result['Generator'] = self.generator
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')
        if m.get('Input') is not None:
            temp_model = UpdateFunctionResourceRequestDataGeneratorsInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class UpdateFunctionResourceRequestData(TeaModel):
    def __init__(self, content=None, generators=None):
        self.content = content  # type: str
        self.generators = generators  # type: list[UpdateFunctionResourceRequestDataGenerators]

    def validate(self):
        if self.generators:
            for k in self.generators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateFunctionResourceRequestData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        result['Generators'] = []
        if self.generators is not None:
            for k in self.generators:
                result['Generators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        self.generators = []
        if m.get('Generators') is not None:
            for k in m.get('Generators'):
                temp_model = UpdateFunctionResourceRequestDataGenerators()
                self.generators.append(temp_model.from_map(k))
        return self


class UpdateFunctionResourceRequest(TeaModel):
    def __init__(self, data=None, description=None):
        self.data = data  # type: UpdateFunctionResourceRequestData
        self.description = description  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateFunctionResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateFunctionResourceRequestData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateFunctionResourceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: float
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionResourceResponseBody, self).to_map()
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


class UpdateFunctionResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFunctionResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSearchStrategyRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: SearchStrategy

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSearchStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SearchStrategy()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSummariesRequestBody(TeaModel):
    def __init__(self, element=None, ellipsis=None, field=None, len=None, snippet=None):
        self.element = element  # type: str
        self.ellipsis = ellipsis  # type: str
        self.field = field  # type: str
        self.len = len  # type: int
        self.snippet = snippet  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSummariesRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.ellipsis is not None:
            result['ellipsis'] = self.ellipsis
        if self.field is not None:
            result['field'] = self.field
        if self.len is not None:
            result['len'] = self.len
        if self.snippet is not None:
            result['snippet'] = self.snippet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('ellipsis') is not None:
            self.ellipsis = m.get('ellipsis')
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('len') is not None:
            self.len = m.get('len')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        return self


class UpdateSummariesRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        self.body = body  # type: list[UpdateSummariesRequestBody]
        # true
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSummariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateSummariesRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateSummariesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation was successful.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSummariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSummariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateDataSourcesRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: DataSource

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DataSource()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidateDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


