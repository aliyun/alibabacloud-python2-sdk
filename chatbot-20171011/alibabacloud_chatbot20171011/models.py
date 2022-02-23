# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Children(TeaModel):
    def __init__(self, area_code=None, category_id=None, childrens=None, name=None, parent_category_id=None):
        # 地区代号
        self.area_code = area_code  # type: str
        # 分类Id
        self.category_id = category_id  # type: long
        # 子元素
        self.childrens = childrens  # type: list[Children]
        # 名称
        self.name = name  # type: str
        # 父分类Id
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        if self.childrens:
            for k in self.childrens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Children, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['Childrens'] = []
        if self.childrens is not None:
            for k in self.childrens:
                result['Childrens'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.childrens = []
        if m.get('Childrens') is not None:
            for k in m.get('Childrens'):
                temp_model = Children()
                self.childrens.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class IntentCreateDTO(TeaModel):
    def __init__(self, intent_id=None, name=None, rule_check=None, slot=None, user_say=None):
        # IntentId
        self.intent_id = intent_id  # type: long
        # Name
        self.name = name  # type: str
        # RuleCheck
        self.rule_check = rule_check  # type: list[RuleMtopDTO]
        self.slot = slot  # type: list[SlotrecordMtopDTO]
        # UserSay
        self.user_say = user_say  # type: list[UsersayMtopDTO]

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IntentCreateDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.name is not None:
            result['Name'] = self.name
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = RuleMtopDTO()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = SlotrecordMtopDTO()
                self.slot.append(temp_model.from_map(k))
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = UsersayMtopDTO()
                self.user_say.append(temp_model.from_map(k))
        return self


class PaasButtonDTO(TeaModel):
    def __init__(self, name=None, text=None, type=None):
        # Name
        self.name = name  # type: str
        # Text
        self.text = text  # type: str
        # Type
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasButtonDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasButtonListDTO(TeaModel):
    def __init__(self, button=None, intro=None):
        # Button
        self.button = button  # type: list[PaasButtonDTO]
        # Intro
        self.intro = intro  # type: str

    def validate(self):
        if self.button:
            for k in self.button:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasButtonListDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Button'] = []
        if self.button is not None:
            for k in self.button:
                result['Button'].append(k.to_map() if k else None)
        if self.intro is not None:
            result['Intro'] = self.intro
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.button = []
        if m.get('Button') is not None:
            for k in m.get('Button'):
                temp_model = PaasButtonDTO()
                self.button.append(temp_model.from_map(k))
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        return self


class PaasConditionEntryDTO(TeaModel):
    def __init__(self, id=None, name=None, term=None, type=None, value=None):
        # Id
        self.id = id  # type: str
        # Name
        self.name = name  # type: str
        # Term
        self.term = term  # type: str
        # Type
        self.type = type  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasConditionEntryDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.term is not None:
            result['Term'] = self.term
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Term') is not None:
            self.term = m.get('Term')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PaasConditionSetDTO(TeaModel):
    def __init__(self, condition_entries=None):
        # ConditionEntries
        self.condition_entries = condition_entries  # type: list[PaasConditionEntryDTO]

    def validate(self):
        if self.condition_entries:
            for k in self.condition_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasConditionSetDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionEntries'] = []
        if self.condition_entries is not None:
            for k in self.condition_entries:
                result['ConditionEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.condition_entries = []
        if m.get('ConditionEntries') is not None:
            for k in m.get('ConditionEntries'):
                temp_model = PaasConditionEntryDTO()
                self.condition_entries.append(temp_model.from_map(k))
        return self


class PaasEdgeDTO(TeaModel):
    def __init__(self, id=None, label=None, source=None, target=None):
        # Id
        self.id = id  # type: str
        # Label
        self.label = label  # type: str
        # Source
        self.source = source  # type: str
        # Target
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasEdgeDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class PaasEntryDTO(TeaModel):
    def __init__(self, plugin_field_data_entry=None):
        # PluginFieldDataEntry
        self.plugin_field_data_entry = plugin_field_data_entry  # type: PaasEntryPluginFieldDataDTO

    def validate(self):
        if self.plugin_field_data_entry:
            self.plugin_field_data_entry.validate()

    def to_map(self):
        _map = super(PaasEntryDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_entry is not None:
            result['PluginFieldDataEntry'] = self.plugin_field_data_entry.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginFieldDataEntry') is not None:
            temp_model = PaasEntryPluginFieldDataDTO()
            self.plugin_field_data_entry = temp_model.from_map(m['PluginFieldDataEntry'])
        return self


class PaasEntryPluginFieldDataDTO(TeaModel):
    def __init__(self, content_entry=None, life_span=None, name=None):
        # ContentEntry
        self.content_entry = content_entry  # type: list[PaasConditionSetDTO]
        # LifeSpan
        self.life_span = life_span  # type: long
        # Name
        self.name = name  # type: str

    def validate(self):
        if self.content_entry:
            for k in self.content_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasEntryPluginFieldDataDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentEntry'] = []
        if self.content_entry is not None:
            for k in self.content_entry:
                result['ContentEntry'].append(k.to_map() if k else None)
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.content_entry = []
        if m.get('ContentEntry') is not None:
            for k in m.get('ContentEntry'):
                temp_model = PaasConditionSetDTO()
                self.content_entry.append(temp_model.from_map(k))
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasFunctionDTO(TeaModel):
    def __init__(self, plugin_field_data_function=None):
        # PluginFieldDataFunction
        self.plugin_field_data_function = plugin_field_data_function  # type: PaasFunctionPluginFieldDataDTO

    def validate(self):
        if self.plugin_field_data_function:
            self.plugin_field_data_function.validate()

    def to_map(self):
        _map = super(PaasFunctionDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_function is not None:
            result['PluginFieldDataFunction'] = self.plugin_field_data_function.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginFieldDataFunction') is not None:
            temp_model = PaasFunctionPluginFieldDataDTO()
            self.plugin_field_data_function = temp_model.from_map(m['PluginFieldDataFunction'])
        return self


class PaasFunctionPluginFieldDataDTO(TeaModel):
    def __init__(self, aliyun_function=None, aliyun_service=None, code=None, description=None, end_point=None,
                 function=None, name=None, params=None, switch=None, type=None):
        # AliyunFunction
        self.aliyun_function = aliyun_function  # type: str
        # AliyunService
        self.aliyun_service = aliyun_service  # type: str
        # Code
        self.code = code  # type: str
        # Description
        self.description = description  # type: str
        # EndPoint
        self.end_point = end_point  # type: str
        # Function
        self.function = function  # type: str
        # Name
        self.name = name  # type: str
        # Params
        self.params = params  # type: dict[str, any]
        # Switch
        self.switch = switch  # type: list[PaasSwitchCaseDTO]
        # Type
        self.type = type  # type: str

    def validate(self):
        if self.switch:
            for k in self.switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasFunctionPluginFieldDataDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_function is not None:
            result['AliyunFunction'] = self.aliyun_function
        if self.aliyun_service is not None:
            result['AliyunService'] = self.aliyun_service
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.function is not None:
            result['Function'] = self.function
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        result['Switch'] = []
        if self.switch is not None:
            for k in self.switch:
                result['Switch'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunFunction') is not None:
            self.aliyun_function = m.get('AliyunFunction')
        if m.get('AliyunService') is not None:
            self.aliyun_service = m.get('AliyunService')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        self.switch = []
        if m.get('Switch') is not None:
            for k in m.get('Switch'):
                temp_model = PaasSwitchCaseDTO()
                self.switch.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasFunctionPluginParams(TeaModel):
    def __init__(self, body=None, header=None, method=None, query=None, url=None):
        # Body
        self.body = body  # type: str
        # Header
        self.header = header  # type: dict[str, str]
        # Method
        self.method = method  # type: str
        # Query
        self.query = query  # type: dict[str, str]
        # Url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasFunctionPluginParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.header is not None:
            result['Header'] = self.header
        if self.method is not None:
            result['Method'] = self.method
        if self.query is not None:
            result['Query'] = self.query
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PaasNodeDTO(TeaModel):
    def __init__(self, code=None, id=None, label=None, plugin_data=None, xx=None, yy=None):
        # Code
        self.code = code  # type: str
        # Id
        self.id = id  # type: str
        # Label
        self.label = label  # type: str
        # PluginData
        self.plugin_data = plugin_data  # type: PaasPluginDataDTO
        # Xx
        self.xx = xx  # type: float
        # Yy
        self.yy = yy  # type: float

    def validate(self):
        if self.plugin_data:
            self.plugin_data.validate()

    def to_map(self):
        _map = super(PaasNodeDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data.to_map()
        if self.xx is not None:
            result['Xx'] = self.xx
        if self.yy is not None:
            result['Yy'] = self.yy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('PluginData') is not None:
            temp_model = PaasPluginDataDTO()
            self.plugin_data = temp_model.from_map(m['PluginData'])
        if m.get('Xx') is not None:
            self.xx = m.get('Xx')
        if m.get('Yy') is not None:
            self.yy = m.get('Yy')
        return self


class PaasPluginDataDTO(TeaModel):
    def __init__(self, entry=None, function=None, response=None, slot=None):
        self.entry = entry  # type: PaasEntryDTO
        self.function = function  # type: PaasFunctionDTO
        self.response = response  # type: PaasResponseDTO
        self.slot = slot  # type: PaasSlotDTO

    def validate(self):
        if self.entry:
            self.entry.validate()
        if self.function:
            self.function.validate()
        if self.response:
            self.response.validate()
        if self.slot:
            self.slot.validate()

    def to_map(self):
        _map = super(PaasPluginDataDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.slot is not None:
            result['Slot'] = self.slot.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = PaasEntryDTO()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('Function') is not None:
            temp_model = PaasFunctionDTO()
            self.function = temp_model.from_map(m['Function'])
        if m.get('Response') is not None:
            temp_model = PaasResponseDTO()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Slot') is not None:
            temp_model = PaasSlotDTO()
            self.slot = temp_model.from_map(m['Slot'])
        return self


class PaasProcessData(TeaModel):
    def __init__(self, edges=None, nodes=None):
        # Edges
        self.edges = edges  # type: list[PaasEdgeDTO]
        # Nodes
        self.nodes = nodes  # type: list[PaasNodeDTO]

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasProcessData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        return self


class PaasResponseDTO(TeaModel):
    def __init__(self, plugin_field_data_response=None):
        self.plugin_field_data_response = plugin_field_data_response  # type: PaasResponsePluginFieldDataDTO

    def validate(self):
        if self.plugin_field_data_response:
            self.plugin_field_data_response.validate()

    def to_map(self):
        _map = super(PaasResponseDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_response is not None:
            result['PluginFieldDataResponse'] = self.plugin_field_data_response.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginFieldDataResponse') is not None:
            temp_model = PaasResponsePluginFieldDataDTO()
            self.plugin_field_data_response = temp_model.from_map(m['PluginFieldDataResponse'])
        return self


class PaasResponseNodeContentDTO(TeaModel):
    def __init__(self, button_list=None, image=None, text=None, type=None):
        # ButtonList
        self.button_list = button_list  # type: PaasButtonListDTO
        # Image
        self.image = image  # type: str
        # Text
        self.text = text  # type: str
        # Type
        self.type = type  # type: str

    def validate(self):
        if self.button_list:
            self.button_list.validate()

    def to_map(self):
        _map = super(PaasResponseNodeContentDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_list is not None:
            result['ButtonList'] = self.button_list.to_map()
        if self.image is not None:
            result['Image'] = self.image
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ButtonList') is not None:
            temp_model = PaasButtonListDTO()
            self.button_list = temp_model.from_map(m['ButtonList'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasResponsePluginFieldDataDTO(TeaModel):
    def __init__(self, content_response=None, name=None):
        # ContentResponse
        self.content_response = content_response  # type: PaasResponseNodeContentDTO
        # Name
        self.name = name  # type: str

    def validate(self):
        if self.content_response:
            self.content_response.validate()

    def to_map(self):
        _map = super(PaasResponsePluginFieldDataDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_response is not None:
            result['ContentResponse'] = self.content_response.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentResponse') is not None:
            temp_model = PaasResponseNodeContentDTO()
            self.content_response = temp_model.from_map(m['ContentResponse'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasSlotConfigDTO(TeaModel):
    def __init__(self, is_array=None, is_necessary=None, life_span=None, name=None, question=None, value=None):
        # IsArray
        self.is_array = is_array  # type: bool
        # IsNecessary
        self.is_necessary = is_necessary  # type: bool
        # LifeSpan
        self.life_span = life_span  # type: int
        # Name
        self.name = name  # type: str
        # Question
        self.question = question  # type: list[str]
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasSlotConfigDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PaasSlotDTO(TeaModel):
    def __init__(self, plugin_field_data_slot=None):
        self.plugin_field_data_slot = plugin_field_data_slot  # type: PaasSlotPluginFieldDataDTO

    def validate(self):
        if self.plugin_field_data_slot:
            self.plugin_field_data_slot.validate()

    def to_map(self):
        _map = super(PaasSlotDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_slot is not None:
            result['PluginFieldDataSlot'] = self.plugin_field_data_slot.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PluginFieldDataSlot') is not None:
            temp_model = PaasSlotPluginFieldDataDTO()
            self.plugin_field_data_slot = temp_model.from_map(m['PluginFieldDataSlot'])
        return self


class PaasSlotPluginFieldDataDTO(TeaModel):
    def __init__(self, content_slot=None, intent_id=None, intent_name=None, is_sys_intent=None, name=None):
        # ContentSlot
        self.content_slot = content_slot  # type: list[PaasSlotConfigDTO]
        # IntentId
        self.intent_id = intent_id  # type: str
        # IntentName
        self.intent_name = intent_name  # type: str
        # IsSysIntent
        self.is_sys_intent = is_sys_intent  # type: bool
        # Name
        self.name = name  # type: str

    def validate(self):
        if self.content_slot:
            for k in self.content_slot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PaasSlotPluginFieldDataDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentSlot'] = []
        if self.content_slot is not None:
            for k in self.content_slot:
                result['ContentSlot'].append(k.to_map() if k else None)
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.is_sys_intent is not None:
            result['IsSysIntent'] = self.is_sys_intent
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.content_slot = []
        if m.get('ContentSlot') is not None:
            for k in m.get('ContentSlot'):
                temp_model = PaasSlotConfigDTO()
                self.content_slot.append(temp_model.from_map(k))
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsSysIntent') is not None:
            self.is_sys_intent = m.get('IsSysIntent')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasSwitchCaseDTO(TeaModel):
    def __init__(self, id=None, label=None, type=None, value=None, variable_name=None):
        # Id
        self.id = id  # type: str
        # Label
        self.label = label  # type: str
        # Type
        self.type = type  # type: str
        # Value
        self.value = value  # type: str
        # VariableName
        self.variable_name = variable_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PaasSwitchCaseDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        return self


class RuleMtopDTO(TeaModel):
    def __init__(self, error=None, strict=None, text=None, warning=None):
        # Error
        self.error = error  # type: list[str]
        # Strict
        self.strict = strict  # type: bool
        # Text
        self.text = text  # type: str
        # Warning
        self.warning = warning  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RuleMtopDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.text is not None:
            result['Text'] = self.text
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class SectionMtopDTO(TeaModel):
    def __init__(self, slot_id=None, text=None):
        # SlotId
        self.slot_id = slot_id  # type: str
        # Text
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SectionMtopDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SlotrecordMtopDTO(TeaModel):
    def __init__(self, id=None, is_array=None, is_necessary=None, life_span=None, name=None, question=None, tags=None,
                 value=None):
        # Id
        self.id = id  # type: str
        # IsArray
        self.is_array = is_array  # type: bool
        # IsNecessary
        self.is_necessary = is_necessary  # type: bool
        # LifeSpan
        self.life_span = life_span  # type: int
        # Name
        self.name = name  # type: str
        # Question
        self.question = question  # type: list[str]
        # Tags
        self.tags = tags  # type: list[TagMtopDTO]
        # Value
        self.value = value  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SlotrecordMtopDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagMtopDTO()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagMtopDTO(TeaModel):
    def __init__(self, user_say_id=None, value=None):
        # UserSayId
        self.user_say_id = user_say_id  # type: str
        # Value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagMtopDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateDialogFlowModuleDefinition(TeaModel):
    def __init__(self, edges=None, nodes=None):
        # Edges
        self.edges = edges  # type: list[PaasEdgeDTO]
        # Nodes
        self.nodes = nodes  # type: list[PaasNodeDTO]

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateDialogFlowModuleDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        return self


class UsersayMtopDTO(TeaModel):
    def __init__(self, data=None, id=None, strict=None):
        # Data
        self.data = data  # type: list[SectionMtopDTO]
        # Id
        self.id = id  # type: str
        # Strict
        self.strict = strict  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UsersayMtopDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SectionMtopDTO()
                self.data.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class ActivatePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, perspective_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivatePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class ActivatePerspectiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivatePerspectiveResponseBody, self).to_map()
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


class ActivatePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ActivatePerspectiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActivatePerspectiveResponse, self).to_map()
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
            temp_model = ActivatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSynonymRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None, synonym=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str
        self.synonym = synonym  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSynonymRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class AddSynonymResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSynonymResponseBody, self).to_map()
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


class AddSynonymResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddSynonymResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSynonymResponse, self).to_map()
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
            temp_model = AddSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppendEntityMemberRequestMember(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppendEntityMemberRequestMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class AppendEntityMemberRequest(TeaModel):
    def __init__(self, agent_key=None, apply_type=None, entity_id=None, member=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.apply_type = apply_type  # type: str
        self.entity_id = entity_id  # type: long
        self.member = member  # type: AppendEntityMemberRequestMember

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super(AppendEntityMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member is not None:
            result['Member'] = self.member.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            temp_model = AppendEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        return self


class AppendEntityMemberShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, apply_type=None, entity_id=None, member_shrink=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.apply_type = apply_type  # type: str
        self.entity_id = entity_id  # type: long
        self.member_shrink = member_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppendEntityMemberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            self.member_shrink = m.get('Member')
        return self


class AppendEntityMemberResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppendEntityMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppendEntityMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppendEntityMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppendEntityMemberResponse, self).to_map()
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
            temp_model = AppendEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(self, instance_id=None, perspective=None, recommend_num=None, session_id=None, utterance=None):
        self.instance_id = instance_id  # type: str
        self.perspective = perspective  # type: list[str]
        self.recommend_num = recommend_num  # type: int
        self.session_id = session_id  # type: str
        self.utterance = utterance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateResponseBodyAssociate(TeaModel):
    def __init__(self, title=None):
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResponseBodyAssociate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AssociateResponseBody(TeaModel):
    def __init__(self, associate=None, message_id=None, request_id=None, session_id=None):
        self.associate = associate  # type: list[AssociateResponseBodyAssociate]
        self.message_id = message_id  # type: str
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AssociateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateResponse, self).to_map()
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
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(self, instance_id=None, intent_name=None, knowledge_id=None, perspective=None, recommend=None,
                 sender_id=None, sender_nick=None, session_id=None, tag=None, utterance=None, vendor_param=None):
        self.instance_id = instance_id  # type: str
        self.intent_name = intent_name  # type: str
        self.knowledge_id = knowledge_id  # type: str
        self.perspective = perspective  # type: list[str]
        self.recommend = recommend  # type: bool
        self.sender_id = sender_id  # type: str
        self.sender_nick = sender_nick  # type: str
        self.session_id = session_id  # type: str
        self.tag = tag  # type: str
        self.utterance = utterance  # type: str
        self.vendor_param = vendor_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatResponseBodyMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(self, knowledge_id=None, title=None):
        self.knowledge_id = knowledge_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesKnowledgeRelatedKnowledges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesKnowledge(TeaModel):
    def __init__(self, answer_source=None, category=None, content=None, content_type=None, hit_statement=None,
                 id=None, related_knowledges=None, score=None, summary=None, title=None):
        self.answer_source = answer_source  # type: str
        self.category = category  # type: str
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        self.hit_statement = hit_statement  # type: str
        self.id = id  # type: str
        self.related_knowledges = related_knowledges  # type: list[ChatResponseBodyMessagesKnowledgeRelatedKnowledges]
        self.score = score  # type: float
        self.summary = summary  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessagesKnowledge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.id is not None:
            result['Id'] = self.id
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(self, answer_source=None, category=None, content=None, knowledge_id=None, score=None, summary=None,
                 title=None):
        self.answer_source = answer_source  # type: str
        self.category = category  # type: str
        self.content = content  # type: str
        self.knowledge_id = knowledge_id  # type: str
        self.score = score  # type: float
        self.summary = summary  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesRecommends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.score is not None:
            result['Score'] = self.score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(self, is_hit=None, name=None, origin=None, value=None):
        self.is_hit = is_hit  # type: bool
        self.name = name  # type: str
        self.origin = origin  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChatResponseBodyMessagesTextSlots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_hit is not None:
            result['IsHit'] = self.is_hit
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsHit') is not None:
            self.is_hit = m.get('IsHit')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(self, answer_source=None, article_title=None, content=None, content_type=None, dialog_name=None,
                 ext=None, external_flags=None, hit_statement=None, intent_name=None, meta_data=None, node_id=None,
                 node_name=None, score=None, slots=None, user_defined_chat_title=None):
        self.answer_source = answer_source  # type: str
        self.article_title = article_title  # type: str
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        self.dialog_name = dialog_name  # type: str
        self.ext = ext  # type: dict[str, any]
        self.external_flags = external_flags  # type: dict[str, any]
        self.hit_statement = hit_statement  # type: str
        self.intent_name = intent_name  # type: str
        self.meta_data = meta_data  # type: str
        self.node_id = node_id  # type: str
        self.node_name = node_name  # type: str
        self.score = score  # type: float
        self.slots = slots  # type: list[ChatResponseBodyMessagesTextSlots]
        self.user_defined_chat_title = user_defined_chat_title  # type: str

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessagesText, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.score is not None:
            result['Score'] = self.score
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(self, answer_source=None, answer_type=None, knowledge=None, recommends=None, text=None, type=None):
        self.answer_source = answer_source  # type: str
        self.answer_type = answer_type  # type: str
        self.knowledge = knowledge  # type: ChatResponseBodyMessagesKnowledge
        self.recommends = recommends  # type: list[ChatResponseBodyMessagesRecommends]
        self.text = text  # type: ChatResponseBodyMessagesText
        self.type = type  # type: str

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super(ChatResponseBodyMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ChatResponseBody(TeaModel):
    def __init__(self, message_id=None, messages=None, request_id=None, session_id=None, tag=None):
        self.message_id = message_id  # type: str
        self.messages = messages  # type: list[ChatResponseBodyMessages]
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str
        self.tag = tag  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ChatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChatResponse, self).to_map()
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
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBotRequest(TeaModel):
    def __init__(self, agent_key=None, avatar=None, introduction=None, language_code=None, name=None,
                 robot_type=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.avatar = avatar  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.name = name  # type: str
        self.robot_type = robot_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateBotResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBotResponse, self).to_map()
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
            temp_model = CreateBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, biz_code=None, knowledge_type=None, name=None, parent_category_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.biz_code = biz_code  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateCategoryResponseBody(TeaModel):
    def __init__(self, category_id=None, request_id=None, success=None):
        self.category_id = category_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCategoryResponse, self).to_map()
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
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCoreWordRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCoreWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class CreateCoreWordResponseBody(TeaModel):
    def __init__(self, core_word_code=None, request_id=None):
        self.core_word_code = core_word_code  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCoreWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCoreWordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCoreWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCoreWordResponse, self).to_map()
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
            temp_model = CreateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogRequest(TeaModel):
    def __init__(self, agent_key=None, description=None, dialog_name=None, instance_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.description = description  # type: str
        self.dialog_name = dialog_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDialogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDialogResponseBody(TeaModel):
    def __init__(self, dialog_id=None, request_id=None):
        self.dialog_id = dialog_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDialogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDialogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDialogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDialogResponse, self).to_map()
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
            temp_model = CreateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEntityRequestMembers(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class CreateEntityRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, entity_name=None, entity_type=None, members=None, regex=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members = members  # type: list[CreateEntityRequestMembers]
        self.regex = regex  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = CreateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, entity_name=None, entity_type=None, members_shrink=None,
                 regex=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members_shrink = members_shrink  # type: str
        self.regex = regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEntityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEntityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEntityResponse, self).to_map()
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
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, intent_definition=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.intent_definition = intent_definition  # type: IntentCreateDTO

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super(CreateIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        return self


class CreateIntentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, intent_definition_shrink=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.intent_definition_shrink = intent_definition_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIntentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentResponse, self).to_map()
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
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(self, knowledge_id=None, title=None):
        self.knowledge_id = knowledge_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKnowledgeRequestKnowledgeOutlines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateKnowledgeRequestKnowledgeSimQuestions(TeaModel):
    def __init__(self, title=None):
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKnowledgeRequestKnowledgeSimQuestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(self, content=None, perspective_ids=None, plain_text=None):
        self.content = content  # type: str
        self.perspective_ids = perspective_ids  # type: list[str]
        self.plain_text = plain_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKnowledgeRequestKnowledgeSolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        return self


class CreateKnowledgeRequestKnowledge(TeaModel):
    def __init__(self, category_id=None, end_date=None, knowledge_title=None, knowledge_type=None, outlines=None,
                 sim_questions=None, solutions=None, start_date=None):
        self.category_id = category_id  # type: long
        self.end_date = end_date  # type: str
        self.knowledge_title = knowledge_title  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.outlines = outlines  # type: list[CreateKnowledgeRequestKnowledgeOutlines]
        self.sim_questions = sim_questions  # type: list[CreateKnowledgeRequestKnowledgeSimQuestions]
        self.solutions = solutions  # type: list[CreateKnowledgeRequestKnowledgeSolutions]
        self.start_date = start_date  # type: str

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateKnowledgeRequestKnowledge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = CreateKnowledgeRequestKnowledgeOutlines()
                self.outlines.append(temp_model.from_map(k))
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = CreateKnowledgeRequestKnowledgeSimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = CreateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class CreateKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge = knowledge  # type: CreateKnowledgeRequestKnowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super(CreateKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            temp_model = CreateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class CreateKnowledgeShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_shrink=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_shrink = knowledge_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKnowledgeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class CreateKnowledgeResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKnowledgeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKnowledgeResponse, self).to_map()
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
            temp_model = CreateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePerspectiveResponseBody(TeaModel):
    def __init__(self, perspective_id=None, request_id=None):
        self.perspective_id = perspective_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePerspectiveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePerspectiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePerspectiveResponse, self).to_map()
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
            temp_model = CreatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBotRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteBotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBotResponseBody, self).to_map()
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


class DeleteBotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBotResponse, self).to_map()
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
            temp_model = DeleteBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCategoryResponse, self).to_map()
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCoreWordRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCoreWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DeleteCoreWordResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCoreWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCoreWordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCoreWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCoreWordResponse, self).to_map()
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
            temp_model = DeleteCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDialogRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDialogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DeleteDialogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDialogResponseBody, self).to_map()
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


class DeleteDialogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDialogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDialogResponse, self).to_map()
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
            temp_model = DeleteDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DeleteEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEntityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEntityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEntityResponse, self).to_map()
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
            temp_model = DeleteEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(self, agent_key=None, intent_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIntentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIntentResponse, self).to_map()
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
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteKnowledgeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKnowledgeResponseBody, self).to_map()
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


class DeleteKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteKnowledgeResponse, self).to_map()
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
            temp_model = DeleteKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBotRequest(TeaModel):
    def __init__(self, agent_key=None, instance_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeBotResponseBodyCategories(TeaModel):
    def __init__(self, category_id=None, name=None, parent_category_id=None):
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBotResponseBodyCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class DescribeBotResponseBody(TeaModel):
    def __init__(self, avatar=None, categories=None, create_time=None, instance_id=None, introduction=None,
                 language_code=None, logo=None, name=None, request_id=None, time_zone=None):
        self.avatar = avatar  # type: str
        self.categories = categories  # type: list[DescribeBotResponseBodyCategories]
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.logo = logo  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.time_zone = time_zone  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeBotResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeBotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBotResponse, self).to_map()
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
            temp_model = DescribeBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(self, category_id=None, name=None, parent_category_id=None, request_id=None):
        self.category_id = category_id  # type: long
        self.name = name  # type: str
        self.parent_category_id = parent_category_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCategoryResponse, self).to_map()
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
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCoreWordRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCoreWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DescribeCoreWordResponseBody(TeaModel):
    def __init__(self, core_word_code=None, core_word_name=None, create_time=None, modify_time=None,
                 request_id=None, synonyms=None):
        self.core_word_code = core_word_code  # type: str
        self.core_word_name = core_word_name  # type: str
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCoreWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class DescribeCoreWordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCoreWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCoreWordResponse, self).to_map()
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
            temp_model = DescribeCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDialogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogResponseBody(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, description=None,
                 dialog_id=None, dialog_name=None, is_online=None, is_sample_dialog=None, modify_time=None,
                 modify_user_id=None, modify_user_name=None, request_id=None, status=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.description = description  # type: str
        self.dialog_id = dialog_id  # type: long
        self.dialog_name = dialog_name  # type: str
        self.is_online = is_online  # type: bool
        self.is_sample_dialog = is_sample_dialog  # type: bool
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDialogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDialogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDialogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDialogResponse, self).to_map()
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
            temp_model = DescribeDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogFlowRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDialogFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogFlowResponseBody(TeaModel):
    def __init__(self, account_id=None, create_time=None, create_user_id=None, create_user_name=None,
                 dialog_id=None, dialog_name=None, global_vars=None, instance_id=None, modify_time=None, modify_user_id=None,
                 modify_user_name=None, module_definition=None, module_id=None, module_name=None, request_id=None, status=None,
                 tags=None, templates=None):
        self.account_id = account_id  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.dialog_id = dialog_id  # type: long
        self.dialog_name = dialog_name  # type: str
        self.global_vars = global_vars  # type: dict[str, any]
        self.instance_id = instance_id  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.module_definition = module_definition  # type: PaasProcessData
        self.module_id = module_id  # type: long
        self.module_name = module_name  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int
        self.tags = tags  # type: str
        self.templates = templates  # type: str

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super(DescribeDialogFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.global_vars is not None:
            result['GlobalVars'] = self.global_vars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('GlobalVars') is not None:
            self.global_vars = m.get('GlobalVars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ModuleDefinition') is not None:
            temp_model = PaasProcessData()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class DescribeDialogFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDialogFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDialogFlowResponse, self).to_map()
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
            temp_model = DescribeDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntitiesRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DescribeEntitiesResponseBodyMembers(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntitiesResponseBodyMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class DescribeEntitiesResponseBody(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, entity_id=None,
                 entity_name=None, entity_type=None, members=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 regex=None, request_id=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members = members  # type: list[DescribeEntitiesResponseBodyMembers]
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.regex = regex  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeEntitiesResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEntitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEntitiesResponse, self).to_map()
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
            temp_model = DescribeEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntentRequest(TeaModel):
    def __init__(self, agent_key=None, intent_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DescribeIntentResponseBodyRuleCheck(TeaModel):
    def __init__(self, error=None, strict=None, text=None, warning=None):
        self.error = error  # type: list[str]
        self.strict = strict  # type: bool
        self.text = text  # type: str
        self.warning = warning  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentResponseBodyRuleCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.text is not None:
            result['Text'] = self.text
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class DescribeIntentResponseBodySlotTags(TeaModel):
    def __init__(self, user_say_id=None, value=None):
        self.user_say_id = user_say_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentResponseBodySlotTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIntentResponseBodySlot(TeaModel):
    def __init__(self, is_array=None, is_necessary=None, life_span=None, name=None, question=None, slot_id=None,
                 tags=None, value=None):
        self.is_array = is_array  # type: bool
        self.is_necessary = is_necessary  # type: bool
        self.life_span = life_span  # type: int
        self.name = name  # type: str
        self.question = question  # type: list[str]
        self.slot_id = slot_id  # type: str
        self.tags = tags  # type: list[DescribeIntentResponseBodySlotTags]
        self.value = value  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIntentResponseBodySlot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeIntentResponseBodySlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIntentResponseBodyUserSayData(TeaModel):
    def __init__(self, slot_id=None, text=None):
        self.slot_id = slot_id  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIntentResponseBodyUserSayData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeIntentResponseBodyUserSay(TeaModel):
    def __init__(self, data=None, strict=None, user_say_id=None):
        self.data = data  # type: list[DescribeIntentResponseBodyUserSayData]
        self.strict = strict  # type: bool
        self.user_say_id = user_say_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIntentResponseBodyUserSay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeIntentResponseBodyUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, dialog_id=None, intent_id=None,
                 modify_time=None, modify_user_id=None, modify_user_name=None, name=None, request_id=None, rule_check=None,
                 slot=None, type=None, user_say=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.dialog_id = dialog_id  # type: long
        self.intent_id = intent_id  # type: long
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.rule_check = rule_check  # type: list[DescribeIntentResponseBodyRuleCheck]
        self.slot = slot  # type: list[DescribeIntentResponseBodySlot]
        self.type = type  # type: str
        self.user_say = user_say  # type: list[DescribeIntentResponseBodyUserSay]

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = DescribeIntentResponseBodyRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = DescribeIntentResponseBodySlot()
                self.slot.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = DescribeIntentResponseBodyUserSay()
                self.user_say.append(temp_model.from_map(k))
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIntentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIntentResponse, self).to_map()
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
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DescribeKnowledgeResponseBodyOutlines(TeaModel):
    def __init__(self, knowledge_id=None, outline_id=None, title=None):
        self.knowledge_id = knowledge_id  # type: long
        self.outline_id = outline_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKnowledgeResponseBodyOutlines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeKnowledgeResponseBodySimQuestions(TeaModel):
    def __init__(self, create_time=None, modify_time=None, sim_question_id=None, title=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.sim_question_id = sim_question_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKnowledgeResponseBodySimQuestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeKnowledgeResponseBodySolutions(TeaModel):
    def __init__(self, content=None, create_time=None, modify_time=None, perspective_ids=None, plain_text=None,
                 solution_id=None, summary=None):
        self.content = content  # type: str
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.perspective_ids = perspective_ids  # type: list[str]
        self.plain_text = plain_text  # type: str
        self.solution_id = solution_id  # type: long
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKnowledgeResponseBodySolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class DescribeKnowledgeResponseBody(TeaModel):
    def __init__(self, category_id=None, core_words=None, create_time=None, create_user_name=None, end_date=None,
                 key_words=None, knowledge_id=None, knowledge_status=None, knowledge_title=None, knowledge_type=None,
                 modify_time=None, modify_user_name=None, outlines=None, request_id=None, sim_questions=None, solutions=None,
                 start_date=None, version=None):
        self.category_id = category_id  # type: long
        self.core_words = core_words  # type: list[str]
        self.create_time = create_time  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_date = end_date  # type: str
        self.key_words = key_words  # type: list[str]
        self.knowledge_id = knowledge_id  # type: long
        self.knowledge_status = knowledge_status  # type: int
        self.knowledge_title = knowledge_title  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.modify_time = modify_time  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.outlines = outlines  # type: list[DescribeKnowledgeResponseBodyOutlines]
        self.request_id = request_id  # type: str
        self.sim_questions = sim_questions  # type: list[DescribeKnowledgeResponseBodySimQuestions]
        self.solutions = solutions  # type: list[DescribeKnowledgeResponseBodySolutions]
        self.start_date = start_date  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKnowledgeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = DescribeKnowledgeResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = DescribeKnowledgeResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = DescribeKnowledgeResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKnowledgeResponse, self).to_map()
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
            temp_model = DescribeKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, perspective_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(self, create_time=None, create_user_name=None, modify_time=None, modify_user_name=None, name=None,
                 perspective_code=None, perspective_id=None, request_id=None, self_define=None, status=None):
        self.create_time = create_time  # type: str
        self.create_user_name = create_user_name  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.name = name  # type: str
        self.perspective_code = perspective_code  # type: str
        self.perspective_id = perspective_id  # type: str
        self.request_id = request_id  # type: str
        self.self_define = self_define  # type: bool
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePerspectiveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePerspectiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePerspectiveResponse, self).to_map()
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
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDialogFlowRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDialogFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DisableDialogFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDialogFlowResponseBody, self).to_map()
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


class DisableDialogFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableDialogFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableDialogFlowResponse, self).to_map()
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
            temp_model = DisableDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DisableKnowledgeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableKnowledgeResponseBody, self).to_map()
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


class DisableKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableKnowledgeResponse, self).to_map()
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
            temp_model = DisableKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(self, agent_key=None, feedback=None, instance_id=None, message_id=None, session_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.feedback = feedback  # type: str
        self.instance_id = instance_id  # type: str
        self.message_id = message_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(self, feedback=None, http_status=None, message_id=None, request_id=None, success=None):
        self.feedback = feedback  # type: str
        self.http_status = http_status  # type: long
        self.message_id = message_id  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FeedbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FeedbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FeedbackResponse, self).to_map()
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
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(self, agent_key=None, task_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncResultResponse, self).to_map()
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
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotChatDataRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotChatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotChatDataResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotChatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotChatDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBotChatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBotChatDataResponse, self).to_map()
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
            temp_model = GetBotChatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotDsStatDataRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotDsStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotDsStatDataResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotDsStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotDsStatDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBotDsStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBotDsStatDataResponse, self).to_map()
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
            temp_model = GetBotDsStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotKnowledgeStatDataRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotKnowledgeStatDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotKnowledgeStatDataResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotKnowledgeStatDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotKnowledgeStatDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBotKnowledgeStatDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBotKnowledgeStatDataResponse, self).to_map()
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
            temp_model = GetBotKnowledgeStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotSessionDataRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotSessionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotSessionDataResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBotSessionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotSessionDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBotSessionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBotSessionDataResponse, self).to_map()
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
            temp_model = GetBotSessionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationListRequest(TeaModel):
    def __init__(self, agent_key=None, end_date=None, instance_id=None, page_number=None, page_size=None,
                 sender_id=None, session_id=None, start_date=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_date = end_date  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sender_id = sender_id  # type: str
        self.session_id = session_id  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConversationListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetConversationListResponseBody(TeaModel):
    def __init__(self, messages=None, page_number=None, page_size=None, request_id=None, total_counts=None):
        self.messages = messages  # type: list[dict[str, any]]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_counts = total_counts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConversationListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class GetConversationListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetConversationListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConversationListResponse, self).to_map()
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
            temp_model = GetConversationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotChatHistorysRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotChatHistorysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotChatHistorysResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotChatHistorysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotChatHistorysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotChatHistorysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotChatHistorysResponse, self).to_map()
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
            temp_model = ListBotChatHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdDsDatasRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotColdDsDatasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotColdDsDatasResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotColdDsDatasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotColdDsDatasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotColdDsDatasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotColdDsDatasResponse, self).to_map()
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
            temp_model = ListBotColdDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdKnowledgesRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotColdKnowledgesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotColdKnowledgesResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotColdKnowledgesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotColdKnowledgesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotColdKnowledgesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotColdKnowledgesResponse, self).to_map()
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
            temp_model = ListBotColdKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotDsDetailsRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotDsDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotDsDetailsResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotDsDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotDsDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotDsDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotDsDetailsResponse, self).to_map()
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
            temp_model = ListBotDsDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotDsDatasRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotHotDsDatasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotHotDsDatasResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotHotDsDatasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotHotDsDatasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotHotDsDatasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotHotDsDatasResponse, self).to_map()
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
            temp_model = ListBotHotDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotKnowledgesRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: int
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotHotKnowledgesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotHotKnowledgesResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotHotKnowledgesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotHotKnowledgesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotHotKnowledgesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotHotKnowledgesResponse, self).to_map()
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
            temp_model = ListBotHotKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotKnowledgeDetailsRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, limit=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotKnowledgeDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotKnowledgeDetailsResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotKnowledgeDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotKnowledgeDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotKnowledgeDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotKnowledgeDetailsResponse, self).to_map()
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
            temp_model = ListBotKnowledgeDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotReceptionDetailDatasRequest(TeaModel):
    def __init__(self, agent_key=None, end_time=None, robot_instance_id=None, start_time=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.end_time = end_time  # type: str
        self.robot_instance_id = robot_instance_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotReceptionDetailDatasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotReceptionDetailDatasResponseBody(TeaModel):
    def __init__(self, cost_time=None, datas=None, request_id=None):
        self.cost_time = cost_time  # type: str
        self.datas = datas  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBotReceptionDetailDatasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotReceptionDetailDatasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBotReceptionDetailDatasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBotReceptionDetailDatasResponse, self).to_map()
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
            temp_model = ListBotReceptionDetailDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationLogsRequest(TeaModel):
    def __init__(self, agent_key=None, session_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConversationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListConversationLogsResponseBody(TeaModel):
    def __init__(self, chat_logs=None, request_id=None, rounds=None):
        self.chat_logs = chat_logs  # type: list[dict[str, any]]
        self.request_id = request_id  # type: str
        self.rounds = rounds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConversationLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_logs is not None:
            result['ChatLogs'] = self.chat_logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rounds is not None:
            result['Rounds'] = self.rounds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChatLogs') is not None:
            self.chat_logs = m.get('ChatLogs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')
        return self


class ListConversationLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConversationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConversationLogsResponse, self).to_map()
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
            temp_model = ListConversationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveKnowledgeCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, knowledge_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveKnowledgeCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class MoveKnowledgeCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveKnowledgeCategoryResponseBody, self).to_map()
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


class MoveKnowledgeCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveKnowledgeCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveKnowledgeCategoryResponse, self).to_map()
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
            temp_model = MoveKnowledgeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDialogFlowRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishDialogFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class PublishDialogFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishDialogFlowResponseBody, self).to_map()
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


class PublishDialogFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishDialogFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishDialogFlowResponse, self).to_map()
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
            temp_model = PublishDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, async=None, knowledge_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.async = async  # type: bool
        self.knowledge_id = knowledge_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.async is not None:
            result['Async'] = self.async
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class PublishKnowledgeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishKnowledgeResponseBody, self).to_map()
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


class PublishKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishKnowledgeResponse, self).to_map()
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
            temp_model = PublishKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBotsRequest(TeaModel):
    def __init__(self, agent_key=None, page_number=None, page_size=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBotsResponseBodyBots(TeaModel):
    def __init__(self, avatar=None, create_time=None, instance_id=None, introduction=None, language_code=None,
                 name=None, time_zone=None):
        self.avatar = avatar  # type: str
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.introduction = introduction  # type: str
        self.language_code = language_code  # type: str
        self.name = name  # type: str
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBotsResponseBodyBots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class QueryBotsResponseBody(TeaModel):
    def __init__(self, bots=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.bots = bots  # type: list[QueryBotsResponseBodyBots]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.bots:
            for k in self.bots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
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
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = QueryBotsResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryBotsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBotsResponse, self).to_map()
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
            temp_model = QueryBotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCategoriesRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_type=None, parent_category_id=None, show_childrens=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_type = knowledge_type  # type: long
        self.parent_category_id = parent_category_id  # type: long
        self.show_childrens = show_childrens  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCategoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.show_childrens is not None:
            result['ShowChildrens'] = self.show_childrens
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('ShowChildrens') is not None:
            self.show_childrens = m.get('ShowChildrens')
        return self


class QueryCategoriesResponseBody(TeaModel):
    def __init__(self, categories=None, request_id=None):
        self.categories = categories  # type: list[Children]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCategoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = Children()
                self.categories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCategoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCategoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCategoriesResponse, self).to_map()
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
            temp_model = QueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCoreWordsRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None, page_number=None, page_size=None, synonym=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.synonym = synonym  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCoreWordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class QueryCoreWordsResponseBodyCoreWords(TeaModel):
    def __init__(self, core_word_code=None, core_word_name=None, create_time=None, modify_time=None, synonyms=None):
        self.core_word_code = core_word_code  # type: str
        self.core_word_name = core_word_name  # type: str
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCoreWordsResponseBodyCoreWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class QueryCoreWordsResponseBody(TeaModel):
    def __init__(self, core_words=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.core_words = core_words  # type: list[QueryCoreWordsResponseBodyCoreWords]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.core_words:
            for k in self.core_words:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCoreWordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoreWords'] = []
        if self.core_words is not None:
            for k in self.core_words:
                result['CoreWords'].append(k.to_map() if k else None)
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
        self.core_words = []
        if m.get('CoreWords') is not None:
            for k in m.get('CoreWords'):
                temp_model = QueryCoreWordsResponseBodyCoreWords()
                self.core_words.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCoreWordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCoreWordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCoreWordsResponse, self).to_map()
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
            temp_model = QueryCoreWordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDialogsRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_name=None, instance_id=None, page_number=None, page_size=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_name = dialog_name  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDialogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDialogsResponseBodyDialogs(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, description=None,
                 dialog_id=None, dialog_name=None, is_online=None, is_sample_dialog=None, modify_time=None,
                 modify_user_id=None, modify_user_name=None, status=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.description = description  # type: str
        self.dialog_id = dialog_id  # type: long
        self.dialog_name = dialog_name  # type: str
        self.is_online = is_online  # type: bool
        self.is_sample_dialog = is_sample_dialog  # type: bool
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDialogsResponseBodyDialogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDialogsResponseBody(TeaModel):
    def __init__(self, dialogs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.dialogs = dialogs  # type: list[QueryDialogsResponseBodyDialogs]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dialogs:
            for k in self.dialogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDialogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
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
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = QueryDialogsResponseBodyDialogs()
                self.dialogs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDialogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryDialogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDialogsResponse, self).to_map()
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
            temp_model = QueryDialogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEntitiesRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, entity_name=None, page_number=None, page_size=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.entity_name = entity_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEntitiesResponseBodyEntitiesMembers(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEntitiesResponseBodyEntitiesMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class QueryEntitiesResponseBodyEntities(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, entity_id=None,
                 entity_name=None, entity_type=None, members=None, modify_time=None, modify_user_id=None, modify_user_name=None,
                 regex=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members = members  # type: list[QueryEntitiesResponseBodyEntitiesMembers]
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.regex = regex  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEntitiesResponseBodyEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = QueryEntitiesResponseBodyEntitiesMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class QueryEntitiesResponseBody(TeaModel):
    def __init__(self, entities=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.entities = entities  # type: list[QueryEntitiesResponseBodyEntities]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = QueryEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryEntitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEntitiesResponse, self).to_map()
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
            temp_model = QueryEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentsRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, intent_name=None, page_number=None, page_size=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.intent_name = intent_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryIntentsResponseBodyIntentsRuleCheck(TeaModel):
    def __init__(self, error=None, strict=None, text=None, warning=None):
        self.error = error  # type: list[str]
        self.strict = strict  # type: bool
        self.text = text  # type: str
        self.warning = warning  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntentsRuleCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.text is not None:
            result['Text'] = self.text
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class QueryIntentsResponseBodyIntentsSlotTags(TeaModel):
    def __init__(self, user_say_id=None, value=None):
        self.user_say_id = user_say_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntentsSlotTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryIntentsResponseBodyIntentsSlot(TeaModel):
    def __init__(self, is_array=None, is_necessary=None, life_span=None, name=None, question=None, slot_id=None,
                 tags=None, value=None):
        self.is_array = is_array  # type: bool
        self.is_necessary = is_necessary  # type: bool
        self.life_span = life_span  # type: int
        self.name = name  # type: str
        self.question = question  # type: list[str]
        self.slot_id = slot_id  # type: str
        self.tags = tags  # type: list[QueryIntentsResponseBodyIntentsSlotTags]
        self.value = value  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntentsSlot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = QueryIntentsResponseBodyIntentsSlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryIntentsResponseBodyIntentsUserSayData(TeaModel):
    def __init__(self, slot_id=None, text=None):
        self.slot_id = slot_id  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntentsUserSayData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QueryIntentsResponseBodyIntentsUserSay(TeaModel):
    def __init__(self, data=None, strict=None, user_say_id=None):
        self.data = data  # type: list[QueryIntentsResponseBodyIntentsUserSayData]
        self.strict = strict  # type: bool
        self.user_say_id = user_say_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntentsUserSay, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIntentsResponseBodyIntentsUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class QueryIntentsResponseBodyIntents(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, intent_id=None,
                 modify_time=None, modify_user_id=None, modify_user_name=None, name=None, rule_check=None, slot=None,
                 user_say=None):
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.create_user_name = create_user_name  # type: str
        self.intent_id = intent_id  # type: long
        self.modify_time = modify_time  # type: str
        self.modify_user_id = modify_user_id  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.name = name  # type: str
        self.rule_check = rule_check  # type: list[QueryIntentsResponseBodyIntentsRuleCheck]
        self.slot = slot  # type: list[QueryIntentsResponseBodyIntentsSlot]
        self.user_say = user_say  # type: list[QueryIntentsResponseBodyIntentsUserSay]

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentsResponseBodyIntents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = QueryIntentsResponseBodyIntentsRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = QueryIntentsResponseBodyIntentsSlot()
                self.slot.append(temp_model.from_map(k))
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = QueryIntentsResponseBodyIntentsUserSay()
                self.user_say.append(temp_model.from_map(k))
        return self


class QueryIntentsResponseBody(TeaModel):
    def __init__(self, intents=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.intents = intents  # type: list[QueryIntentsResponseBodyIntents]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.intents:
            for k in self.intents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intents'] = []
        if self.intents is not None:
            for k in self.intents:
                result['Intents'].append(k.to_map() if k else None)
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
        self.intents = []
        if m.get('Intents') is not None:
            for k in m.get('Intents'):
                temp_model = QueryIntentsResponseBodyIntents()
                self.intents.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryIntentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryIntentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentsResponse, self).to_map()
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
            temp_model = QueryIntentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryKnowledgesRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, core_word_name=None, knowledge_title=None,
                 page_number=None, page_size=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.core_word_name = core_word_name  # type: str
        self.knowledge_title = knowledge_title  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryKnowledgesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryKnowledgesResponseBodyKnowledges(TeaModel):
    def __init__(self, category_id=None, core_words=None, create_time=None, create_user_name=None, end_date=None,
                 knowledge_id=None, knowledge_status=None, knowledge_title=None, modify_time=None, modify_user_name=None,
                 start_date=None, version=None):
        self.category_id = category_id  # type: long
        self.core_words = core_words  # type: list[str]
        self.create_time = create_time  # type: str
        self.create_user_name = create_user_name  # type: str
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.knowledge_status = knowledge_status  # type: int
        self.knowledge_title = knowledge_title  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.start_date = start_date  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryKnowledgesResponseBodyKnowledges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryKnowledgesResponseBody(TeaModel):
    def __init__(self, knowledges=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.knowledges = knowledges  # type: list[QueryKnowledgesResponseBodyKnowledges]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.knowledges:
            for k in self.knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryKnowledgesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Knowledges'] = []
        if self.knowledges is not None:
            for k in self.knowledges:
                result['Knowledges'].append(k.to_map() if k else None)
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
        self.knowledges = []
        if m.get('Knowledges') is not None:
            for k in m.get('Knowledges'):
                temp_model = QueryKnowledgesResponseBodyKnowledges()
                self.knowledges.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryKnowledgesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryKnowledgesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryKnowledgesResponse, self).to_map()
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
            temp_model = QueryKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesRequest(TeaModel):
    def __init__(self, agent_key=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPerspectivesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(self, create_time=None, create_user_name=None, modify_time=None, modify_user_name=None, name=None,
                 perspective_code=None, perspective_id=None, self_define=None, status=None):
        self.create_time = create_time  # type: str
        self.create_user_name = create_user_name  # type: str
        self.modify_time = modify_time  # type: str
        self.modify_user_name = modify_user_name  # type: str
        self.name = name  # type: str
        self.perspective_code = perspective_code  # type: str
        self.perspective_id = perspective_id  # type: str
        self.self_define = self_define  # type: bool
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPerspectivesResponseBodyPerspectives, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(self, perspectives=None, request_id=None):
        self.perspectives = perspectives  # type: list[QueryPerspectivesResponseBodyPerspectives]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.perspectives:
            for k in self.perspectives:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPerspectivesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryPerspectivesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPerspectivesResponse, self).to_map()
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
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEntitiesRequest(TeaModel):
    def __init__(self, agent_key=None, entity_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySystemEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBodySystemEntities(TeaModel):
    def __init__(self, default_question=None, entity_code=None, entity_name=None):
        self.default_question = default_question  # type: str
        self.entity_code = entity_code  # type: str
        self.entity_name = entity_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySystemEntitiesResponseBodySystemEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_question is not None:
            result['DefaultQuestion'] = self.default_question
        if self.entity_code is not None:
            result['EntityCode'] = self.entity_code
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultQuestion') is not None:
            self.default_question = m.get('DefaultQuestion')
        if m.get('EntityCode') is not None:
            self.entity_code = m.get('EntityCode')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBody(TeaModel):
    def __init__(self, request_id=None, system_entities=None):
        self.request_id = request_id  # type: str
        self.system_entities = system_entities  # type: list[QuerySystemEntitiesResponseBodySystemEntities]

    def validate(self):
        if self.system_entities:
            for k in self.system_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySystemEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SystemEntities'] = []
        if self.system_entities is not None:
            for k in self.system_entities:
                result['SystemEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.system_entities = []
        if m.get('SystemEntities') is not None:
            for k in m.get('SystemEntities'):
                temp_model = QuerySystemEntitiesResponseBodySystemEntities()
                self.system_entities.append(temp_model.from_map(k))
        return self


class QuerySystemEntitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySystemEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySystemEntitiesResponse, self).to_map()
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
            temp_model = QuerySystemEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntityMemberRequestMember(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntityMemberRequestMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class RemoveEntityMemberRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, member=None, remove_type=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.member = member  # type: RemoveEntityMemberRequestMember
        self.remove_type = remove_type  # type: str

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super(RemoveEntityMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member is not None:
            result['Member'] = self.member.to_map()
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            temp_model = RemoveEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        return self


class RemoveEntityMemberShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, member_shrink=None, remove_type=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.member_shrink = member_shrink  # type: str
        self.remove_type = remove_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntityMemberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            self.member_shrink = m.get('Member')
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        return self


class RemoveEntityMemberResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntityMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveEntityMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveEntityMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveEntityMemberResponse, self).to_map()
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
            temp_model = RemoveEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSynonymRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_name=None, synonym=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_name = core_word_name  # type: str
        self.synonym = synonym  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSynonymRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class RemoveSynonymResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSynonymResponseBody, self).to_map()
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


class RemoveSynonymResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveSynonymResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSynonymResponse, self).to_map()
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
            temp_model = RemoveSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestDialogFlowRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestDialogFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class TestDialogFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestDialogFlowResponseBody, self).to_map()
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


class TestDialogFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TestDialogFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TestDialogFlowResponse, self).to_map()
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
            temp_model = TestDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(self, agent_key=None, category_id=None, name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.category_id = category_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCategoryResponse, self).to_map()
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
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCoreWordRequest(TeaModel):
    def __init__(self, agent_key=None, core_word_code=None, core_word_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.core_word_code = core_word_code  # type: str
        self.core_word_name = core_word_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCoreWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class UpdateCoreWordResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCoreWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCoreWordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCoreWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCoreWordResponse, self).to_map()
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
            temp_model = UpdateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogRequest(TeaModel):
    def __init__(self, agent_key=None, description=None, dialog_id=None, dialog_name=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.description = description  # type: str
        self.dialog_id = dialog_id  # type: long
        self.dialog_name = dialog_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDialogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        return self


class UpdateDialogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDialogResponseBody, self).to_map()
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


class UpdateDialogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDialogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDialogResponse, self).to_map()
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
            temp_model = UpdateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogFlowRequestModuleDefinition(TeaModel):
    def __init__(self, global_vars=None, module_definition=None):
        self.global_vars = global_vars  # type: dict[str, any]
        self.module_definition = module_definition  # type: PaasProcessData

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super(UpdateDialogFlowRequestModuleDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_vars is not None:
            result['GlobalVars'] = self.global_vars
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalVars') is not None:
            self.global_vars = m.get('GlobalVars')
        if m.get('ModuleDefinition') is not None:
            temp_model = PaasProcessData()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        return self


class UpdateDialogFlowRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, module_definition=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.module_definition = module_definition  # type: UpdateDialogFlowRequestModuleDefinition

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super(UpdateDialogFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            temp_model = UpdateDialogFlowRequestModuleDefinition()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        return self


class UpdateDialogFlowShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, dialog_id=None, module_definition_shrink=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.dialog_id = dialog_id  # type: long
        self.module_definition_shrink = module_definition_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDialogFlowShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition_shrink is not None:
            result['ModuleDefinition'] = self.module_definition_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            self.module_definition_shrink = m.get('ModuleDefinition')
        return self


class UpdateDialogFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDialogFlowResponseBody, self).to_map()
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


class UpdateDialogFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDialogFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDialogFlowResponse, self).to_map()
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
            temp_model = UpdateDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequestMembers(TeaModel):
    def __init__(self, member_name=None, synonyms=None):
        self.member_name = member_name  # type: str
        self.synonyms = synonyms  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, entity_name=None, entity_type=None, members=None, regex=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members = members  # type: list[UpdateEntityRequestMembers]
        self.regex = regex  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, entity_id=None, entity_name=None, entity_type=None, members_shrink=None,
                 regex=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_name = entity_name  # type: str
        self.entity_type = entity_type  # type: str
        self.members_shrink = members_shrink  # type: str
        self.regex = regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(self, entity_id=None, request_id=None):
        self.entity_id = entity_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEntityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEntityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEntityResponse, self).to_map()
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
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(self, agent_key=None, intent_definition=None, intent_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.intent_definition = intent_definition  # type: IntentCreateDTO
        self.intent_id = intent_id  # type: long

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super(UpdateIntentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, intent_definition_shrink=None, intent_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.intent_definition_shrink = intent_definition_shrink  # type: str
        self.intent_id = intent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(self, intent_id=None, request_id=None):
        self.intent_id = intent_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIntentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIntentResponse, self).to_map()
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
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(self, action=None, knowledge_id=None, outline_id=None, title=None):
        self.action = action  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.outline_id = outline_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKnowledgeRequestKnowledgeOutlines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateKnowledgeRequestKnowledgeSimQuestions(TeaModel):
    def __init__(self, action=None, sim_question_id=None, title=None):
        self.action = action  # type: str
        self.sim_question_id = sim_question_id  # type: long
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKnowledgeRequestKnowledgeSimQuestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(self, action=None, content=None, perspective_ids=None, plain_text=None, solution_id=None):
        self.action = action  # type: str
        self.content = content  # type: str
        self.perspective_ids = perspective_ids  # type: list[str]
        self.plain_text = plain_text  # type: str
        self.solution_id = solution_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKnowledgeRequestKnowledgeSolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.content is not None:
            result['Content'] = self.content
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class UpdateKnowledgeRequestKnowledge(TeaModel):
    def __init__(self, category_id=None, end_date=None, knowledge_id=None, knowledge_title=None,
                 knowledge_type=None, outlines=None, sim_questions=None, solutions=None, start_date=None):
        self.category_id = category_id  # type: long
        self.end_date = end_date  # type: str
        self.knowledge_id = knowledge_id  # type: long
        self.knowledge_title = knowledge_title  # type: str
        self.knowledge_type = knowledge_type  # type: int
        self.outlines = outlines  # type: list[UpdateKnowledgeRequestKnowledgeOutlines]
        self.sim_questions = sim_questions  # type: list[UpdateKnowledgeRequestKnowledgeSimQuestions]
        self.solutions = solutions  # type: list[UpdateKnowledgeRequestKnowledgeSolutions]
        self.start_date = start_date  # type: str

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateKnowledgeRequestKnowledge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = UpdateKnowledgeRequestKnowledgeOutlines()
                self.outlines.append(temp_model.from_map(k))
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = UpdateKnowledgeRequestKnowledgeSimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = UpdateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class UpdateKnowledgeRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge = knowledge  # type: UpdateKnowledgeRequestKnowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super(UpdateKnowledgeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            temp_model = UpdateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class UpdateKnowledgeShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, knowledge_shrink=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.knowledge_shrink = knowledge_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKnowledgeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class UpdateKnowledgeResponseBody(TeaModel):
    def __init__(self, knowledge_id=None, request_id=None):
        self.knowledge_id = knowledge_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKnowledgeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateKnowledgeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateKnowledgeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKnowledgeResponse, self).to_map()
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
            temp_model = UpdateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(self, agent_key=None, name=None, perspective_id=None):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key  # type: str
        self.name = name  # type: str
        self.perspective_id = perspective_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePerspectiveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class UpdatePerspectiveResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePerspectiveResponseBody, self).to_map()
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


class UpdatePerspectiveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePerspectiveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePerspectiveResponse, self).to_map()
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
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


