# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataProductListLogMapValueExtraParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # The ID of the extended parameter.
        self.key = key  # type: str
        # The value of the extended parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataProductListLogMapValueExtraParameters, self).to_map()
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


class DataProductListLogMapValue(TeaModel):
    def __init__(self, log_code=None, log_name=None, log_name_en=None, log_name_key=None, status=None,
                 can_operate_or_not=None, topic=None, extra_parameters=None):
        # The code of the log.
        self.log_code = log_code  # type: str
        # This parameter is deprecated.
        self.log_name = log_name  # type: str
        # This parameter is deprecated.
        self.log_name_en = log_name_en  # type: str
        # The language code of the log that is used to indicate the language in which the log is displayed.
        self.log_name_key = log_name_key  # type: str
        # The status of the log delivery. Valid values:
        # 
        # *   true: The logs are being delivered.
        # *   false: The log delivery feature is disabled.
        self.status = status  # type: bool
        # Indicates whether the log delivery feature can be enabled or disabled. The feature can be enabled or disabled only by the administrator of the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.can_operate_or_not = can_operate_or_not  # type: bool
        # The topic of the log in the Logstore. The value is an index field in the Logstore that can be used to distinguish different logs.
        self.topic = topic  # type: str
        # The extended parameter.
        self.extra_parameters = extra_parameters  # type: list[DataProductListLogMapValueExtraParameters]

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataProductListLogMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        if self.topic is not None:
            result['Topic'] = self.topic
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = DataProductListLogMapValueExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        return self


class AddDataSourceRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_name=None,
                 data_source_instance_params=None, data_source_instance_remark=None, data_source_type=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        # *   aliyun
        self.cloud_code = cloud_code  # type: str
        # The name of the data source.
        self.data_source_instance_name = data_source_instance_name  # type: str
        # The parameters of the data source. Set this parameter to a JSON array.
        self.data_source_instance_params = data_source_instance_params  # type: str
        # The remarks on the data source.
        self.data_source_instance_remark = data_source_instance_remark  # type: str
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_params is not None:
            result['DataSourceInstanceParams'] = self.data_source_instance_params
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceParams') is not None:
            self.data_source_instance_params = m.get('DataSourceInstanceParams')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDataSourceResponseBodyData(TeaModel):
    def __init__(self, count=None, data_source_instance_id=None):
        # The number of data sources that are added. The value 1 indicates that data source is added, and a value less than or equal to 0 indicates that the data source failed to be added.
        self.count = count  # type: int
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        return self


class AddDataSourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: AddDataSourceResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDataSourceLogRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None,
                 data_source_instance_logs=None, log_code=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The parameters of the data source. Set this parameter to a JSON array.
        self.data_source_instance_logs = data_source_instance_logs  # type: str
        # The log code.
        self.log_code = log_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataSourceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceLogs') is not None:
            self.data_source_instance_logs = m.get('DataSourceInstanceLogs')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDataSourceLogResponseBodyData(TeaModel):
    def __init__(self, count=None, log_instance_id=None):
        # The number of logs that are added. The value 1 indicates that the log is added, and a value less than or equal to 0 indicates that the log failed to be added.
        self.count = count  # type: int
        # The ID of the log. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.log_instance_id = log_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDataSourceLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class AddDataSourceLogResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: AddDataSourceLogResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddDataSourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDataSourceLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddDataSourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDataSourceLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(self, added_user_id=None, region_id=None):
        # The ID of the Alibaba Cloud account.
        self.added_user_id = added_user_id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_user_id is not None:
            result['AddedUserId'] = self.added_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddedUserId') is not None:
            self.added_user_id = m.get('AddedUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the Alibaba Cloud account is added to the threat analysis feature.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserSourceLogConfigRequest(TeaModel):
    def __init__(self, deleted=None, dis_play_line=None, region_id=None, source_log_code=None, source_log_info=None,
                 source_prod_code=None, sub_user_id=None):
        # Specifies whether to add logs or delete added logs. Valid values:
        # 
        # *   \-1: deletes added logs.
        # *   0: adds logs.
        self.deleted = deleted  # type: int
        # The display details of the Logstore.
        self.dis_play_line = dis_play_line  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The details of the Logstore that you want to use in the JSON string format.
        self.source_log_info = source_log_info  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserSourceLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.dis_play_line is not None:
            result['DisPlayLine'] = self.dis_play_line
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_info is not None:
            result['SourceLogInfo'] = self.source_log_info
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('DisPlayLine') is not None:
            self.dis_play_line = m.get('DisPlayLine')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogInfo') is not None:
            self.source_log_info = m.get('SourceLogInfo')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class AddUserSourceLogConfigResponseBodyData(TeaModel):
    def __init__(self, diplay_line=None, displayed=None, imported=None, main_user_id=None, source_log_code=None,
                 source_prod_code=None, sub_user_id=None, sub_user_name=None):
        # The display details of the Logstore.
        self.diplay_line = diplay_line  # type: str
        # Indicates whether the details of added logs are returned. Valid values: true false
        self.displayed = displayed  # type: bool
        # Indicates whether the logs are added to the threat analysis feature. Valid values: true false
        self.imported = imported  # type: bool
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str
        # The ID of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserSourceLogConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diplay_line is not None:
            result['DiplayLine'] = self.diplay_line
        if self.displayed is not None:
            result['Displayed'] = self.displayed
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiplayLine') is not None:
            self.diplay_line = m.get('DiplayLine')
        if m.get('Displayed') is not None:
            self.displayed = m.get('Displayed')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class AddUserSourceLogConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: AddUserSourceLogConfigResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddUserSourceLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddUserSourceLogConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserSourceLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUserSourceLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserSourceLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddUserSourceLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchJobCheckRequest(TeaModel):
    def __init__(self, region_id=None, submit_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside.
        self.region_id = region_id  # type: str
        # The id of task.
        self.submit_id = submit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductListLogList(TeaModel):
    def __init__(self, error_code=None, log_code=None, log_store_name_pattern=None, product_code=None,
                 project_name_pattern=None, region_code=None):
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The log code.
        self.log_code = log_code  # type: str
        # The pattern of SLS log store name.
        self.log_store_name_pattern = log_store_name_pattern  # type: str
        # The code of product.
        self.product_code = product_code  # type: str
        # The pattern of SLS project name.
        self.project_name_pattern = project_name_pattern  # type: str
        # The ID of the region in which the instance resides.
        self.region_code = region_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskListProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        # The list of log.
        self.log_list = log_list  # type: list[BatchJobCheckResponseBodyDataErrTaskListProductListLogList]
        # The code of the product.
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskListProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        # The list of product.
        self.product_list = product_list  # type: list[BatchJobCheckResponseBodyDataErrTaskListProductList]
        # The account id of aliyun.
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobCheckResponseBodyData(TeaModel):
    def __init__(self, config_id=None, err_task_list=None, failed_count=None, finish_count=None, folder_id=None,
                 task_count=None, task_status=None):
        # The ID of the task configuration.
        self.config_id = config_id  # type: str
        # The list of error task.
        self.err_task_list = err_task_list  # type: list[BatchJobCheckResponseBodyDataErrTaskList]
        # The number of custom route entries that failed to be added.
        self.failed_count = failed_count  # type: int
        # The number of scan tasks that are complete.
        self.finish_count = finish_count  # type: int
        # The ID of the folder.
        self.folder_id = folder_id  # type: str
        # The number of existing tasks that are created to add logs within the data source.
        self.task_count = task_count  # type: int
        # The status of task.
        self.task_status = task_status  # type: str

    def validate(self):
        if self.err_task_list:
            for k in self.err_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ErrTaskList'] = []
        if self.err_task_list is not None:
            for k in self.err_task_list:
                result['ErrTaskList'].append(k.to_map() if k else None)
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.err_task_list = []
        if m.get('ErrTaskList') is not None:
            for k in m.get('ErrTaskList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskList()
                self.err_task_list.append(temp_model.from_map(k))
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class BatchJobCheckResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: BatchJobCheckResponseBodyData
        # The error code.
        self.err_code = err_code  # type: str
        # The message returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchJobCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchJobCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchJobSubmitRequest(TeaModel):
    def __init__(self, json_config=None, region_id=None):
        # The detail config of task.
        self.json_config = json_config  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobSubmitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_config is not None:
            result['JsonConfig'] = self.json_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonConfig') is not None:
            self.json_config = m.get('JsonConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductListLogList(TeaModel):
    def __init__(self, error_code=None, log_code=None, log_store_name_pattern=None, product_code=None,
                 project_name_pattern=None, region_code=None):
        # The error code returned.
        self.error_code = error_code  # type: str
        # The log code.
        self.log_code = log_code  # type: str
        # The pattern of SLS log store name.
        self.log_store_name_pattern = log_store_name_pattern  # type: str
        # The code of product.
        self.product_code = product_code  # type: str
        # The pattern of SLS project name.
        self.project_name_pattern = project_name_pattern  # type: str
        # The ID of the region in which the instance resides.
        self.region_code = region_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigListProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        # The list of log.
        self.log_list = log_list  # type: list[BatchJobSubmitResponseBodyDataConfigListProductListLogList]
        # The code of the product.
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigListProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobSubmitResponseBodyDataConfigList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        # The list of product.
        self.product_list = product_list  # type: list[BatchJobSubmitResponseBodyDataConfigListProductList]
        # The account id of aliyun.
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobSubmitResponseBodyData(TeaModel):
    def __init__(self, config_id=None, config_list=None, submit_id=None, task_count=None):
        # The ID of the task configuration.
        self.config_id = config_id  # type: str
        # The list of task configure.
        self.config_list = config_list  # type: list[BatchJobSubmitResponseBodyDataConfigList]
        # The id of task.
        self.submit_id = submit_id  # type: str
        # The number of existing tasks that are created to add logs within the data source.
        self.task_count = task_count  # type: int

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class BatchJobSubmitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: BatchJobSubmitResponseBodyData
        # The error code.
        self.err_code = err_code  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobSubmitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobSubmitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchJobSubmitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchJobSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAccountRequest(TeaModel):
    def __init__(self, access_id=None, account_id=None, account_name=None, cloud_code=None, region_id=None):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id  # type: str
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The username of the cloud account.
        self.account_name = account_name  # type: str
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BindAccountResponseBodyData(TeaModel):
    def __init__(self, count=None):
        # The number of the cloud accounts that are added to the threat analysis feature. The value 1 indicates that the account is added, and a value less than or equal to 0 indicates that the account failed to be added.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class BindAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: BindAccountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BindAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BindAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDeliveryRequest(TeaModel):
    def __init__(self, log_code=None, product_code=None, region_id=None):
        # The log code of the cloud service, such as the code of the process log for Security Center. You can obtain the log code from the response of the ListDelivery operation.
        self.log_code = log_code  # type: str
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloseDeliveryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the threat analysis feature was disabled. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloseDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutomateResponseConfigRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAutomateResponseConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigResponseBody, self).to_map()
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


class DeleteAutomateResponseConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutomateResponseConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindAccountRequest(TeaModel):
    def __init__(self, access_id=None, account_id=None, bind_id=None, cloud_code=None, region_id=None):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id  # type: str
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The ID generated when the account is added to the threat analysis feature. You can call the [ListBindAccount](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListBindAccount) operation to query the ID.
        self.bind_id = bind_id  # type: long
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBindAccountResponseBodyData(TeaModel):
    def __init__(self, count=None):
        # The number of cloud accounts that are removed. The value 1 indicates that cloud account is removed, and a value less than or equal to 0 indicates that the cloud account failed to be removed.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DeleteBindAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DeleteBindAccountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteBindAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteBindAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBindAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBindAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBindAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizeRuleRequest(TeaModel):
    def __init__(self, region_id=None, rule_id=None):
        # The region in which the service is deployed.
        self.region_id = region_id  # type: str
        # The ID of the rule.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: int
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizeRuleResponseBody, self).to_map()
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


class DeleteCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomizeRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDataSourceResponseBodyData(TeaModel):
    def __init__(self, count=None):
        # The number of data sources that are removed. The value 1 indicates that data source is removed, and a value less than or equal to 0 indicates that the data source failed to be removed.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DeleteDataSourceResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceLogRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None, log_instance_id=None,
                 region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The ID of the log. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) operation to query the IDs of logs.
        self.log_instance_id = log_instance_id  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDataSourceLogResponseBodyData(TeaModel):
    def __init__(self, count=None, log_instance_id=None):
        # The number of logs that are removed. The value 1 indicates that the log is removed, and a value less than or equal to 0 indicates that the log failed to be removed.
        self.count = count  # type: int
        # The ID of the log. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.log_instance_id = log_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class DeleteDataSourceLogResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DeleteDataSourceLogResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteDataSourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataSourceLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataSourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSourceLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuickQueryRequest(TeaModel):
    def __init__(self, region_id=None, search_name=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # The name of the saved search.
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class DeleteQuickQueryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the saved search is deleted. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQuickQueryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, added_user_id=None, region_id=None):
        # The ID of the Alibaba Cloud account.
        self.added_user_id = added_user_id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_user_id is not None:
            result['AddedUserId'] = self.added_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddedUserId') is not None:
            self.added_user_id = m.get('AddedUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the Alibaba Cloud account is removed. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhiteRuleListRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        # The unique ID of the whitelist rule.
        self.id = id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: any
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhiteRuleListResponseBody, self).to_map()
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


class DeleteWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWhiteRuleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAggregateFunctionRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAggregateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAggregateFunctionResponseBodyData(TeaModel):
    def __init__(self, function=None, function_name=None):
        # The aggregate function.
        self.function = function  # type: str
        # The display name of the aggregate function.
        self.function_name = function_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['Function'] = self.function
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeAggregateFunctionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAggregateFunctionResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAggregateFunctionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAggregateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAggregateFunctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAggregateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSceneResponseBodyDataTargets(TeaModel):
    def __init__(self, name=None, type=None, value=None, values=None):
        # The display name of the attribute for the entity.
        self.name = name  # type: str
        # The attribute of the entity.
        self.type = type  # type: str
        # The right operand that is displayed by default in the whitelist rule.
        self.value = value  # type: str
        # The right operands supported by the whitelist rule.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneResponseBodyData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_tile=None, alert_tile_id=None, alert_type=None,
                 alert_type_id=None, targets=None):
        # The name of the alert. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_name = alert_name  # type: str
        # The ID of the alert name.
        self.alert_name_id = alert_name_id  # type: str
        # The title of the alert notification. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_tile = alert_tile  # type: str
        # The ID of the alert title.
        self.alert_tile_id = alert_tile_id  # type: str
        # The type of the alert. The value varies based on the display language (Chinese or English) of the Security Center console.
        self.alert_type = alert_type  # type: str
        # The ID of the alert type.
        self.alert_type_id = alert_type_id  # type: str
        # The information about the entities for which you need to add the alert to the whitelist.
        self.targets = targets  # type: list[DescribeAlertSceneResponseBodyDataTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAlertSceneResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSceneResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneByEventRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        # The ID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneByEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSceneByEventResponseBodyDataTargets(TeaModel):
    def __init__(self, name=None, type=None, value=None, values=None):
        # The display name of the entity attribute field that can be added to the whitelist.
        self.name = name  # type: str
        # The entity attribute field that can be added to the whitelist.
        self.type = type  # type: str
        # The right operand that is displayed by default in the whitelist rule.
        self.value = value  # type: str
        # The supported right operands of the whitelist rule.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneByEventResponseBodyData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_tile=None, alert_tile_id=None, alert_type=None,
                 alert_type_id=None, targets=None):
        # The alert name. The display name of the alert name varies based on the language of the system, such as Chinese and English.
        self.alert_name = alert_name  # type: str
        # The ID of the alert name.
        self.alert_name_id = alert_name_id  # type: str
        # The alert title. The display name of the alert title varies based on the language of the system, such as Chinese and English.
        self.alert_tile = alert_tile  # type: str
        # The ID of the alert title.
        self.alert_tile_id = alert_tile_id  # type: str
        # The alert type. The display name of the alert type varies based on the language of the system, such as Chinese and English.
        self.alert_type = alert_type  # type: str
        # The ID of the alert type.
        self.alert_type_id = alert_type_id  # type: str
        # The objects that can be added to the whitelist.
        self.targets = targets  # type: list[DescribeAlertSceneByEventResponseBodyDataTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneByEventResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneByEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAlertSceneByEventResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSceneByEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneByEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSceneByEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertSceneByEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceRequest(TeaModel):
    def __init__(self, end_time=None, level=None, region_id=None, start_time=None):
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The risk levels. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.level = level  # type: list[str]
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.level is not None:
            result['Level'] = self.level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertSourceResponseBodyData(TeaModel):
    def __init__(self, source=None, source_name=None):
        # The internal code of the alert data source.
        self.source = source  # type: str
        # The name of the alert data source.
        self.source_name = source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAlertSourceResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceWithEventRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSourceWithEventResponseBodyData(TeaModel):
    def __init__(self, source=None, source_name=None):
        # The internal code of the alert data source.
        self.source = source  # type: str
        # The name of the alert data source.
        self.source_name = source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceWithEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAlertSourceWithEventResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSourceWithEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceWithEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSourceWithEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertSourceWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertTypeRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertTypeResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None):
        # The type of the risk.
        self.alert_type = alert_type  # type: str
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        return self


class DescribeAlertTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAlertTypeResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsRequest(TeaModel):
    def __init__(self, alert_title=None, alert_uuid=None, current_page=None, end_time=None, is_defend=None,
                 level=None, page_size=None, region_id=None, source=None, start_time=None, sub_user_id=None):
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # Specifies whether an attack is defended. Valid values:
        # 
        # *   0: detected.
        # *   1: blocked.
        self.is_defend = is_defend  # type: str
        # The risk level. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.level = level  # type: list[str]
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The source of the alert.
        self.source = source  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        # The attribute key.
        self.key = key  # type: str
        # The name of the key.
        self.key_name = key_name  # type: str
        # The value of the key.
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        # The description of the alert.
        self.alert_desc = alert_desc  # type: str
        # The internal code of the alert description.
        self.alert_desc_code = alert_desc_code  # type: str
        # The description of the alert in English.
        self.alert_desc_en = alert_desc_en  # type: str
        # The details of the alert.
        self.alert_detail = alert_detail  # type: str
        # The displayed details of the alert.
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsResponseBodyDataResponseDataAlertInfoList]
        # The threat level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.alert_level = alert_level  # type: str
        # The name of the alert.
        self.alert_name = alert_name  # type: str
        # The internal code of the alert name.
        self.alert_name_code = alert_name_code  # type: str
        # The name of the alert in English.
        self.alert_name_en = alert_name_en  # type: str
        # The service for which the alert associated with the event is generated.
        self.alert_src_prod = alert_src_prod  # type: str
        # The sub-module of ther alert source.
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The title of the alert in English.
        self.alert_title_en = alert_title_en  # type: str
        # The alert type.
        self.alert_type = alert_type  # type: str
        # The internal code of the alert type.
        self.alert_type_code = alert_type_code  # type: str
        # The type of the alert in English.
        self.alert_type_en = alert_type_en  # type: str
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The details of the asset.
        self.asset_list = asset_list  # type: str
        # The tag of the ATT\&CK attack.
        self.att_ck = att_ck  # type: str
        # The cloud code. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The time when the alert was closed.
        self.end_time = end_time  # type: str
        # The time when the alert was received.
        self.gmt_create = gmt_create  # type: str
        # The time when the alert was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The unique ID of the alert.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # Indicates whether an attack is defended. Valid values:
        # 
        # *   0: detected.
        # *   1: blocked.
        self.is_defend = is_defend  # type: str
        # The time when the alert was recorded.
        self.log_time = log_time  # type: str
        # The UUID of the alert log.
        self.log_uuid = log_uuid  # type: str
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id  # type: long
        # The time when the alert is triggered.
        self.occur_time = occur_time  # type: str
        # The time at which the alert was first generated.
        self.start_time = start_time  # type: str
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeAlertsResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeAlertsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeAlertsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeAlertsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsCountRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, start_time=None):
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertsCountResponseBodyData(TeaModel):
    def __init__(self, all=None, high=None, low=None, medium=None, product_num=None):
        # The total number of alerts.
        self.all = all  # type: long
        # The number of high-risk alerts.
        self.high = high  # type: long
        # The number of low-risk alerts.
        self.low = low  # type: long
        # The number of medium-risk alerts.
        self.medium = medium  # type: long
        # The number of connected services.
        self.product_num = product_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.high is not None:
            result['High'] = self.high
        if self.low is not None:
            result['Low'] = self.low
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.product_num is not None:
            result['ProductNum'] = self.product_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('ProductNum') is not None:
            self.product_num = m.get('ProductNum')
        return self


class DescribeAlertsCountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeAlertsCountResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeAlertsCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEntityRequest(TeaModel):
    def __init__(self, current_page=None, entity_id=None, incident_uuid=None, page_size=None, region_id=None,
                 sophon_task_id=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The ID of the entity.
        self.entity_id = entity_id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The ID of the SOAR handing policy.
        self.sophon_task_id = sophon_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeAlertsWithEntityResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        # The attribute key.
        self.key = key  # type: str
        # The name of the key.
        self.key_name = key_name  # type: str
        # The value of the key.
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        # The description of the alert.
        self.alert_desc = alert_desc  # type: str
        # The internal code of the alert description.
        self.alert_desc_code = alert_desc_code  # type: str
        # The alert description in English.
        self.alert_desc_en = alert_desc_en  # type: str
        # The details of the alert.
        self.alert_detail = alert_detail  # type: str
        # The displayed details of the alert.
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList]
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.alert_level = alert_level  # type: str
        # The name of the alert.
        self.alert_name = alert_name  # type: str
        # The internal code of the alert name.
        self.alert_name_code = alert_name_code  # type: str
        # The name of the alert.
        self.alert_name_en = alert_name_en  # type: str
        # The source of the alert.
        self.alert_src_prod = alert_src_prod  # type: str
        # The sub-module of the alert source.
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The alert title in English.
        self.alert_title_en = alert_title_en  # type: str
        # The type of the alert.
        self.alert_type = alert_type  # type: str
        # The internal code of the alert type.
        self.alert_type_code = alert_type_code  # type: str
        # The alert type in English.
        self.alert_type_en = alert_type_en  # type: str
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The details of the asset.
        self.asset_list = asset_list  # type: str
        # The tag of the ATT\&CK attack.
        self.att_ck = att_ck  # type: str
        # The cloud code. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The time when the alert was closed.
        self.end_time = end_time  # type: str
        # The time when the alert was received.
        self.gmt_create = gmt_create  # type: str
        # The time when the alert was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The unique ID of the alert.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # Specifies whether an attack is defended. Valid values:
        # 
        # *   0: detected
        # *   1: blocked
        self.is_defend = is_defend  # type: str
        # The time when the alert was recorded.
        self.log_time = log_time  # type: str
        # The UUID of the alert log.
        self.log_uuid = log_uuid  # type: str
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id  # type: long
        # The time when the alert was triggered.
        self.occur_time = occur_time  # type: str
        # The time at which the alert was first generated.
        self.start_time = start_time  # type: str
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEntityResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeAlertsWithEntityResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeAlertsWithEntityResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEntityResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEntityResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeAlertsWithEntityResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeAlertsWithEntityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsWithEntityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertsWithEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEventRequest(TeaModel):
    def __init__(self, alert_title=None, current_page=None, incident_uuid=None, is_defend=None, level=None,
                 page_size=None, region_id=None, source=None, sub_user_id=None):
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The ID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # Specifies whether an attack is defended. Valid values:
        # 
        # *   0: detected
        # *   1: blocked
        self.is_defend = is_defend  # type: str
        # The risk levels. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.level = level  # type: list[str]
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The data source of the alert.
        self.source = source  # type: str
        # The ID of the account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        # The attribute key.
        self.key = key  # type: str
        # The name of the key.
        self.key_name = key_name  # type: str
        # The value of the key.
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        # The description of the alert.
        self.alert_desc = alert_desc  # type: str
        # The internal code of the alert description.
        self.alert_desc_code = alert_desc_code  # type: str
        # The alert description in English.
        self.alert_desc_en = alert_desc_en  # type: str
        # The details of the alert.
        self.alert_detail = alert_detail  # type: str
        # The displayed details of the alert.
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList]
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.alert_level = alert_level  # type: str
        # The name of the alert.
        self.alert_name = alert_name  # type: str
        # The internal code of the alert name.
        self.alert_name_code = alert_name_code  # type: str
        # The alert name in English.
        self.alert_name_en = alert_name_en  # type: str
        # The source of the alert.
        self.alert_src_prod = alert_src_prod  # type: str
        # The sub-module of the alert source.
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The alert title in English.
        self.alert_title_en = alert_title_en  # type: str
        # The type of the alert.
        self.alert_type = alert_type  # type: str
        # The internal code of the alert type.
        self.alert_type_code = alert_type_code  # type: str
        # The alert type in English.
        self.alert_type_en = alert_type_en  # type: str
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The details of the asset.
        self.asset_list = asset_list  # type: str
        # The tag of the ATT\&CK attack.
        self.att_ck = att_ck  # type: str
        # The cloud code. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The time when the alert was closed.
        self.end_time = end_time  # type: str
        # The time when the alert was received.
        self.gmt_create = gmt_create  # type: str
        # The time when the alert was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The unique ID of the alert.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # Indicates whether an attack is defended. Valid values:
        # 
        # *   0: detected
        # *   1: blocked
        self.is_defend = is_defend  # type: str
        # The time when the alert was recorded.
        self.log_time = log_time  # type: str
        # The UUID of the alert log.
        self.log_uuid = log_uuid  # type: str
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id  # type: long
        # The time when the alert was triggered.
        self.occur_time = occur_time  # type: str
        # The time at which the alert was first generated.
        self.start_time = start_time  # type: str
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeAlertsWithEventResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeAlertsWithEventResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEventResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeAlertsWithEventResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeAlertsWithEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsWithEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlertsWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackTimeLineRequest(TeaModel):
    def __init__(self, asset_name=None, end_time=None, incident_uuid=None, region_id=None, start_time=None):
        # The name of the asset.
        self.asset_name = asset_name  # type: str
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackTimeLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAttackTimeLineResponseBodyData(TeaModel):
    def __init__(self, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_time=None, alert_title=None, alert_title_en=None,
                 alert_type=None, alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_id=None, asset_list=None,
                 asset_name=None, att_ck=None, cloud_code=None, incident_uuid=None, log_time=None):
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.alert_level = alert_level  # type: str
        # The alert name in English.
        self.alert_name = alert_name  # type: str
        # The internal code of the alert name.
        self.alert_name_code = alert_name_code  # type: str
        # The alert name in English.
        self.alert_name_en = alert_name_en  # type: str
        # The source of the alert.
        self.alert_src_prod = alert_src_prod  # type: str
        # The sub-module of the alert source.
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        # The time when the alert was triggered.
        self.alert_time = alert_time  # type: long
        # The title of the alert.
        self.alert_title = alert_title  # type: str
        # The alert title in English.
        self.alert_title_en = alert_title_en  # type: str
        # The type of the alert.
        self.alert_type = alert_type  # type: str
        # The internal code of the alert type.
        self.alert_type_code = alert_type_code  # type: str
        # The alert type in English.
        self.alert_type_en = alert_type_en  # type: str
        # The UUID of the alert
        self.alert_uuid = alert_uuid  # type: str
        # The logical ID of the asset.
        self.asset_id = asset_id  # type: str
        # The details of the asset.
        self.asset_list = asset_list  # type: str
        # The name of the asset.
        self.asset_name = asset_name  # type: str
        # The tag of the ATT\&CK attack.
        self.att_ck = att_ck  # type: str
        # The cloud code. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The time when the alert was recorded.
        self.log_time = log_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        return self


class DescribeAttackTimeLineResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAttackTimeLineResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAttackTimeLineResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAttackTimeLineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAttackTimeLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAttackTimeLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuthRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAuthResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the SIEM system is granted the required permissions. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuthResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigCounterRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigCounterResponseBodyData(TeaModel):
    def __init__(self, all=None, online=None):
        # The total number of rules.
        self.all = all  # type: long
        # The number of enabled rules.
        self.online = online  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class DescribeAutomateResponseConfigCounterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeAutomateResponseConfigCounterResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeAutomateResponseConfigCounterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigCounterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigCounterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAutomateResponseConfigCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigFeatureRequest(TeaModel):
    def __init__(self, auto_response_type=None, region_id=None):
        # The type of the automated response rule. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums(TeaModel):
    def __init__(self, value=None, value_mds=None):
        # The enumerated value of the right operand.
        self.value = value  # type: str
        # The internal code of the enumerated value.
        self.value_mds = value_mds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_mds is not None:
            result['ValueMds'] = self.value_mds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueMds') is not None:
            self.value_mds = m.get('ValueMds')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators(TeaModel):
    def __init__(self, has_right_value=None, index=None, operator=None, operator_desc_cn=None,
                 operator_desc_en=None, operator_name=None, support_data_type=None, support_tag=None):
        # Indicates whether the right operand is required. Valid values:
        # 
        # *   true
        # *   false
        self.has_right_value = has_right_value  # type: bool
        # The position of the operator in the operator list.
        self.index = index  # type: int
        # The operator.
        self.operator = operator  # type: str
        # The description of the operator in Chinese.
        self.operator_desc_cn = operator_desc_cn  # type: str
        # The description of the operator in English.
        self.operator_desc_en = operator_desc_en  # type: str
        # The display name of the operator.
        self.operator_name = operator_name  # type: str
        # The data types that are supported by the current operator. The data types are separated by commas (,).
        self.support_data_type = support_data_type  # type: str
        # The scenarios that are supported by the operator. Multiple scenarios are separated by commas (,), such as aggregation scenarios. This parameter is empty by default.
        self.support_tag = support_tag  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_right_value is not None:
            result['HasRightValue'] = self.has_right_value
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasRightValue') is not None:
            self.has_right_value = m.get('HasRightValue')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyData(TeaModel):
    def __init__(self, data_type=None, feature=None, right_value_enums=None, support_operators=None):
        # The data type of the condition field in the automated response rule.
        self.data_type = data_type  # type: str
        # The name of the condition field in the automated response rule.
        self.feature = feature  # type: str
        # The enumerated values of the right operand for the field.
        self.right_value_enums = right_value_enums  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums]
        # The operators that are supported for the condition field.
        self.support_operators = support_operators  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators]

    def validate(self):
        if self.right_value_enums:
            for k in self.right_value_enums:
                if k:
                    k.validate()
        if self.support_operators:
            for k in self.support_operators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.feature is not None:
            result['Feature'] = self.feature
        result['RightValueEnums'] = []
        if self.right_value_enums is not None:
            for k in self.right_value_enums:
                result['RightValueEnums'].append(k.to_map() if k else None)
        result['SupportOperators'] = []
        if self.support_operators is not None:
            for k in self.support_operators:
                result['SupportOperators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        self.right_value_enums = []
        if m.get('RightValueEnums') is not None:
            for k in m.get('RightValueEnums'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums()
                self.right_value_enums.append(temp_model.from_map(k))
        self.support_operators = []
        if m.get('SupportOperators') is not None:
            for k in m.get('SupportOperators'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators()
                self.support_operators.append(temp_model.from_map(k))
        return self


class DescribeAutomateResponseConfigFeatureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigFeatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAutomateResponseConfigFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigPlayBooksRequest(TeaModel):
    def __init__(self, auto_response_type=None, entity_type=None, region_id=None):
        # The type of the automated response rule. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type  # type: str
        # The entity type of the playbook. Valid values:
        # 
        # *   ip
        # *   process
        # *   file
        self.entity_type = entity_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBodyData(TeaModel):
    def __init__(self, description=None, display_name=None, name=None, param_type=None, uuid=None):
        # The description of the playbook.
        self.description = description  # type: str
        # The display name of the playbook.
        self.display_name = display_name  # type: str
        # The unique identifier name of the playbook.
        self.name = name  # type: str
        # The input parameter template of the playbook. Valid values:
        # 
        # *   template-ip: IP address
        # *   template-process: process
        # *   template-filee: file
        self.param_type = param_type  # type: str
        # The UUID of the playbook.
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeAutomateResponseConfigPlayBooksResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAutomateResponseConfigPlayBooksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigPlayBooksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigPlayBooksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAutomateResponseConfigPlayBooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsRequest(TeaModel):
    def __init__(self, asset_type=None, current_page=None, incident_uuid=None, page_size=None, region_id=None):
        # The type of the asset. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.asset_type = asset_type  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        # The attribute key.
        self.key = key  # type: str
        # The name of the key.
        self.key_name = key_name  # type: str
        # The value of the key.
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_uuid=None, aliuid=None, asset_id=None, asset_info=None, asset_name=None,
                 asset_type=None, cloud_code=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None,
                 sub_user_id=None):
        # The UUID of the alert associated with the event.
        self.alert_uuid = alert_uuid  # type: str
        # The ID of the Alibaba Cloud account in SIEM.
        self.aliuid = aliuid  # type: long
        # The logical ID of the asset.
        self.asset_id = asset_id  # type: str
        # The display information of the asset is in the JSON format.
        self.asset_info = asset_info  # type: list[DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo]
        # The name of the asset.
        self.asset_name = asset_name  # type: str
        # The type of the asset. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.asset_type = asset_type  # type: str
        # The cloud code of the entity. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The time when the asset was synchronized.
        self.gmt_create = gmt_create  # type: str
        # The time when the asset was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the asset.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The ID of the associated account to which the asset belongs.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.asset_info:
            for k in self.asset_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        result['AssetInfo'] = []
        if self.asset_info is not None:
            for k in self.asset_info:
                result['AssetInfo'].append(k.to_map() if k else None)
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        self.asset_info = []
        if m.get('AssetInfo') is not None:
            for k in m.get('AssetInfo'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo()
                self.asset_info.append(temp_model.from_map(k))
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeCloudSiemAssetsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeCloudSiemAssetsResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeCloudSiemAssetsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemAssetsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemAssetsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCloudSiemAssetsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCloudSiemAssetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemAssetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCloudSiemAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsCounterRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsCounterResponseBodyData(TeaModel):
    def __init__(self, asset_num=None, asset_type=None):
        # The number of assets.
        self.asset_num = asset_num  # type: int
        # The type of the asset. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.asset_type = asset_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        return self


class DescribeCloudSiemAssetsCounterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeCloudSiemAssetsCounterResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCloudSiemAssetsCounterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsCounterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemAssetsCounterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCloudSiemAssetsCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventDetailRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemEventDetailResponseBodyData(TeaModel):
    def __init__(self, alert_num=None, aliuid=None, asset_num=None, att_ck_labels=None, data_sources=None,
                 description=None, description_en=None, ext_content=None, gmt_create=None, gmt_modified=None,
                 incident_name=None, incident_name_en=None, incident_uuid=None, remark=None, status=None, threat_level=None,
                 threat_score=None):
        # The number of alerts that are associated with the event.
        self.alert_num = alert_num  # type: int
        # The ID of the Alibaba Cloud account to which the event belongs.
        self.aliuid = aliuid  # type: long
        # The number of assets that are associated with the event.
        self.asset_num = asset_num  # type: int
        # The tags of the ATT\&CK attacks.
        self.att_ck_labels = att_ck_labels  # type: list[str]
        # The source of the alert.
        self.data_sources = data_sources  # type: list[str]
        # The description of the event.
        self.description = description  # type: str
        # The description of the event in English.
        self.description_en = description_en  # type: str
        # The extended information of the event in the JSON format.
        self.ext_content = ext_content  # type: str
        # The time when the event occurred.
        self.gmt_create = gmt_create  # type: str
        # The time when the event was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The name of the event.
        self.incident_name = incident_name  # type: str
        # The name of the event in English.
        self.incident_name_en = incident_name_en  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The remarks of the event.
        self.remark = remark  # type: str
        # The status of the event. Valid values:
        # 
        # *   0: not handled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status  # type: int
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str
        # The risk score of the event. The score ranges from 0 to 100. A higher score indicates a higher risk level.
        self.threat_score = threat_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCloudSiemEventDetailResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCloudSiemEventDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemEventDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCloudSiemEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventsRequest(TeaModel):
    def __init__(self, asset_id=None, current_page=None, end_time=None, event_name=None, incident_uuid=None,
                 order=None, order_field=None, page_size=None, region_id=None, start_time=None, status=None,
                 thread_level=None):
        # The ID of the asset that is associated with the event.
        self.asset_id = asset_id  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The name of the event.
        self.event_name = event_name  # type: str
        # The ID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The sort order. Valid values:
        # 
        # *   desc: descending order
        # *   asc: ascending order
        self.order = order  # type: str
        # The sort field. Valid values:
        # 
        # *   GmtModified: sorts the events by creation time. This is the default value.
        # *   ThreatScore: sorts the events by risk score.
        self.order_field = order_field  # type: str
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handling
        # *   5: handling failed
        # *   10: handled
        self.status = status  # type: int
        # The risk levels of the events. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.thread_level = thread_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.thread_level is not None:
            result['ThreadLevel'] = self.thread_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreadLevel') is not None:
            self.thread_level = m.get('ThreadLevel')
        return self


class DescribeCloudSiemEventsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemEventsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_num=None, aliuid=None, asset_num=None, att_ck_labels=None, data_sources=None,
                 description=None, description_en=None, ext_content=None, gmt_create=None, gmt_modified=None,
                 incident_name=None, incident_name_en=None, incident_uuid=None, remark=None, status=None, threat_level=None,
                 threat_score=None):
        # The number of alerts that are associated with the event.
        self.alert_num = alert_num  # type: int
        # The ID of the Alibaba Cloud account to which the event belongs.
        self.aliuid = aliuid  # type: long
        # The number of assets that are associated with the event.
        self.asset_num = asset_num  # type: int
        # The tags of the ATT\&CK attack.
        self.att_ck_labels = att_ck_labels  # type: list[str]
        # The sources of the alert.
        self.data_sources = data_sources  # type: list[str]
        # The description of the event.
        self.description = description  # type: str
        # The event description in English.
        self.description_en = description_en  # type: str
        # The extended event information in the JSON format.
        self.ext_content = ext_content  # type: str
        # The time when the event occurred.
        self.gmt_create = gmt_create  # type: str
        # The time when the event was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The name of the event.
        self.incident_name = incident_name  # type: str
        # The event name in English.
        self.incident_name_en = incident_name_en  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The remarks of the event.
        self.remark = remark  # type: str
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handling
        # *   5: handling failed
        # *   10: handled
        self.status = status  # type: int
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str
        # The risk score of the event. Valid values: 0 to 100. A higher value indicates a higher risk level.
        self.threat_score = threat_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeCloudSiemEventsResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeCloudSiemEventsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemEventsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemEventsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemEventsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCloudSiemEventsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCloudSiemEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCloudSiemEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCsImportedProdStatusByUserRequest(TeaModel):
    def __init__(self, region_id=None, source_log_prod=None, user_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The code of the cloud service.
        self.source_log_prod = source_log_prod  # type: str
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCsImportedProdStatusByUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_prod is not None:
            result['SourceLogProd'] = self.source_log_prod
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogProd') is not None:
            self.source_log_prod = m.get('SourceLogProd')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCsImportedProdStatusByUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the cloud service is activated for the account. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCsImportedProdStatusByUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCsImportedProdStatusByUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCsImportedProdStatusByUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCsImportedProdStatusByUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCsImportedProdStatusByUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleRequest(TeaModel):
    def __init__(self, region_id=None, rule_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The ID of the rule.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeCustomizeRuleResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        # The risk type.
        self.alert_type = alert_type  # type: str
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds  # type: str
        # The ID of the Alibaba Cloud account in SIEM.
        self.aliuid = aliuid  # type: long
        # The extended information about event generation. If the value of eventTransferType is allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window. The HTML escape characters are reversed.
        self.event_transfer_ext = event_transfer_ext  # type: str
        # Indicates whether the alert generates an event. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.event_transfer_switch = event_transfer_switch  # type: int
        # The event generation method. Valid values:
        # 
        # *   default: The default method is used.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type  # type: str
        # The time when the custom rule was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the custom rule was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the custom rule.
        self.id = id  # type: long
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The internal code of the log source.
        self.log_source_mds = log_source_mds  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The internal code of the log type.
        self.log_type_mds = log_type_mds  # type: str
        # The window length of the rule. The HTML escape characters are reversed.
        self.query_cycle = query_cycle  # type: str
        # The query condition of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_condition = rule_condition  # type: str
        # The description of the rule.
        self.rule_desc = rule_desc  # type: str
        # The log aggregation field. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_group = rule_group  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The threshold configuration of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_threshold = rule_threshold  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str
        # The rule status. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class DescribeCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCustomizeRuleResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleCountRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleCountResponseBodyData(TeaModel):
    def __init__(self, high_rule_num=None, in_use_rule_num=None, low_rule_num=None, medium_rule_num=None):
        # The number of rules that are used to identify high-risk threats.
        self.high_rule_num = high_rule_num  # type: int
        # The total number of rules.
        self.in_use_rule_num = in_use_rule_num  # type: int
        # The number of rules that are used to identify low-risk threats.
        self.low_rule_num = low_rule_num  # type: int
        # The number of rules that are used to identify medium-risk threats.
        self.medium_rule_num = medium_rule_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.high_rule_num is not None:
            result['HighRuleNum'] = self.high_rule_num
        if self.in_use_rule_num is not None:
            result['InUseRuleNum'] = self.in_use_rule_num
        if self.low_rule_num is not None:
            result['LowRuleNum'] = self.low_rule_num
        if self.medium_rule_num is not None:
            result['MediumRuleNum'] = self.medium_rule_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HighRuleNum') is not None:
            self.high_rule_num = m.get('HighRuleNum')
        if m.get('InUseRuleNum') is not None:
            self.in_use_rule_num = m.get('InUseRuleNum')
        if m.get('LowRuleNum') is not None:
            self.low_rule_num = m.get('LowRuleNum')
        if m.get('MediumRuleNum') is not None:
            self.medium_rule_num = m.get('MediumRuleNum')
        return self


class DescribeCustomizeRuleCountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCustomizeRuleCountResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCustomizeRuleCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomizeRuleCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestResponseBodyData(TeaModel):
    def __init__(self, id=None, simulate_data=None, status=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The historical data that is used in the simulation test.
        self.simulate_data = simulate_data  # type: str
        # The status of the rule. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.simulate_data is not None:
            result['SimulateData'] = self.simulate_data
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SimulateData') is not None:
            self.simulate_data = m.get('SimulateData')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeCustomizeRuleTestResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeCustomizeRuleTestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestHistogramRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestHistogramResponseBodyData(TeaModel):
    def __init__(self, count=None, from_=None, to=None):
        # The number of alerts that are generated in the query time range.
        self.count = count  # type: long
        # The start of the time range for querying alerts. The value is a UNIX timestamp. Unit: seconds.
        self.from_ = from_  # type: long
        # The end of the time range for querying alerts. The value is a UNIX timestamp. Unit: seconds.
        self.to = to  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeCustomizeRuleTestHistogramResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeCustomizeRuleTestHistogramResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCustomizeRuleTestHistogramResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestHistogramResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleTestHistogramResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomizeRuleTestHistogramResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSourceInstanceRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSourceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams(TeaModel):
    def __init__(self, para_code=None, para_value=None):
        # The code of the parameter.
        self.para_code = para_code  # type: str
        # The value of the parameter.
        self.para_value = para_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        return self


class DescribeDataSourceInstanceResponseBodyData(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None,
                 data_source_instance_params=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The parameters of the data source.
        self.data_source_instance_params = data_source_instance_params  # type: list[DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams]

    def validate(self):
        if self.data_source_instance_params:
            for k in self.data_source_instance_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSourceInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        result['DataSourceInstanceParams'] = []
        if self.data_source_instance_params is not None:
            for k in self.data_source_instance_params:
                result['DataSourceInstanceParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        self.data_source_instance_params = []
        if m.get('DataSourceInstanceParams') is not None:
            for k in m.get('DataSourceInstanceParams'):
                temp_model = DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams()
                self.data_source_instance_params.append(temp_model.from_map(k))
        return self


class DescribeDataSourceInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DescribeDataSourceInstanceResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDataSourceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDataSourceInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataSourceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataSourceInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataSourceInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataSourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataSourceParametersRequest(TeaModel):
    def __init__(self, cloud_code=None, data_source_type=None, region_id=None):
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        # *   aliyun
        self.cloud_code = cloud_code  # type: str
        # The type of the data source. Valid values:
        # 
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        self.data_source_type = data_source_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSourceParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataSourceParametersResponseBodyDataParamValue(TeaModel):
    def __init__(self, label=None, value=None):
        # The display value.
        self.label = label  # type: str
        # The actual value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataSourceParametersResponseBodyDataParamValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDataSourceParametersResponseBodyData(TeaModel):
    def __init__(self, can_editted=None, cloud_code=None, data_source_type=None, default_value=None, disabled=None,
                 format_check=None, hit=None, para_code=None, para_level=None, para_name=None, para_type=None, param_value=None,
                 required=None, title=None):
        # Indicates whether the edit operation is supported. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.can_editted = can_editted  # type: int
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud OBS
        # *   wafApi: download API of Tencent Cloud WAF
        # *   ckafka: Tencent Cloud CKafka
        self.data_source_type = data_source_type  # type: str
        # The default value of the parameter.
        self.default_value = default_value  # type: str
        # Indicates whether the modification operation is forbidden. Valid values:
        # 
        # *   true
        # *   false
        self.disabled = disabled  # type: bool
        # The method that is used to check the parameter format.
        self.format_check = format_check  # type: str
        # The additional information.
        self.hit = hit  # type: str
        # The code of the parameter.
        self.para_code = para_code  # type: str
        # The parameter level. Valid values:
        # 
        # *   1: data source
        # *   2: log
        self.para_level = para_level  # type: int
        # The name of the parameter.
        self.para_name = para_name  # type: str
        # The data type of the parameter.
        self.para_type = para_type  # type: str
        # The value of the parameter.
        self.param_value = param_value  # type: list[DescribeDataSourceParametersResponseBodyDataParamValue]
        # Indicates whether the parameter is required. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.required = required  # type: int
        # The note on the parameter value.
        self.title = title  # type: str

    def validate(self):
        if self.param_value:
            for k in self.param_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSourceParametersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_editted is not None:
            result['CanEditted'] = self.can_editted
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.format_check is not None:
            result['FormatCheck'] = self.format_check
        if self.hit is not None:
            result['Hit'] = self.hit
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_level is not None:
            result['ParaLevel'] = self.para_level
        if self.para_name is not None:
            result['ParaName'] = self.para_name
        if self.para_type is not None:
            result['ParaType'] = self.para_type
        result['ParamValue'] = []
        if self.param_value is not None:
            for k in self.param_value:
                result['ParamValue'].append(k.to_map() if k else None)
        if self.required is not None:
            result['Required'] = self.required
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanEditted') is not None:
            self.can_editted = m.get('CanEditted')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('FormatCheck') is not None:
            self.format_check = m.get('FormatCheck')
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')
        if m.get('ParaName') is not None:
            self.para_name = m.get('ParaName')
        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')
        self.param_value = []
        if m.get('ParamValue') is not None:
            for k in m.get('ParamValue'):
                temp_model = DescribeDataSourceParametersResponseBodyDataParamValue()
                self.param_value.append(temp_model.from_map(k))
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeDataSourceParametersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[DescribeDataSourceParametersResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataSourceParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDataSourceParametersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataSourceParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataSourceParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataSourceParametersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataSourceParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeAndPlaybookRequest(TeaModel):
    def __init__(self, current_page=None, entity_type=None, incident_uuid=None, page_size=None, region_id=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The entity type. Valid values:
        # 
        # *   ip: IP address
        # *   process: process
        # *   file: file
        self.entity_type = entity_type  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList(TeaModel):
    def __init__(self, description=None, display_name=None, name=None, op_code=None, op_level=None,
                 param_config=None, task_config=None, waf_playbook=None):
        # The playbook description.
        self.description = description  # type: str
        # The display name of the playbook.
        self.display_name = display_name  # type: str
        # The playbook name, which is the unique identifier of the playbook.
        self.name = name  # type: str
        # The opcode of the playbook, which corresponds to the opcode of the playbook recommended for entity handling.
        self.op_code = op_code  # type: str
        # Indicates whether quick event handling is selected by default. Valid values:
        # 
        # *   2: Quick event handling is selected.
        # *   1: Quick event handling is displayed but not selected.
        self.op_level = op_level  # type: str
        self.param_config = param_config  # type: list[any]
        # The opcode configuration.
        self.task_config = task_config  # type: str
        # Indicates whether the playbook is intended for Web Application Firewall (WAF). Valid values:
        # 
        # *   true
        # *   false
        self.waf_playbook = waf_playbook  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.op_code is not None:
            result['OpCode'] = self.op_code
        if self.op_level is not None:
            result['OpLevel'] = self.op_level
        if self.param_config is not None:
            result['ParamConfig'] = self.param_config
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config
        if self.waf_playbook is not None:
            result['WafPlaybook'] = self.waf_playbook
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OpCode') is not None:
            self.op_code = m.get('OpCode')
        if m.get('OpLevel') is not None:
            self.op_level = m.get('OpLevel')
        if m.get('ParamConfig') is not None:
            self.param_config = m.get('ParamConfig')
        if m.get('TaskConfig') is not None:
            self.task_config = m.get('TaskConfig')
        if m.get('WafPlaybook') is not None:
            self.waf_playbook = m.get('WafPlaybook')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_num=None, dispose=None, entity_id=None, entity_info=None, opcode_map=None,
                 opcode_set=None, playbook_list=None, scope=None):
        # The number of alerts that are associated with the entity.
        self.alert_num = alert_num  # type: int
        # The object for handling.
        self.dispose = dispose  # type: str
        # The entity ID
        self.entity_id = entity_id  # type: long
        # The entity information.
        self.entity_info = entity_info  # type: dict[str, any]
        # The key-value pairs each of which consists of opcode and oplevel.
        self.opcode_map = opcode_map  # type: dict[str, str]
        # An array consisting of the codes of playbooks that are recommended for entity handling.
        self.opcode_set = opcode_set  # type: list[str]
        # The playbooks that can handle the entity.
        self.playbook_list = playbook_list  # type: list[DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList]
        # An array consisting of the IDs of the users who can handle objects.
        self.scope = scope  # type: list[any]

    def validate(self):
        if self.playbook_list:
            for k in self.playbook_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.dispose is not None:
            result['Dispose'] = self.dispose
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.opcode_map is not None:
            result['OpcodeMap'] = self.opcode_map
        if self.opcode_set is not None:
            result['OpcodeSet'] = self.opcode_set
        result['PlaybookList'] = []
        if self.playbook_list is not None:
            for k in self.playbook_list:
                result['PlaybookList'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Dispose') is not None:
            self.dispose = m.get('Dispose')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('OpcodeMap') is not None:
            self.opcode_map = m.get('OpcodeMap')
        if m.get('OpcodeSet') is not None:
            self.opcode_set = m.get('OpcodeSet')
        self.playbook_list = []
        if m.get('PlaybookList') is not None:
            for k in m.get('PlaybookList'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList()
                self.playbook_list.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DescribeDisposeAndPlaybookResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeDisposeAndPlaybookResponseBodyDataPageInfo
        # The detailed data
        self.response_data = response_data  # type: list[DescribeDisposeAndPlaybookResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeDisposeAndPlaybookResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeDisposeAndPlaybookResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeDisposeAndPlaybookResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeDisposeAndPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeAndPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDisposeAndPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDisposeAndPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeStrategyPlaybookRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, start_time=None):
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDisposeStrategyPlaybookResponseBodyData(TeaModel):
    def __init__(self, playbook_name=None, playbook_uuid=None):
        # The playbook name, which is the unique identifier of the playbook.
        self.playbook_name = playbook_name  # type: str
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeDisposeStrategyPlaybookResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeDisposeStrategyPlaybookResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDisposeStrategyPlaybookResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeStrategyPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDisposeStrategyPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDisposeStrategyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntityInfoRequest(TeaModel):
    def __init__(self, entity_id=None, entity_identity=None, incident_uuid=None, region_id=None,
                 sophon_task_id=None):
        # The logical ID of the entity.
        self.entity_id = entity_id  # type: long
        # The feature value of the entity. Fuzzy match is supported.
        self.entity_identity = entity_identity  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The ID of the SOAR handling policy.
        self.sophon_task_id = sophon_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntityInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeEntityInfoResponseBodyData(TeaModel):
    def __init__(self, entity_id=None, entity_info=None, entity_type=None, tip_info=None):
        # The logical ID of the entity.
        self.entity_id = entity_id  # type: long
        # The information about the entry.
        self.entity_info = entity_info  # type: dict[str, any]
        # The type of the entity. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.entity_type = entity_type  # type: str
        # The information about the risk Intelligence.
        self.tip_info = tip_info  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntityInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.tip_info is not None:
            result['TipInfo'] = self.tip_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('TipInfo') is not None:
            self.tip_info = m.get('TipInfo')
        return self


class DescribeEntityInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeEntityInfoResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEntityInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeEntityInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEntityInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEntityInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEntityInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEntityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventCountByThreatLevelRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEventCountByThreatLevelResponseBodyData(TeaModel):
    def __init__(self, event_num=None, high_level_event_num=None, low_level_event_num=None,
                 medium_level_event_num=None, undeal_event_num=None):
        # The total number of events.
        self.event_num = event_num  # type: long
        # The number of high-risk events.
        self.high_level_event_num = high_level_event_num  # type: long
        # The number of low-risk events.
        self.low_level_event_num = low_level_event_num  # type: long
        # The number of medium-risk events.
        self.medium_level_event_num = medium_level_event_num  # type: long
        # The number of unhandled events.
        self.undeal_event_num = undeal_event_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_num is not None:
            result['EventNum'] = self.event_num
        if self.high_level_event_num is not None:
            result['HighLevelEventNum'] = self.high_level_event_num
        if self.low_level_event_num is not None:
            result['LowLevelEventNum'] = self.low_level_event_num
        if self.medium_level_event_num is not None:
            result['MediumLevelEventNum'] = self.medium_level_event_num
        if self.undeal_event_num is not None:
            result['UndealEventNum'] = self.undeal_event_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')
        if m.get('HighLevelEventNum') is not None:
            self.high_level_event_num = m.get('HighLevelEventNum')
        if m.get('LowLevelEventNum') is not None:
            self.low_level_event_num = m.get('LowLevelEventNum')
        if m.get('MediumLevelEventNum') is not None:
            self.medium_level_event_num = m.get('MediumLevelEventNum')
        if m.get('UndealEventNum') is not None:
            self.undeal_event_num = m.get('UndealEventNum')
        return self


class DescribeEventCountByThreatLevelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeEventCountByThreatLevelResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeEventCountByThreatLevelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventCountByThreatLevelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventCountByThreatLevelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventCountByThreatLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventDisposeRequest(TeaModel):
    def __init__(self, current_page=None, incident_uuid=None, page_size=None, region_id=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDisposeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEventDisposeResponseBodyDataReceiverInfo(TeaModel):
    def __init__(self, channel=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None,
                 message_title=None, receiver=None, status=None):
        # The channel of the contact information. Valid values:
        # 
        # *   message
        # *   mail
        self.channel = channel  # type: str
        # The creation time.
        self.gmt_create = gmt_create  # type: str
        # The modification time.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the recipient who receives the event handling result.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The message title.
        self.message_title = message_title  # type: str
        # The contact information of the recipient.
        self.receiver = receiver  # type: str
        # Indicates whether the message is sent. Valid values:
        # 
        # *   0: not sent
        # *   1: sent
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBodyDataReceiverInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.message_title is not None:
            result['MessageTitle'] = self.message_title
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('MessageTitle') is not None:
            self.message_title = m.get('MessageTitle')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBodyData(TeaModel):
    def __init__(self, event_dispose=None, receiver_info=None, remark=None, status=None):
        # An array consisting of JSON objects that are configured for event handling.
        self.event_dispose = event_dispose  # type: list[any]
        # The JSON object that is configured for an alert recipient.
        self.receiver_info = receiver_info  # type: DescribeEventDisposeResponseBodyDataReceiverInfo
        # The description of the event.
        self.remark = remark  # type: str
        # The status of the event. Valid values:
        # 
        # *   0: not handled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status  # type: int

    def validate(self):
        if self.receiver_info:
            self.receiver_info.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info.to_map()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('ReceiverInfo') is not None:
            temp_model = DescribeEventDisposeResponseBodyDataReceiverInfo()
            self.receiver_info = temp_model.from_map(m['ReceiverInfo'])
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeEventDisposeResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeEventDisposeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventDisposeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventDisposeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventDisposeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportedLogCountRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImportedLogCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeImportedLogCountResponseBodyData(TeaModel):
    def __init__(self, imported_log_count=None, total_log_count=None, un_imported_log_count=None):
        # The number of logs that are added.
        self.imported_log_count = imported_log_count  # type: int
        # The total number of logs.
        self.total_log_count = total_log_count  # type: int
        # The number of logs that are not added.
        self.un_imported_log_count = un_imported_log_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImportedLogCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count
        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count
        if self.un_imported_log_count is not None:
            result['UnImportedLogCount'] = self.un_imported_log_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')
        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')
        if m.get('UnImportedLogCount') is not None:
            self.un_imported_log_count = m.get('UnImportedLogCount')
        return self


class DescribeImportedLogCountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DescribeImportedLogCountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeImportedLogCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeImportedLogCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImportedLogCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImportedLogCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImportedLogCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeImportedLogCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobStatusRequest(TeaModel):
    def __init__(self, region_id=None, submit_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The id of collection task.
        self.submit_id = submit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        return self


class DescribeJobStatusResponseBodyDataErrTaskListProductListLogList(TeaModel):
    def __init__(self, error_code=None, log_code=None, log_store_name_pattern=None, product_code=None,
                 project_name_pattern=None, region_code=None):
        # The error code.
        self.error_code = error_code  # type: str
        # The log code.
        self.log_code = log_code  # type: str
        # The pattern of SLS logstore name.
        self.log_store_name_pattern = log_store_name_pattern  # type: str
        # The code of product.
        self.product_code = product_code  # type: str
        # The pattern of SLS project name.
        self.project_name_pattern = project_name_pattern  # type: str
        # The ID of the region in which the instance resides.
        self.region_code = region_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyDataErrTaskListProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class DescribeJobStatusResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        # The list of log.
        self.log_list = log_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskListProductListLogList]
        # The code of product.
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyDataErrTaskListProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeJobStatusResponseBodyDataErrTaskList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        # The list of product.
        self.product_list = product_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskListProductList]
        # The account id of aliyun.
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyDataErrTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeJobStatusResponseBodyData(TeaModel):
    def __init__(self, config_id=None, err_task_list=None, failed_count=None, finish_count=None, folder_id=None,
                 task_count=None, task_status=None):
        # The ID of the task configuration.
        self.config_id = config_id  # type: str
        # The list of failed task.
        self.err_task_list = err_task_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskList]
        # The number of failed tasks.
        self.failed_count = failed_count  # type: int
        # The number of scan tasks that are complete.
        self.finish_count = finish_count  # type: int
        # The ID of the folder.
        self.folder_id = folder_id  # type: str
        # The number of existing tasks that are created to add logs within the data source.
        self.task_count = task_count  # type: int
        # The status of submitted task.
        self.task_status = task_status  # type: str

    def validate(self):
        if self.err_task_list:
            for k in self.err_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ErrTaskList'] = []
        if self.err_task_list is not None:
            for k in self.err_task_list:
                result['ErrTaskList'].append(k.to_map() if k else None)
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.err_task_list = []
        if m.get('ErrTaskList') is not None:
            for k in m.get('ErrTaskList'):
                temp_model = DescribeJobStatusResponseBodyDataErrTaskList()
                self.err_task_list.append(temp_model.from_map(k))
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeJobStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeJobStatusResponseBodyData
        # The error code.
        self.err_code = err_code  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = DescribeJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogFieldsRequest(TeaModel):
    def __init__(self, log_source=None, log_type=None, region_id=None):
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogFieldsResponseBodyData(TeaModel):
    def __init__(self, activity_name=None, field_desc=None, field_name=None, field_type=None, log_code=None):
        # The type of the log to which the field belongs.
        self.activity_name = activity_name  # type: str
        # The internal code of the field description.
        self.field_desc = field_desc  # type: str
        # The name of the field.
        self.field_name = field_name  # type: str
        # The data type of the field. Valid values:
        # 
        # *   varchar
        # *   bigint
        self.field_type = field_type  # type: str
        # The log source to which the field belongs.
        self.log_code = log_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogFieldsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.field_desc is not None:
            result['FieldDesc'] = self.field_desc
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('FieldDesc') is not None:
            self.field_desc = m.get('FieldDesc')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        return self


class DescribeLogFieldsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeLogFieldsResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogFieldsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogFieldsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogFieldsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogSourceRequest(TeaModel):
    def __init__(self, log_type=None, region_id=None):
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogSourceResponseBodyData(TeaModel):
    def __init__(self, log_source=None, log_source_name=None):
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The internal code of the log source.
        self.log_source_name = log_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_name is not None:
            result['LogSourceName'] = self.log_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceName') is not None:
            self.log_source_name = m.get('LogSourceName')
        return self


class DescribeLogSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeLogSourceResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogStoreResponseBodyData(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, log_store_name=None,
                 max_split_shard=None, shard_count=None, ttl=None):
        # Indicates whether the following time points are added after the log arrives: the time points when the public IP address of the client and the log arrive. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta  # type: bool
        # Indicates whether the automatic sharding feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split  # type: bool
        # Indicates whether the web tracking feature is enabled to collect user information from browsers, iOS applications, or Android applications. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking  # type: bool
        # The name of the Logstore in Simple Log Service.
        self.log_store_name = log_store_name  # type: str
        # The maximum number of shards that can be generated by using the automatic sharding feature.
        self.max_split_shard = max_split_shard  # type: int
        # The number of shards in Log Service.
        self.shard_count = shard_count  # type: int
        # The retention period of data. Unit: day.
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['AppendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['AutoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['EnableTracking'] = self.enable_tracking
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.max_split_shard is not None:
            result['MaxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppendMeta') is not None:
            self.append_meta = m.get('AppendMeta')
        if m.get('AutoSplit') is not None:
            self.auto_split = m.get('AutoSplit')
        if m.get('EnableTracking') is not None:
            self.enable_tracking = m.get('EnableTracking')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('MaxSplitShard') is not None:
            self.max_split_shard = m.get('MaxSplitShard')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeLogStoreResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response of the threat analysis feature.
        self.data = data  # type: DescribeLogStoreResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeLogStoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeLogStoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogStoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogStoreResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogTypeRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogTypeResponseBodyData(TeaModel):
    def __init__(self, log_type=None, log_type_name=None):
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The internal code of the log type.
        self.log_type_name = log_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_name is not None:
            result['LogTypeName'] = self.log_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeName') is not None:
            self.log_type_name = m.get('LogTypeName')
        return self


class DescribeLogTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeLogTypeResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOperatorsRequest(TeaModel):
    def __init__(self, region_id=None, scene_type=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The type of the scenario in which the operator is used. Valid values:
        # 
        # *   If you do not specify this parameter, the default scenario is used.
        # *   AGGREGATE: AGGREGATE scenario.
        self.scene_type = scene_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOperatorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class DescribeOperatorsResponseBodyData(TeaModel):
    def __init__(self, index=None, operator=None, operator_desc_cn=None, operator_desc_en=None, operator_name=None,
                 support_data_type=None, support_tag=None):
        # The position of the operator in the operator list.
        self.index = index  # type: int
        # The operator.
        self.operator = operator  # type: str
        # The description of the operator in Chinese.
        self.operator_desc_cn = operator_desc_cn  # type: str
        # The description of the operator in English.
        self.operator_desc_en = operator_desc_en  # type: str
        # The display name of the operator.
        self.operator_name = operator_name  # type: str
        # The data types that are supported by the current operator. The data types are separated by commas (,).
        self.support_data_type = support_data_type  # type: str
        # The scenarios that are supported by the operator. Multiple scenarios are separated by commas (,), such as AGGREGATE scenarios. This parameter is empty by default.
        self.support_tag = support_tag  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOperatorsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeOperatorsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeOperatorsResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOperatorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeOperatorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOperatorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOperatorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOperatorsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOperatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProdCountRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProdCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeProdCountResponseBodyData(TeaModel):
    def __init__(self, aliyun_prod_count=None, hcloud_prod_count=None, qcloud_prod_count=None):
        # The number of Alibaba Cloud services.
        self.aliyun_prod_count = aliyun_prod_count  # type: int
        # The number of Huawei Cloud services.
        self.hcloud_prod_count = hcloud_prod_count  # type: int
        # The number of Tencent Cloud services.
        self.qcloud_prod_count = qcloud_prod_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProdCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_prod_count is not None:
            result['AliyunProdCount'] = self.aliyun_prod_count
        if self.hcloud_prod_count is not None:
            result['HcloudProdCount'] = self.hcloud_prod_count
        if self.qcloud_prod_count is not None:
            result['QcloudProdCount'] = self.qcloud_prod_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunProdCount') is not None:
            self.aliyun_prod_count = m.get('AliyunProdCount')
        if m.get('HcloudProdCount') is not None:
            self.hcloud_prod_count = m.get('HcloudProdCount')
        if m.get('QcloudProdCount') is not None:
            self.qcloud_prod_count = m.get('QcloudProdCount')
        return self


class DescribeProdCountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DescribeProdCountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeProdCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeProdCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProdCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeProdCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProdCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProdCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScopeUsersRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScopeUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeScopeUsersResponseBodyData(TeaModel):
    def __init__(self, ali_uid=None, domains=None, instance_id=None, user_name=None):
        # The ID of the security information and event management (SIEM) user.
        self.ali_uid = ali_uid  # type: long
        # An array consisting of the domain names that are protected by the WAF instance.
        self.domains = domains  # type: list[str]
        # The ID of the Web Application Firewall (WAF) instance.
        self.instance_id = instance_id  # type: str
        # The username.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScopeUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeScopeUsersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeScopeUsersResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeScopeUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeScopeUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeScopeUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeScopeUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScopeUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScopeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceStatusRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the threat analysis feature is authorized to access the resource directory. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStorageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the projects and Logstores that are created for the threat analysis feature exist in Simple Log Service. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStorageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBuyStatusRequest(TeaModel):
    def __init__(self, region_id=None, sub_user_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserBuyStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeUserBuyStatusResponseBodyData(TeaModel):
    def __init__(self, can_buy=None, capacity=None, duration_days=None, end_time=None, main_user_id=None,
                 main_user_name=None, master_user_id=None, master_user_name=None, sas_instance_id=None, sub_user_id=None,
                 sub_user_name=None):
        # Indicates whether the logon Alibaba Cloud account can be used to place orders for the threat analysis feature, such as purchase, upgrade, and specifications change orders. Valid values:
        # 
        # *   true
        # *   false
        self.can_buy = can_buy  # type: bool
        # The log storage capacity that is purchased for the threat analysis feature. Unit: GB.
        self.capacity = capacity  # type: int
        # The number of days before the expiration time of the threat analysis feature.
        self.duration_days = duration_days  # type: long
        # The timestamp when the threat analysis feature expires. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The username of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_name = main_user_name  # type: str
        # The ID of the management account of the resource directory.
        self.master_user_id = master_user_id  # type: long
        # The display name of the management account of the resource directory.
        self.master_user_name = master_user_name  # type: str
        # The instance ID of Security Center.
        self.sas_instance_id = sas_instance_id  # type: str
        # The ID of the logon Alibaba Cloud account.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the logon Alibaba Cloud account.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserBuyStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_buy is not None:
            result['CanBuy'] = self.can_buy
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.duration_days is not None:
            result['DurationDays'] = self.duration_days
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.main_user_name is not None:
            result['MainUserName'] = self.main_user_name
        if self.master_user_id is not None:
            result['MasterUserId'] = self.master_user_id
        if self.master_user_name is not None:
            result['MasterUserName'] = self.master_user_name
        if self.sas_instance_id is not None:
            result['SasInstanceId'] = self.sas_instance_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanBuy') is not None:
            self.can_buy = m.get('CanBuy')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('DurationDays') is not None:
            self.duration_days = m.get('DurationDays')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('MainUserName') is not None:
            self.main_user_name = m.get('MainUserName')
        if m.get('MasterUserId') is not None:
            self.master_user_id = m.get('MasterUserId')
        if m.get('MasterUserName') is not None:
            self.master_user_name = m.get('MasterUserName')
        if m.get('SasInstanceId') is not None:
            self.sas_instance_id = m.get('SasInstanceId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class DescribeUserBuyStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: DescribeUserBuyStatusResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUserBuyStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserBuyStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBuyStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserBuyStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserBuyStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserBuyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafScopeRequest(TeaModel):
    def __init__(self, entity_id=None, region_id=None):
        # The ID of the entity.
        self.entity_id = entity_id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWafScopeResponseBodyData(TeaModel):
    def __init__(self, aliuid=None, domains=None, instance_id=None):
        # The ID of the Alibaba Cloud account in SIEM.
        self.aliuid = aliuid  # type: long
        # The domain names that are protected by the WAF instance.
        self.domains = domains  # type: list[str]
        # The ID of the WAF instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafScopeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeWafScopeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[DescribeWafScopeResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWafScopeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeWafScopeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWafScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWafScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWafScopeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWafScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhiteRuleListRequest(TeaModel):
    def __init__(self, alert_name=None, alert_type=None, current_page=None, incident_uuid=None, page_size=None,
                 region_id=None):
        # The name of the alert.
        self.alert_name = alert_name  # type: str
        # The type of the alert.
        self.alert_type = alert_type  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWhiteRuleListResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft(TeaModel):
    def __init__(self, is_var=None, modifier=None, modifier_param=None, type=None, value=None):
        # Indicates whether the left operand is a variable. Valid values:
        # 
        # *   true: variable
        # *   false: constant
        self.is_var = is_var  # type: bool
        # The remarks on the left operand.
        self.modifier = modifier  # type: str
        # The key-value pair information of the remarks.
        self.modifier_param = modifier_param  # type: dict[str, any]
        # Indicates whether the left operand is a constant. Valid values:
        # 
        # *   true
        # *   false
        self.type = type  # type: str
        # The variable of the left operand.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight(TeaModel):
    def __init__(self, is_var=None, modifier=None, modifier_param=None, type=None, value=None):
        # Indicates whether the right operand is a constant or a runtime variable that is obtained from the runtime context. Valid values:
        # 
        # *   true: runtime variable
        # *   false: constant
        self.is_var = is_var  # type: bool
        # The remarks on the right operand.
        self.modifier = modifier  # type: str
        # The key-value pair information of the remarks.
        self.modifier_param = modifier_param  # type: dict[str, any]
        # The data type of the right operand.
        self.type = type  # type: str
        # The right operand.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions(TeaModel):
    def __init__(self, is_not=None, item_id=None, left=None, operator=None, right=None):
        # Indicates whether the result is inverted. Valid values:
        # 
        # *   true
        # *   false
        self.is_not = is_not  # type: bool
        # The ID of the rule condition.
        self.item_id = item_id  # type: int
        # The left operand of the rule condition.
        self.left = left  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft
        # The logical operator of the rule condition. Valid values:
        # 
        # *   `=`: equals to
        # *   `<>`: does not equal to
        # *   `in`: contains
        # *   `not in`: does not contain
        # *   `REGEXP`: matches a regular expression
        # *   `NOT REGEXP`: does not match a regular expression
        self.operator = operator  # type: str
        # The right operand of the rule condition.
        self.right = right  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight

    def validate(self):
        if self.left:
            self.left.validate()
        if self.right:
            self.right.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_not is not None:
            result['IsNot'] = self.is_not
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.left is not None:
            result['Left'] = self.left.to_map()
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.right is not None:
            result['Right'] = self.right.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsNot') is not None:
            self.is_not = m.get('IsNot')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Left') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft()
            self.left = temp_model.from_map(m['Left'])
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Right') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight()
            self.right = temp_model.from_map(m['Right'])
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpression(TeaModel):
    def __init__(self, conditions=None, logic=None):
        # The rule conditions.
        self.conditions = conditions  # type: list[DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions]
        # The logical relationships among the rule conditions.
        self.logic = logic  # type: str

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_type=None, alert_type_id=None, alert_uuid=None,
                 aliuid=None, expression=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, status=None,
                 sub_aliuid=None):
        # The alert name.
        self.alert_name = alert_name  # type: str
        # The ID of the alert name.
        self.alert_name_id = alert_name_id  # type: str
        # The alert type.
        self.alert_type = alert_type  # type: str
        # The ID of the alert type.
        self.alert_type_id = alert_type_id  # type: str
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.aliuid = aliuid  # type: long
        # The conditions in the rule. The value is a JSON array.
        self.expression = expression  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpression
        # The time when the whitelist rule was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the whitelist rule was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the whitelist rule.
        self.id = id  # type: long
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The status of the whitelist rule. Valid values:
        # 
        # *   1: enabled
        # *   0: disabled
        self.status = status  # type: int
        # The ID of the Alibaba Cloud account that is used to create the whitelist rule.
        self.sub_aliuid = sub_aliuid  # type: long

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.expression is not None:
            result['Expression'] = self.expression.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Expression') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpression()
            self.expression = temp_model.from_map(m['Expression'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        return self


class DescribeWhiteRuleListResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: DescribeWhiteRuleListResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[DescribeWhiteRuleListResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: DescribeWhiteRuleListResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DescribeWhiteRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoQuickFieldRequest(TeaModel):
    def __init__(self, from_=None, index=None, page=None, region_id=None, reverse=None, size=None, to=None):
        # The time when the quick analysis starts. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: int
        # The index field.
        self.index = index  # type: str
        # The number of pages to return. Default value: 1.
        self.page = page  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # The sorting of the query and analysis results. By default, the results are sorted in descending order.
        self.reverse = reverse  # type: bool
        # The number of entries per page. Default value: 10.
        self.size = size  # type: int
        # The time when the quick analysis ends. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoQuickFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.index is not None:
            result['Index'] = self.index
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.size is not None:
            result['Size'] = self.size
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DoQuickFieldResponseBodyData(TeaModel):
    def __init__(self, agg_queryd=None, complete_or_not=None, count=None, has_sql=None, keys=None, limited=None,
                 logs=None, pquery=None, processed_rows=None, query_mode=None, where_query=None):
        # This parameter is deprecated.
        self.agg_queryd = agg_queryd  # type: str
        # Indicates whether the quick analysis was successful. Valid values:
        # 
        # *   true
        # *   false
        self.complete_or_not = complete_or_not  # type: bool
        # The number of entries returned.
        self.count = count  # type: int
        # This parameter is deprecated.
        self.has_sql = has_sql  # type: bool
        # This parameter is deprecated.
        self.keys = keys  # type: list[str]
        # This parameter is deprecated.
        self.limited = limited  # type: long
        # The logs queried by using the quick analysis feature.
        self.logs = logs  # type: list[any]
        # This parameter is deprecated.
        self.pquery = pquery  # type: str
        # The number of entries queried.
        self.processed_rows = processed_rows  # type: long
        # This parameter is deprecated.
        self.query_mode = query_mode  # type: int
        # This parameter is deprecated.
        self.where_query = where_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoQuickFieldResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_queryd is not None:
            result['AggQueryd'] = self.agg_queryd
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSQL'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.pquery is not None:
            result['PQuery'] = self.pquery
        if self.processed_rows is not None:
            result['ProcessedRows'] = self.processed_rows
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.where_query is not None:
            result['WhereQuery'] = self.where_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AggQueryd') is not None:
            self.agg_queryd = m.get('AggQueryd')
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSQL') is not None:
            self.has_sql = m.get('HasSQL')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PQuery') is not None:
            self.pquery = m.get('PQuery')
        if m.get('ProcessedRows') is not None:
            self.processed_rows = m.get('ProcessedRows')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('WhereQuery') is not None:
            self.where_query = m.get('WhereQuery')
        return self


class DoQuickFieldResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response of the quick analysis.
        self.data = data  # type: DoQuickFieldResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DoQuickFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DoQuickFieldResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DoQuickFieldResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DoQuickFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoQuickFieldResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DoQuickFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoSelfDelegateRequest(TeaModel):
    def __init__(self, ali_uid=None, delegate_or_not=None, region_id=None):
        # The Alibaba Cloud account of an ordinary member of the threat analysis feature.
        self.ali_uid = ali_uid  # type: long
        # Specifies whether to use a delegated administrator account. Valid values:
        # 
        # *   1: use a delegated administrator account.
        # *   0: do not use a delegated administrator account.
        self.delegate_or_not = delegate_or_not  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoSelfDelegateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.delegate_or_not is not None:
            result['DelegateOrNot'] = self.delegate_or_not
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DelegateOrNot') is not None:
            self.delegate_or_not = m.get('DelegateOrNot')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoSelfDelegateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether a regular member is authorized. Valid values:
        # 
        # *   true: The member is authorized.
        # *   false: The authorization is canceled.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoSelfDelegateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DoSelfDelegateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DoSelfDelegateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoSelfDelegateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DoSelfDelegateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAccessForCloudSiemRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAccessForCloudSiemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAccessForCloudSiemResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAccessForCloudSiemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableAccessForCloudSiemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableAccessForCloudSiemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAccessForCloudSiemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAccessForCloudSiemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableServiceForCloudSiemRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableServiceForCloudSiemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableServiceForCloudSiemResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the threat analysis feature is authorized to access the resource directory. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableServiceForCloudSiemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableServiceForCloudSiemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableServiceForCloudSiemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableServiceForCloudSiemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableServiceForCloudSiemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCapacityRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetCapacityResponseBodyData(TeaModel):
    def __init__(self, exist_log_store=None, preserved_capacity=None, used_capacity=None):
        # Indicates whether the Logstores for the threat analysis feature exist on the user side. Valid values:
        # 
        # *   true: The logs are in the normal state. The log analysis feature is available.
        # *   false: The logs are being cleared. The log analysis feature is unavailable.
        self.exist_log_store = exist_log_store  # type: bool
        # The purchased storage capacity of the threat analysis feature. Unit: GB.
        self.preserved_capacity = preserved_capacity  # type: long
        # The billable storage capacity of the threat analysis feature. Unit: GB.
        self.used_capacity = used_capacity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_log_store is not None:
            result['ExistLogStore'] = self.exist_log_store
        if self.preserved_capacity is not None:
            result['PreservedCapacity'] = self.preserved_capacity
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExistLogStore') is not None:
            self.exist_log_store = m.get('ExistLogStore')
        if m.get('PreservedCapacity') is not None:
            self.preserved_capacity = m.get('PreservedCapacity')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class GetCapacityResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The information about the storage capacity.
        self.data = data  # type: GetCapacityResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCapacityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCapacityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistogramsRequest(TeaModel):
    def __init__(self, from_=None, query=None, region_id=None, to=None):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.from_ = from_  # type: int
        # The SQL statement. Only search statements are supported. Analytic statements are not supported. For more information about the syntax and limits of search statements, see [Log search overview](~~29060~~).
        self.query = query  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyDataHistograms(TeaModel):
    def __init__(self, completed_or_not=None, count=None, from_=None, to=None):
        # Indicates whether the query results within the subinterval is complete. Valid values:
        # 
        # *   true: The query is complete and the returned result is complete.
        # *   false: The query is complete but the returned result is incomplete. You must repeat the request to obtain the complete result.
        self.completed_or_not = completed_or_not  # type: bool
        # The number of logs within the subinterval.
        self.count = count  # type: long
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: int
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsResponseBodyDataHistograms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_or_not is not None:
            result['CompletedOrNot'] = self.completed_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedOrNot') is not None:
            self.completed_or_not = m.get('CompletedOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyData(TeaModel):
    def __init__(self, histograms=None, server=None, total_count=None):
        # The distribution of logs.
        self.histograms = histograms  # type: list[GetHistogramsResponseBodyDataHistograms]
        # The name of the server.
        self.server = server  # type: str
        # The number of logs that are generated within the subinterval.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.histograms:
            for k in self.histograms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHistogramsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Histograms'] = []
        if self.histograms is not None:
            for k in self.histograms:
                result['Histograms'].append(k.to_map() if k else None)
        if self.server is not None:
            result['Server'] = self.server
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.histograms = []
        if m.get('Histograms') is not None:
            for k in m.get('Histograms'):
                temp_model = GetHistogramsResponseBodyDataHistograms()
                self.histograms.append(temp_model.from_map(k))
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data of the charts.
        self.data = data  # type: GetHistogramsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHistogramsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetHistogramsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHistogramsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHistogramsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHistogramsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHistogramsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsRequest(TeaModel):
    def __init__(self, from_=None, page_index=None, page_size=None, query=None, region_id=None, reverse_or_not=None,
                 to=None, total=None):
        # The time when the query starts. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.from_ = from_  # type: int
        # The page number. Pages start from page 1.
        self.page_index = page_index  # type: int
        # The number of entries per page. Valid values: 0 to 100.
        self.page_size = page_size  # type: int
        # The search statement or the analytic statement. For more information, see [Log search overview](https://help.aliyun.com/zh/sls/user-guide/log-analysis-overview?spm=a2c4g.11186623.0.i1#t13103.html) and [Log analysis overview](https://help.aliyun.com/zh/sls/user-guide/search-syntax?spm=a2c4g.11186623.0.i0#concept-tnd-1jq-zdb).
        self.query = query  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # Specifies whether to sort the results of the log query by time in minutes in descending order. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.reverse_or_not = reverse_or_not  # type: bool
        # The time when the query ends. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.to = to  # type: int
        # The total number of entries returned.
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse_or_not is not None:
            result['ReverseOrNot'] = self.reverse_or_not
        if self.to is not None:
            result['To'] = self.to
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReverseOrNot') is not None:
            self.reverse_or_not = m.get('ReverseOrNot')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLogsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetLogsResponseBodyDataResponseData(TeaModel):
    def __init__(self, complete_or_not=None, cost=None, count=None, has_sql=None, keys=None, lines=None):
        # The status of the log query. Valid values:
        # 
        # *   true: The query is complete and the returned result is complete.
        # *   false: The query is complete but the returned result is incomplete. You must resend the request to obtain the complete result.
        self.complete_or_not = complete_or_not  # type: bool
        # The time period of the log query. Unit: milliseconds.
        self.cost = cost  # type: long
        # The number of entries returned.
        self.count = count  # type: int
        # Indicated whether an analytic statement is contained. Valid values:
        # 
        # *   true
        # *   false
        self.has_sql = has_sql  # type: bool
        # The index fields of the logs.
        self.keys = keys  # type: list[str]
        # The raw data generated in the query.
        self.lines = lines  # type: list[any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSql'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSql') is not None:
            self.has_sql = m.get('HasSql')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class GetLogsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The result on the current page.
        self.page_info = page_info  # type: GetLogsResponseBodyDataPageInfo
        # The log.
        self.response_data = response_data  # type: GetLogsResponseBodyDataResponseData

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            self.response_data.validate()

    def to_map(self):
        _map = super(GetLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.response_data is not None:
            result['ResponseData'] = self.response_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = GetLogsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('ResponseData') is not None:
            temp_model = GetLogsResponseBodyDataResponseData()
            self.response_data = temp_model.from_map(m['ResponseData'])
        return self


class GetLogsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The results of the log query.
        self.data = data  # type: GetLogsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

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
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuickQueryRequest(TeaModel):
    def __init__(self, region_id=None, search_name=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # The name of the saved search.
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetQuickQueryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The query statement.
        self.data = data  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuickQueryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStorageResponseBodyData(TeaModel):
    def __init__(self, can_operate=None, display_region=None, region=None, ttl=None):
        # Indicates whether the storage region can be changed for once. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.can_operate = can_operate  # type: bool
        # Indicates whether the storage region can be changed. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.display_region = display_region  # type: bool
        # The region in which the logs are stored. Default value: cn-shanghai. Valid values: cn-shanghai for the China site and ap-southeast-1 for the international site.
        self.region = region  # type: str
        # The storage period of logs. Unit: day. Default value: 180. Valid values: 30 to 3000.
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate is not None:
            result['CanOperate'] = self.can_operate
        if self.display_region is not None:
            result['DisplayRegion'] = self.display_region
        if self.region is not None:
            result['Region'] = self.region
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanOperate') is not None:
            self.can_operate = m.get('CanOperate')
        if m.get('DisplayRegion') is not None:
            self.display_region = m.get('DisplayRegion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class GetStorageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The information about the storage.
        self.data = data  # type: GetStorageResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStorageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountAccessIdRequest(TeaModel):
    def __init__(self, cloud_code=None, region_id=None):
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountAccessIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountAccessIdResponseBodyData(TeaModel):
    def __init__(self, access_id=None, access_id_md_5=None, account_id=None, account_str=None, bound=None,
                 cloud_code=None, sub_user_id=None):
        # The AccessKey ID of the cloud account that is added to the threat analysis feature.
        self.access_id = access_id  # type: str
        # The MD5 hash value of the AccessKey ID.
        self.access_id_md_5 = access_id_md_5  # type: str
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The information about the cloud account to which the AccessKey ID belongs. The value is in the following format: Alibaba Cloud account ID|Alibaba Cloud account username|AccessKey ID.
        self.account_str = account_str  # type: str
        # Indicates whether the cloud account to which the AccessKey ID belongs is added to the threat analysis feature. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.bound = bound  # type: int
        # The code of the cloud service provider.
        self.cloud_code = cloud_code  # type: str
        # The ID of the Alibaba Cloud account that is used to add the third-party cloud account.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountAccessIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_id_md_5 is not None:
            result['AccessIdMd5'] = self.access_id_md_5
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_str is not None:
            result['AccountStr'] = self.account_str
        if self.bound is not None:
            result['Bound'] = self.bound
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessIdMd5') is not None:
            self.access_id_md_5 = m.get('AccessIdMd5')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountStr') is not None:
            self.account_str = m.get('AccountStr')
        if m.get('Bound') is not None:
            self.bound = m.get('Bound')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAccountAccessIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: list[ListAccountAccessIdResponseBodyData]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountAccessIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccountAccessIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccountAccessIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountAccessIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountAccessIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountAccessIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsByLogRequest(TeaModel):
    def __init__(self, cloud_code=None, log_codes=None, prod_code=None, region_id=None):
        # The code that is used for multi-cloud environments.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        # *   aliyun
        self.cloud_code = cloud_code  # type: str
        # The codes of logs. The value is a JSON array.
        self.log_codes = log_codes  # type: list[str]
        # The code of the service.
        self.prod_code = prod_code  # type: str
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsByLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountsByLogResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, imported=None, log_code=None, main_user_id=None,
                 prod_code=None, sub_user_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The name of the cloud account.
        self.account_name = account_name  # type: str
        # Indicates whether the account is added. Valid values: -1: yes -0: no
        self.imported = imported  # type: int
        # The code of the log.
        self.log_code = log_code  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The code of the service.
        self.prod_code = prod_code  # type: str
        # The ID of the Alibaba Cloud account for which the threat analysis feature is enabled.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsByLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAccountsByLogResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListAccountsByLogResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsByLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccountsByLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountsByLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountsByLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountsByLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountsByLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllProdsRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllProdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAllProdsResponseBodyDataProdList(TeaModel):
    def __init__(self, cloud_code=None, imported_log_count=None, modify_time=None, prod_code=None,
                 total_log_count=None):
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The number of logs within the cloud service that are added to the threat analysis feature.
        self.imported_log_count = imported_log_count  # type: int
        # The time when the logs within the cloud service were last added to the threat analysis feature.
        self.modify_time = modify_time  # type: str
        # The code of the cloud service.
        self.prod_code = prod_code  # type: str
        # The total number of logs within the cloud service.
        self.total_log_count = total_log_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllProdsResponseBodyDataProdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')
        return self


class ListAllProdsResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_size=None, prod_list=None, total_count=None):
        # The page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The cloud services.
        self.prod_list = prod_list  # type: list[ListAllProdsResponseBodyDataProdList]
        # The total number of logs.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.prod_list:
            for k in self.prod_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAllProdsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProdList'] = []
        if self.prod_list is not None:
            for k in self.prod_list:
                result['ProdList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.prod_list = []
        if m.get('ProdList') is not None:
            for k in m.get('ProdList'):
                temp_model = ListAllProdsResponseBodyDataProdList()
                self.prod_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAllProdsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: ListAllProdsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAllProdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAllProdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAllProdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAllProdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAllProdsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAllProdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutomateResponseConfigsRequest(TeaModel):
    def __init__(self, action_type=None, auto_response_type=None, current_page=None, id=None, page_size=None,
                 playbook_uuid=None, region_id=None, rule_name=None, status=None, sub_user_id=None):
        # The type of the handling action. Valid values:
        # 
        # *   doPlaybook: runs a playbook.
        # *   changeEventStatus: changes the status of an event.
        # *   changeThreatLevel: changes the risk level of an event.
        self.action_type = action_type  # type: str
        # The type of the automated response rule. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The ID of the automated response rule.
        self.id = id  # type: long
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The name of the automated response rule.
        self.rule_name = rule_name  # type: str
        # The status of the rule. Valid values:
        # 
        # *   0: disabled
        # *   100: enabled
        self.status = status  # type: int
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutomateResponseConfigsResponseBodyDataResponseData(TeaModel):
    def __init__(self, action_config=None, action_type=None, aliuid=None, auto_response_type=None,
                 execution_condition=None, gmt_create=None, gmt_modified=None, id=None, rule_name=None, status=None, sub_user_id=None):
        # The configuration of the action that is performed after the rule is hit. The value is in JSON format.
        self.action_config = action_config  # type: str
        # The type of the handling action. Multiple types are separated by commas (,). Valid values:
        # 
        # *   doPlaybook: runs a playbook.
        # *   changeEventStatus: changes the status of an event.
        # *   changeThreatLevel: changes the risk level of an event.
        self.action_type = action_type  # type: str
        # The ID of the Alibaba Cloud account that is associated with the rule in SIEM.
        self.aliuid = aliuid  # type: long
        # The type of the automated response rule. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type  # type: str
        # The trigger condition of the rule. The value is in the JSON format.
        self.execution_condition = execution_condition  # type: str
        # The creation time.
        self.gmt_create = gmt_create  # type: str
        # The update time.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the automated response rule.
        self.id = id  # type: long
        # The name of the automated response rule.
        self.rule_name = rule_name  # type: str
        # The status of the rule. Valid values:
        # 
        # *   0: disabled
        # *   100: enabled
        self.status = status  # type: int
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: ListAutomateResponseConfigsResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[ListAutomateResponseConfigsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListAutomateResponseConfigsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListAutomateResponseConfigsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListAutomateResponseConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ListAutomateResponseConfigsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ListAutomateResponseConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutomateResponseConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAutomateResponseConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAutomateResponseConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindAccountRequest(TeaModel):
    def __init__(self, cloud_code=None, region_id=None):
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBindAccountResponseBodyData(TeaModel):
    def __init__(self, access_id=None, account_id=None, account_name=None, bind_id=None, cloud_code=None,
                 create_user=None, data_source_count=None, modify_time=None):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id  # type: str
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The username of the cloud account.
        self.account_name = account_name  # type: str
        # The ID that is generated when the cloud account is added.
        self.bind_id = bind_id  # type: long
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the account that is used to add the cloud account.
        self.create_user = create_user  # type: str
        # The number of data sources that are added to the threat analysis feature within the cloud account.
        self.data_source_count = data_source_count  # type: long
        # The modification time.
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.data_source_count is not None:
            result['DataSourceCount'] = self.data_source_count
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DataSourceCount') is not None:
            self.data_source_count = m.get('DataSourceCount')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListBindAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListBindAccountResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBindAccountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindDataSourcesRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        # *   aliyun
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBindDataSourcesResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, cloud_code=None, data_source_instance_id=None,
                 data_source_name=None, data_source_remark=None, data_source_type=None, log_count=None, task_count=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The username of the cloud account.
        self.account_name = account_name  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The name of the data source.
        self.data_source_name = data_source_name  # type: str
        # The remarks on the data source.
        self.data_source_remark = data_source_remark  # type: str
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type  # type: str
        # The number of logs that are added within the data source.
        self.log_count = log_count  # type: int
        # The number of existing tasks that are created to add logs within the data source.
        self.task_count = task_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindDataSourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_remark is not None:
            result['DataSourceRemark'] = self.data_source_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceRemark') is not None:
            self.data_source_remark = m.get('DataSourceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class ListBindDataSourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListBindDataSourcesResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBindDataSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindDataSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemCustomizeRulesRequest(TeaModel):
    def __init__(self, alert_type=None, current_page=None, end_time=None, id=None, page_size=None, region_id=None,
                 rule_name=None, rule_type=None, start_time=None, status=None, threat_level=None):
        # The alert type.
        self.alert_type = alert_type  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the custom rule.
        self.id = id  # type: str
        # The number of entries per page. The value can be up to 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The name of the rule. The name can contain letters, digits, underscores (\_), and periods (.).
        self.rule_name = rule_name  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the rule. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The risk level. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        # The type of the risk.
        self.alert_type = alert_type  # type: str
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds  # type: str
        # The ID of the Alibaba Cloud account in SIEM.
        self.aliuid = aliuid  # type: long
        # The extended information about event generation. If the value of eventTransferType is allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window. The HTML escape characters are reversed.
        self.event_transfer_ext = event_transfer_ext  # type: str
        # Indicates whether the system generates an event for the alert. Valid values:
        # 
        # *   0: no.
        # *   1: yes.
        self.event_transfer_switch = event_transfer_switch  # type: int
        # The event generation method. Valid values:
        # 
        # *   default: The default method is used.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type  # type: str
        # The time when the custom rule was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the custom rule was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the custom rule.
        self.id = id  # type: long
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The internal code of the log source.
        self.log_source_mds = log_source_mds  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The internal code of the log type.
        self.log_type_mds = log_type_mds  # type: str
        # The window length of the rule. The HTML escape characters are reversed.
        self.query_cycle = query_cycle  # type: str
        # The query condition of the rule in the JSON format. The HTML escape characters are reversed.
        self.rule_condition = rule_condition  # type: str
        # The description of the rule.
        self.rule_desc = rule_desc  # type: str
        # The log aggregation field of the rule. The value is a JSON string. The HTML escape characters are reversed.
        self.rule_group = rule_group  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The threshold configurations of the rule in the JSON format. The HTML escape characters are reversed.
        self.rule_threshold = rule_threshold  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str
        # The rule status. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The threat level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: ListCloudSiemCustomizeRulesResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[ListCloudSiemCustomizeRulesResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemCustomizeRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemCustomizeRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemCustomizeRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ListCloudSiemCustomizeRulesResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ListCloudSiemCustomizeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemCustomizeRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCloudSiemCustomizeRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCloudSiemCustomizeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemPredefinedRulesRequest(TeaModel):
    def __init__(self, alert_type=None, current_page=None, end_time=None, id=None, page_size=None, region_id=None,
                 rule_name=None, rule_type=None, start_time=None, status=None, threat_level=None):
        # The alert type.
        self.alert_type = alert_type  # type: str
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the rule.
        self.id = id  # type: str
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The name of the rule. The name can contain letters, digits, underscores (\_), and periods (.).
        self.rule_name = rule_name  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the rule. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The risk level. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_type=None, gmt_create=None, gmt_modified=None, id=None, rule_desc_mds=None,
                 rule_name=None, rule_name_mds=None, source=None, status=None, threat_level=None):
        # The type of the risk.
        self.alert_type = alert_type  # type: str
        # The time when the rule was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the rule was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the predefined rule.
        self.id = id  # type: long
        # The internal code of the rule description.
        self.rule_desc_mds = rule_desc_mds  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The internal code of the rule name.
        self.rule_name_mds = rule_name_mds  # type: str
        # The log source of the rule.
        self.source = source  # type: str
        # The status of the predefined rule. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The threat level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_desc_mds is not None:
            result['RuleDescMds'] = self.rule_desc_mds
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_name_mds is not None:
            result['RuleNameMds'] = self.rule_name_mds
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleDescMds') is not None:
            self.rule_desc_mds = m.get('RuleDescMds')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleNameMds') is not None:
            self.rule_name_mds = m.get('RuleNameMds')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: ListCloudSiemPredefinedRulesResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[ListCloudSiemPredefinedRulesResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemPredefinedRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemPredefinedRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemPredefinedRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ListCloudSiemPredefinedRulesResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ListCloudSiemPredefinedRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemPredefinedRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCloudSiemPredefinedRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCloudSiemPredefinedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomizeRuleTestResultRequest(TeaModel):
    def __init__(self, current_page=None, id=None, page_size=None, region_id=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The ID of the rule.
        self.id = id  # type: long
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomizeRuleTestResultResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomizeRuleTestResultResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_detail=None, alert_src_prod=None, alert_src_prod_module=None,
                 att_ck=None, event_name=None, event_type=None, level=None, log_source=None, log_time=None, log_type=None,
                 main_user_id=None, online_status=None, sub_user_id=None, uuid=None):
        # The description of the alert.
        self.alert_desc = alert_desc  # type: str
        # The alert details in the JSON format.
        self.alert_detail = alert_detail  # type: str
        # The source of the alert.
        self.alert_src_prod = alert_src_prod  # type: str
        # The sub-module of the source.
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        # The tag of the ATT\&CK attack.
        self.att_ck = att_ck  # type: str
        # The name of the alert, which corresponds to the name of the custom rule.
        self.event_name = event_name  # type: str
        # The risk type, which indicates the alert type.
        self.event_type = event_type  # type: str
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.level = level  # type: str
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The time when the alert was recorded.
        self.log_time = log_time  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id  # type: str
        # The status of the alert data. Valid values:
        # 
        # *   test: business test data
        # *   online: online data
        self.online_status = online_status  # type: str
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id  # type: str
        # The UUID of the alert.
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.level is not None:
            result['Level'] = self.level
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListCustomizeRuleTestResultResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: ListCustomizeRuleTestResultResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[ListCustomizeRuleTestResultResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCustomizeRuleTestResultResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCustomizeRuleTestResultResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCustomizeRuleTestResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ListCustomizeRuleTestResultResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ListCustomizeRuleTestResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCustomizeRuleTestResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomizeRuleTestResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomizeRuleTestResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceLogsRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code that is used for multi-cloud environments. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The value is obtained after the threat analysis feature calculates the MD5 hash value of a parameter.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams(TeaModel):
    def __init__(self, para_code=None, para_value=None):
        # The parameter code of the log.
        self.para_code = para_code  # type: str
        # The parameter value of the log.
        self.para_value = para_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.para_code is not None:
            result['ParaCode'] = self.para_code
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        return self


class ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs(TeaModel):
    def __init__(self, log_code=None, log_instance_id=None, log_mds_code=None, log_params=None, task_status=None):
        # The code of the log.
        self.log_code = log_code  # type: str
        # The ID of the log. The value is obtained after the threat analysis feature calculates the MD5 hash value of a parameter.
        self.log_instance_id = log_instance_id  # type: str
        # The display code of the log.
        self.log_mds_code = log_mds_code  # type: str
        # The parameters of the log.
        self.log_params = log_params  # type: list[ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams]
        # Indicates whether the task for which logs are collected is enabled. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.task_status = task_status  # type: int

    def validate(self):
        if self.log_params:
            for k in self.log_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        result['LogParams'] = []
        if self.log_params is not None:
            for k in self.log_params:
                result['LogParams'].append(k.to_map() if k else None)
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        self.log_params = []
        if m.get('LogParams') is not None:
            for k in m.get('LogParams'):
                temp_model = ListDataSourceLogsResponseBodyDataDataSourceInstanceLogsLogParams()
                self.log_params.append(temp_model.from_map(k))
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class ListDataSourceLogsResponseBodyData(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None,
                 data_source_instance_logs=None, data_source_instance_name=None, data_source_instance_remark=None, sub_user_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code that is used for multi-cloud environments. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The value is obtained after the threat analysis feature calculates the MD5 hash value of a parameter.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The logs of the data source.
        self.data_source_instance_logs = data_source_instance_logs  # type: list[ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs]
        # The name of the data source.
        self.data_source_instance_name = data_source_instance_name  # type: str
        # The remarks of the data source.
        self.data_source_instance_remark = data_source_instance_remark  # type: str
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.data_source_instance_logs:
            for k in self.data_source_instance_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        result['DataSourceInstanceLogs'] = []
        if self.data_source_instance_logs is not None:
            for k in self.data_source_instance_logs:
                result['DataSourceInstanceLogs'].append(k.to_map() if k else None)
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        self.data_source_instance_logs = []
        if m.get('DataSourceInstanceLogs') is not None:
            for k in m.get('DataSourceInstanceLogs'):
                temp_model = ListDataSourceLogsResponseBodyDataDataSourceInstanceLogs()
                self.data_source_instance_logs.append(temp_model.from_map(k))
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListDataSourceLogsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: ListDataSourceLogsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDataSourceLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDataSourceLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTypesRequest(TeaModel):
    def __init__(self, cloud_code=None, region_id=None):
        # The code of the third-party cloud service.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDataSourceTypesResponseBodyData(TeaModel):
    def __init__(self, cloud_code=None, data_source_type=None):
        # The code of the third-party cloud service.
        self.cloud_code = cloud_code  # type: str
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        return self


class ListDataSourceTypesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListDataSourceTypesResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDataSourceTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDeliveryResponseBodyDataProductListLogListExtraParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # The ID of the extended parameter.
        self.key = key  # type: str
        # The value of the extended parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductListLogListExtraParameters, self).to_map()
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


class ListDeliveryResponseBodyDataProductListLogList(TeaModel):
    def __init__(self, can_operate_or_not=None, extra_parameters=None, log_code=None, log_name=None,
                 log_name_en=None, log_name_key=None, status=None, topic=None):
        # Indicates whether the log delivery feature can be enabled or disabled. The feature can be enabled or disabled only by the administrator of the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.can_operate_or_not = can_operate_or_not  # type: bool
        # The extended parameter.
        self.extra_parameters = extra_parameters  # type: list[ListDeliveryResponseBodyDataProductListLogListExtraParameters]
        # The code of the log.
        self.log_code = log_code  # type: str
        # This parameter is deprecated.
        self.log_name = log_name  # type: str
        # This parameter is deprecated.
        self.log_name_en = log_name_en  # type: str
        # The language code of the log that is used to indicate the language in which the log is displayed.
        self.log_name_key = log_name_key  # type: str
        # The status of the log delivery. Valid values:
        # 
        # *   true: The logs are being delivered.
        # *   false: The log delivery feature is disabled.
        self.status = status  # type: bool
        # The topic of the log in the Logstore. The value is an index field in the Logstore that can be used to distinguish different logs.
        self.topic = topic  # type: str

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = ListDeliveryResponseBodyDataProductListLogListExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListDeliveryResponseBodyDataProductList(TeaModel):
    def __init__(self, log_list=None, log_map=None, product_code=None, product_name=None):
        # The logs of the cloud services.
        self.log_list = log_list  # type: list[ListDeliveryResponseBodyDataProductListLogList]
        # The log group. For example, in Security Center, the logs of hosts and networks are stored in different groups. Key indicates the group information, and value indicates the logs in the group.
        self.log_map = log_map  # type: dict[str, list[DataProductListLogMapValue]]
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code  # type: str
        # This parameter is deprecated.
        self.product_name = product_name  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()
        if self.log_map:
            for v in self.log_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        result['LogMap'] = {}
        if self.log_map is not None:
            for k, v in self.log_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['LogMap'][k] = l1
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = ListDeliveryResponseBodyDataProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        self.log_map = {}
        if m.get('LogMap') is not None:
            for k, v in m.get('LogMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataProductListLogMapValue()
                    l1.append(temp_model.from_map(k1))
                self.log_map['k'] = l1
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListDeliveryResponseBodyData(TeaModel):
    def __init__(self, dashboard_url=None, display_switch_or_not=None, log_store_name=None, product_list=None,
                 project_name=None, search_url=None):
        # The URL that is displayed in charts.
        self.dashboard_url = dashboard_url  # type: str
        # Indicates whether the log delivery switch is displayed. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        self.display_switch_or_not = display_switch_or_not  # type: bool
        # The name of the Logstore for the threat analysis feature on the user side. The value is in the cloud_siem format.
        self.log_store_name = log_store_name  # type: str
        # The cloud services.
        self.product_list = product_list  # type: list[ListDeliveryResponseBodyDataProductList]
        # The name of the project for the threat analysis feature in Simple Log service on the user side. The value is in the aliyun-cloudsiem-data-${aliUid}-${region} format.
        self.project_name = project_name  # type: str
        # The URL that is used for log analysis.
        self.search_url = search_url  # type: str

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_url is not None:
            result['DashboardUrl'] = self.dashboard_url
        if self.display_switch_or_not is not None:
            result['DisplaySwitchOrNot'] = self.display_switch_or_not
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.search_url is not None:
            result['SearchUrl'] = self.search_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardUrl') is not None:
            self.dashboard_url = m.get('DashboardUrl')
        if m.get('DisplaySwitchOrNot') is not None:
            self.display_switch_or_not = m.get('DisplaySwitchOrNot')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListDeliveryResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SearchUrl') is not None:
            self.search_url = m.get('SearchUrl')
        return self


class ListDeliveryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: ListDeliveryResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDeliveryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisposeStrategyRequest(TeaModel):
    def __init__(self, current_page=None, effective_status=None, end_time=None, entity_identity=None,
                 entity_type=None, order=None, order_field=None, page_size=None, playbook_name=None, playbook_types=None,
                 playbook_uuid=None, region_id=None, sophon_task_id=None, start_time=None):
        # The page number. Pages start from page 1.
        self.current_page = current_page  # type: int
        # The status of the policy. Valid values:
        # 
        # *   0: invalid
        # *   1: valid
        self.effective_status = effective_status  # type: int
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The feature value of the entity. Fuzzy match is supported.
        self.entity_identity = entity_identity  # type: str
        # The entity type of the playbook. Valid values:
        # 
        # *   ip
        # *   process
        # *   file
        self.entity_type = entity_type  # type: str
        # The sort order. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.order = order  # type: str
        # The sort field. Valid values:
        # 
        # *   GmtModified: sorts the policies by update time.
        # *   GmtCreate: sorts the policies by creation time.
        # *   FinishTime: sorts the policies by end time.
        self.order_field = order_field  # type: str
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size  # type: int
        # The name of the playbook, which is the unique identifier of the playbook.
        self.playbook_name = playbook_name  # type: str
        # The type of the playbook. Valid values:
        # 
        # *   system: user-triggered playbook
        # *   custom: event-triggered playbook
        # *   custom_alert: alert-triggered playbook
        # *   soar-manual: user-run playbook
        # *   soar-mdr: MDR-run playbook
        self.playbook_types = playbook_types  # type: str
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The ID of the SOAR handling policy.
        self.sophon_task_id = sophon_task_id  # type: str
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_types is not None:
            result['PlaybookTypes'] = self.playbook_types
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookTypes') is not None:
            self.playbook_types = m.get('PlaybookTypes')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDisposeStrategyResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The current page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDisposeStrategyResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_uuid=None, aliuid=None, effective_status=None, entity=None, entity_id=None,
                 entity_type=None, error_message=None, finish_time=None, gmt_create=None, gmt_modified=None, id=None,
                 incident_name=None, incident_uuid=None, playbook_name=None, playbook_type=None, playbook_uuid=None, scope=None,
                 sophon_task_id=None, status=None, sub_aliuid=None, task_param=None):
        # The UUID of the alert.
        self.alert_uuid = alert_uuid  # type: str
        # The ID of the Alibaba Cloud account that is associated with the policy in SIEM.
        self.aliuid = aliuid  # type: long
        # The status of the policy. Valid values:
        # 
        # *   0: invalid
        # *   1: valid
        self.effective_status = effective_status  # type: int
        # The details of the entity. The value is a JSON array.
        self.entity = entity  # type: list[any]
        # The ID of the entity.
        self.entity_id = entity_id  # type: long
        # The type of the entity. Valid values:
        # 
        # *   ip
        # *   process
        # *   file
        self.entity_type = entity_type  # type: str
        # The summary information about the failed task.
        self.error_message = error_message  # type: str
        # The end time of the task.
        self.finish_time = finish_time  # type: str
        # The creation time.
        self.gmt_create = gmt_create  # type: str
        # The update time.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the policy.
        self.id = id  # type: long
        # The name of the event.
        self.incident_name = incident_name  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The name of the playbook, which is the unique identifier of the playbook.
        self.playbook_name = playbook_name  # type: str
        # The type of the playbook. Valid values:
        # 
        # *   system: user-triggered playbook
        # *   custom: event-triggered playbook
        # *   custom_alert: alert-triggered playbook
        # *   soar-manual: user-run playbook
        # *   soar-mdr: MDR-run playbook
        self.playbook_type = playbook_type  # type: str
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid  # type: str
        # The scope of the policy.
        self.scope = scope  # type: list[any]
        # The ID of the SOAR handling policy.
        self.sophon_task_id = sophon_task_id  # type: str
        # The running status of the playbook. Valid values:
        # 
        # *   200: successful
        # *   10: deleted
        # *   5: failed
        # *   0: initial
        self.status = status  # type: int
        # The ID of the Alibaba account that is used to configure the policy.
        self.sub_aliuid = sub_aliuid  # type: long
        # The parameters that are used to trigger the playbook. The value is in the JSON format.
        self.task_param = task_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.entity is not None:
            result['Entity'] = self.entity
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('Entity') is not None:
            self.entity = m.get('Entity')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        return self


class ListDisposeStrategyResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        # The pagination information.
        self.page_info = page_info  # type: ListDisposeStrategyResponseBodyDataPageInfo
        # The detailed data.
        self.response_data = response_data  # type: list[ListDisposeStrategyResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListDisposeStrategyResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListDisposeStrategyResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListDisposeStrategyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: ListDisposeStrategyResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ListDisposeStrategyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDisposeStrategyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDisposeStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDisposeStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImportedLogsByProdRequest(TeaModel):
    def __init__(self, cloud_code=None, prod_code=None, region_id=None):
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The code of the cloud service.
        self.prod_code = prod_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImportedLogsByProdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListImportedLogsByProdResponseBodyData(TeaModel):
    def __init__(self, auto_imported=None, cloud_code=None, imported=None, imported_user_count=None, log_code=None,
                 log_mds_code=None, modify_time=None, prod_code=None, total_user_count=None, un_imported_user_count=None):
        # Indicates whether the log is automatically added to the threat analysis feature within newly added accounts. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.auto_imported = auto_imported  # type: int
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # Indicates whether the log is added to the threat analysis feature. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.imported = imported  # type: int
        # The number of users who have added the log.
        self.imported_user_count = imported_user_count  # type: int
        # The log code.
        self.log_code = log_code  # type: str
        # The display log code.
        self.log_mds_code = log_mds_code  # type: str
        # The time when the log was last added.
        self.modify_time = modify_time  # type: str
        # The code of the cloud service to which the log belongs.
        self.prod_code = prod_code  # type: str
        # The total number of users who have the log.
        self.total_user_count = total_user_count  # type: int
        # The number of users who have not added the log.
        self.un_imported_user_count = un_imported_user_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImportedLogsByProdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.imported_user_count is not None:
            result['ImportedUserCount'] = self.imported_user_count
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        if self.un_imported_user_count is not None:
            result['UnImportedUserCount'] = self.un_imported_user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('ImportedUserCount') is not None:
            self.imported_user_count = m.get('ImportedUserCount')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        if m.get('UnImportedUserCount') is not None:
            self.un_imported_user_count = m.get('UnImportedUserCount')
        return self


class ListImportedLogsByProdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListImportedLogsByProdResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImportedLogsByProdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListImportedLogsByProdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImportedLogsByProdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListImportedLogsByProdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImportedLogsByProdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImportedLogsByProdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOperationResponseBodyData(TeaModel):
    def __init__(self, admin_or_not=None, operation_list=None):
        # Indicates whether the user is an administrator. Valid values:
        # 
        # *   true
        # *   false
        self.admin_or_not = admin_or_not  # type: bool
        # The resources on which the permissions are granted.
        self.operation_list = operation_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_or_not is not None:
            result['AdminOrNot'] = self.admin_or_not
        if self.operation_list is not None:
            result['OperationList'] = self.operation_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdminOrNot') is not None:
            self.admin_or_not = m.get('AdminOrNot')
        if m.get('OperationList') is not None:
            self.operation_list = m.get('OperationList')
        return self


class ListOperationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: ListOperationResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListOperationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListOperationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOperationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOperationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectLogStoresRequest(TeaModel):
    def __init__(self, region_id=None, source_log_code=None, source_prod_code=None, sub_user_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectLogStoresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListProjectLogStoresResponseBodyData(TeaModel):
    def __init__(self, end_point=None, local_name=None, log_store=None, main_user_id=None, project=None,
                 region_id=None, sub_user_id=None, sub_user_name=None):
        # The endpoint of the Simple Log Service project.
        self.end_point = end_point  # type: str
        # The name of the region in which the Simple Log Service project resides.
        self.local_name = local_name  # type: str
        # The name of the Simple Log Service Logstore.
        self.log_store = log_store  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The name of the Simple Log Service project.
        self.project = project  # type: str
        # The ID of the region in which the Simple Log Service project resides.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectLogStoresResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListProjectLogStoresResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListProjectLogStoresResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectLogStoresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProjectLogStoresResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectLogStoresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectLogStoresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectLogStoresResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuickQueryRequest(TeaModel):
    def __init__(self, offset=None, page_size=None, region_id=None):
        # The line from which the query starts. Default value: 0.
        self.offset = offset  # type: int
        # The number of entries per page. Valid values: 1 to 500.
        self.page_size = page_size  # type: int
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListQuickQueryResponseBodyDataQuickQueryList(TeaModel):
    def __init__(self, display_name=None, query=None, search_name=None):
        # The alias of the saved search.
        self.display_name = display_name  # type: str
        # The query statement corresponding to the saved search.
        self.query = query  # type: str
        # The name of the saved search.
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuickQueryResponseBodyDataQuickQueryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListQuickQueryResponseBodyData(TeaModel):
    def __init__(self, count=None, quick_query_list=None, total=None):
        # The number of saved searches per page.
        self.count = count  # type: int
        # The saved search.
        self.quick_query_list = quick_query_list  # type: list[ListQuickQueryResponseBodyDataQuickQueryList]
        # The total number of saved searches that meet the query conditions.
        self.total = total  # type: int

    def validate(self):
        if self.quick_query_list:
            for k in self.quick_query_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['QuickQueryList'] = []
        if self.quick_query_list is not None:
            for k in self.quick_query_list:
                result['QuickQueryList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.quick_query_list = []
        if m.get('QuickQueryList') is not None:
            for k in m.get('QuickQueryList'):
                temp_model = ListQuickQueryResponseBodyDataQuickQueryList()
                self.quick_query_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQuickQueryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The response parameters.
        self.data = data  # type: ListQuickQueryResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQuickQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRdUsersRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRdUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRdUsersResponseBodyData(TeaModel):
    def __init__(self, delegated_or_not=None, joined=None, joined_time=None, main_user_id=None, sub_user_id=None,
                 sub_user_name=None):
        # Indicates whether the account can be used to view the logs and alerts within the account.
        self.delegated_or_not = delegated_or_not  # type: bool
        # Indicates whether the account is added to the threat analysis feature for centralized management. Valid values:
        # 
        # *   true
        # *   false
        self.joined = joined  # type: bool
        # The time when the account was added to the threat analysis feature.
        self.joined_time = joined_time  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The ID of the Alibaba Cloud account that is used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRdUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegated_or_not is not None:
            result['DelegatedOrNot'] = self.delegated_or_not
        if self.joined is not None:
            result['Joined'] = self.joined
        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelegatedOrNot') is not None:
            self.delegated_or_not = m.get('DelegatedOrNot')
        if m.get('Joined') is not None:
            self.joined = m.get('Joined')
        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListRdUsersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListRdUsersResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRdUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRdUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRdUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRdUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRdUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRdUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserProdLogsRequest(TeaModel):
    def __init__(self, region_id=None, source_log_code=None, source_prod_code=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserProdLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        return self


class ListUserProdLogsResponseBodyData(TeaModel):
    def __init__(self, display_line=None, displayed=None, imported=None, is_deleted=None, main_user_id=None,
                 source_log_code=None, source_log_info=None, source_prod_code=None, sub_user_id=None, sub_user_name=None):
        # The display details of the Logstore.
        self.display_line = display_line  # type: str
        # Indicates whether the details of the added log are returned. Valid values:
        # 
        # *   true
        # *   false
        self.displayed = displayed  # type: bool
        # Indicates whether the log is added to the threat analysis feature. Valid values:
        # 
        # *   true
        # *   false
        self.imported = imported  # type: bool
        # Indicates whether the log is added to the threat analysis feature. Valid values:
        # 
        # *   0: yes
        # *   1: no
        self.is_deleted = is_deleted  # type: int
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The details of the Logstore. The value is a JSON string.
        self.source_log_info = source_log_info  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str
        # The ID of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserProdLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_line is not None:
            result['DisplayLine'] = self.display_line
        if self.displayed is not None:
            result['Displayed'] = self.displayed
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_info is not None:
            result['SourceLogInfo'] = self.source_log_info
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayLine') is not None:
            self.display_line = m.get('DisplayLine')
        if m.get('Displayed') is not None:
            self.displayed = m.get('Displayed')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogInfo') is not None:
            self.source_log_info = m.get('SourceLogInfo')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListUserProdLogsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListUserProdLogsResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserProdLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserProdLogsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserProdLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserProdLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserProdLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserProdLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersByProdRequest(TeaModel):
    def __init__(self, region_id=None, source_prod_code=None):
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersByProdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        return self


class ListUsersByProdResponseBodyData(TeaModel):
    def __init__(self, cloud_code=None, imported=None, log_mds_code=None, main_user_id=None, source_log_code=None,
                 source_log_name=None, source_prod_code=None, sub_user_id=None, sub_user_name=None):
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # Indicates whether the log is added to the threat analysis feature.
        self.imported = imported  # type: bool
        # The display log code. The value is based on your console settings.
        self.log_mds_code = log_mds_code  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id  # type: long
        # The log code.
        self.source_log_code = source_log_code  # type: str
        # The log name.
        self.source_log_name = source_log_name  # type: str
        # The code of the cloud service.
        self.source_prod_code = source_prod_code  # type: str
        # The ID of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id  # type: long
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersByProdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code
        if self.source_log_name is not None:
            result['SourceLogName'] = self.source_log_name
        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')
        if m.get('SourceLogName') is not None:
            self.source_log_name = m.get('SourceLogName')
        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')
        return self


class ListUsersByProdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: list[ListUsersByProdResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersByProdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUsersByProdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsersByProdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersByProdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersByProdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersByProdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBindAccountRequest(TeaModel):
    def __init__(self, access_id=None, account_id=None, account_name=None, bind_id=None, cloud_code=None,
                 region_id=None):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id  # type: str
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The username of the cloud account.
        self.account_name = account_name  # type: str
        # The ID that is generated by the system when the account is added. You can call the ListBindAccount operation to query the ID.
        self.bind_id = bind_id  # type: long
        # The code of the cloud service provider.
        # 
        # Enumeration values:
        # 
        # *   qcloud
        # *   hcloud
        self.cloud_code = cloud_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBindAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyBindAccountResponseBodyData(TeaModel):
    def __init__(self, count=None):
        # The number of the accounts that are modified. The value 1 indicates that the modification is successful, and a value less than or equal to 0 indicates that the modification failed.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBindAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ModifyBindAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: ModifyBindAccountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyBindAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyBindAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBindAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBindAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBindAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBindAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None,
                 data_source_instance_name=None, data_source_instance_params=None, data_source_instance_remark=None, data_source_type=None,
                 region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [DescribeDataSourceInstance](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CDescribeDataSourceInstance) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The name of the data source.
        self.data_source_instance_name = data_source_instance_name  # type: str
        # The parameters of the data source in the JSON string format.
        self.data_source_instance_params = data_source_instance_params  # type: str
        # The remarks on the data source.
        self.data_source_instance_remark = data_source_instance_remark  # type: str
        # The type of the data source. Valid values:
        # 
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        self.data_source_type = data_source_type  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_name is not None:
            result['DataSourceInstanceName'] = self.data_source_instance_name
        if self.data_source_instance_params is not None:
            result['DataSourceInstanceParams'] = self.data_source_instance_params
        if self.data_source_instance_remark is not None:
            result['DataSourceInstanceRemark'] = self.data_source_instance_remark
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceName') is not None:
            self.data_source_instance_name = m.get('DataSourceInstanceName')
        if m.get('DataSourceInstanceParams') is not None:
            self.data_source_instance_params = m.get('DataSourceInstanceParams')
        if m.get('DataSourceInstanceRemark') is not None:
            self.data_source_instance_remark = m.get('DataSourceInstanceRemark')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDataSourceResponseBodyData(TeaModel):
    def __init__(self, count=None, data_source_instance_id=None):
        # The number of data sources that are modified. The value 1 indicates that the modification is successful, and a value less than or equal to 0 indicates that the modification failed.
        self.count = count  # type: int
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: ModifyDataSourceResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceLogRequest(TeaModel):
    def __init__(self, account_id=None, cloud_code=None, data_source_instance_id=None,
                 data_source_instance_logs=None, data_source_type=None, log_code=None, log_instance_id=None, region_id=None):
        # The ID of the cloud account.
        self.account_id = account_id  # type: str
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code  # type: str
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [DescribeDataSourceInstance](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CDescribeDataSourceInstance) operation to query the IDs of data sources.
        self.data_source_instance_id = data_source_instance_id  # type: str
        # The parameters of the data source. Set this parameter to a JSON string.
        self.data_source_instance_logs = data_source_instance_logs  # type: str
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type  # type: str
        # The log code.
        self.log_code = log_code  # type: str
        # The ID of the log. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters. You can call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\&activeTabKey=api%7CListDataSourceLogs) to query log IDs.
        self.log_instance_id = log_instance_id  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id
        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')
        if m.get('DataSourceInstanceLogs') is not None:
            self.data_source_instance_logs = m.get('DataSourceInstanceLogs')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDataSourceLogResponseBodyData(TeaModel):
    def __init__(self, count=None, log_instance_id=None):
        # The number of logs that are modified. The value 1 indicates that the modification is successful, and a value less than or equal to 0 indicates that the modification failed.
        self.count = count  # type: int
        # The ID of the log. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.log_instance_id = log_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')
        return self


class ModifyDataSourceLogResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: ModifyDataSourceLogResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyDataSourceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyDataSourceLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDataSourceLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataSourceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataSourceLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDeliveryRequest(TeaModel):
    def __init__(self, log_code=None, product_code=None, region_id=None):
        # The log code of the cloud service, such as the code of the process log for Security Center. If you leave this parameter empty, operations are performed on all logs of the cloud service.
        self.log_code = log_code  # type: str
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        self.product_code = product_code  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenDeliveryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the log delivery feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostAutomateResponseConfigRequest(TeaModel):
    def __init__(self, action_config=None, action_type=None, auto_response_type=None, execution_condition=None,
                 id=None, region_id=None, rule_name=None, sub_user_id=None):
        # The configuration of the action that is performed after the rule is hit. The value is in JSON format.
        self.action_config = action_config  # type: str
        # The action that is performed after the rule is hit. Separate multiple values with commas (,). Valid values:
        # 
        # *   doPlaybook: Execute a playbook.
        # *   changeEventStatus: Change the event status.
        # *   changeThreatLevel: Change the threat level of the event.
        self.action_type = action_type  # type: str
        # The rule type. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type  # type: str
        # The trigger condition of the rule. The value is in JSON format.
        self.execution_condition = execution_condition  # type: str
        # The rule ID.
        self.id = id  # type: long
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The rule name.
        self.rule_name = rule_name  # type: str
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostAutomateResponseConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class PostAutomateResponseConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostAutomateResponseConfigResponseBody, self).to_map()
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


class PostAutomateResponseConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostAutomateResponseConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostAutomateResponseConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleRequest(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, event_transfer_ext=None, event_transfer_switch=None,
                 event_transfer_type=None, id=None, log_source=None, log_source_mds=None, log_type=None, log_type_mds=None,
                 query_cycle=None, region_id=None, rule_condition=None, rule_desc=None, rule_group=None, rule_name=None,
                 rule_threshold=None, threat_level=None):
        # The risk type.
        self.alert_type = alert_type  # type: str
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds  # type: str
        # The extended information about event generation. If eventTransferType is set to allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window.
        self.event_transfer_ext = event_transfer_ext  # type: str
        # Specifies whether to convert an alert to an event. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.event_transfer_switch = event_transfer_switch  # type: int
        # The event generation method. Valid values:
        # 
        # *   default: The default method is used.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type  # type: str
        # The ID of the rule.
        self.id = id  # type: long
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The internal code of the log source.
        self.log_source_mds = log_source_mds  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The internal code of the log type.
        self.log_type_mds = log_type_mds  # type: str
        # The window length of the rule.
        self.query_cycle = query_cycle  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The query condition of the rule. The value is in the JSON format.
        self.rule_condition = rule_condition  # type: str
        # The description of the rule.
        self.rule_desc = rule_desc  # type: str
        # The log aggregation field of the rule. The value is a JSON string.
        self.rule_group = rule_group  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The threshold configuration of the rule. The value is in the JSON format.
        self.rule_threshold = rule_threshold  # type: str
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        # The risk type.
        self.alert_type = alert_type  # type: str
        # The internal code of the risk type.
        self.alert_type_mds = alert_type_mds  # type: str
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.aliuid = aliuid  # type: long
        # The extended information about event generation. If eventTransferType is set to allToSingle, the value of this parameter indicates the length and unit of the alert aggregation window. The HTML escape characters are reversed.
        self.event_transfer_ext = event_transfer_ext  # type: str
        # Indicates whether the system generates an event for the alert. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.event_transfer_switch = event_transfer_switch  # type: int
        # The event generation method. Valid values:
        # 
        # *   default: The default method is used.
        # *   singleToSingle: The system generates an event for each alert.
        # *   allToSingle: The system generates an event for alerts within a period of time.
        self.event_transfer_type = event_transfer_type  # type: str
        # The time when the custom rule was created.
        self.gmt_create = gmt_create  # type: str
        # The time when the custom rule was last updated.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the custom rule.
        self.id = id  # type: long
        # The log source of the rule.
        self.log_source = log_source  # type: str
        # The internal code of the log source.
        self.log_source_mds = log_source_mds  # type: str
        # The log type of the rule.
        self.log_type = log_type  # type: str
        # The internal code of the log type.
        self.log_type_mds = log_type_mds  # type: str
        # The window length of the rule. The HTML escape characters are reversed.
        self.query_cycle = query_cycle  # type: str
        # The query condition of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_condition = rule_condition  # type: str
        # The description of the rule.
        self.rule_desc = rule_desc  # type: str
        # The log aggregation field of the rule. The value is a JSON string. The HTML escape characters are reversed.
        self.rule_group = rule_group  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The threshold configuration of the rule. The value is in the JSON format. The HTML escape characters are reversed.
        self.rule_threshold = rule_threshold  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str
        # The rule status. Valid values:
        # 
        # *   0: The rule is in the initial state.
        # *   10: The simulation data is tested.
        # *   15: The business data is being tested.
        # *   20: The business data test ends.
        # *   100: The rule takes effect.
        self.status = status  # type: int
        # The risk level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: PostCustomizeRuleResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = PostCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None, simulated_data=None, test_type=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The simulation data for the testing. This parameter is available only when TestType is set to simulate.
        self.simulated_data = simulated_data  # type: str
        # The testing type. Valid values:
        # 
        # *   simulate: simulation data test
        # *   business: business data test
        self.test_type = test_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.simulated_data is not None:
            result['SimulatedData'] = self.simulated_data
        if self.test_type is not None:
            result['TestType'] = self.test_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SimulatedData') is not None:
            self.simulated_data = m.get('SimulatedData')
        if m.get('TestType') is not None:
            self.test_type = m.get('TestType')
        return self


class PostCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: any
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleTestResponseBody, self).to_map()
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


class PostCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleTestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventDisposeAndWhiteruleListRequest(TeaModel):
    def __init__(self, event_dispose=None, incident_uuid=None, receiver_info=None, region_id=None, remark=None,
                 status=None):
        # The configuration of event handling. The value is a JSON object.
        self.event_dispose = event_dispose  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The configuration of the alert recipient. The value is a JSON object.
        self.receiver_info = receiver_info  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The remarks of the event.
        self.remark = remark  # type: str
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('ReceiverInfo') is not None:
            self.receiver_info = m.get('ReceiverInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostEventDisposeAndWhiteruleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListResponseBody, self).to_map()
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


class PostEventDisposeAndWhiteruleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostEventDisposeAndWhiteruleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostEventDisposeAndWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventWhiteruleListRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None, whiterule_list=None):
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The alert whitelist rule. The value is a JSON object.
        self.whiterule_list = whiterule_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventWhiteruleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.whiterule_list is not None:
            result['WhiteruleList'] = self.whiterule_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteruleList') is not None:
            self.whiterule_list = m.get('WhiteruleList')
        return self


class PostEventWhiteruleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventWhiteruleListResponseBody, self).to_map()
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


class PostEventWhiteruleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostEventWhiteruleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostEventWhiteruleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostEventWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostFinishCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        # The ID of the rule.
        self.id = id  # type: long
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PostFinishCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: any
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestResponseBody, self).to_map()
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


class PostFinishCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostFinishCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostFinishCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostRuleStatusChangeRequest(TeaModel):
    def __init__(self, ids=None, in_use=None, region_id=None, rule_type=None):
        # The rule IDs. The value is a JSON array.
        self.ids = ids  # type: str
        # Specifies whether to enable the rule. Valid values:
        # 
        # *   true
        # *   false
        self.in_use = in_use  # type: bool
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The type of the rule. Valid values:
        # 
        # *   predefine
        # *   customize
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostRuleStatusChangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class PostRuleStatusChangeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: any
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostRuleStatusChangeResponseBody, self).to_map()
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


class PostRuleStatusChangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostRuleStatusChangeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostRuleStatusChangeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PostRuleStatusChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreCapacityRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreCapacityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestoreCapacityResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the release command has been sent. Valid values:
        # 
        # *   true: The command has been sent and the storage space is being released.
        # *   false: The command failed to be sent.
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestoreCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreCapacityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestoreCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveQuickQueryRequest(TeaModel):
    def __init__(self, display_name=None, query=None, region_id=None):
        # The name of the saved search.
        self.display_name = display_name  # type: str
        # The query statement.
        self.query = query  # type: str
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SaveQuickQueryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the query statement is saved as a saved search. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveQuickQueryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetStorageRequest(TeaModel):
    def __init__(self, region=None, region_id=None, ttl=None):
        # The storage region of logs. By default, the region of the data management center is used and cannot be changed. cn-shanghai is used for the China data management center, and ap-southeast-1 is used for the Outside China data management center. To change the region, contact the technical support of threat analysis.
        self.region = region  # type: str
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str
        # The storage duration of logs. Default value: 180. Minimum value: 30. Maximum value: 3000. Unit: days.
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SetStorageResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Indicates whether the settings are saved. Valid values:
        # 
        # *   true
        # *   false
        self.data = data  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetStorageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShowQuickAnalysisRequest(TeaModel):
    def __init__(self, region_id=None):
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in the Chinese mainland or in the China (Hong Kong) region.
        # *   ap-southeast-1: Your assets reside in regions outside the Chinese mainland, excluding the China (Hong Kong) region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShowQuickAnalysisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ShowQuickAnalysisResponseBodyData(TeaModel):
    def __init__(self, index_list=None):
        # The index fields of the logs.
        self.index_list = index_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShowQuickAnalysisResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_list is not None:
            result['IndexList'] = self.index_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IndexList') is not None:
            self.index_list = m.get('IndexList')
        return self


class ShowQuickAnalysisResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The index fields.
        self.data = data  # type: ShowQuickAnalysisResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ShowQuickAnalysisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ShowQuickAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ShowQuickAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShowQuickAnalysisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ShowQuickAnalysisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ShowQuickAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImportLogTasksRequest(TeaModel):
    def __init__(self, accounts=None, auto_imported=None, cloud_code=None, log_codes=None, prod_code=None,
                 region_id=None):
        # The accounts that you want to add. The value is a JSON array. Valid values:
        # 
        # *   AccountId: the IDs of the accounts.
        # 
        # *   Imported: specifies whether to add the accounts. Valid values:
        # 
        #     *   0: no
        #     *   1: yes
        self.accounts = accounts  # type: str
        # Specifies whether to automatically add the account for which the logging feature is configured. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.auto_imported = auto_imported  # type: int
        # The code that is used for multi-cloud environments.
        # 
        # Valid values:
        # 
        # *   qcloud.
        # *   hcloud.
        # *   aliyun.
        self.cloud_code = cloud_code  # type: str
        # The logs that you want to collect. The value is a JSON array.
        self.log_codes = log_codes  # type: str
        # The code of the service.
        self.prod_code = prod_code  # type: str
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitImportLogTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts
        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            self.accounts = m.get('Accounts')
        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitImportLogTasksResponseBodyData(TeaModel):
    def __init__(self, count=None):
        # The number of log collection tasks that are submitted.
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitImportLogTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class SubmitImportLogTasksResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data returned.
        self.data = data  # type: SubmitImportLogTasksResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitImportLogTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitImportLogTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitImportLogTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitImportLogTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitImportLogTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitImportLogTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitJobsRequest(TeaModel):
    def __init__(self, json_param=None, region_id=None):
        # The parameters of the logs that you want to add. The value is a JSON array, which contains the following parameters:\
        # 
        # 
        # *   SourceProdCode: the code of the cloud service.
        # 
        # *   SourceLogCode: the code of the log.
        # 
        # *   Deleted: specifies whether to add the log. Valid values:
        # 
        #     *   0: yes
        #     *   1: no
        self.json_param = json_param  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitJobsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The total number of tasks.
        self.data = data  # type: int
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutomateResponseConfigStatusRequest(TeaModel):
    def __init__(self, ids=None, in_use=None, region_id=None):
        # The IDs of the automatic response rules. The value is a JSON array.
        self.ids = ids  # type: str
        # Specifies whether the rule is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.in_use = in_use  # type: bool
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAutomateResponseConfigStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusResponseBody, self).to_map()
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


class UpdateAutomateResponseConfigStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAutomateResponseConfigStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAutomateResponseConfigStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWhiteRuleListRequest(TeaModel):
    def __init__(self, expression=None, incident_uuid=None, region_id=None, white_rule_id=None):
        # The alert whitelist rule. The value is a JSON object.
        self.expression = expression  # type: str
        # The UUID of the event.
        self.incident_uuid = incident_uuid  # type: str
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id  # type: str
        # The unique ID of the whitelist rule.
        self.white_rule_id = white_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_rule_id is not None:
            result['WhiteRuleId'] = self.white_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteRuleId') is not None:
            self.white_rule_id = m.get('WhiteRuleId')
        return self


class UpdateWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: int
        # The data returned.
        self.data = data  # type: any
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteRuleListResponseBody, self).to_map()
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


class UpdateWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWhiteRuleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


