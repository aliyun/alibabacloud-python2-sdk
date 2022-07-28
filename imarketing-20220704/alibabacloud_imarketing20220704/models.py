# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateDeviceRequest(TeaModel):
    def __init__(self, channel_id=None, city=None, device_model_number=None, device_name=None, device_type=None,
                 district=None, extra_map=None, first_scene=None, floor=None, location_name=None, media_id=None,
                 outer_code=None, province=None, second_scene=None):
        self.channel_id = channel_id  # type: str
        self.city = city  # type: str
        self.device_model_number = device_model_number  # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.district = district  # type: str
        self.extra_map = extra_map  # type: dict[str, any]
        self.first_scene = first_scene  # type: str
        self.floor = floor  # type: str
        self.location_name = location_name  # type: str
        self.media_id = media_id  # type: str
        self.outer_code = outer_code  # type: str
        self.province = province  # type: str
        self.second_scene = second_scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.city is not None:
            result['City'] = self.city
        if self.device_model_number is not None:
            result['DeviceModelNumber'] = self.device_model_number
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.district is not None:
            result['District'] = self.district
        if self.extra_map is not None:
            result['ExtraMap'] = self.extra_map
        if self.first_scene is not None:
            result['FirstScene'] = self.first_scene
        if self.floor is not None:
            result['Floor'] = self.floor
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.outer_code is not None:
            result['OuterCode'] = self.outer_code
        if self.province is not None:
            result['Province'] = self.province
        if self.second_scene is not None:
            result['SecondScene'] = self.second_scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DeviceModelNumber') is not None:
            self.device_model_number = m.get('DeviceModelNumber')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('ExtraMap') is not None:
            self.extra_map = m.get('ExtraMap')
        if m.get('FirstScene') is not None:
            self.first_scene = m.get('FirstScene')
        if m.get('Floor') is not None:
            self.floor = m.get('Floor')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OuterCode') is not None:
            self.outer_code = m.get('OuterCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SecondScene') is not None:
            self.second_scene = m.get('SecondScene')
        return self


