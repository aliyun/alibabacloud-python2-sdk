# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CarbonEmissionElecSummaryItem(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, ratio=None, raw_data=None):
        self.carbon_emission_data = carbon_emission_data  # type: float
        self.data_unit = data_unit  # type: str
        self.name = name  # type: str
        self.ratio = ratio  # type: float
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CarbonEmissionElecSummaryItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class ConstituteItemEnvGasEmissions(TeaModel):
    def __init__(self, carbon_emission_data=None, gas_emission_data=None, name=None, type=None):
        self.carbon_emission_data = carbon_emission_data  # type: float
        self.gas_emission_data = gas_emission_data  # type: float
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConstituteItemEnvGasEmissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.gas_emission_data is not None:
            result['gasEmissionData'] = self.gas_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('gasEmissionData') is not None:
            self.gas_emission_data = m.get('gasEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ConstituteItem(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, emission_source=None, emission_source_key=None,
                 enterprise_name=None, env_gas_emissions=None, name=None, name_key=None, ratio=None, raw_data=None,
                 sub_constitute_items=None):
        self.carbon_emission_data = carbon_emission_data  # type: float
        self.data_unit = data_unit  # type: str
        self.emission_source = emission_source  # type: str
        self.emission_source_key = emission_source_key  # type: str
        self.enterprise_name = enterprise_name  # type: str
        self.env_gas_emissions = env_gas_emissions  # type: list[ConstituteItemEnvGasEmissions]
        self.name = name  # type: str
        self.name_key = name_key  # type: str
        self.ratio = ratio  # type: float
        self.raw_data = raw_data  # type: float
        self.sub_constitute_items = sub_constitute_items  # type: list[ConstituteItem]

    def validate(self):
        if self.env_gas_emissions:
            for k in self.env_gas_emissions:
                if k:
                    k.validate()
        if self.sub_constitute_items:
            for k in self.sub_constitute_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ConstituteItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.emission_source is not None:
            result['emissionSource'] = self.emission_source
        if self.emission_source_key is not None:
            result['emissionSourceKey'] = self.emission_source_key
        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name
        result['envGasEmissions'] = []
        if self.env_gas_emissions is not None:
            for k in self.env_gas_emissions:
                result['envGasEmissions'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        result['subConstituteItems'] = []
        if self.sub_constitute_items is not None:
            for k in self.sub_constitute_items:
                result['subConstituteItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('emissionSource') is not None:
            self.emission_source = m.get('emissionSource')
        if m.get('emissionSourceKey') is not None:
            self.emission_source_key = m.get('emissionSourceKey')
        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')
        self.env_gas_emissions = []
        if m.get('envGasEmissions') is not None:
            for k in m.get('envGasEmissions'):
                temp_model = ConstituteItemEnvGasEmissions()
                self.env_gas_emissions.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        self.sub_constitute_items = []
        if m.get('subConstituteItems') is not None:
            for k in m.get('subConstituteItems'):
                temp_model = ConstituteItem()
                self.sub_constitute_items.append(temp_model.from_map(k))
        return self


class EpdInventoryConstituteItem(TeaModel):
    def __init__(self, carbon_emission=None, factor=None, factor_dataset=None, factor_id=None, factor_type=None,
                 factor_unit=None, inventory_id=None, inventory_unit=None, inventory_value=None,
                 inventory_value_per_product=None, inventory_value_per_product_unit=None, items=None, name=None, num=None, percent=None,
                 quantity=None, resource_type=None, state=None, unit=None):
        self.carbon_emission = carbon_emission  # type: float
        self.factor = factor  # type: str
        self.factor_dataset = factor_dataset  # type: str
        self.factor_id = factor_id  # type: str
        self.factor_type = factor_type  # type: int
        self.factor_unit = factor_unit  # type: str
        self.inventory_id = inventory_id  # type: long
        self.inventory_unit = inventory_unit  # type: str
        self.inventory_value = inventory_value  # type: float
        self.inventory_value_per_product = inventory_value_per_product  # type: float
        self.inventory_value_per_product_unit = inventory_value_per_product_unit  # type: str
        self.items = items  # type: list[EpdInventoryConstituteItem]
        self.name = name  # type: str
        self.num = num  # type: long
        self.percent = percent  # type: float
        self.quantity = quantity  # type: float
        self.resource_type = resource_type  # type: str
        self.state = state  # type: int
        self.unit = unit  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EpdInventoryConstituteItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.factor is not None:
            result['factor'] = self.factor
        if self.factor_dataset is not None:
            result['factorDataset'] = self.factor_dataset
        if self.factor_id is not None:
            result['factorId'] = self.factor_id
        if self.factor_type is not None:
            result['factorType'] = self.factor_type
        if self.factor_unit is not None:
            result['factorUnit'] = self.factor_unit
        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id
        if self.inventory_unit is not None:
            result['inventoryUnit'] = self.inventory_unit
        if self.inventory_value is not None:
            result['inventoryValue'] = self.inventory_value
        if self.inventory_value_per_product is not None:
            result['inventoryValuePerProduct'] = self.inventory_value_per_product
        if self.inventory_value_per_product_unit is not None:
            result['inventoryValuePerProductUnit'] = self.inventory_value_per_product_unit
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.num is not None:
            result['num'] = self.num
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.state is not None:
            result['state'] = self.state
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('factor') is not None:
            self.factor = m.get('factor')
        if m.get('factorDataset') is not None:
            self.factor_dataset = m.get('factorDataset')
        if m.get('factorId') is not None:
            self.factor_id = m.get('factorId')
        if m.get('factorType') is not None:
            self.factor_type = m.get('factorType')
        if m.get('factorUnit') is not None:
            self.factor_unit = m.get('factorUnit')
        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')
        if m.get('inventoryUnit') is not None:
            self.inventory_unit = m.get('inventoryUnit')
        if m.get('inventoryValue') is not None:
            self.inventory_value = m.get('inventoryValue')
        if m.get('inventoryValuePerProduct') is not None:
            self.inventory_value_per_product = m.get('inventoryValuePerProduct')
        if m.get('inventoryValuePerProductUnit') is not None:
            self.inventory_value_per_product_unit = m.get('inventoryValuePerProductUnit')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = EpdInventoryConstituteItem()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GwpInventoryConstitute(TeaModel):
    def __init__(self, by_resource_type=None, carbon_emission=None, items=None, name=None, percent=None,
                 resource_type=None, unit=None):
        self.by_resource_type = by_resource_type  # type: list[GwpResourceConstitute]
        self.carbon_emission = carbon_emission  # type: float
        self.items = items  # type: list[GwpInventoryConstitute]
        self.name = name  # type: str
        self.percent = percent  # type: float
        self.resource_type = resource_type  # type: int
        self.unit = unit  # type: str

    def validate(self):
        if self.by_resource_type:
            for k in self.by_resource_type:
                if k:
                    k.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GwpInventoryConstitute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['byResourceType'] = []
        if self.by_resource_type is not None:
            for k in self.by_resource_type:
                result['byResourceType'].append(k.to_map() if k else None)
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k in m.get('byResourceType'):
                temp_model = GwpResourceConstitute()
                self.by_resource_type.append(temp_model.from_map(k))
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GwpInventoryConstitute()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GwpResourceConstitute(TeaModel):
    def __init__(self, carbon_emission=None, name=None, percent=None, resource_type=None, unit=None):
        self.carbon_emission = carbon_emission  # type: float
        self.name = name  # type: str
        self.percent = percent  # type: str
        self.resource_type = resource_type  # type: int
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GwpResourceConstitute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class OrgEmissionModuleEmissionList(TeaModel):
    def __init__(self, carbon_emission_data=None, name=None, name_key=None, ratio=None):
        self.carbon_emission_data = carbon_emission_data  # type: float
        self.name = name  # type: str
        self.name_key = name_key  # type: str
        self.ratio = ratio  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrgEmissionModuleEmissionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        return self


class OrgEmission(TeaModel):
    def __init__(self, carbon_emission_data=None, module_emission_list=None, name=None, name_key=None, ratio=None,
                 sub_emission_items=None, weighting_carbon_emission_data=None, weighting_proportion=None, weighting_ratio=None):
        self.carbon_emission_data = carbon_emission_data  # type: float
        self.module_emission_list = module_emission_list  # type: list[OrgEmissionModuleEmissionList]
        self.name = name  # type: str
        self.name_key = name_key  # type: str
        self.ratio = ratio  # type: float
        self.sub_emission_items = sub_emission_items  # type: list[OrgEmission]
        self.weighting_carbon_emission_data = weighting_carbon_emission_data  # type: float
        self.weighting_proportion = weighting_proportion  # type: float
        self.weighting_ratio = weighting_ratio  # type: float

    def validate(self):
        if self.module_emission_list:
            for k in self.module_emission_list:
                if k:
                    k.validate()
        if self.sub_emission_items:
            for k in self.sub_emission_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrgEmission, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        result['moduleEmissionList'] = []
        if self.module_emission_list is not None:
            for k in self.module_emission_list:
                result['moduleEmissionList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        result['subEmissionItems'] = []
        if self.sub_emission_items is not None:
            for k in self.sub_emission_items:
                result['subEmissionItems'].append(k.to_map() if k else None)
        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data
        if self.weighting_proportion is not None:
            result['weightingProportion'] = self.weighting_proportion
        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        self.module_emission_list = []
        if m.get('moduleEmissionList') is not None:
            for k in m.get('moduleEmissionList'):
                temp_model = OrgEmissionModuleEmissionList()
                self.module_emission_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        self.sub_emission_items = []
        if m.get('subEmissionItems') is not None:
            for k in m.get('subEmissionItems'):
                temp_model = OrgEmission()
                self.sub_emission_items.append(temp_model.from_map(k))
        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')
        if m.get('weightingProportion') is not None:
            self.weighting_proportion = m.get('weightingProportion')
        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')
        return self


class GenerateResultRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GenerateResultResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data. `true` indicates that the request is successful, `false` indicates that the request fails.
        self.data = data  # type: bool
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAreaElecConstituteRequest(TeaModel):
    def __init__(self, code=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Year.
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAreaElecConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetAreaElecConstituteResponseBodyData(TeaModel):
    def __init__(self, light=None, nuclear=None, renewing=None, urban=None, water=None, wind=None, zero=None):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light  # type: list[CarbonEmissionElecSummaryItem]
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear  # type: list[CarbonEmissionElecSummaryItem]
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing  # type: list[CarbonEmissionElecSummaryItem]
        # Data on mains electricity consumption and carbon emission of each enterprise.
        self.urban = urban  # type: list[CarbonEmissionElecSummaryItem]
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water  # type: list[CarbonEmissionElecSummaryItem]
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind  # type: list[CarbonEmissionElecSummaryItem]
        # Data of zero electricity consumption and carbon emission of each enterprise.
        self.zero = zero  # type: list[CarbonEmissionElecSummaryItem]

    def validate(self):
        if self.light:
            for k in self.light:
                if k:
                    k.validate()
        if self.nuclear:
            for k in self.nuclear:
                if k:
                    k.validate()
        if self.renewing:
            for k in self.renewing:
                if k:
                    k.validate()
        if self.urban:
            for k in self.urban:
                if k:
                    k.validate()
        if self.water:
            for k in self.water:
                if k:
                    k.validate()
        if self.wind:
            for k in self.wind:
                if k:
                    k.validate()
        if self.zero:
            for k in self.zero:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAreaElecConstituteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['light'] = []
        if self.light is not None:
            for k in self.light:
                result['light'].append(k.to_map() if k else None)
        result['nuclear'] = []
        if self.nuclear is not None:
            for k in self.nuclear:
                result['nuclear'].append(k.to_map() if k else None)
        result['renewing'] = []
        if self.renewing is not None:
            for k in self.renewing:
                result['renewing'].append(k.to_map() if k else None)
        result['urban'] = []
        if self.urban is not None:
            for k in self.urban:
                result['urban'].append(k.to_map() if k else None)
        result['water'] = []
        if self.water is not None:
            for k in self.water:
                result['water'].append(k.to_map() if k else None)
        result['wind'] = []
        if self.wind is not None:
            for k in self.wind:
                result['wind'].append(k.to_map() if k else None)
        result['zero'] = []
        if self.zero is not None:
            for k in self.zero:
                result['zero'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.light = []
        if m.get('light') is not None:
            for k in m.get('light'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.light.append(temp_model.from_map(k))
        self.nuclear = []
        if m.get('nuclear') is not None:
            for k in m.get('nuclear'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.nuclear.append(temp_model.from_map(k))
        self.renewing = []
        if m.get('renewing') is not None:
            for k in m.get('renewing'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.renewing.append(temp_model.from_map(k))
        self.urban = []
        if m.get('urban') is not None:
            for k in m.get('urban'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.urban.append(temp_model.from_map(k))
        self.water = []
        if m.get('water') is not None:
            for k in m.get('water'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.water.append(temp_model.from_map(k))
        self.wind = []
        if m.get('wind') is not None:
            for k in m.get('wind'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.wind.append(temp_model.from_map(k))
        self.zero = []
        if m.get('zero') is not None:
            for k in m.get('zero'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.zero.append(temp_model.from_map(k))
        return self


class GetAreaElecConstituteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetAreaElecConstituteResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAreaElecConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAreaElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetAreaElecConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAreaElecConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAreaElecConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAreaElecConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCarbonEmissionTrendRequest(TeaModel):
    def __init__(self, code=None, module_code=None, module_type=None, trend_type=None, year_list=None):
        # The enterprise code.
        self.code = code  # type: str
        # Module code.
        self.module_code = module_code  # type: str
        # Module type.
        self.module_type = module_type  # type: int
        # Trend Type.
        self.trend_type = trend_type  # type: int
        # The list of inventory year.
        self.year_list = year_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCarbonEmissionTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.trend_type is not None:
            result['trendType'] = self.trend_type
        if self.year_list is not None:
            result['yearList'] = self.year_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('trendType') is not None:
            self.trend_type = m.get('trendType')
        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')
        return self


class GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems(TeaModel):
    def __init__(self, carbon_emission_data=None, month=None, year=None):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The month.
        self.month = month  # type: int
        # The year.
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataActualEmissionList(TeaModel):
    def __init__(self, items=None, year=None):
        # Data item list.
        self.items = items  # type: list[GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems]
        # The year.
        self.year = year  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBodyDataActualEmissionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems(TeaModel):
    def __init__(self, carbon_emission_data=None, month=None, year=None):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The month.
        self.month = month  # type: int
        # The year.
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataTargetEmissionList(TeaModel):
    def __init__(self, items=None, year=None):
        # Data item list.
        self.items = items  # type: list[GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems]
        # The year.
        self.year = year  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBodyDataTargetEmissionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyData(TeaModel):
    def __init__(self, actual_emission_list=None, target_emission_list=None):
        # Actual emission list.
        self.actual_emission_list = actual_emission_list  # type: list[GetCarbonEmissionTrendResponseBodyDataActualEmissionList]
        # Target Emission List.
        self.target_emission_list = target_emission_list  # type: list[GetCarbonEmissionTrendResponseBodyDataTargetEmissionList]

    def validate(self):
        if self.actual_emission_list:
            for k in self.actual_emission_list:
                if k:
                    k.validate()
        if self.target_emission_list:
            for k in self.target_emission_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actualEmissionList'] = []
        if self.actual_emission_list is not None:
            for k in self.actual_emission_list:
                result['actualEmissionList'].append(k.to_map() if k else None)
        result['targetEmissionList'] = []
        if self.target_emission_list is not None:
            for k in self.target_emission_list:
                result['targetEmissionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actual_emission_list = []
        if m.get('actualEmissionList') is not None:
            for k in m.get('actualEmissionList'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataActualEmissionList()
                self.actual_emission_list.append(temp_model.from_map(k))
        self.target_emission_list = []
        if m.get('targetEmissionList') is not None:
            for k in m.get('targetEmissionList'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataTargetEmissionList()
                self.target_emission_list.append(temp_model.from_map(k))
        return self


class GetCarbonEmissionTrendResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetCarbonEmissionTrendResponseBodyData
        # Id of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetCarbonEmissionTrendResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCarbonEmissionTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCarbonEmissionTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCarbonEmissionTrendResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCarbonEmissionTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataItemListRequest(TeaModel):
    def __init__(self, code=None):
        # The enterprise code.
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataItemListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetDataItemListResponseBodyData(TeaModel):
    def __init__(self, code=None, name=None, period=None, unit=None):
        # The identifier of the data item.
        self.code = code  # type: str
        # The name of the data item.
        self.name = name  # type: str
        # Data filling method, 1: monthly value 2: annual value.
        self.period = period  # type: int
        # The data item unit.
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataItemListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetDataItemListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Response parameters.
        self.data = data  # type: list[GetDataItemListResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDataItemListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetDataItemListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataItemListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataItemListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataItemListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataQualityAnalysisRequest(TeaModel):
    def __init__(self, code=None, data_quality_evaluation_type=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # Data quality assessment type: 1 is DQI and 2 is DQR.
        self.data_quality_evaluation_type = data_quality_evaluation_type  # type: long
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataQualityAnalysisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_quality_evaluation_type is not None:
            result['dataQualityEvaluationType'] = self.data_quality_evaluation_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataQualityEvaluationType') is not None:
            self.data_quality_evaluation_type = m.get('dataQualityEvaluationType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetDataQualityAnalysisResponseBodyDataDataQualityScore(TeaModel):
    def __init__(self, g_1=None, g_2=None, g_3=None, g_4=None):
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1  # type: float
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2  # type: float
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3  # type: float
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyDataDataQualityScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.g_1 is not None:
            result['g1'] = self.g_1
        if self.g_2 is not None:
            result['g2'] = self.g_2
        if self.g_3 is not None:
            result['g3'] = self.g_3
        if self.g_4 is not None:
            result['g4'] = self.g_4
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('g1') is not None:
            self.g_1 = m.get('g1')
        if m.get('g2') is not None:
            self.g_2 = m.get('g2')
        if m.get('g3') is not None:
            self.g_3 = m.get('g3')
        if m.get('g4') is not None:
            self.g_4 = m.get('g4')
        return self


class GetDataQualityAnalysisResponseBodyDataDataQuality(TeaModel):
    def __init__(self, inventory=None, score=None):
        # Inventory name
        self.inventory = inventory  # type: str
        # Score. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality.
        self.score = score  # type: GetDataQualityAnalysisResponseBodyDataDataQualityScore

    def validate(self):
        if self.score:
            self.score.validate()

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyDataDataQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.score is not None:
            result['score'] = self.score.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('score') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyDataDataQualityScore()
            self.score = temp_model.from_map(m['score'])
        return self


class GetDataQualityAnalysisResponseBodyDataDataQualityResult(TeaModel):
    def __init__(self, data_quality_score=None, g_1=None, g_2=None, g_3=None, g_4=None):
        # The score. This parameter is applicable to DQR results. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality. The number of valid digits is kept to four decimal places.
        self.data_quality_score = data_quality_score  # type: float
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1  # type: float
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2  # type: float
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3  # type: float
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyDataDataQualityResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_quality_score is not None:
            result['data_quality_score'] = self.data_quality_score
        if self.g_1 is not None:
            result['g1'] = self.g_1
        if self.g_2 is not None:
            result['g2'] = self.g_2
        if self.g_3 is not None:
            result['g3'] = self.g_3
        if self.g_4 is not None:
            result['g4'] = self.g_4
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data_quality_score') is not None:
            self.data_quality_score = m.get('data_quality_score')
        if m.get('g1') is not None:
            self.g_1 = m.get('g1')
        if m.get('g2') is not None:
            self.g_2 = m.get('g2')
        if m.get('g3') is not None:
            self.g_3 = m.get('g3')
        if m.get('g4') is not None:
            self.g_4 = m.get('g4')
        return self


class GetDataQualityAnalysisResponseBodyDataSensitivityList(TeaModel):
    def __init__(self, id=None, inventory=None, reduction_list=None, sensitivity=None):
        # Inventory id
        self.id = id  # type: str
        # Name of the inventory item.
        self.inventory = inventory  # type: str
        # List of emission reduction measures.
        self.reduction_list = reduction_list  # type: list[str]
        # Sensitivity percentage.
        self.sensitivity = sensitivity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyDataSensitivityList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.reduction_list is not None:
            result['reductionList'] = self.reduction_list
        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('reductionList') is not None:
            self.reduction_list = m.get('reductionList')
        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')
        return self


class GetDataQualityAnalysisResponseBodyDataUncertaintyValues(TeaModel):
    def __init__(self, inventory=None, uncertainty_contribution=None):
        # The name of the inventory. Format: process name / inventory name.
        self.inventory = inventory  # type: str
        # Inventory uncertainty absolute contribution size. The impact of the quality of each inventory data on the carbon footprint results in the modeling process, when the uncertain contribution of a list is large, please improve its data quality as much as possible to improve the accuracy of carbon footprint analysis. The meaning of "1.4964" is not determined to contribute 1.4964 kgCO₂ e/unit, where unit is the unit of the product.
        self.uncertainty_contribution = uncertainty_contribution  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyDataUncertaintyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.uncertainty_contribution is not None:
            result['uncertaintyContribution'] = self.uncertainty_contribution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('uncertaintyContribution') is not None:
            self.uncertainty_contribution = m.get('uncertaintyContribution')
        return self


class GetDataQualityAnalysisResponseBodyData(TeaModel):
    def __init__(self, data_quality=None, data_quality_result=None, sensitivity_list=None, uncertainty=None,
                 uncertainty_values=None):
        # Score of each inventory.
        self.data_quality = data_quality  # type: list[GetDataQualityAnalysisResponseBodyDataDataQuality]
        # Data quality result.
        self.data_quality_result = data_quality_result  # type: GetDataQualityAnalysisResponseBodyDataDataQualityResult
        # Sensitivity analysis list
        self.sensitivity_list = sensitivity_list  # type: list[GetDataQualityAnalysisResponseBodyDataSensitivityList]
        # Uncertainty value. The model\"s overall percentage uncertainty results. "10.00%" symbolizes a 10.00% uncertainty, indicating that the carbon footprint lies within ±10.00%. This is derived from a weighted aggregation of individual inventory uncertainties.
        self.uncertainty = uncertainty  # type: str
        # Uncertainty list
        self.uncertainty_values = uncertainty_values  # type: list[GetDataQualityAnalysisResponseBodyDataUncertaintyValues]

    def validate(self):
        if self.data_quality:
            for k in self.data_quality:
                if k:
                    k.validate()
        if self.data_quality_result:
            self.data_quality_result.validate()
        if self.sensitivity_list:
            for k in self.sensitivity_list:
                if k:
                    k.validate()
        if self.uncertainty_values:
            for k in self.uncertainty_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataQuality'] = []
        if self.data_quality is not None:
            for k in self.data_quality:
                result['dataQuality'].append(k.to_map() if k else None)
        if self.data_quality_result is not None:
            result['dataQualityResult'] = self.data_quality_result.to_map()
        result['sensitivityList'] = []
        if self.sensitivity_list is not None:
            for k in self.sensitivity_list:
                result['sensitivityList'].append(k.to_map() if k else None)
        if self.uncertainty is not None:
            result['uncertainty'] = self.uncertainty
        result['uncertaintyValues'] = []
        if self.uncertainty_values is not None:
            for k in self.uncertainty_values:
                result['uncertaintyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_quality = []
        if m.get('dataQuality') is not None:
            for k in m.get('dataQuality'):
                temp_model = GetDataQualityAnalysisResponseBodyDataDataQuality()
                self.data_quality.append(temp_model.from_map(k))
        if m.get('dataQualityResult') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyDataDataQualityResult()
            self.data_quality_result = temp_model.from_map(m['dataQualityResult'])
        self.sensitivity_list = []
        if m.get('sensitivityList') is not None:
            for k in m.get('sensitivityList'):
                temp_model = GetDataQualityAnalysisResponseBodyDataSensitivityList()
                self.sensitivity_list.append(temp_model.from_map(k))
        if m.get('uncertainty') is not None:
            self.uncertainty = m.get('uncertainty')
        self.uncertainty_values = []
        if m.get('uncertaintyValues') is not None:
            for k in m.get('uncertaintyValues'):
                temp_model = GetDataQualityAnalysisResponseBodyDataUncertaintyValues()
                self.uncertainty_values.append(temp_model.from_map(k))
        return self


class GetDataQualityAnalysisResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetDataQualityAnalysisResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataQualityAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataQualityAnalysisResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataQualityAnalysisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataQualityAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceInfoRequest(TeaModel):
    def __init__(self, device_id=None, ds=None, factory_id=None):
        # The ID of the device.
        self.device_id = device_id  # type: str
        # The date on which the statistics are collected.
        self.ds = ds  # type: str
        # The ID of the site.
        self.factory_id = factory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.ds is not None:
            result['ds'] = self.ds
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceInfoResponseBodyDataRecordList(TeaModel):
    def __init__(self, identifier=None, param_name=None, statistics_date=None, type=None, unit=None, value=None):
        # The identifier of the device.
        self.identifier = identifier  # type: str
        # The name of the parameter.
        self.param_name = param_name  # type: str
        # The date on which the statistics were collected.
        self.statistics_date = statistics_date  # type: str
        # The type of the measuring point.
        self.type = type  # type: str
        # The unit of the parameter value.
        self.unit = unit  # type: str
        # The value of the measuring point.
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceInfoResponseBodyDataRecordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.statistics_date is not None:
            result['statisticsDate'] = self.statistics_date
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('statisticsDate') is not None:
            self.statistics_date = m.get('statisticsDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetDeviceInfoResponseBodyData(TeaModel):
    def __init__(self, device_id=None, device_name=None, first_type_name=None, record_list=None,
                 second_type_name=None):
        # The ID of the device.
        self.device_id = device_id  # type: str
        # The name of the device.
        self.device_name = device_name  # type: str
        # The level 1 meter type.
        self.first_type_name = first_type_name  # type: str
        # The device parameters.
        self.record_list = record_list  # type: list[GetDeviceInfoResponseBodyDataRecordList]
        # The level 2 meter type.
        self.second_type_name = second_type_name  # type: str

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        result['recordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['recordList'].append(k.to_map() if k else None)
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        self.record_list = []
        if m.get('recordList') is not None:
            for k in m.get('recordList'):
                temp_model = GetDeviceInfoResponseBodyDataRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetDeviceInfoResponseBodyData
        # The HTTP status code.
        self.http_code = http_code  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceListRequest(TeaModel):
    def __init__(self, factory_id=None):
        # The ID of the site.
        self.factory_id = factory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceListResponseBodyDataDeviceListInfo(TeaModel):
    def __init__(self, const_kva=None, ct=None, magnification=None, pressure=None, pt=None):
        # The rated capacity.
        self.const_kva = const_kva  # type: int
        # The transformation ratio of current.
        self.ct = ct  # type: int
        # The magnification ratio.
        self.magnification = magnification  # type: int
        # The high and low voltage.
        self.pressure = pressure  # type: int
        # The transformation ratio of voltage.
        self.pt = pt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceListResponseBodyDataDeviceListInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.const_kva is not None:
            result['constKva'] = self.const_kva
        if self.ct is not None:
            result['ct'] = self.ct
        if self.magnification is not None:
            result['magnification'] = self.magnification
        if self.pressure is not None:
            result['pressure'] = self.pressure
        if self.pt is not None:
            result['pt'] = self.pt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('constKva') is not None:
            self.const_kva = m.get('constKva')
        if m.get('ct') is not None:
            self.ct = m.get('ct')
        if m.get('magnification') is not None:
            self.magnification = m.get('magnification')
        if m.get('pressure') is not None:
            self.pressure = m.get('pressure')
        if m.get('pt') is not None:
            self.pt = m.get('pt')
        return self


class GetDeviceListResponseBodyDataDeviceList(TeaModel):
    def __init__(self, device_id=None, device_name=None, first_type_name=None, info=None, parent_device=None,
                 second_type_name=None):
        # The ID of the device.
        self.device_id = device_id  # type: str
        # The name of the device.
        self.device_name = device_name  # type: str
        # The level 1 meter type.
        self.first_type_name = first_type_name  # type: str
        # The information about the device.
        self.info = info  # type: GetDeviceListResponseBodyDataDeviceListInfo
        # The ID of the parent device.
        self.parent_device = parent_device  # type: str
        # The level 2 meter type.
        self.second_type_name = second_type_name  # type: str

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBodyDataDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.parent_device is not None:
            result['parentDevice'] = self.parent_device
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        if m.get('info') is not None:
            temp_model = GetDeviceListResponseBodyDataDeviceListInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('parentDevice') is not None:
            self.parent_device = m.get('parentDevice')
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceListResponseBodyData(TeaModel):
    def __init__(self, code=None, device_list=None, factory_id=None, http_code=None, success=None):
        # The code returned for the request.
        self.code = code  # type: str
        # The devices.
        self.device_list = device_list  # type: list[GetDeviceListResponseBodyDataDeviceList]
        # The ID of the site.
        self.factory_id = factory_id  # type: str
        # The HTTP status code.
        self.http_code = http_code  # type: int
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['deviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['deviceList'].append(k.to_map() if k else None)
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.device_list = []
        if m.get('deviceList') is not None:
            for k in m.get('deviceList'):
                temp_model = GetDeviceListResponseBodyDataDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        # The code returned for the request.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetDeviceListResponseBodyData
        # The HTTP status code.
        self.http_code = http_code  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElecConstituteRequest(TeaModel):
    def __init__(self, code=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Year.
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecConstituteResponseBodyDataLight(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataLight, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataNuclear(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataNuclear, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataRenewing(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataRenewing, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataUrban(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataUrban, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataWater(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataWater, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataWind(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataWind, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataZero(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, name=None, name_key=None, ratio=None,
                 raw_data=None):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # The name.
        self.name = name  # type: str
        # The unique identifier of name.
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyDataZero, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyData(TeaModel):
    def __init__(self, light=None, nuclear=None, renewing=None, urban=None, water=None, wind=None, zero=None):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light  # type: GetElecConstituteResponseBodyDataLight
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear  # type: GetElecConstituteResponseBodyDataNuclear
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing  # type: GetElecConstituteResponseBodyDataRenewing
        # Data on mains power electricity consumption and carbon emission of each enterprise.
        self.urban = urban  # type: GetElecConstituteResponseBodyDataUrban
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water  # type: GetElecConstituteResponseBodyDataWater
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind  # type: GetElecConstituteResponseBodyDataWind
        # Data of zero electricity consumption and carbon emission of each enterprise.
        self.zero = zero  # type: GetElecConstituteResponseBodyDataZero

    def validate(self):
        if self.light:
            self.light.validate()
        if self.nuclear:
            self.nuclear.validate()
        if self.renewing:
            self.renewing.validate()
        if self.urban:
            self.urban.validate()
        if self.water:
            self.water.validate()
        if self.wind:
            self.wind.validate()
        if self.zero:
            self.zero.validate()

    def to_map(self):
        _map = super(GetElecConstituteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.light is not None:
            result['light'] = self.light.to_map()
        if self.nuclear is not None:
            result['nuclear'] = self.nuclear.to_map()
        if self.renewing is not None:
            result['renewing'] = self.renewing.to_map()
        if self.urban is not None:
            result['urban'] = self.urban.to_map()
        if self.water is not None:
            result['water'] = self.water.to_map()
        if self.wind is not None:
            result['wind'] = self.wind.to_map()
        if self.zero is not None:
            result['zero'] = self.zero.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('light') is not None:
            temp_model = GetElecConstituteResponseBodyDataLight()
            self.light = temp_model.from_map(m['light'])
        if m.get('nuclear') is not None:
            temp_model = GetElecConstituteResponseBodyDataNuclear()
            self.nuclear = temp_model.from_map(m['nuclear'])
        if m.get('renewing') is not None:
            temp_model = GetElecConstituteResponseBodyDataRenewing()
            self.renewing = temp_model.from_map(m['renewing'])
        if m.get('urban') is not None:
            temp_model = GetElecConstituteResponseBodyDataUrban()
            self.urban = temp_model.from_map(m['urban'])
        if m.get('water') is not None:
            temp_model = GetElecConstituteResponseBodyDataWater()
            self.water = temp_model.from_map(m['water'])
        if m.get('wind') is not None:
            temp_model = GetElecConstituteResponseBodyDataWind()
            self.wind = temp_model.from_map(m['wind'])
        if m.get('zero') is not None:
            temp_model = GetElecConstituteResponseBodyDataZero()
            self.zero = temp_model.from_map(m['zero'])
        return self


class GetElecConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: GetElecConstituteResponseBodyData
        # Id of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetElecConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetElecConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetElecConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetElecConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetElecConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElecTrendRequest(TeaModel):
    def __init__(self, code=None, year_list=None):
        # The enterprise code.
        self.code = code  # type: str
        # List of years.
        self.year_list = year_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year_list is not None:
            result['yearList'] = self.year_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')
        return self


class GetElecTrendResponseBodyDataLight(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power type name.
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataLight, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataNuclear(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The price unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataNuclear, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataRenewing(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The price unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataRenewing, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataUrban(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The price unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataUrban, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataWater(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataWater, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataWind(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The price unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataWind, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataZero(TeaModel):
    def __init__(self, carbon_emission_data=None, data_unit=None, month=None, name=None, name_key=None, ratio=None,
                 raw_data=None, year=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # The price unit.
        self.data_unit = data_unit  # type: str
        # Month
        self.month = month  # type: int
        # Power Type Name
        self.name = name  # type: str
        # Power Type Code
        self.name_key = name_key  # type: str
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio  # type: float
        # Electricity consumption
        self.raw_data = raw_data  # type: float
        # Year
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElecTrendResponseBodyDataZero, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyData(TeaModel):
    def __init__(self, light=None, nuclear=None, renewing=None, urban=None, water=None, wind=None, zero=None):
        # Photoelectricity monthly electricity consumption and carbon emissions and other data.
        self.light = light  # type: list[GetElecTrendResponseBodyDataLight]
        # Monthly electricity consumption and carbon emissions data for nuclear power
        self.nuclear = nuclear  # type: list[GetElecTrendResponseBodyDataNuclear]
        # Monthly data on renewable electricity consumption and carbon emissions
        self.renewing = renewing  # type: list[GetElecTrendResponseBodyDataRenewing]
        # Data such as monthly electricity consumption and carbon emissions from the mains.
        self.urban = urban  # type: list[GetElecTrendResponseBodyDataUrban]
        # Monthly data on electricity consumption and carbon emissions for hydropower.
        self.water = water  # type: list[GetElecTrendResponseBodyDataWater]
        # Monthly wind power consumption and carbon emission data
        self.wind = wind  # type: list[GetElecTrendResponseBodyDataWind]
        # Zero electricity monthly electricity consumption and carbon emissions and other data.
        self.zero = zero  # type: list[GetElecTrendResponseBodyDataZero]

    def validate(self):
        if self.light:
            for k in self.light:
                if k:
                    k.validate()
        if self.nuclear:
            for k in self.nuclear:
                if k:
                    k.validate()
        if self.renewing:
            for k in self.renewing:
                if k:
                    k.validate()
        if self.urban:
            for k in self.urban:
                if k:
                    k.validate()
        if self.water:
            for k in self.water:
                if k:
                    k.validate()
        if self.wind:
            for k in self.wind:
                if k:
                    k.validate()
        if self.zero:
            for k in self.zero:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetElecTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['light'] = []
        if self.light is not None:
            for k in self.light:
                result['light'].append(k.to_map() if k else None)
        result['nuclear'] = []
        if self.nuclear is not None:
            for k in self.nuclear:
                result['nuclear'].append(k.to_map() if k else None)
        result['renewing'] = []
        if self.renewing is not None:
            for k in self.renewing:
                result['renewing'].append(k.to_map() if k else None)
        result['urban'] = []
        if self.urban is not None:
            for k in self.urban:
                result['urban'].append(k.to_map() if k else None)
        result['water'] = []
        if self.water is not None:
            for k in self.water:
                result['water'].append(k.to_map() if k else None)
        result['wind'] = []
        if self.wind is not None:
            for k in self.wind:
                result['wind'].append(k.to_map() if k else None)
        result['zero'] = []
        if self.zero is not None:
            for k in self.zero:
                result['zero'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.light = []
        if m.get('light') is not None:
            for k in m.get('light'):
                temp_model = GetElecTrendResponseBodyDataLight()
                self.light.append(temp_model.from_map(k))
        self.nuclear = []
        if m.get('nuclear') is not None:
            for k in m.get('nuclear'):
                temp_model = GetElecTrendResponseBodyDataNuclear()
                self.nuclear.append(temp_model.from_map(k))
        self.renewing = []
        if m.get('renewing') is not None:
            for k in m.get('renewing'):
                temp_model = GetElecTrendResponseBodyDataRenewing()
                self.renewing.append(temp_model.from_map(k))
        self.urban = []
        if m.get('urban') is not None:
            for k in m.get('urban'):
                temp_model = GetElecTrendResponseBodyDataUrban()
                self.urban.append(temp_model.from_map(k))
        self.water = []
        if m.get('water') is not None:
            for k in m.get('water'):
                temp_model = GetElecTrendResponseBodyDataWater()
                self.water.append(temp_model.from_map(k))
        self.wind = []
        if m.get('wind') is not None:
            for k in m.get('wind'):
                temp_model = GetElecTrendResponseBodyDataWind()
                self.wind.append(temp_model.from_map(k))
        self.zero = []
        if m.get('zero') is not None:
            for k in m.get('zero'):
                temp_model = GetElecTrendResponseBodyDataZero()
                self.zero.append(temp_model.from_map(k))
        return self


class GetElecTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetElecTrendResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetElecTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetElecTrendResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetElecTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetElecTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetElecTrendResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetElecTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmissionSourceConstituteRequest(TeaModel):
    def __init__(self, code=None, module_code=None, module_type=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Module code.
        self.module_code = module_code  # type: str
        # Module type.
        self.module_type = module_type  # type: int
        # Year of inventory.
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmissionSourceConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetEmissionSourceConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Response parameters
        self.data = data  # type: list[ConstituteItem]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEmissionSourceConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ConstituteItem()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEmissionSourceConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEmissionSourceConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmissionSourceConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEmissionSourceConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmissionSummaryRequest(TeaModel):
    def __init__(self, code=None, module_code=None, module_type=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Module code.
        self.module_code = module_code  # type: str
        # Module type.
        self.module_type = module_type  # type: int
        # Year of inventory.
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmissionSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetEmissionSummaryResponseBodyData(TeaModel):
    def __init__(self, actual_emission_ratio=None, carbon_save_conversion=None,
                 current_period_carbon_emission_data=None, is_weighting=None, last_period_carbon_emission_data=None,
                 last_period_weighting_carbon_emission_data=None, ratio=None, total_carbon_emission_data=None, weighting_carbon_emission_data=None,
                 weighting_ratio=None):
        # Percentage of scheduled.
        self.actual_emission_ratio = actual_emission_ratio  # type: float
        # Carbon emissions reduction.
        self.carbon_save_conversion = carbon_save_conversion  # type: float
        # Statistical indicators for this cycle.
        self.current_period_carbon_emission_data = current_period_carbon_emission_data  # type: float
        # Whether to show the weighting ratio carbon emission.
        self.is_weighting = is_weighting  # type: bool
        # Last period statistical indicators.
        self.last_period_carbon_emission_data = last_period_carbon_emission_data  # type: float
        # Calculation of carbon emissions based on shareholding ratio in the last cycle.
        self.last_period_weighting_carbon_emission_data = last_period_weighting_carbon_emission_data  # type: float
        # Year-on-year.
        self.ratio = ratio  # type: float
        # Total carbon emissions.
        self.total_carbon_emission_data = total_carbon_emission_data  # type: float
        # Calculate carbon emissions by share ratio
        self.weighting_carbon_emission_data = weighting_carbon_emission_data  # type: float
        # Year-on-year of weighting ratio carbon emissions.
        self.weighting_ratio = weighting_ratio  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmissionSummaryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_emission_ratio is not None:
            result['actualEmissionRatio'] = self.actual_emission_ratio
        if self.carbon_save_conversion is not None:
            result['carbonSaveConversion'] = self.carbon_save_conversion
        if self.current_period_carbon_emission_data is not None:
            result['currentPeriodCarbonEmissionData'] = self.current_period_carbon_emission_data
        if self.is_weighting is not None:
            result['isWeighting'] = self.is_weighting
        if self.last_period_carbon_emission_data is not None:
            result['lastPeriodCarbonEmissionData'] = self.last_period_carbon_emission_data
        if self.last_period_weighting_carbon_emission_data is not None:
            result['lastPeriodWeightingCarbonEmissionData'] = self.last_period_weighting_carbon_emission_data
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.total_carbon_emission_data is not None:
            result['totalCarbonEmissionData'] = self.total_carbon_emission_data
        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data
        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actualEmissionRatio') is not None:
            self.actual_emission_ratio = m.get('actualEmissionRatio')
        if m.get('carbonSaveConversion') is not None:
            self.carbon_save_conversion = m.get('carbonSaveConversion')
        if m.get('currentPeriodCarbonEmissionData') is not None:
            self.current_period_carbon_emission_data = m.get('currentPeriodCarbonEmissionData')
        if m.get('isWeighting') is not None:
            self.is_weighting = m.get('isWeighting')
        if m.get('lastPeriodCarbonEmissionData') is not None:
            self.last_period_carbon_emission_data = m.get('lastPeriodCarbonEmissionData')
        if m.get('lastPeriodWeightingCarbonEmissionData') is not None:
            self.last_period_weighting_carbon_emission_data = m.get('lastPeriodWeightingCarbonEmissionData')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('totalCarbonEmissionData') is not None:
            self.total_carbon_emission_data = m.get('totalCarbonEmissionData')
        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')
        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')
        return self


class GetEmissionSummaryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Details of summarized data
        self.data = data  # type: GetEmissionSummaryResponseBodyData
        # Id of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEmissionSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEmissionSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEmissionSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEmissionSummaryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmissionSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEmissionSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEpdInventoryConstituteRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEpdInventoryConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetEpdInventoryConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # List of environmental impact results.
        self.data = data  # type: list[EpdInventoryConstituteItem]
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEpdInventoryConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = EpdInventoryConstituteItem()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEpdInventoryConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEpdInventoryConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEpdInventoryConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEpdInventoryConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEpdSummaryRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEpdSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetEpdSummaryResponseBodyData(TeaModel):
    def __init__(self, carbon_emission=None, indicator=None, key=None, method=None, name=None, num=None,
                 pre_unit=None, state=None):
        # Emissions. The result is maintained up to 31 decimal places for precise intermediate calculation and subsequently truncated for display. It is advised to pair the emissions figure with the unit of the environmental impact result for a comprehensive understanding.
        self.carbon_emission = carbon_emission  # type: float
        # The evaluation index adopted for the environmental impact
        self.indicator = indicator  # type: str
        # The category key. The environmental impact category. Currently, a maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.key = key  # type: str
        # Calculation method standard
        self.method = method  # type: str
        # The name of the category.
        self.name = name  # type: str
        # Category num: the unique serial number of the environmental impact category. A maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.num = num  # type: long
        # Environmental impact result Value Unit.
        self.pre_unit = pre_unit  # type: str
        # The data status. 1 indicates that the calculation is accurate, 2 indicates that the default data is used, and 3 indicates that the missing factor uses the value of 0.
        self.state = state  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEpdSummaryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.indicator is not None:
            result['indicator'] = self.indicator
        if self.key is not None:
            result['key'] = self.key
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.num is not None:
            result['num'] = self.num
        if self.pre_unit is not None:
            result['preUnit'] = self.pre_unit
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('indicator') is not None:
            self.indicator = m.get('indicator')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('preUnit') is not None:
            self.pre_unit = m.get('preUnit')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class GetEpdSummaryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Response parameters
        self.data = data  # type: list[GetEpdSummaryResponseBodyData]
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEpdSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetEpdSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEpdSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEpdSummaryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEpdSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEpdSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFootprintListRequest(TeaModel):
    def __init__(self, code=None, current_page=None, page_size=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The pagination parameter. The number of the page that starts from 1.
        self.current_page = current_page  # type: long
        # The number of entries returned on each page.
        self.page_size = page_size  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFootprintListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetFootprintListResponseBodyDataRecords(TeaModel):
    def __init__(self, amount=None, auth_status=None, check_end_time=None, check_start_time=None, code=None,
                 created_by=None, id=None, is_demo_model=None, life_cycle=None, life_cycle_type=None, name=None, type=None,
                 unit=None):
        # The amount of the product.
        self.amount = amount  # type: float
        # Authentication status enumeration value, please refer to [link](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.auth_status = auth_status  # type: long
        # Calculation end time.
        self.check_end_time = check_end_time  # type: str
        # Calculation start time.
        self.check_start_time = check_start_time  # type: str
        # The enterprise code.
        self.code = code  # type: str
        # The user who created it.
        self.created_by = created_by  # type: str
        # The product ID.
        self.id = id  # type: long
        # Indicates whether the demo model is a built-in model. A value of 1 indicates a true value and a value of 0 indicates a false value.
        self.is_demo_model = is_demo_model  # type: long
        # The literal expression corresponding to lifeCycleType, `From Cradle to Gate` and `From Cradle to Grave`.
        self.life_cycle = life_cycle  # type: str
        # 1 is `From Cradle to Gate`, and 2 is `From Cradle to Grave`.
        self.life_cycle_type = life_cycle_type  # type: long
        # The product name.
        self.name = name  # type: str
        # Product category enumeration value, please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.type = type  # type: str
        # Unit enumeration value. Please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFootprintListResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.auth_status is not None:
            result['authStatus'] = self.auth_status
        if self.check_end_time is not None:
            result['checkEndTime'] = self.check_end_time
        if self.check_start_time is not None:
            result['checkStartTime'] = self.check_start_time
        if self.code is not None:
            result['code'] = self.code
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.is_demo_model is not None:
            result['isDemoModel'] = self.is_demo_model
        if self.life_cycle is not None:
            result['lifeCycle'] = self.life_cycle
        if self.life_cycle_type is not None:
            result['lifeCycleType'] = self.life_cycle_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('authStatus') is not None:
            self.auth_status = m.get('authStatus')
        if m.get('checkEndTime') is not None:
            self.check_end_time = m.get('checkEndTime')
        if m.get('checkStartTime') is not None:
            self.check_start_time = m.get('checkStartTime')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDemoModel') is not None:
            self.is_demo_model = m.get('isDemoModel')
        if m.get('lifeCycle') is not None:
            self.life_cycle = m.get('lifeCycle')
        if m.get('lifeCycleType') is not None:
            self.life_cycle_type = m.get('lifeCycleType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetFootprintListResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_size=None, records=None, total=None, total_page=None):
        # The page number.
        self.current_page = current_page  # type: long
        # The number of entries returned on each page.
        self.page_size = page_size  # type: long
        # Product Detail List.
        self.records = records  # type: list[GetFootprintListResponseBodyDataRecords]
        # The total number of entries returned.
        self.total = total  # type: long
        # Total Pages
        self.total_page = total_page  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFootprintListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        if self.total_page is not None:
            result['totalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetFootprintListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')
        return self


class GetFootprintListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetFootprintListResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFootprintListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetFootprintListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetFootprintListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFootprintListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFootprintListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFootprintListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGasConstituteRequest(TeaModel):
    def __init__(self, code=None, module_code=None, module_type=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Module code.
        self.module_code = module_code  # type: str
        # Module type.
        self.module_type = module_type  # type: int
        # Year
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGasConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetGasConstituteResponseBodyData(TeaModel):
    def __init__(self, carbon_emission_data=None, gas_emission_data=None, name=None, ratio=None, type=None):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data  # type: float
        # Gas emissions
        self.gas_emission_data = gas_emission_data  # type: float
        # Name of gas
        self.name = name  # type: str
        # Proportion of carbon emissions. Example value: 0.5 (50%)
        self.ratio = ratio  # type: float
        # Gas Type
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGasConstituteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.gas_emission_data is not None:
            result['gasEmissionData'] = self.gas_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('gasEmissionData') is not None:
            self.gas_emission_data = m.get('gasEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetGasConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[GetGasConstituteResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGasConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetGasConstituteResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGasConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGasConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGasConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGasConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpBenchmarkListRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpBenchmarkListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpBenchmarkListResponseBodyDataItems(TeaModel):
    def __init__(self, active_reduction=None, benchmark_emission=None, benchmark_name=None, carbon_emission=None,
                 name=None, percent=None):
        # `activeReduction=benchmarkEmission-carbonEmission` Generally, baseline emissions are greater than inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.active_reduction = active_reduction  # type: float
        # Benchmark emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.benchmark_emission = benchmark_emission  # type: float
        # Benchmark name
        self.benchmark_name = benchmark_name  # type: str
        # Inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.carbon_emission = carbon_emission  # type: float
        # name
        self.name = name  # type: str
        # Unused temporarily.
        self.percent = percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpBenchmarkListResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_reduction is not None:
            result['activeReduction'] = self.active_reduction
        if self.benchmark_emission is not None:
            result['benchmarkEmission'] = self.benchmark_emission
        if self.benchmark_name is not None:
            result['benchmarkName'] = self.benchmark_name
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('activeReduction') is not None:
            self.active_reduction = m.get('activeReduction')
        if m.get('benchmarkEmission') is not None:
            self.benchmark_emission = m.get('benchmarkEmission')
        if m.get('benchmarkName') is not None:
            self.benchmark_name = m.get('benchmarkName')
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class GetGwpBenchmarkListResponseBodyData(TeaModel):
    def __init__(self, items=None, unit=None):
        # Active carbon reduction ranking list.
        self.items = items  # type: list[GetGwpBenchmarkListResponseBodyDataItems]
        # unit of emissions. The default value is `kgCO₂e/productUnit`. 
        # The `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpBenchmarkListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetGwpBenchmarkListResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpBenchmarkListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpBenchmarkListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGwpBenchmarkListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpBenchmarkListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpBenchmarkSummaryRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpBenchmarkSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpBenchmarkSummaryResponseBodyDataItems(TeaModel):
    def __init__(self, name=None, percent=None, quantity=None, unit=None):
        # Name of carbon reduction details.
        self.name = name  # type: str
        # Percentage of emissions. The value is of the string type. Two decimal places are reserved for numbers. For example, "99.01" indicates the 99.01% of this type of emissions to the total emissions. Note that the returned string itself does not contain a percent sign.
        self.percent = percent  # type: str
        # Emission amount is presented with four decimal places. Normally, modeling doesn\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity  # type: long
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpBenchmarkSummaryResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkSummaryResponseBodyData(TeaModel):
    def __init__(self, items=None, quantity=None, unit=None):
        # Carbon Reduction Contribution Top4 Details.
        self.items = items  # type: list[GetGwpBenchmarkSummaryResponseBodyDataItems]
        # Emission amount is presented with four decimal places. Normally, modeling doesn\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity  # type: long
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkSummaryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpBenchmarkSummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkSummaryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetGwpBenchmarkSummaryResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpBenchmarkSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpBenchmarkSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGwpBenchmarkSummaryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGwpBenchmarkSummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpBenchmarkSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpInventoryConstituteRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpInventoryConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpInventoryConstituteResponseBodyData(TeaModel):
    def __init__(self, by_resource_type=None, carbon_emission=None, items=None, name=None, unit=None):
        # Aggregated by resource type of an inventory.
        self.by_resource_type = by_resource_type  # type: list[GwpInventoryConstitute]
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission  # type: float
        # Organized by hierarchy from high to low, according to the flow-> process-> inventory hierarchy.
        self.items = items  # type: list[GwpInventoryConstitute]
        # The name.
        self.name = name  # type: str
        # Emission Unit.
        self.unit = unit  # type: str

    def validate(self):
        if self.by_resource_type:
            for k in self.by_resource_type:
                if k:
                    k.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGwpInventoryConstituteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['byResourceType'] = []
        if self.by_resource_type is not None:
            for k in self.by_resource_type:
                result['byResourceType'].append(k.to_map() if k else None)
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k in m.get('byResourceType'):
                temp_model = GwpInventoryConstitute()
                self.by_resource_type.append(temp_model.from_map(k))
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GwpInventoryConstitute()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventoryConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetGwpInventoryConstituteResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGwpInventoryConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpInventoryConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpInventoryConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGwpInventoryConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGwpInventoryConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpInventoryConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpInventorySummaryRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpInventorySummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpInventorySummaryResponseBodyDataItems(TeaModel):
    def __init__(self, name=None, percent=None, quantity=None, unit=None):
        # Inventory resource type name.
        self.name = name  # type: str
        # Percentage.
        self.percent = percent  # type: str
        # Quantity.
        self.quantity = quantity  # type: float
        # The unit.
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGwpInventorySummaryResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventorySummaryResponseBodyData(TeaModel):
    def __init__(self, items=None, quantity=None, result_generate_time=None, unit=None):
        # Top 4 types of carbon footprint contribution.
        self.items = items  # type: list[GetGwpInventorySummaryResponseBodyDataItems]
        # The emission quantity.
        self.quantity = quantity  # type: float
        # The time when the result was generated, in the millisecond timestamp format.
        self.result_generate_time = result_generate_time  # type: long
        # Emission Unit.
        self.unit = unit  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGwpInventorySummaryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.result_generate_time is not None:
            result['resultGenerateTime'] = self.result_generate_time
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpInventorySummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('resultGenerateTime') is not None:
            self.result_generate_time = m.get('resultGenerateTime')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventorySummaryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned results.
        self.data = data  # type: GetGwpInventorySummaryResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGwpInventorySummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpInventorySummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpInventorySummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGwpInventorySummaryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGwpInventorySummaryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpInventorySummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventoryListRequest(TeaModel):
    def __init__(self, code=None, emission_type=None, group=None, method_type=None, product_id=None,
                 product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # Type of emission
        # 
        # >  Valid values: footprint | emission. Meaning: footprint: all inventories are involved in the calculation; emission: only inventories with positive and zero emissions are involved in the calculation, and negative numbers are not involved in the calculation.
        self.emission_type = emission_type  # type: str
        # Group by
        # 
        # >  Valid values: resource | process | resourceType | processType. Meaning: resource: aggregation by inventory group, process: aggregation by operation group, resourceType: aggregation by inventory type, processType: aggregation by phase group
        self.group = group  # type: str
        # The type of the obtained environmental impact: gwp indicates the carbon footprint of climate change. For more information, see the type value of the enumerated values.
        self.method_type = method_type  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInventoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.emission_type is not None:
            result['emissionType'] = self.emission_type
        if self.group is not None:
            result['group'] = self.group
        if self.method_type is not None:
            result['methodType'] = self.method_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('emissionType') is not None:
            self.emission_type = m.get('emissionType')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('methodType') is not None:
            self.method_type = m.get('methodType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetInventoryListResponseBodyDataItems(TeaModel):
    def __init__(self, carbon_emission=None, name=None, percent=None, process_name=None):
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission  # type: float
        # Name 
        # 
        # > The name is related to the request parameters group. Request parameters: resource, return name parameter meaning: list name; request parameters: process, return name parameter meaning: process name; request parameters: resourceType, return name parameter meaning: inventory resource type name; request parameters: processType, return name parameter meaning: flow name.
        self.name = name  # type: str
        # Percentage
        self.percent = percent  # type: str
        # Process Name: It is only meaningful when the request parameters group is resource.
        self.process_name = process_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInventoryListResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.process_name is not None:
            result['processName'] = self.process_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        return self


class GetInventoryListResponseBodyData(TeaModel):
    def __init__(self, items=None, product_unit=None, unit=None):
        # Inventory detail.
        self.items = items  # type: list[GetInventoryListResponseBodyDataItems]
        # Unit of product.
        self.product_unit = product_unit  # type: str
        # Emission Unit: The default value is kgCO₂ /productUnit. productUnit is the unit selected for the product. The unit value is changed to tCO₂ e/productUnit or gCO₂ e/productUnit based on the emission quantity. For more information, see the quantity column.
        self.unit = unit  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInventoryListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.product_unit is not None:
            result['productUnit'] = self.product_unit
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetInventoryListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('productUnit') is not None:
            self.product_unit = m.get('productUnit')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetInventoryListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetInventoryListResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInventoryListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetInventoryListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetInventoryListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInventoryListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInventoryListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInventoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgAndFactoryResponseBodyDataFactoryList(TeaModel):
    def __init__(self, factory_id=None, factory_name=None):
        # The ID of the site.
        self.factory_id = factory_id  # type: str
        # The name of the site.
        self.factory_name = factory_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBodyDataFactoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.factory_name is not None:
            result['factoryName'] = self.factory_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('factoryName') is not None:
            self.factory_name = m.get('factoryName')
        return self


class GetOrgAndFactoryResponseBodyData(TeaModel):
    def __init__(self, aliyun_pk=None, factory_list=None, organization_id=None, organization_name=None):
        # The ID of the Alibaba Cloud account.
        self.aliyun_pk = aliyun_pk  # type: str
        # The sites.
        self.factory_list = factory_list  # type: list[GetOrgAndFactoryResponseBodyDataFactoryList]
        # The ID of the organization.
        self.organization_id = organization_id  # type: str
        # The name of the organization.
        self.organization_name = organization_name  # type: str

    def validate(self):
        if self.factory_list:
            for k in self.factory_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_pk is not None:
            result['aliyunPk'] = self.aliyun_pk
        result['factoryList'] = []
        if self.factory_list is not None:
            for k in self.factory_list:
                result['factoryList'].append(k.to_map() if k else None)
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.organization_name is not None:
            result['organizationName'] = self.organization_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunPk') is not None:
            self.aliyun_pk = m.get('aliyunPk')
        self.factory_list = []
        if m.get('factoryList') is not None:
            for k in m.get('factoryList'):
                temp_model = GetOrgAndFactoryResponseBodyDataFactoryList()
                self.factory_list.append(temp_model.from_map(k))
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('organizationName') is not None:
            self.organization_name = m.get('organizationName')
        return self


class GetOrgAndFactoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        # The code returned for the request.
        self.code = code  # type: str
        # data
        self.data = data  # type: list[GetOrgAndFactoryResponseBodyData]
        # The HTTP status code.
        self.http_code = http_code  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetOrgAndFactoryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetOrgAndFactoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrgAndFactoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrgAndFactoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgConstituteRequest(TeaModel):
    def __init__(self, code=None, module_code=None, module_type=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Module code.
        self.module_code = module_code  # type: str
        # Module type.
        self.module_type = module_type  # type: int
        # Year.
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrgConstituteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetOrgConstituteResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: OrgEmission
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOrgConstituteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = OrgEmission()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetOrgConstituteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrgConstituteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrgConstituteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrgConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPcrInfoRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: str
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPcrInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetPcrInfoResponseBodyData(TeaModel):
    def __init__(self, create_time=None, name=None, url=None):
        # The timestamp when the report was created. The timestamp is in milliseconds.
        self.create_time = create_time  # type: str
        # Report name
        self.name = name  # type: str
        # Download url link.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPcrInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetPcrInfoResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: GetPcrInfoResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPcrInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPcrInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPcrInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPcrInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPcrInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPcrInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReductionProposalRequest(TeaModel):
    def __init__(self, code=None, data_quality_evaluation_type=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The type of the data quality evaluation. 1 is DQI and 2 is DQR.
        self.data_quality_evaluation_type = data_quality_evaluation_type  # type: int
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReductionProposalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_quality_evaluation_type is not None:
            result['dataQualityEvaluationType'] = self.data_quality_evaluation_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataQualityEvaluationType') is not None:
            self.data_quality_evaluation_type = m.get('dataQualityEvaluationType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetReductionProposalResponseBodyData(TeaModel):
    def __init__(self, reduction=None, reduction_evaluation=None):
        # Proactive carbon reduction recommendations and advice.
        self.reduction = reduction  # type: str
        # Active carbon reduction assessment.
        self.reduction_evaluation = reduction_evaluation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReductionProposalResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reduction is not None:
            result['reduction'] = self.reduction
        if self.reduction_evaluation is not None:
            result['reductionEvaluation'] = self.reduction_evaluation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('reduction') is not None:
            self.reduction = m.get('reduction')
        if m.get('reductionEvaluation') is not None:
            self.reduction_evaluation = m.get('reductionEvaluation')
        return self


class GetReductionProposalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: GetReductionProposalResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetReductionProposalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetReductionProposalResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetReductionProposalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetReductionProposalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReductionProposalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetReductionProposalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsCompletedRequest(TeaModel):
    def __init__(self, code=None, product_id=None, product_type=None):
        # The enterprise code.
        self.code = code  # type: str
        # The product id.
        self.product_id = product_id  # type: long
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        self.product_type = product_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsCompletedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class IsCompletedResponseBodyData(TeaModel):
    def __init__(self, modified_time=None, task_key=None, task_short_result=None, task_status=None):
        # Modified time in milliseconds, e.g. 1711438780000.
        self.modified_time = modified_time  # type: long
        # The unique key of this generation task.
        self.task_key = task_key  # type: str
        # Unused temporarily.
        self.task_short_result = task_short_result  # type: str
        # The status of the report generation task. The possible values are `running`, `success`, and `error`, which mean generating, generating succeeded, and generating failed, respectively. If you encounter a result generation failure, check the model, correct the model, and then generate the result again.
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IsCompletedResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.task_key is not None:
            result['taskKey'] = self.task_key
        if self.task_short_result is not None:
            result['taskShortResult'] = self.task_short_result
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('taskKey') is not None:
            self.task_key = m.get('taskKey')
        if m.get('taskShortResult') is not None:
            self.task_short_result = m.get('taskShortResult')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class IsCompletedResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: IsCompletedResponseBodyData
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(IsCompletedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = IsCompletedResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class IsCompletedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IsCompletedResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IsCompletedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsCompletedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDeviceDataRequestDevices(TeaModel):
    def __init__(self, data=None, device_id=None, record_time=None):
        # Measuring point information To avoid accuracy problems, the measurement point data is uniformly transmitted to the string. The function of missing required fields cannot be used normally. Some functions may be affected due to the lack of recommend fields. For details, please refer to the notes of equipment measuring points in the appendix. [Reference Point Definition](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf
        # )
        self.data = data  # type: dict[str, any]
        # If the deviceType parameter is set to 12, 13, or 17, you must set the system_id parameter. The field name is still device_id. If the deviceType parameter is set to 15 or 16, no Other situations will be transmitted.
        self.device_id = device_id  # type: str
        # Data generation time of measuring point.
        self.record_time = record_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushDeviceDataRequestDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.record_time is not None:
            result['recordTime'] = self.record_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('recordTime') is not None:
            self.record_time = m.get('recordTime')
        return self


class PushDeviceDataRequest(TeaModel):
    def __init__(self, device_type=None, devices=None):
        # The type of the device. [View device type definitions](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf)
        self.device_type = device_type  # type: str
        # List of devices to which data is pushed.
        self.devices = devices  # type: list[PushDeviceDataRequestDevices]

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PushDeviceDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['deviceType'] = self.device_type
        result['devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')
        self.devices = []
        if m.get('devices') is not None:
            for k in m.get('devices'):
                temp_model = PushDeviceDataRequestDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class PushDeviceDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Whether the data is pushed successfully. Success is returned.
        self.data = data  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushDeviceDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushDeviceDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushDeviceDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushDeviceDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushDeviceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushItemDataRequestItems(TeaModel):
    def __init__(self, code=None, month=None, value=None):
        # The data item code.
        self.code = code  # type: str
        # The month.
        self.month = month  # type: str
        # The value of the data item.
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushItemDataRequestItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.month is not None:
            result['month'] = self.month
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PushItemDataRequest(TeaModel):
    def __init__(self, code=None, items=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Push data list.
        self.items = items  # type: PushItemDataRequestItems
        # The year of the data created.
        self.year = year  # type: str

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(PushItemDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.items is not None:
            result['items'] = self.items.to_map()
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('items') is not None:
            temp_model = PushItemDataRequestItems()
            self.items = temp_model.from_map(m['items'])
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class PushItemDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Whether the data is pushed successfully.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushItemDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushItemDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushItemDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushItemDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushItemDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecalculateCarbonEmissionRequest(TeaModel):
    def __init__(self, code=None, year=None):
        # The enterprise code.
        self.code = code  # type: str
        # Year of inventory.
        self.year = year  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecalculateCarbonEmissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class RecalculateCarbonEmissionResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data. A value of true indicates that the request is successful. A value of false indicates that the request fails.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecalculateCarbonEmissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RecalculateCarbonEmissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecalculateCarbonEmissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecalculateCarbonEmissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecalculateCarbonEmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