class CreateDeviceShrinkRequest(TeaModel):
    def __init__(self, channel_id=None, city=None, device_model_number=None, device_name=None, device_type=None,
                 district=None, extra_map_shrink=None, first_scene=None, floor=None, location_name=None, media_id=None,
                 outer_code=None, province=None, second_scene=None):
        self.channel_id = channel_id  # type: str
        self.city = city  # type: str
        self.device_model_number = device_model_number  # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.district = district  # type: str
        self.extra_map_shrink = extra_map_shrink  # type: str
        self.first_scene = first_scene  # type: str
        self.floor = floor  # type: str
        self.location_name = location_name  # type: str
        self.media_id = media_id  # type: str
        self.outer_code = outer_code  # type: str
        self.province = province  # type: str
        self.second_scene = second_scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.city is not None:
            result['City'] = self.city
        if self.device_model_number is not None:
            result['DeviceModelNumber'] = self.device_model_number
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.district is not None:
            result['District'] = self.district
        if self.extra_map_shrink is not None:
            result['ExtraMap'] = self.extra_map_shrink
        if self.first_scene is not None:
            result['FirstScene'] = self.first_scene
        if self.floor is not None:
            result['Floor'] = self.floor
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.outer_code is not None:
            result['OuterCode'] = self.outer_code
        if self.province is not None:
            result['Province'] = self.province
        if self.second_scene is not None:
            result['SecondScene'] = self.second_scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DeviceModelNumber') is not None:
            self.device_model_number = m.get('DeviceModelNumber')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('ExtraMap') is not None:
            self.extra_map_shrink = m.get('ExtraMap')
        if m.get('FirstScene') is not None:
            self.first_scene = m.get('FirstScene')
        if m.get('Floor') is not None:
            self.floor = m.get('Floor')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OuterCode') is not None:
            self.outer_code = m.get('OuterCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SecondScene') is not None:
            self.second_scene = m.get('SecondScene')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.model = model  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBrandPageRequest(TeaModel):
    def __init__(self, account_no=None, main_id=None, main_name=None, page_index=None, page_size=None):
        self.account_no = account_no  # type: str
        self.main_id = main_id  # type: long
        self.main_name = main_name  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBrandPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.main_id is not None:
            result['MainId'] = self.main_id
        if self.main_name is not None:
            result['MainName'] = self.main_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('MainId') is not None:
            self.main_id = m.get('MainId')
        if m.get('MainName') is not None:
            self.main_name = m.get('MainName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetBrandPageResponseBodyDataList(TeaModel):
    def __init__(self, account_no=None, account_type=None, company=None, main_id=None, main_name=None,
                 parent_main_id=None):
        self.account_no = account_no  # type: str
        self.account_type = account_type  # type: str
        self.company = company  # type: str
        self.main_id = main_id  # type: long
        self.main_name = main_name  # type: str
        self.parent_main_id = parent_main_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBrandPageResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.company is not None:
            result['Company'] = self.company
        if self.main_id is not None:
            result['MainId'] = self.main_id
        if self.main_name is not None:
            result['MainName'] = self.main_name
        if self.parent_main_id is not None:
            result['ParentMainId'] = self.parent_main_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Company') is not None:
            self.company = m.get('Company')
        if m.get('MainId') is not None:
            self.main_id = m.get('MainId')
        if m.get('MainName') is not None:
            self.main_name = m.get('MainName')
        if m.get('ParentMainId') is not None:
            self.parent_main_id = m.get('ParentMainId')
        return self


class GetBrandPageResponseBodyDataPageInfo(TeaModel):
    def __init__(self, page=None, page_size=None, total_number=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total_number = total_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBrandPageResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class GetBrandPageResponseBodyData(TeaModel):
    def __init__(self, list=None, page_info=None):
        self.list = list  # type: list[GetBrandPageResponseBodyDataList]
        self.page_info = page_info  # type: GetBrandPageResponseBodyDataPageInfo

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetBrandPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetBrandPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = GetBrandPageResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class GetBrandPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: GetBrandPageResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetBrandPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetBrandPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBrandPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBrandPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBrandPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBrandPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBusinessIdRequest(TeaModel):
    def __init__(self, business_id=None):
        self.business_id = business_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBusinessIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        return self


class GetBusinessIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBusinessIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBusinessIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBusinessIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBusinessIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBusinessIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLeadsListPageRequest(TeaModel):
    def __init__(self, component_id=None, content_id=None, creative_id=None, end_time=None, main_id=None,
                 page_index=None, page_size=None, start_time=None, task_id=None):
        self.component_id = component_id  # type: long
        self.content_id = content_id  # type: long
        self.creative_id = creative_id  # type: long
        self.end_time = end_time  # type: long
        self.main_id = main_id  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLeadsListPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.creative_id is not None:
            result['CreativeId'] = self.creative_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.main_id is not None:
            result['MainId'] = self.main_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('CreativeId') is not None:
            self.creative_id = m.get('CreativeId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MainId') is not None:
            self.main_id = m.get('MainId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetLeadsListPageResponseBodyData(TeaModel):
    def __init__(self, component_id=None, content_id=None, creative_id=None, leads_detail=None, serial_id=None,
                 task_id=None):
        self.component_id = component_id  # type: str
        self.content_id = content_id  # type: str
        self.creative_id = creative_id  # type: str
        self.leads_detail = leads_detail  # type: str
        self.serial_id = serial_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLeadsListPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.creative_id is not None:
            result['CreativeId'] = self.creative_id
        if self.leads_detail is not None:
            result['LeadsDetail'] = self.leads_detail
        if self.serial_id is not None:
            result['SerialId'] = self.serial_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('CreativeId') is not None:
            self.creative_id = m.get('CreativeId')
        if m.get('LeadsDetail') is not None:
            self.leads_detail = m.get('LeadsDetail')
        if m.get('SerialId') is not None:
            self.serial_id = m.get('SerialId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetLeadsListPageResponseBodyPageInfo(TeaModel):
    def __init__(self, page=None, page_size=None, total_number=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total_number = total_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLeadsListPageResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class GetLeadsListPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, page_info=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetLeadsListPageResponseBodyData
        self.error_message = error_message  # type: str
        self.page_info = page_info  # type: GetLeadsListPageResponseBodyPageInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetLeadsListPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
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
            temp_model = GetLeadsListPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PageInfo') is not None:
            temp_model = GetLeadsListPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLeadsListPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLeadsListPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLeadsListPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLeadsListPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMainPartListByUserIdResponseBodyData(TeaModel):
    def __init__(self, token=None):
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMainPartListByUserIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetMainPartListByUserIdResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: GetMainPartListByUserIdResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMainPartListByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMainPartListByUserIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMainPartListByUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMainPartListByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMainPartListByUserIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMainPartListByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMainPartPageRequest(TeaModel):
    def __init__(self, main_id=None, main_name=None, page_index=None, page_size=None):
        self.main_id = main_id  # type: long
        self.main_name = main_name  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMainPartPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_id is not None:
            result['MainId'] = self.main_id
        if self.main_name is not None:
            result['MainName'] = self.main_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MainId') is not None:
            self.main_id = m.get('MainId')
        if m.get('MainName') is not None:
            self.main_name = m.get('MainName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetMainPartPageResponseBodyDataListAccountTypeList(TeaModel):
    def __init__(self, account_type=None, account_type_desc=None):
        self.account_type = account_type  # type: str
        self.account_type_desc = account_type_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMainPartPageResponseBodyDataListAccountTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_type_desc is not None:
            result['AccountTypeDesc'] = self.account_type_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountTypeDesc') is not None:
            self.account_type_desc = m.get('AccountTypeDesc')
        return self


class GetMainPartPageResponseBodyDataList(TeaModel):
    def __init__(self, account_type_list=None, company=None, main_id=None, main_name=None):
        self.account_type_list = account_type_list  # type: list[GetMainPartPageResponseBodyDataListAccountTypeList]
        self.company = company  # type: str
        self.main_id = main_id  # type: long
        self.main_name = main_name  # type: str

    def validate(self):
        if self.account_type_list:
            for k in self.account_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMainPartPageResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountTypeList'] = []
        if self.account_type_list is not None:
            for k in self.account_type_list:
                result['AccountTypeList'].append(k.to_map() if k else None)
        if self.company is not None:
            result['Company'] = self.company
        if self.main_id is not None:
            result['MainId'] = self.main_id
        if self.main_name is not None:
            result['MainName'] = self.main_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_type_list = []
        if m.get('AccountTypeList') is not None:
            for k in m.get('AccountTypeList'):
                temp_model = GetMainPartPageResponseBodyDataListAccountTypeList()
                self.account_type_list.append(temp_model.from_map(k))
        if m.get('Company') is not None:
            self.company = m.get('Company')
        if m.get('MainId') is not None:
            self.main_id = m.get('MainId')
        if m.get('MainName') is not None:
            self.main_name = m.get('MainName')
        return self


class GetMainPartPageResponseBodyDataPageInfo(TeaModel):
    def __init__(self, page=None, page_size=None, total_number=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total_number = total_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMainPartPageResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_number is not None:
            result['totalNumber'] = self.total_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalNumber') is not None:
            self.total_number = m.get('totalNumber')
        return self


class GetMainPartPageResponseBodyData(TeaModel):
    def __init__(self, list=None, page_info=None):
        self.list = list  # type: list[GetMainPartPageResponseBodyDataList]
        self.page_info = page_info  # type: GetMainPartPageResponseBodyDataPageInfo

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetMainPartPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetMainPartPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = GetMainPartPageResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        return self


class GetMainPartPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: GetMainPartPageResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMainPartPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetMainPartPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMainPartPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMainPartPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMainPartPageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMainPartPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserFinishedAdRequest(TeaModel):
    def __init__(self, adid=None, clicklink=None, id=None, mediaid=None, tagid=None, uid=None):
        self.adid = adid  # type: long
        self.clicklink = clicklink  # type: str
        self.id = id  # type: str
        self.mediaid = mediaid  # type: str
        self.tagid = tagid  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserFinishedAdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adid is not None:
            result['Adid'] = self.adid
        if self.clicklink is not None:
            result['Clicklink'] = self.clicklink
        if self.id is not None:
            result['Id'] = self.id
        if self.mediaid is not None:
            result['Mediaid'] = self.mediaid
        if self.tagid is not None:
            result['Tagid'] = self.tagid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adid') is not None:
            self.adid = m.get('Adid')
        if m.get('Clicklink') is not None:
            self.clicklink = m.get('Clicklink')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mediaid') is not None:
            self.mediaid = m.get('Mediaid')
        if m.get('Tagid') is not None:
            self.tagid = m.get('Tagid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetUserFinishedAdResponseBodyHeader(TeaModel):
    def __init__(self, cost_time=None, rpc_id=None, trace_id=None, version=None):
        self.cost_time = cost_time  # type: long
        self.rpc_id = rpc_id  # type: str
        self.trace_id = trace_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserFinishedAdResponseBodyHeader, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetUserFinishedAdResponseBodyResult(TeaModel):
    def __init__(self, commission=None, marketing_type=None, objective=None, success=None):
        self.commission = commission  # type: str
        self.marketing_type = marketing_type  # type: str
        self.objective = objective  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserFinishedAdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commission is not None:
            result['Commission'] = self.commission
        if self.marketing_type is not None:
            result['MarketingType'] = self.marketing_type
        if self.objective is not None:
            result['Objective'] = self.objective
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Commission') is not None:
            self.commission = m.get('Commission')
        if m.get('MarketingType') is not None:
            self.marketing_type = m.get('MarketingType')
        if m.get('Objective') is not None:
            self.objective = m.get('Objective')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserFinishedAdResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, ext=None, header=None, request_id=None, result=None,
                 success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.ext = ext  # type: dict[str, str]
        self.header = header  # type: GetUserFinishedAdResponseBodyHeader
        self.request_id = request_id  # type: str
        self.result = result  # type: GetUserFinishedAdResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.header:
            self.header.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetUserFinishedAdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Header') is not None:
            temp_model = GetUserFinishedAdResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetUserFinishedAdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserFinishedAdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserFinishedAdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserFinishedAdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserFinishedAdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvertisingRequestApp(TeaModel):
    def __init__(self, ext=None, mediaid=None, sn=None):
        self.ext = ext  # type: dict[str, any]
        self.mediaid = mediaid  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingRequestApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.mediaid is not None:
            result['Mediaid'] = self.mediaid
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Mediaid') is not None:
            self.mediaid = m.get('Mediaid')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ListAdvertisingRequestDeviceGeo(TeaModel):
    def __init__(self, city=None, district=None, lat=None, lon=None, province=None):
        self.city = city  # type: str
        self.district = district  # type: str
        self.lat = lat  # type: float
        self.lon = lon  # type: float
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingRequestDeviceGeo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.district is not None:
            result['District'] = self.district
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListAdvertisingRequestDevice(TeaModel):
    def __init__(self, androidid=None, androidmd_5=None, caid=None, carrier=None, connectiontype=None,
                 devicetype=None, geo=None, idfa=None, imei=None, imeimd_5=None, ip=None, language=None, mac=None, macmd_5=None,
                 make=None, model=None, oaid=None, os=None, osv=None, ua=None, utdid=None):
        self.androidid = androidid  # type: str
        self.androidmd_5 = androidmd_5  # type: str
        self.caid = caid  # type: str
        self.carrier = carrier  # type: str
        self.connectiontype = connectiontype  # type: int
        self.devicetype = devicetype  # type: int
        self.geo = geo  # type: ListAdvertisingRequestDeviceGeo
        self.idfa = idfa  # type: str
        self.imei = imei  # type: str
        self.imeimd_5 = imeimd_5  # type: str
        self.ip = ip  # type: str
        self.language = language  # type: str
        self.mac = mac  # type: str
        self.macmd_5 = macmd_5  # type: str
        self.make = make  # type: str
        self.model = model  # type: str
        self.oaid = oaid  # type: str
        self.os = os  # type: str
        self.osv = osv  # type: str
        self.ua = ua  # type: str
        self.utdid = utdid  # type: str

    def validate(self):
        if self.geo:
            self.geo.validate()

    def to_map(self):
        _map = super(ListAdvertisingRequestDevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.androidid is not None:
            result['Androidid'] = self.androidid
        if self.androidmd_5 is not None:
            result['Androidmd5'] = self.androidmd_5
        if self.caid is not None:
            result['Caid'] = self.caid
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.connectiontype is not None:
            result['Connectiontype'] = self.connectiontype
        if self.devicetype is not None:
            result['Devicetype'] = self.devicetype
        if self.geo is not None:
            result['Geo'] = self.geo.to_map()
        if self.idfa is not None:
            result['Idfa'] = self.idfa
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.imeimd_5 is not None:
            result['Imeimd5'] = self.imeimd_5
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.language is not None:
            result['Language'] = self.language
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.macmd_5 is not None:
            result['Macmd5'] = self.macmd_5
        if self.make is not None:
            result['Make'] = self.make
        if self.model is not None:
            result['Model'] = self.model
        if self.oaid is not None:
            result['Oaid'] = self.oaid
        if self.os is not None:
            result['Os'] = self.os
        if self.osv is not None:
            result['Osv'] = self.osv
        if self.ua is not None:
            result['Ua'] = self.ua
        if self.utdid is not None:
            result['Utdid'] = self.utdid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Androidid') is not None:
            self.androidid = m.get('Androidid')
        if m.get('Androidmd5') is not None:
            self.androidmd_5 = m.get('Androidmd5')
        if m.get('Caid') is not None:
            self.caid = m.get('Caid')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Connectiontype') is not None:
            self.connectiontype = m.get('Connectiontype')
        if m.get('Devicetype') is not None:
            self.devicetype = m.get('Devicetype')
        if m.get('Geo') is not None:
            temp_model = ListAdvertisingRequestDeviceGeo()
            self.geo = temp_model.from_map(m['Geo'])
        if m.get('Idfa') is not None:
            self.idfa = m.get('Idfa')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('Imeimd5') is not None:
            self.imeimd_5 = m.get('Imeimd5')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Macmd5') is not None:
            self.macmd_5 = m.get('Macmd5')
        if m.get('Make') is not None:
            self.make = m.get('Make')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Oaid') is not None:
            self.oaid = m.get('Oaid')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Osv') is not None:
            self.osv = m.get('Osv')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')
        return self


class ListAdvertisingRequestImp(TeaModel):
    def __init__(self, id=None, tagid=None):
        self.id = id  # type: str
        self.tagid = tagid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingRequestImp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tagid is not None:
            result['Tagid'] = self.tagid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Tagid') is not None:
            self.tagid = m.get('Tagid')
        return self


class ListAdvertisingRequestUser(TeaModel):
    def __init__(self, id=None, usertype=None):
        self.id = id  # type: str
        self.usertype = usertype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.usertype is not None:
            result['Usertype'] = self.usertype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Usertype') is not None:
            self.usertype = m.get('Usertype')
        return self


class ListAdvertisingRequest(TeaModel):
    def __init__(self, app=None, dealtype=None, device=None, ext=None, id=None, imp=None, test=None, user=None):
        self.app = app  # type: ListAdvertisingRequestApp
        self.dealtype = dealtype  # type: int
        self.device = device  # type: ListAdvertisingRequestDevice
        self.ext = ext  # type: dict[str, any]
        self.id = id  # type: str
        self.imp = imp  # type: list[ListAdvertisingRequestImp]
        self.test = test  # type: int
        self.user = user  # type: ListAdvertisingRequestUser

    def validate(self):
        if self.app:
            self.app.validate()
        if self.device:
            self.device.validate()
        if self.imp:
            for k in self.imp:
                if k:
                    k.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(ListAdvertisingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.dealtype is not None:
            result['Dealtype'] = self.dealtype
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.id is not None:
            result['Id'] = self.id
        result['Imp'] = []
        if self.imp is not None:
            for k in self.imp:
                result['Imp'].append(k.to_map() if k else None)
        if self.test is not None:
            result['Test'] = self.test
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = ListAdvertisingRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('Dealtype') is not None:
            self.dealtype = m.get('Dealtype')
        if m.get('Device') is not None:
            temp_model = ListAdvertisingRequestDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.imp = []
        if m.get('Imp') is not None:
            for k in m.get('Imp'):
                temp_model = ListAdvertisingRequestImp()
                self.imp.append(temp_model.from_map(k))
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('User') is not None:
            temp_model = ListAdvertisingRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListAdvertisingShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, dealtype=None, device_shrink=None, ext_shrink=None, id=None, imp_shrink=None,
                 test=None, user_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.dealtype = dealtype  # type: int
        self.device_shrink = device_shrink  # type: str
        self.ext_shrink = ext_shrink  # type: str
        self.id = id  # type: str
        self.imp_shrink = imp_shrink  # type: str
        self.test = test  # type: int
        self.user_shrink = user_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.dealtype is not None:
            result['Dealtype'] = self.dealtype
        if self.device_shrink is not None:
            result['Device'] = self.device_shrink
        if self.ext_shrink is not None:
            result['Ext'] = self.ext_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.imp_shrink is not None:
            result['Imp'] = self.imp_shrink
        if self.test is not None:
            result['Test'] = self.test
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('Dealtype') is not None:
            self.dealtype = m.get('Dealtype')
        if m.get('Device') is not None:
            self.device_shrink = m.get('Device')
        if m.get('Ext') is not None:
            self.ext_shrink = m.get('Ext')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Imp') is not None:
            self.imp_shrink = m.get('Imp')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class ListAdvertisingResponseBodyHeader(TeaModel):
    def __init__(self, cost_time=None, rpc_id=None, trace_id=None, version=None):
        self.cost_time = cost_time  # type: long
        self.rpc_id = rpc_id  # type: str
        self.trace_id = trace_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyHeader, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsIcon(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbidBidAdsIcon, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsImages(TeaModel):
    def __init__(self, desc=None, format=None, url=None):
        self.desc = desc  # type: str
        self.format = format  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbidBidAdsImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.format is not None:
            result['Format'] = self.format
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers(TeaModel):
    def __init__(self, imps=None):
        self.imps = imps  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imps is not None:
            result['Imps'] = self.imps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Imps') is not None:
            self.imps = m.get('Imps')
        return self


class ListAdvertisingResponseBodyResultSeatbidBidAds(TeaModel):
    def __init__(self, crid=None, crurl=None, icon=None, id=None, images=None, interacttype=None, labeltype=None,
                 landingurls=None, marketingtype=None, objective=None, price=None, seat=None, style=None, title=None,
                 trackers=None, type=None):
        self.crid = crid  # type: str
        self.crurl = crurl  # type: str
        self.icon = icon  # type: ListAdvertisingResponseBodyResultSeatbidBidAdsIcon
        self.id = id  # type: str
        self.images = images  # type: list[ListAdvertisingResponseBodyResultSeatbidBidAdsImages]
        self.interacttype = interacttype  # type: int
        self.labeltype = labeltype  # type: str
        self.landingurls = landingurls  # type: list[str]
        self.marketingtype = marketingtype  # type: str
        self.objective = objective  # type: str
        self.price = price  # type: str
        self.seat = seat  # type: str
        self.style = style  # type: str
        self.title = title  # type: str
        self.trackers = trackers  # type: ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers
        self.type = type  # type: str

    def validate(self):
        if self.icon:
            self.icon.validate()
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.trackers:
            self.trackers.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbidBidAds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crid is not None:
            result['Crid'] = self.crid
        if self.crurl is not None:
            result['Crurl'] = self.crurl
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.id is not None:
            result['Id'] = self.id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.interacttype is not None:
            result['Interacttype'] = self.interacttype
        if self.labeltype is not None:
            result['Labeltype'] = self.labeltype
        if self.landingurls is not None:
            result['Landingurls'] = self.landingurls
        if self.marketingtype is not None:
            result['Marketingtype'] = self.marketingtype
        if self.objective is not None:
            result['Objective'] = self.objective
        if self.price is not None:
            result['Price'] = self.price
        if self.seat is not None:
            result['Seat'] = self.seat
        if self.style is not None:
            result['Style'] = self.style
        if self.title is not None:
            result['Title'] = self.title
        if self.trackers is not None:
            result['Trackers'] = self.trackers.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Crid') is not None:
            self.crid = m.get('Crid')
        if m.get('Crurl') is not None:
            self.crurl = m.get('Crurl')
        if m.get('Icon') is not None:
            temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsImages()
                self.images.append(temp_model.from_map(k))
        if m.get('Interacttype') is not None:
            self.interacttype = m.get('Interacttype')
        if m.get('Labeltype') is not None:
            self.labeltype = m.get('Labeltype')
        if m.get('Landingurls') is not None:
            self.landingurls = m.get('Landingurls')
        if m.get('Marketingtype') is not None:
            self.marketingtype = m.get('Marketingtype')
        if m.get('Objective') is not None:
            self.objective = m.get('Objective')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Seat') is not None:
            self.seat = m.get('Seat')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Trackers') is not None:
            temp_model = ListAdvertisingResponseBodyResultSeatbidBidAdsTrackers()
            self.trackers = temp_model.from_map(m['Trackers'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAdvertisingResponseBodyResultSeatbidBid(TeaModel):
    def __init__(self, ads=None, impid=None):
        self.ads = ads  # type: list[ListAdvertisingResponseBodyResultSeatbidBidAds]
        self.impid = impid  # type: str

    def validate(self):
        if self.ads:
            for k in self.ads:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbidBid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ads'] = []
        if self.ads is not None:
            for k in self.ads:
                result['Ads'].append(k.to_map() if k else None)
        if self.impid is not None:
            result['Impid'] = self.impid
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ads = []
        if m.get('Ads') is not None:
            for k in m.get('Ads'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBidAds()
                self.ads.append(temp_model.from_map(k))
        if m.get('Impid') is not None:
            self.impid = m.get('Impid')
        return self


class ListAdvertisingResponseBodyResultSeatbid(TeaModel):
    def __init__(self, bid=None):
        self.bid = bid  # type: list[ListAdvertisingResponseBodyResultSeatbidBid]

    def validate(self):
        if self.bid:
            for k in self.bid:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResultSeatbid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bid'] = []
        if self.bid is not None:
            for k in self.bid:
                result['Bid'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bid = []
        if m.get('Bid') is not None:
            for k in m.get('Bid'):
                temp_model = ListAdvertisingResponseBodyResultSeatbidBid()
                self.bid.append(temp_model.from_map(k))
        return self


class ListAdvertisingResponseBodyResult(TeaModel):
    def __init__(self, bidid=None, id=None, seatbid=None):
        self.bidid = bidid  # type: str
        self.id = id  # type: str
        self.seatbid = seatbid  # type: list[ListAdvertisingResponseBodyResultSeatbid]

    def validate(self):
        if self.seatbid:
            for k in self.seatbid:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bidid is not None:
            result['Bidid'] = self.bidid
        if self.id is not None:
            result['Id'] = self.id
        result['Seatbid'] = []
        if self.seatbid is not None:
            for k in self.seatbid:
                result['Seatbid'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bidid') is not None:
            self.bidid = m.get('Bidid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.seatbid = []
        if m.get('Seatbid') is not None:
            for k in m.get('Seatbid'):
                temp_model = ListAdvertisingResponseBodyResultSeatbid()
                self.seatbid.append(temp_model.from_map(k))
        return self


class ListAdvertisingResponseBody(TeaModel):
    def __init__(self, errorcode=None, errormsg=None, ext=None, header=None, request_id=None, result=None,
                 success=None):
        self.errorcode = errorcode  # type: str
        self.errormsg = errormsg  # type: str
        self.ext = ext  # type: dict[str, str]
        self.header = header  # type: ListAdvertisingResponseBodyHeader
        self.request_id = request_id  # type: str
        self.result = result  # type: ListAdvertisingResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.header:
            self.header.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.errorcode is not None:
            result['Errorcode'] = self.errorcode
        if self.errormsg is not None:
            result['Errormsg'] = self.errormsg
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Errorcode') is not None:
            self.errorcode = m.get('Errorcode')
        if m.get('Errormsg') is not None:
            self.errormsg = m.get('Errormsg')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('Header') is not None:
            temp_model = ListAdvertisingResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAdvertisingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAdvertisingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAdvertisingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAdvertisingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAdvertisingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSmsRequest(TeaModel):
    def __init__(self, phone_numbers=None):
        self.phone_numbers = phone_numbers  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendSmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        return self


class SendSmsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendSmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendSmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendSmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendSmsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


