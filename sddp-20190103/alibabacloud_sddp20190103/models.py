# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateConfigRequest(TeaModel):
    def __init__(self, code=None, description=None, feature_type=None, lang=None, source_ip=None, value=None):
        # The code of the common configuration item. Valid values:
        # 
        # *   **access_failed_cnt**: the maximum number of access attempts allowed when Data Security Center (DSC) fails to access an unauthorized resource.
        # *   **access_permission_exprie_max_days**: the maximum idle period allowed for access permissions before an alert is triggered.
        # *   **log_datasize_avg_days**: the minimum percentage of the volume of logs of a specific type generated on the current day to the average volume of logs generated in the previous 10 days before an alert is triggered.
        self.code = code  # type: str
        # The description of the common configuration item.
        self.description = description  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str
        # The value of the common configuration item. The meaning of this parameter varies with the value of the Code parameter.
        # 
        # *   If you set the Code parameter to **access_failed_cnt**, the Value parameter specifies the maximum number of access attempts allowed when DSC fails to access an unauthorized resource.
        # *   If you set the Code parameter to **access_permission_exprie_max_days**, the Value parameter specifies the maximum idle period allowed for access permissions before an alert is triggered.
        # *   If you set the Code parameter to **log_datasize_avg_days**, the Value parameter specifies the minimum percentage of the volume of logs of a specific type generated on the current day to the average amount of logs generated in the previous 10 days before an alert is triggered.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConfigResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # The ID of the common alert configuration.
        self.id = id  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataLimitRequest(TeaModel):
    def __init__(self, audit_status=None, auto_scan=None, certificate_permission=None, enable=None,
                 engine_type=None, event_status=None, feature_type=None, lang=None, log_store_day=None, ocr_status=None,
                 parent_id=None, password=None, port=None, resource_type=None, sampling_size=None, service_region_id=None,
                 source_ip=None, user_name=None):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.audit_status = audit_status  # type: int
        # Specifies whether to automatically trigger a re-scan after a rule is modified. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # > When a re-scan is triggered, DSC scans all data in your data asset.
        self.auto_scan = auto_scan  # type: int
        # The permissions. Valid values:
        # 
        # *   **ReadOnly**: read-only permissions
        # *   **ReadWrite**: read and write permissions
        self.certificate_permission = certificate_permission  # type: str
        # Specifies whether to enable sensitive data detection. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # > If this is your first time to authorize DSC to access the data asset, the default value is 1. If this is not your first time to authorize DSC to access the data asset, the default value is the same as that used in the last authorization operation. Both 1 and 0 are possible.
        self.enable = enable  # type: int
        # The database engine that is run by the instance. Valid values:
        # 
        # *   **MySQL**\
        # *   **SQLServer**\
        self.engine_type = engine_type  # type: str
        # Specifies whether to enable anomalous event detection. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes (default)
        self.event_status = event_status  # type: int
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The retention period of raw logs after you enable the security audit feature. Unit: days. Valid values:
        # 
        # *   **30**\
        # *   **90**\
        # *   **180**\
        # *   **365**\
        self.log_store_day = log_store_day  # type: int
        # Specifies whether to enable optical character recognition (OCR). Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.ocr_status = ocr_status  # type: int
        # The name of the data asset.
        self.parent_id = parent_id  # type: str
        # The password that is used to access the database.
        self.password = password  # type: str
        # The port that is used to connect to the database.
        self.port = port  # type: int
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1** :MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4** :Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: int
        # The number of sensitive data samples that are collected after sensitive data detection is enabled. Valid values:
        # 
        # *   **0**\
        # *   **5**\
        # *   **10**\
        self.sampling_size = sampling_size  # type: int
        # The region in which the data asset resides. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing).
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-huhehaote**: China (Hohhot)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        self.service_region_id = service_region_id  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str
        # The username that is used to access the database.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataLimitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.certificate_permission is not None:
            result['CertificatePermission'] = self.certificate_permission
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('CertificatePermission') is not None:
            self.certificate_permission = m.get('CertificatePermission')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateDataLimitResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # The ID of the data asset.
        self.id = id  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataLimitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataLimitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataLimitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataLimitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(self, category=None, content=None, content_category=None, description=None, lang=None,
                 match_type=None, name=None, product_code=None, product_id=None, risk_level_id=None, rule_type=None,
                 source_ip=None, stat_express=None, status=None, support_form=None, target=None, warn_level=None):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category  # type: int
        # The content of the sensitive data detection rule. You can specify a regular expression or keywords that are used to match sensitive fields or text.
        self.content = content  # type: str
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category  # type: int
        # The description of the rule.
        self.description = description  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The match type. Valid values:
        # 
        # *   **1**: rule-based match
        # *   **2**: dictionary-based match
        self.match_type = match_type  # type: int
        # The name of the sensitive data detection rule.
        self.name = name  # type: str
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute**, **OSS**, **ADS**, **OTS**, and **RDS**.
        self.product_code = product_code  # type: str
        # The ID of the service to which the data asset belongs. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: sensitive data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        # *   **99**: custom rule
        self.rule_type = rule_type  # type: int
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str
        # The statistical expression.
        self.stat_express = stat_express  # type: str
        # Specifies whether to enable the sensitive data detection rule. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.status = status  # type: int
        # The type of the data asset. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data asset
        # *   **2**: unstructured data asset
        # 
        # > If you set the parameter to 1 or 2, rules that support all data assets and rules that support the queried data asset type are returned.
        self.support_form = support_form  # type: int
        # The code of the service to which the sensitive data detection rule is applied. Valid values include **MaxCompute**, **OSS**, **ADS**, **OTS**, and **RDS**.
        self.target = target  # type: str
        # The risk level of the alert that is triggered. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.description is not None:
            result['Description'] = self.description
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.stat_express is not None:
            result['StatExpress'] = self.stat_express
        if self.status is not None:
            result['Status'] = self.status
        if self.support_form is not None:
            result['SupportForm'] = self.support_form
        if self.target is not None:
            result['Target'] = self.target
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StatExpress') is not None:
            self.stat_express = m.get('StatExpress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # The unique ID of the sensitive data detection rule.
        self.id = id  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScanTaskRequest(TeaModel):
    def __init__(self, data_limit_id=None, feature_type=None, interval_day=None, lang=None, oss_scan_path=None,
                 resource_type=None, run_hour=None, run_minute=None, scan_range=None, scan_range_content=None, source_ip=None,
                 task_name=None, task_user_name=None):
        # The unique ID of the data asset, such as an instance, a database, and a bucket. You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the unique ID.
        self.data_limit_id = data_limit_id  # type: long
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The interval between two consecutive custom scan tasks. Unit: days. Valid values: 1 to 2147483648.
        self.interval_day = interval_day  # type: int
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The data to be scanned in the Object Storage Service (OSS) bucket. Prefix match, suffix match, and regular expression match are supported.
        self.oss_scan_path = oss_scan_path  # type: str
        # The type of the service to which the data assets to be scanned belong. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.resource_type = resource_type  # type: long
        # The time when the scan task is executed next time. Unit: hours.
        self.run_hour = run_hour  # type: int
        # The time when the scan task is executed next time. Unit: minutes.
        self.run_minute = run_minute  # type: int
        # The matching rule that specifies the scan scope of the custom scan task. This parameter takes effect only if you set the **ScanRangeContent** parameter. Valid values:
        # 
        # *   **0**: exact match
        # *   **1**: prefix match
        # *   **2**: suffix match
        # *   **3**: regular expression match
        self.scan_range = scan_range  # type: int
        # The data to be scanned in a structured data asset. Prefix match, suffix match, and regular expression match are supported.
        self.scan_range_content = scan_range_content  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str
        # The name of the scan task.
        self.task_name = task_name  # type: str
        # The account that is used to create the scan task.
        self.task_user_name = task_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScanTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit_id is not None:
            result['DataLimitId'] = self.data_limit_id
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.interval_day is not None:
            result['IntervalDay'] = self.interval_day
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.oss_scan_path is not None:
            result['OssScanPath'] = self.oss_scan_path
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.run_hour is not None:
            result['RunHour'] = self.run_hour
        if self.run_minute is not None:
            result['RunMinute'] = self.run_minute
        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range
        if self.scan_range_content is not None:
            result['ScanRangeContent'] = self.scan_range_content
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_user_name is not None:
            result['TaskUserName'] = self.task_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataLimitId') is not None:
            self.data_limit_id = m.get('DataLimitId')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('IntervalDay') is not None:
            self.interval_day = m.get('IntervalDay')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OssScanPath') is not None:
            self.oss_scan_path = m.get('OssScanPath')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RunHour') is not None:
            self.run_hour = m.get('RunHour')
        if m.get('RunMinute') is not None:
            self.run_minute = m.get('RunMinute')
        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')
        if m.get('ScanRangeContent') is not None:
            self.scan_range_content = m.get('ScanRangeContent')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskUserName') is not None:
            self.task_user_name = m.get('TaskUserName')
        return self


class CreateScanTaskResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # The ID of the custom scan task.
        self.id = id  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScanTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScanTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateScanTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScanTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlrRoleRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, source_ip=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlrRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateSlrRoleResponseBody(TeaModel):
    def __init__(self, has_permission=None, request_id=None):
        # Indicates whether the service-linked role was created. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_permission = has_permission  # type: bool
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlrRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSlrRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSlrRoleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSlrRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSlrRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLimitRequest(TeaModel):
    def __init__(self, feature_type=None, id=None, lang=None, source_ip=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The ID of the data asset.
        # 
        # You can call the DescribeDataLimits operation to query the IDs of data assets. The value of the Id response parameter indicates the ID of a data asset.
        self.id = id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLimitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteDataLimitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataLimitResponseBody, self).to_map()
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


class DeleteDataLimitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataLimitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataLimitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(self, feature_type=None, id=None, lang=None, source_ip=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The ID of the sensitive data detection rule.
        self.id = id  # type: long
        # The language of the content within the request and response. Valid values: **zh** and **en**. The value zh indicates Chinese, and the value en indicates English.
        self.lang = lang  # type: str
        # This parameter is deprecated.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleResponseBody, self).to_map()
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


class DeleteRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryTemplateListRequest(TeaModel):
    def __init__(self, current_page=None, feature_type=None, lang=None, page_size=None, usage_scenario=None):
        self.current_page = current_page  # type: int
        self.feature_type = feature_type  # type: int
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.usage_scenario = usage_scenario  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')
        return self


class DescribeCategoryTemplateListResponseBodyItems(TeaModel):
    def __init__(self, current_risk_level=None, description=None, gmt_create=None, gmt_modified=None, id=None,
                 max_category_level=None, max_risk_level=None, name=None, status=None, support_edit=None, type=None):
        self.current_risk_level = current_risk_level  # type: int
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: long
        self.max_category_level = max_category_level  # type: int
        self.max_risk_level = max_risk_level  # type: int
        self.name = name  # type: str
        self.status = status  # type: int
        self.support_edit = support_edit  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryTemplateListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_risk_level is not None:
            result['CurrentRiskLevel'] = self.current_risk_level
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.max_category_level is not None:
            result['MaxCategoryLevel'] = self.max_category_level
        if self.max_risk_level is not None:
            result['MaxRiskLevel'] = self.max_risk_level
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.support_edit is not None:
            result['SupportEdit'] = self.support_edit
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentRiskLevel') is not None:
            self.current_risk_level = m.get('CurrentRiskLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxCategoryLevel') is not None:
            self.max_category_level = m.get('MaxCategoryLevel')
        if m.get('MaxRiskLevel') is not None:
            self.max_risk_level = m.get('MaxRiskLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportEdit') is not None:
            self.support_edit = m.get('SupportEdit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCategoryTemplateListResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeCategoryTemplateListResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCategoryTemplateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCategoryTemplateListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCategoryTemplateListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCategoryTemplateListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCategoryTemplateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCategoryTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryTemplateRuleListRequest(TeaModel):
    def __init__(self, current_page=None, feature_type=None, lang=None, page_size=None, risk_level_id=None,
                 status=None):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page  # type: int
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The sensitivity level of the data that is not compliant with the rule. Valid values: **1** to **11**. Default value: **null**.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: specifies the S1 sensitivity level.
        # *   **3**: specifies the S2 sensitivity level.
        # *   **4**: specifies the S3 sensitivity level.
        # *   **5**: specifies the S4 sensitivity level.
        # *   **6**: specifies the S5 sensitivity level.
        # *   **7**: specifies the S6 sensitivity level.
        # *   **8**: specifies the S7 sensitivity level.
        # *   **9**: specifies the S8 sensitivity level.
        # *   **10**: specifies the S9 sensitivity level.
        # *   **11**: specifies the S10 sensitivity level.
        # *   **null**: specifies all preceding sensitivity levels.
        self.risk_level_id = risk_level_id  # type: long
        # The status of the rule. Default value: **null**. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # *   **null**: all states
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryTemplateRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryTemplateRuleListResponseBodyItems(TeaModel):
    def __init__(self, description=None, id=None, identification_rule_ids=None, identification_scope=None,
                 name=None, risk_level_id=None, status=None):
        # The description of the rule.
        self.description = description  # type: str
        # The unique ID of the rule.
        self.id = id  # type: long
        # The IDs of sensitive data types. Multiple IDs are separated by commas (,).
        self.identification_rule_ids = identification_rule_ids  # type: str
        # The scan scope of the rule. The value is a JSON array of the STRING type. Each element in a JSON array indicates a scan scope that contains the following fields:
        # 
        # *   **Asset**: the data asset type. Valid values: RDS, DRDS, PolarDB, OTS, ADB, and OceanBase. The value is of the STRING type.
        # 
        # *   **Content**: the scan scope. The value is of the STRING type. Each element in a JSON array indicates a scan scope that contains the following fields:
        # 
        #     *   **Range**: the matching condition. Valid values: Instance, database, table, column, project, bucket, and object. The value project is valid only for data assets in MaxCompute. The values bucket and object are valid only for data assets in Object Storage Service (OSS). The value of this parameter is of the STRING type.
        #     *   **Operator**: the operator. Valid values: equals, regex, prefix, and suffix. The operator equals indicates a full match. The operator regex indicates a match by regular expression. The operator prefix indicates a match by prefix. The operator suffix indicates a match by suffix.
        #     *   **Value**: the matching content. The value is of the STRING type.
        self.identification_scope = identification_scope  # type: str
        # The name of the rule.
        self.name = name  # type: str
        # The sensitivity level of the data that is not compliant with the rule. Valid values: **1** to **11**.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: indicates the S1 sensitivity level.
        # *   **3**: indicates the S2 sensitivity level.
        # *   **4**: indicates the S3 sensitivity level.
        # *   **5**: indicates the S4 sensitivity level.
        # *   **6**: indicates the S5 sensitivity level.
        # *   **7**: indicates the S6 sensitivity level.
        # *   **8**: indicates the S7 sensitivity level.
        # *   **9**: indicates the S8 sensitivity level.
        # *   **10**: indicates the S9 sensitivity level.
        # *   **11**: indicates the S10 sensitivity level.
        # *   **null**: indicates all preceding sensitivity levels.
        self.risk_level_id = risk_level_id  # type: long
        # The status of the rule. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # *   **null**: all states
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCategoryTemplateRuleListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.identification_rule_ids is not None:
            result['IdentificationRuleIds'] = self.identification_rule_ids
        if self.identification_scope is not None:
            result['IdentificationScope'] = self.identification_scope
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdentificationRuleIds') is not None:
            self.identification_rule_ids = m.get('IdentificationRuleIds')
        if m.get('IdentificationScope') is not None:
            self.identification_scope = m.get('IdentificationScope')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCategoryTemplateRuleListResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The list of rules.
        self.items = items  # type: list[DescribeCategoryTemplateRuleListResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of rules in the template.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCategoryTemplateRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCategoryTemplateRuleListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCategoryTemplateRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCategoryTemplateRuleListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCategoryTemplateRuleListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCategoryTemplateRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColumnsRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, instance_name=None, lang=None, name=None, page_size=None,
                 product_code=None, risk_level_id=None, rule_id=None, rule_name=None, sens_level_name=None, table_id=None,
                 table_name=None):
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The ID of the instance to which data in the column of the table belongs.
        # 
        # > You can call the [DescribeInstances](~~DescribeRules~~) operation to query the IDs of instances.
        self.instance_id = instance_id  # type: long
        # The name of the instance to which data in the column of the table belongs.
        self.instance_name = instance_name  # type: str
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The search keyword. Fuzzy match is supported.
        # 
        # For example, if you enter **test**, all columns whose names contain **test** are retrieved.
        self.name = name  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.risk_level_id = risk_level_id  # type: long
        # The ID of the sensitive data detection rule that data in the column of the table hits.
        # 
        # > You can call the [DescribeRules](~~DescribeRules~~) operation to query the IDs of sensitive data detection rules.
        self.rule_id = rule_id  # type: long
        # The name of the sensitive data detection rule that data in the column of the table hits.
        self.rule_name = rule_name  # type: str
        # The name of the sensitivity level of the data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **N/A**: No sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.sens_level_name = sens_level_name  # type: str
        # The ID of the table to which the column belongs.
        # 
        # > You can call the [DescribeTables](~~DescribeTables~~) operation to query the IDs of tables.
        self.table_id = table_id  # type: long
        # The name of the table.
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        # The tag ID.
        # 
        # *   **101**: sensitive personal information
        # *   **102**: personal information
        # *   **103**: important information
        self.id = id  # type: long
        # The tag name.
        # 
        # *   Sensitive personal information
        # *   Personal information
        # *   Important information
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeColumnsResponseBodyItems(TeaModel):
    def __init__(self, creation_time=None, data_type=None, id=None, instance_id=None, instance_name=None,
                 model_tags=None, name=None, odps_risk_level_name=None, odps_risk_level_value=None, product_code=None,
                 revision_id=None, revision_status=None, risk_level_id=None, risk_level_name=None, rule_id=None, rule_name=None,
                 sens_level_name=None, sensitive=None, table_id=None, table_name=None):
        # The time when the data in the column of the table is created. Unit: milliseconds.
        self.creation_time = creation_time  # type: long
        # The type of data in the column of the table.
        self.data_type = data_type  # type: str
        # The ID of the column of the table.
        self.id = id  # type: str
        # The ID of the instance to which data in the column of the table belongs.
        self.instance_id = instance_id  # type: long
        # The name of the instance to which data in the column of the table belongs.
        self.instance_name = instance_name  # type: str
        # A list of tags for data that hits the recognition model.
        self.model_tags = model_tags  # type: list[DescribeColumnsResponseBodyItemsModelTags]
        # The name of the column of the table.
        self.name = name  # type: str
        # The name of the sensitivity level for asset. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.odps_risk_level_name = odps_risk_level_name  # type: str
        # The ID of the sensitivity level of the asset. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.odps_risk_level_value = odps_risk_level_value  # type: int
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The ID of the revision record.
        self.revision_id = revision_id  # type: long
        # Indicates whether the column is revised. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.revision_status = revision_status  # type: long
        # The ID of the sensitivity level of data in the column of the table. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for data in the column of the table. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name  # type: str
        # The ID of the sensitive data detection rule that data in the column of the table hits.
        self.rule_id = rule_id  # type: long
        # The name of the sensitive data detection rule that data in the column of the table hits.
        self.rule_name = rule_name  # type: str
        # The name of the sensitivity level. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.sens_level_name = sens_level_name  # type: str
        # Indicates whether the column contains sensitive data. Valid values:
        # 
        # *   true
        # *   false
        self.sensitive = sensitive  # type: bool
        # The ID of the table.
        self.table_id = table_id  # type: long
        # The name of the table to which the revised column belongs.
        self.table_name = table_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.odps_risk_level_value is not None:
            result['OdpsRiskLevelValue'] = self.odps_risk_level_value
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id
        if self.revision_status is not None:
            result['RevisionStatus'] = self.revision_status
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeColumnsResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('OdpsRiskLevelValue') is not None:
            self.odps_risk_level_value = m.get('OdpsRiskLevelValue')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')
        if m.get('RevisionStatus') is not None:
            self.revision_status = m.get('RevisionStatus')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # A list of columns.
        self.items = items  # type: list[DescribeColumnsResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeColumnsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeColumnsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeColumnsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeColumnsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColumnsV2Request(TeaModel):
    def __init__(self, current_page=None, instance_id=None, instance_name=None, lang=None, name=None, page_size=None,
                 product_code=None, risk_level_id=None, rule_id=None, rule_name=None, sens_level_name=None, table_id=None,
                 table_name=None):
        self.current_page = current_page  # type: int
        self.instance_id = instance_id  # type: long
        self.instance_name = instance_name  # type: str
        self.lang = lang  # type: str
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: str
        self.risk_level_id = risk_level_id  # type: long
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.sens_level_name = sens_level_name  # type: str
        self.table_id = table_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsV2ResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColumnsV2ResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeColumnsV2ResponseBodyItems(TeaModel):
    def __init__(self, creation_time=None, data_type=None, id=None, instance_id=None, instance_name=None,
                 model_tags=None, name=None, odps_risk_level_name=None, odps_risk_level_value=None, product_code=None,
                 revision_id=None, revision_status=None, risk_level_id=None, risk_level_name=None, rule_id=None, rule_name=None,
                 sens_level_name=None, sensitive=None, table_id=None, table_name=None):
        self.creation_time = creation_time  # type: long
        self.data_type = data_type  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: long
        self.instance_name = instance_name  # type: str
        self.model_tags = model_tags  # type: list[DescribeColumnsV2ResponseBodyItemsModelTags]
        self.name = name  # type: str
        self.odps_risk_level_name = odps_risk_level_name  # type: str
        self.odps_risk_level_value = odps_risk_level_value  # type: int
        self.product_code = product_code  # type: str
        self.revision_id = revision_id  # type: long
        self.revision_status = revision_status  # type: long
        self.risk_level_id = risk_level_id  # type: long
        self.risk_level_name = risk_level_name  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.sens_level_name = sens_level_name  # type: str
        self.sensitive = sensitive  # type: bool
        self.table_id = table_id  # type: long
        self.table_name = table_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeColumnsV2ResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.odps_risk_level_value is not None:
            result['OdpsRiskLevelValue'] = self.odps_risk_level_value
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id
        if self.revision_status is not None:
            result['RevisionStatus'] = self.revision_status
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeColumnsV2ResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('OdpsRiskLevelValue') is not None:
            self.odps_risk_level_value = m.get('OdpsRiskLevelValue')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')
        if m.get('RevisionStatus') is not None:
            self.revision_status = m.get('RevisionStatus')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsV2ResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeColumnsV2ResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeColumnsV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeColumnsV2ResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeColumnsV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeColumnsV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeColumnsV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeColumnsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigsRequest(TeaModel):
    def __init__(self, lang=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeConfigsResponseBodyConfigList(TeaModel):
    def __init__(self, code=None, default_value=None, description=None, id=None, value=None):
        # The code of the common configuration item.
        self.code = code  # type: str
        # The description of the default value for the common configuration item.
        self.default_value = default_value  # type: str
        # The description of the common configuration item.
        self.description = description  # type: str
        # The unique ID of the common configuration item.
        self.id = id  # type: long
        # The value of the common configuration item.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigsResponseBodyConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeConfigsResponseBody(TeaModel):
    def __init__(self, config_list=None, request_id=None):
        # An array that consists of common configuration items for alerts.
        self.config_list = config_list  # type: list[DescribeConfigsResponseBodyConfigList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeConfigsResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeConfigsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataAssetsRequest(TeaModel):
    def __init__(self, current_page=None, lang=None, name=None, page_size=None, range_id=None, risk_levels=None,
                 rule_id=None):
        # The number of the page to return.
        self.current_page = current_page  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The keyword that is used to search for data assets. Fuzzy search is supported.
        self.name = name  # type: str
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size  # type: int
        # The type of the data asset that you want to query. Valid values:
        # 
        # *   **1**: MaxCompute project
        # *   **2**: MaxCompute table
        # *   **3**: MaxCompute package
        # *   **11**: AnalyticDB for MySQL database
        # *   **12**: AnalyticDB for MySQL table
        # *   **21**: Object Storage Service (OSS) bucket
        # *   **22**: OSS object
        # *   **31**: Tablestore instance
        # *   **32**: Tablestore table
        # *   **51**: ApsaraDB RDS database
        # *   **52**: ApsaraDB RDS table
        # *   **61**: self-managed database hosted on an Elastic Compute Service (ECS) instance
        # *   **62**: self-managed table hosted on an ECS instance
        # *   **71**: PolarDB-X database
        # *   **72**: PolarDB-X table
        # *   **81**: PolarDB database
        # *   **82**: PolarDB table
        # *   **91**: AnalyticDB for PostgreSQL database
        # *   **92**: AnalyticDB for PostgreSQL table
        self.range_id = range_id  # type: int
        # The sensitivity level of the data asset. Separate multiple sensitivity levels with commas (,). Valid values:
        # 
        # *   **2**: S1, indicating the low sensitivity level
        # *   **3**: S2, indicating the medium sensitivity level
        # *   **4**: S3, indicating the high sensitivity level
        # *   **5**: S4, indicating the highest sensitivity level
        self.risk_levels = risk_levels  # type: str
        # The unique ID of the sensitive data detection rule that the data assets to be queried hit.
        # 
        # > If you query sensitive data detection results based on the sensitive data detection rule that the data assets hit, you can call the [DescribeRules](~~DescribeRules~~) operation to query the ID of the sensitive data detection rule.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataAssetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.range_id is not None:
            result['RangeId'] = self.range_id
        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RangeId') is not None:
            self.range_id = m.get('RangeId')
        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeDataAssetsResponseBodyItems(TeaModel):
    def __init__(self, acl=None, creation_time=None, data_type=None, id=None, labelsec=None, name=None,
                 object_key=None, odps_risk_level_name=None, owner=None, product_code=None, product_id=None, protection=None,
                 risk_level_id=None, risk_level_name=None, rule_name=None, sensitive=None, sensitive_count=None,
                 sensitive_ratio=None, total_count=None):
        # The access control list (ACL) that controls the access permissions on the OSS bucket.
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **21**.
        self.acl = acl  # type: str
        # The time when the data asset was created. Unit: milliseconds.
        self.creation_time = creation_time  # type: long
        # The data type of the data asset.
        self.data_type = data_type  # type: str
        # The ID of the data asset.
        self.id = id  # type: str
        # The sensitivity tag of the data. The value is fixed as **0**. **0**, **1**, **2**, or **3** is returned for this parameter only when you set the parameter **RangeId** to **1**.
        # 
        # *   **0**: unclassified
        # *   **1**: confidential
        # *   **2**: sensitive
        # *   **3**: highly sensitive
        self.labelsec = labelsec  # type: bool
        # The name of the data asset.
        self.name = name  # type: str
        # The key value of the OSS object.
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **22**.
        self.object_key = object_key  # type: str
        # The sensitivity level of the MaxCompute data asset. Valid values:
        # 
        # *   **S1**: low sensitivity level
        # *   **S2**: medium sensitivity level
        # *   **S3**: high sensitivity level
        # *   **S4**: highest sensitivity level
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **1**.
        self.odps_risk_level_name = odps_risk_level_name  # type: str
        # The account that owns the data asset.
        self.owner = owner  # type: str
        # The name of the service to which the data asset belongs.
        self.product_code = product_code  # type: str
        # The ID of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.product_id = product_id  # type: str
        # Indicates whether the data protection mechanism is enabled for the data asset. The value is fixed as **false**. **true** or **false** is returned for this parameter only when you set the parameter **RangeId** to **1**.
        # 
        # *   **false**: The data protection mechanism is disabled.
        # *   **true**: The data protection mechanism is enabled. Only data inbound is supported. Data outbound is not supported.
        self.protection = protection  # type: bool
        # The sensitivity level of the data asset. A higher sensitivity level indicates that the identified data is more sensitive. Valid values:
        # 
        # *   **1**: No sensitive data is identified.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **3**: sensitive data at level 3.
        # *   **5**: sensitive data at level 4.
        # *   **6**: sensitive data at level 5.
        # *   **7**: sensitive data at level 6.
        # *   **8**: sensitive data at level 7.
        # *   **9**: sensitive data at level 8.
        # *   **10**: sensitive data at level 9.
        # *   **11**: sensitive data at level 10.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the data asset.
        self.risk_level_name = risk_level_name  # type: str
        # The name of the sensitive data detection rule that the data asset hits.
        self.rule_name = rule_name  # type: str
        # Indicates whether the data asset contains sensitive data. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sensitive = sensitive  # type: bool
        # The total number of sensitive data assets. For example, the value can be the total number of sensitive MaxCompute projects, packages, or tables, the total number of sensitive ApsaraDB RDS databases or tables, or the total number of sensitive OSS buckets or objects.
        self.sensitive_count = sensitive_count  # type: int
        # The percentage of sensitive data in all data assets.
        self.sensitive_ratio = sensitive_ratio  # type: str
        # The total number of data assets. For example, the value can be the total number of MaxCompute projects, packages, or tables, the total number of ApsaraDB RDS databases or tables, or the total number of OSS buckets or objects.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataAssetsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec
        if self.name is not None:
            result['Name'] = self.name
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.protection is not None:
            result['Protection'] = self.protection
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acl') is not None:
            self.acl = m.get('Acl')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataAssetsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of data assets.
        self.items = items  # type: list[DescribeDataAssetsResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of queried data assets that contain sensitive data.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataAssetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataAssetsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataAssetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataAssetsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataAssetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitDetailRequest(TeaModel):
    def __init__(self, feature_type=None, id=None, lang=None, network_type=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The unique ID of the data asset that you want to query.
        # 
        # > You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the ID of the data asset.
        self.id = id  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Simplified Chinese.
        # *   **en**: English
        self.lang = lang  # type: str
        # The network type of the data asset that you want to query. Valid values:
        # 
        # *   **1**: virtual private cloud (VPC)
        # *   **2**: classic network
        self.network_type = network_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class DescribeDataLimitDetailResponseBodyDataLimit(TeaModel):
    def __init__(self, check_status=None, check_status_name=None, gmt_create=None, id=None, local_name=None,
                 parent_id=None, port=None, region_id=None, resource_type=None, resource_type_code=None, user_name=None):
        # The status of the connectivity test between the data asset and DSC. Valid values:
        # 
        # *   **2**: indicates that the data asset was being connected.
        # *   **3**: indicates that the data asset was connected to DSC.
        # *   **4**: indicates that the data asset failed to be connected.
        self.check_status = check_status  # type: int
        # The result that indicates the status of the connectivity test between the data asset and DSC. Valid values:
        # 
        # *   **Passed**\
        # *   **Failed**\
        # *   **Testing**\
        self.check_status_name = check_status_name  # type: str
        # The time when the data asset was connected to DSC. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The ID of the data asset.
        self.id = id  # type: long
        # The region in which the data asset resides.
        self.local_name = local_name  # type: str
        # The ID and name of the data asset in the service to which the data asset belongs.
        self.parent_id = parent_id  # type: str
        # The port number that is used to connect to the database.
        self.port = port  # type: int
        # The ID of the region in which the data asset resides.
        self.region_id = region_id  # type: str
        # The type of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: long
        # The service to which the data asset belongs. Valid values:
        # 
        # *   **MaxCompute**\
        # *   **OSS**\
        # *   **ADS**\
        # *   **OTS**\
        # *   **RDS**\
        self.resource_type_code = resource_type_code  # type: str
        # The account of the user who manages the data asset.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitDetailResponseBodyDataLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDataLimitDetailResponseBody(TeaModel):
    def __init__(self, data_limit=None, request_id=None):
        # The details of the data asset.
        self.data_limit = data_limit  # type: DescribeDataLimitDetailResponseBodyDataLimit
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_limit:
            self.data_limit.validate()

    def to_map(self):
        _map = super(DescribeDataLimitDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit is not None:
            result['DataLimit'] = self.data_limit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataLimit') is not None:
            temp_model = DescribeDataLimitDetailResponseBodyDataLimit()
            self.data_limit = temp_model.from_map(m['DataLimit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataLimitDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataLimitDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataLimitDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataLimitDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitSetRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, parent_id=None, resource_type=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The parent asset ID of the data asset.
        # 
        # You can call the [DescribeDataLimitDetail](~~DescribeDataLimitDetail~~) or [DescribeDataLimits](~~DescribeDataLimits~~) operation to obtain the parent asset ID of the data asset from the value of the **ParentId** parameter.
        self.parent_id = parent_id  # type: str
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList(TeaModel):
    def __init__(self, check_status=None, check_status_name=None, connector=None, gmt_create=None, id=None,
                 local_name=None, parent_id=None, region_id=None, resource_type=None, resource_type_code=None, user_name=None):
        # Indicates whether the test of connectivity between DSC and the data asset is passed.
        # 
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test is passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status  # type: int
        # The name of the data detection status.
        self.check_status_name = check_status_name  # type: str
        # The connection string that is used to access the data asset.
        self.connector = connector  # type: str
        # The time when the data asset was created. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The ID of the data asset.
        self.id = id  # type: long
        # The region in which the data asset resides.
        self.local_name = local_name  # type: str
        # The parent asset ID of the data asset.
        self.parent_id = parent_id  # type: str
        # The region in which the data asset resides.
        self.region_id = region_id  # type: str
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: long
        # The code of the service to which the data asset belongs. Valid values:
        # 
        # *   **ODPS**\
        # *   **OSS**\
        # *   **ADS**\
        # *   **OTS**\
        # *   **RDS**\
        self.resource_type_code = resource_type_code  # type: str
        # The username that is used to access the data asset.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.connector is not None:
            result['Connector'] = self.connector
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList(TeaModel):
    def __init__(self, bucket_name=None, region_id=None):
        # The name of the OSS bucket to which the OSS object belongs.
        self.bucket_name = bucket_name  # type: str
        # The region ID of the OSS object.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSetRegionList(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitSetResponseBodyDataLimitSetRegionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataLimitSetResponseBodyDataLimitSet(TeaModel):
    def __init__(self, data_limit_list=None, oss_bucket_list=None, region_list=None, resource_type=None,
                 resource_type_code=None, total_count=None):
        # An array that consists of data assets that DSC is authorized to scan.
        self.data_limit_list = data_limit_list  # type: list[DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList]
        # An array consisting of the OSS objects that DSC is authorized to scan.
        self.oss_bucket_list = oss_bucket_list  # type: list[DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList]
        # An array consisting of the regions in which the data assets can be scanned.
        self.region_list = region_list  # type: list[DescribeDataLimitSetResponseBodyDataLimitSetRegionList]
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: long
        # The service to which the data asset belongs. Valid values:
        # 
        # *   **ODPS**\
        # *   **OSS**\
        # *   **ADS**\
        # *   **OTS**\
        # *   **RDS**\
        self.resource_type_code = resource_type_code  # type: str
        # The total number of data objects in the data assets.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data_limit_list:
            for k in self.data_limit_list:
                if k:
                    k.validate()
        if self.oss_bucket_list:
            for k in self.oss_bucket_list:
                if k:
                    k.validate()
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataLimitSetResponseBodyDataLimitSet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataLimitList'] = []
        if self.data_limit_list is not None:
            for k in self.data_limit_list:
                result['DataLimitList'].append(k.to_map() if k else None)
        result['OssBucketList'] = []
        if self.oss_bucket_list is not None:
            for k in self.oss_bucket_list:
                result['OssBucketList'].append(k.to_map() if k else None)
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_limit_list = []
        if m.get('DataLimitList') is not None:
            for k in m.get('DataLimitList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList()
                self.data_limit_list.append(temp_model.from_map(k))
        self.oss_bucket_list = []
        if m.get('OssBucketList') is not None:
            for k in m.get('OssBucketList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList()
                self.oss_bucket_list.append(temp_model.from_map(k))
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = DescribeDataLimitSetResponseBodyDataLimitSetRegionList()
                self.region_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataLimitSetResponseBody(TeaModel):
    def __init__(self, data_limit_set=None, request_id=None):
        # The information about the data asset.
        self.data_limit_set = data_limit_set  # type: DescribeDataLimitSetResponseBodyDataLimitSet
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_limit_set:
            self.data_limit_set.validate()

    def to_map(self):
        _map = super(DescribeDataLimitSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_limit_set is not None:
            result['DataLimitSet'] = self.data_limit_set.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataLimitSet') is not None:
            temp_model = DescribeDataLimitSetResponseBodyDataLimitSet()
            self.data_limit_set = temp_model.from_map(m['DataLimitSet'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataLimitSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataLimitSetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataLimitSetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataLimitSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataLimitsRequest(TeaModel):
    def __init__(self, audit_status=None, check_status=None, current_page=None, datamask_status=None, enable=None,
                 end_time=None, engine_type=None, feature_type=None, lang=None, member_account=None, page_size=None,
                 parent_id=None, resource_type=None, service_region_id=None, start_time=None):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status  # type: int
        # The data detection status. Valid values:
        # 
        # *   **0**: The data detection is ready.
        # *   **1**: The data detection is running.
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status  # type: int
        # The number of the page to return.
        self.current_page = current_page  # type: int
        # Specifies whether DSC has the data de-identification permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.datamask_status = datamask_status  # type: int
        # Specifies whether DSC has the data detection permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable  # type: int
        # The end of the time range to query The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The type of the database engine. Valid values include **MySQL**, **SQLServer**, **Oracle**, **PostgreSQL**, and **MongoDB**.
        self.engine_type = engine_type  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        self.member_account = member_account  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The parent ID of the data asset to be queried. Valid values:
        # 
        # *   The name or ID of the MaxCompute project.
        # *   The name or ID of the OSS bucket.
        # *   The name or ID of the ApsaraDB RDS instance or database.
        self.parent_id = parent_id  # type: str
        # The type of the service to which the data asset to be queried belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed database
        self.resource_type = resource_type  # type: int
        # The region in which the data asset resides.
        self.service_region_id = service_region_id  # type: str
        # The beginning of the time range to query The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataLimitsResponseBodyItems(TeaModel):
    def __init__(self, audit_status=None, auto_scan=None, check_status=None, check_status_name=None,
                 datamask_status=None, db_version=None, enable=None, engine_type=None, error_code=None, error_message=None,
                 event_status=None, gmt_create=None, id=None, instance_description=None, instance_id=None,
                 last_finished_time=None, local_name=None, log_store_day=None, member_account=None, next_start_time=None,
                 ocr_status=None, parent_id=None, port=None, process_status=None, process_total_count=None, region_id=None,
                 resource_type=None, resource_type_code=None, sampling_size=None, security_group_id_list=None,
                 support_audit=None, support_datamask=None, support_event=None, support_ocr=None, support_scan=None,
                 tenant_name=None, total_count=None, user_name=None, v_switch_id_list=None, vpc_id=None):
        # Indicates whether the security audit feature is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status  # type: int
        # Indicates whether the data asset can be automatically scanned. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auto_scan = auto_scan  # type: int
        # The data detection status. Valid values:
        # 
        # *   **0**: The data detection is ready.
        # *   **1**: The data detection is running.
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status  # type: int
        # The name of the data detection status.
        self.check_status_name = check_status_name  # type: str
        # Indicates whether DSC has the data de-identification permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.datamask_status = datamask_status  # type: int
        # The database engine version of the instance.
        self.db_version = db_version  # type: str
        # Indicates whether DSC has the data detection permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable  # type: int
        # The type of the database engine. Valid values include **MySQL**, **SQLServer**, **Oracle**, **PostgreSQL**, and **MongoDB**.
        self.engine_type = engine_type  # type: str
        # The error code that is returned.
        self.error_code = error_code  # type: str
        # The reason for the failure.
        self.error_message = error_message  # type: str
        # Indicates whether the data leak prevention feature is enabled. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes (default value)
        self.event_status = event_status  # type: int
        # The time when the data asset was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The ID of the data asset.
        self.id = id  # type: long
        # The description of the instance.
        self.instance_description = instance_description  # type: str
        # The ID of the instance to which the table belongs.
        self.instance_id = instance_id  # type: str
        # The time when the last scan was finished.
        # 
        # *   The value is a UNIX timestamp.
        # *   Unit: milliseconds.
        self.last_finished_time = last_finished_time  # type: long
        # The region in which the data asset resides.
        self.local_name = local_name  # type: str
        # The retention period of raw logs. Unit: days.
        self.log_store_day = log_store_day  # type: int
        self.member_account = member_account  # type: long
        # The next time when the data asset is scanned. The value is a UNIX timestamp. Unit: milliseconds.
        self.next_start_time = next_start_time  # type: long
        # Indicates whether the optical character recognition (OCR) feature is enabled. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.ocr_status = ocr_status  # type: int
        # The parent ID of the data asset. Valid values include **bucket, db, and project**.
        self.parent_id = parent_id  # type: str
        # The port number of the self-managed database.
        self.port = port  # type: int
        # The status of the data asset scan. Valid values:
        # 
        # *   **-1**: invalid
        # *   **0**: waiting
        # *   **1**: being scanned
        # *   **2**: suspended
        # *   **3**: completed
        self.process_status = process_status  # type: int
        # The total number of data tables or files.
        self.process_total_count = process_total_count  # type: int
        # The region in which the data asset resides.
        self.region_id = region_id  # type: str
        # The type of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed database
        self.resource_type = resource_type  # type: long
        # The code of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.resource_type_code = resource_type_code  # type: str
        # The number of sensitive data samples. Valid values: **0**, **5**, and **10**. Unit: data entries.
        self.sampling_size = sampling_size  # type: int
        # The array consisting of the IDs of the security groups that are used by PrivateLink when you install the DSC agent.
        self.security_group_id_list = security_group_id_list  # type: list[str]
        # Indicates whether the security audit feature is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_audit = support_audit  # type: bool
        # Indicates whether data de-identification is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_datamask = support_datamask  # type: bool
        # Indicates whether anomalous event detection is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_event = support_event  # type: bool
        # Indicates whether OCR is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_ocr = support_ocr  # type: bool
        # Indicates whether the data asset scan feature is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_scan = support_scan  # type: bool
        # The alias of the tenant.
        self.tenant_name = tenant_name  # type: str
        # The total number of fields in the table.
        self.total_count = total_count  # type: int
        # The username that is used to access the data asset.
        self.user_name = user_name  # type: str
        # The array consisting of the IDs of the vSwitches that are used by PrivateLink when you install the DSC agent.
        self.v_switch_id_list = v_switch_id_list  # type: list[str]
        # The ID of the virtual private cloud (VPC) to which the data asset belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataLimitsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_finished_time is not None:
            result['LastFinishedTime'] = self.last_finished_time
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time
        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.process_total_count is not None:
            result['ProcessTotalCount'] = self.process_total_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.security_group_id_list is not None:
            result['SecurityGroupIdList'] = self.security_group_id_list
        if self.support_audit is not None:
            result['SupportAudit'] = self.support_audit
        if self.support_datamask is not None:
            result['SupportDatamask'] = self.support_datamask
        if self.support_event is not None:
            result['SupportEvent'] = self.support_event
        if self.support_ocr is not None:
            result['SupportOcr'] = self.support_ocr
        if self.support_scan is not None:
            result['SupportScan'] = self.support_scan
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastFinishedTime') is not None:
            self.last_finished_time = m.get('LastFinishedTime')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')
        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('ProcessTotalCount') is not None:
            self.process_total_count = m.get('ProcessTotalCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('SecurityGroupIdList') is not None:
            self.security_group_id_list = m.get('SecurityGroupIdList')
        if m.get('SupportAudit') is not None:
            self.support_audit = m.get('SupportAudit')
        if m.get('SupportDatamask') is not None:
            self.support_datamask = m.get('SupportDatamask')
        if m.get('SupportEvent') is not None:
            self.support_event = m.get('SupportEvent')
        if m.get('SupportOcr') is not None:
            self.support_ocr = m.get('SupportOcr')
        if m.get('SupportScan') is not None:
            self.support_scan = m.get('SupportScan')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDataLimitsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the data assets.
        self.items = items  # type: list[DescribeDataLimitsResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataLimitsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataLimitsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataLimitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataLimitsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataLimitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataLimitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataMaskingRunHistoryRequest(TeaModel):
    def __init__(self, current_page=None, dst_type=None, end_time=None, lang=None, main_process_id=None,
                 page_size=None, src_table_name=None, src_type=None, start_time=None, status=None, task_id=None):
        # The number of the page to return.
        self.current_page = current_page  # type: int
        # The type of the service to which the de-identified data belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.dst_type = dst_type  # type: int
        # The end of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The ID of the task.
        # 
        # > If a task has one or more subtasks, the value of the parameter must be the ID of the task. Otherwise, leave this parameter empty.
        self.main_process_id = main_process_id  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the source table.
        self.src_table_name = src_table_name  # type: str
        # The type of the service to which the data to be de-identified belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.src_type = src_type  # type: int
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the de-identification task. Valid values:
        # 
        # *   **-1**: waiting
        # *   **0**: being executed
        # *   **1**: executed
        # *   **2**: failed to be executed
        # *   **3**: terminated
        # *   **4**: partially failed
        self.status = status  # type: int
        # The ID of the de-identification task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataMaskingRunHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.main_process_id is not None:
            result['MainProcessId'] = self.main_process_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MainProcessId') is not None:
            self.main_process_id = m.get('MainProcessId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDataMaskingRunHistoryResponseBodyItems(TeaModel):
    def __init__(self, conflict_count=None, dst_type=None, dst_type_code=None, end_time=None, fail_code=None,
                 fail_msg=None, has_download_file=None, has_sub_process=None, id=None, masking_count=None, percentage=None,
                 run_index=None, src_table_name=None, src_type=None, src_type_code=None, start_time=None, status=None,
                 task_id=None, type=None):
        # The number of rows that are in conflict with the data to be de-identified in the destination table to which the data to be de-identified is moved.
        self.conflict_count = conflict_count  # type: long
        # The type of the service to which the de-identified data belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.dst_type = dst_type  # type: int
        # The service that stores the de-identified data. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.dst_type_code = dst_type_code  # type: str
        # The end time of the de-identification task.
        self.end_time = end_time  # type: long
        # The error code that is returned when the de-identification task fails.
        self.fail_code = fail_code  # type: str
        # The reason why the de-identification task fails.
        self.fail_msg = fail_msg  # type: str
        # Indicates whether a file is available for download.
        # 
        # *   **1**: yes
        # *   **0**: no
        self.has_download_file = has_download_file  # type: int
        # The number of created subtasks.
        self.has_sub_process = has_sub_process  # type: int
        # The ID of the task execution record.
        self.id = id  # type: long
        # The number of rows that are de-identified.
        self.masking_count = masking_count  # type: long
        # The progress of the de-identification task.
        self.percentage = percentage  # type: int
        # The number of times that the de-identification task is executed.
        self.run_index = run_index  # type: int
        # The name of the source table.
        self.src_table_name = src_table_name  # type: str
        # The type of the service to which the data to be de-identified belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.src_type = src_type  # type: int
        # The service to which the data to be de-identified belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.src_type_code = src_type_code  # type: str
        # The time when the de-identification task was executed. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the de-identification task. Valid values:
        # 
        # *   **-1**: waiting
        # *   **0**: being executed
        # *   **1**: executed
        # *   **2**: failed to be executed
        # *   **3**: terminated
        # *   **4**: partially failed
        self.status = status  # type: int
        # The ID of the identification task.
        self.task_id = task_id  # type: str
        # The mode in which the de-identification task is executed. Valid values:
        # 
        # *   **1**: manual
        # *   **2**: scheduled
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataMaskingRunHistoryResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conflict_count is not None:
            result['ConflictCount'] = self.conflict_count
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg
        if self.has_download_file is not None:
            result['HasDownloadFile'] = self.has_download_file
        if self.has_sub_process is not None:
            result['HasSubProcess'] = self.has_sub_process
        if self.id is not None:
            result['Id'] = self.id
        if self.masking_count is not None:
            result['MaskingCount'] = self.masking_count
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.run_index is not None:
            result['RunIndex'] = self.run_index
        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConflictCount') is not None:
            self.conflict_count = m.get('ConflictCount')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')
        if m.get('HasDownloadFile') is not None:
            self.has_download_file = m.get('HasDownloadFile')
        if m.get('HasSubProcess') is not None:
            self.has_sub_process = m.get('HasSubProcess')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaskingCount') is not None:
            self.masking_count = m.get('MaskingCount')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('RunIndex') is not None:
            self.run_index = m.get('RunIndex')
        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDataMaskingRunHistoryResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The execution information about the de-identification task.
        self.items = items  # type: list[DescribeDataMaskingRunHistoryResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataMaskingRunHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataMaskingRunHistoryResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataMaskingRunHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataMaskingRunHistoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataMaskingRunHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataMaskingRunHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataMaskingTasksRequest(TeaModel):
    def __init__(self, current_page=None, dst_type=None, end_time=None, lang=None, page_size=None, search_key=None,
                 start_time=None):
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The service to which the data to be de-identified belongs. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.dst_type = dst_type  # type: int
        # The end of the time range during which the de-identification tasks to be queried are created. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The keyword used to query the de-identification tasks, which can be the task name or ID.
        self.search_key = search_key  # type: str
        # The beginning of the time range during which the de-identification tasks to be queried are created. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataMaskingTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDataMaskingTasksResponseBodyItems(TeaModel):
    def __init__(self, dst_member_account=None, dst_path=None, dst_type=None, dst_type_code=None, gmt_create=None,
                 has_unfinish_process=None, id=None, original_table=None, owner=None, run_count=None, src_member_account=None,
                 src_path=None, src_type=None, src_type_code=None, status=None, task_id=None, task_name=None,
                 trigger_type=None):
        self.dst_member_account = dst_member_account  # type: long
        # The destination directory.
        self.dst_path = dst_path  # type: str
        # The service to which the data to be de-identified belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.dst_type = dst_type  # type: int
        # The service to which the de-identified data belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.dst_type_code = dst_type_code  # type: str
        # The time when the task was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # Indicates whether the de-identification task is running.
        self.has_unfinish_process = has_unfinish_process  # type: bool
        # The ID of the task.
        self.id = id  # type: long
        # Indicates whether the source table is de-identified.
        self.original_table = original_table  # type: bool
        # The user who created the de-identification task.
        self.owner = owner  # type: str
        # The number of times that the de-identification task is run.
        self.run_count = run_count  # type: int
        self.src_member_account = src_member_account  # type: long
        # The source path.
        self.src_path = src_path  # type: str
        # The code of the service to which the data to be de-identified belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.src_type = src_type  # type: int
        # The service to which the data to be de-identified belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.src_type_code = src_type_code  # type: str
        # The status of the task. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.status = status  # type: int
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The name of the task.
        self.task_name = task_name  # type: str
        # The mode in which the de-identification task is run. Valid values:
        # 
        # *   **1**: manual
        # *   **2**: scheduled
        # *   **3**: manual and scheduled
        self.trigger_type = trigger_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataMaskingTasksResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_member_account is not None:
            result['DstMemberAccount'] = self.dst_member_account
        if self.dst_path is not None:
            result['DstPath'] = self.dst_path
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.has_unfinish_process is not None:
            result['HasUnfinishProcess'] = self.has_unfinish_process
        if self.id is not None:
            result['Id'] = self.id
        if self.original_table is not None:
            result['OriginalTable'] = self.original_table
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.run_count is not None:
            result['RunCount'] = self.run_count
        if self.src_member_account is not None:
            result['SrcMemberAccount'] = self.src_member_account
        if self.src_path is not None:
            result['SrcPath'] = self.src_path
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstMemberAccount') is not None:
            self.dst_member_account = m.get('DstMemberAccount')
        if m.get('DstPath') is not None:
            self.dst_path = m.get('DstPath')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HasUnfinishProcess') is not None:
            self.has_unfinish_process = m.get('HasUnfinishProcess')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OriginalTable') is not None:
            self.original_table = m.get('OriginalTable')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RunCount') is not None:
            self.run_count = m.get('RunCount')
        if m.get('SrcMemberAccount') is not None:
            self.src_member_account = m.get('SrcMemberAccount')
        if m.get('SrcPath') is not None:
            self.src_path = m.get('SrcPath')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class DescribeDataMaskingTasksResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of de-identification tasks.
        self.items = items  # type: list[DescribeDataMaskingTasksResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataMaskingTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataMaskingTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataMaskingTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataMaskingTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataMaskingTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataMaskingTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataObjectColumnDetailRequest(TeaModel):
    def __init__(self, current_page=None, feature_type=None, id=None, lang=None, page_size=None, product_id=None,
                 template_id=None):
        self.current_page = current_page  # type: int
        self.feature_type = feature_type  # type: int
        self.id = id  # type: long
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.product_id = product_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDataObjectColumnDetailResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDataObjectColumnDetailResponseBodyItems(TeaModel):
    def __init__(self, categories=None, column_comment=None, column_name=None, data_type=None, id=None,
                 model_tags=None, primary_key=None, risk_level_id=None, risk_level_name=None, rule_id=None, rule_name=None):
        self.categories = categories  # type: list[str]
        self.column_comment = column_comment  # type: str
        self.column_name = column_name  # type: str
        self.data_type = data_type  # type: str
        self.id = id  # type: str
        self.model_tags = model_tags  # type: list[DescribeDataObjectColumnDetailResponseBodyItemsModelTags]
        self.primary_key = primary_key  # type: bool
        self.risk_level_id = risk_level_id  # type: long
        self.risk_level_name = risk_level_name  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeDataObjectColumnDetailResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDataObjectColumnDetailResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeDataObjectColumnDetailResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataObjectColumnDetailResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataObjectColumnDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataObjectColumnDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataObjectColumnDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataObjectColumnDetailV2Request(TeaModel):
    def __init__(self, current_page=None, feature_type=None, id=None, lang=None, page_size=None, product_id=None,
                 template_id=None):
        self.current_page = current_page  # type: int
        self.feature_type = feature_type  # type: int
        self.id = id  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.product_id = product_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDataObjectColumnDetailV2ResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailV2ResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDataObjectColumnDetailV2ResponseBodyItems(TeaModel):
    def __init__(self, categories=None, column_comment=None, column_name=None, data_type=None, id=None,
                 model_tags=None, primary_key=None, risk_level_id=None, risk_level_name=None, rule_id=None, rule_name=None):
        self.categories = categories  # type: list[str]
        self.column_comment = column_comment  # type: str
        self.column_name = column_name  # type: str
        self.data_type = data_type  # type: str
        self.id = id  # type: str
        self.model_tags = model_tags  # type: list[DescribeDataObjectColumnDetailV2ResponseBodyItemsModelTags]
        self.primary_key = primary_key  # type: bool
        self.risk_level_id = risk_level_id  # type: long
        self.risk_level_name = risk_level_name  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailV2ResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.id is not None:
            result['Id'] = self.id
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeDataObjectColumnDetailV2ResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDataObjectColumnDetailV2ResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeDataObjectColumnDetailV2ResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataObjectColumnDetailV2ResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataObjectColumnDetailV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataObjectColumnDetailV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataObjectColumnDetailV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataObjectColumnDetailV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataObjectsRequest(TeaModel):
    def __init__(self, current_page=None, domain_id=None, feature_type=None, file_category_code=None,
                 file_type=None, instance_id=None, lang=None, member_account=None, model_ids=None, model_tag_ids=None,
                 page_size=None, parent_category_ids=None, product_ids=None, query_name=None, risk_levels=None,
                 service_region_id=None, template_id=None):
        self.current_page = current_page  # type: int
        self.domain_id = domain_id  # type: long
        self.feature_type = feature_type  # type: int
        self.file_category_code = file_category_code  # type: long
        self.file_type = file_type  # type: long
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.member_account = member_account  # type: long
        self.model_ids = model_ids  # type: str
        self.model_tag_ids = model_tag_ids  # type: str
        self.page_size = page_size  # type: int
        self.parent_category_ids = parent_category_ids  # type: str
        self.product_ids = product_ids  # type: str
        self.query_name = query_name  # type: str
        self.risk_levels = risk_levels  # type: str
        self.service_region_id = service_region_id  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        if self.model_ids is not None:
            result['ModelIds'] = self.model_ids
        if self.model_tag_ids is not None:
            result['ModelTagIds'] = self.model_tag_ids
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_category_ids is not None:
            result['ParentCategoryIds'] = self.parent_category_ids
        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids
        if self.query_name is not None:
            result['QueryName'] = self.query_name
        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        if m.get('ModelIds') is not None:
            self.model_ids = m.get('ModelIds')
        if m.get('ModelTagIds') is not None:
            self.model_tag_ids = m.get('ModelTagIds')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentCategoryIds') is not None:
            self.parent_category_ids = m.get('ParentCategoryIds')
        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')
        if m.get('QueryName') is not None:
            self.query_name = m.get('QueryName')
        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDataObjectsResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectsResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDataObjectsResponseBodyItemsRuleList(TeaModel):
    def __init__(self, risk_level_id=None, risk_level_name=None, rule_count=None, rule_id=None, rule_name=None):
        self.risk_level_id = risk_level_id  # type: long
        self.risk_level_name = risk_level_name  # type: str
        self.rule_count = rule_count  # type: int
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataObjectsResponseBodyItemsRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeDataObjectsResponseBodyItems(TeaModel):
    def __init__(self, categories=None, id=None, instance_description=None, instance_id=None, last_scan_time=None,
                 member_account=None, model_tags=None, name=None, object_file_category=None, object_type=None, path=None,
                 product_code=None, product_id=None, region_name=None, rule_list=None, sensitive_count=None, template_id=None):
        self.categories = categories  # type: list[str]
        self.id = id  # type: str
        self.instance_description = instance_description  # type: str
        self.instance_id = instance_id  # type: str
        self.last_scan_time = last_scan_time  # type: long
        self.member_account = member_account  # type: long
        self.model_tags = model_tags  # type: list[DescribeDataObjectsResponseBodyItemsModelTags]
        self.name = name  # type: str
        self.object_file_category = object_file_category  # type: str
        self.object_type = object_type  # type: str
        self.path = path  # type: str
        self.product_code = product_code  # type: str
        self.product_id = product_id  # type: long
        self.region_name = region_name  # type: str
        self.rule_list = rule_list  # type: list[DescribeDataObjectsResponseBodyItemsRuleList]
        self.sensitive_count = sensitive_count  # type: int
        self.template_id = template_id  # type: long

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.object_file_category is not None:
            result['ObjectFileCategory'] = self.object_file_category
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.path is not None:
            result['Path'] = self.path
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeDataObjectsResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectFileCategory') is not None:
            self.object_file_category = m.get('ObjectFileCategory')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeDataObjectsResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDataObjectsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeDataObjectsResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataObjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDataObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataObjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataObjectsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataObjectsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDataObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDocTypesRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeDocTypesResponseBodyDocTypeList(TeaModel):
    def __init__(self, code=None, id=None, name=None):
        self.code = code  # type: long
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDocTypesResponseBodyDocTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDocTypesResponseBody(TeaModel):
    def __init__(self, doc_type_list=None, request_id=None):
        self.doc_type_list = doc_type_list  # type: list[DescribeDocTypesResponseBodyDocTypeList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.doc_type_list:
            for k in self.doc_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDocTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocTypeList'] = []
        if self.doc_type_list is not None:
            for k in self.doc_type_list:
                result['DocTypeList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.doc_type_list = []
        if m.get('DocTypeList') is not None:
            for k in m.get('DocTypeList'):
                temp_model = DescribeDocTypesResponseBodyDocTypeList()
                self.doc_type_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDocTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDocTypesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDocTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDocTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventDetailRequest(TeaModel):
    def __init__(self, id=None, lang=None):
        # The ID of the anomalous event.
        # 
        # > You can call the **DescribeEvents** operation to query the ID of the anomalous event.
        self.id = id  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeEventDetailResponseBodyEventDetailChartData(TeaModel):
    def __init__(self, x=None, y=None, z=None):
        # The values of data on the x-axis.
        self.x = x  # type: list[str]
        # The values of data on the y-axis.
        self.y = y  # type: list[str]
        self.z = z  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventDetailChartData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        if self.z is not None:
            result['Z'] = self.z
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('Z') is not None:
            self.z = m.get('Z')
        return self


class DescribeEventDetailResponseBodyEventDetailChart(TeaModel):
    def __init__(self, chat_type=None, data=None, label=None, name=None, type=None, xlabel=None, ylabel=None,
                 zlabel=None):
        self.chat_type = chat_type  # type: int
        # The data in the baseline behavior profile of the anomalous event.
        self.data = data  # type: DescribeEventDetailResponseBodyEventDetailChartData
        # The name of the baseline behavior chart of the anomalous event.
        self.label = label  # type: str
        self.name = name  # type: str
        # The type of the chart. Valid values:
        # 
        # *   **1**: column chart
        # *   **2**: line chart
        self.type = type  # type: str
        # The descriptive label of data on the x-axis.
        self.xlabel = xlabel  # type: str
        # The descriptive label of data on the y-axis.
        self.ylabel = ylabel  # type: str
        self.zlabel = zlabel  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventDetailChart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_type is not None:
            result['ChatType'] = self.chat_type
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.xlabel is not None:
            result['XLabel'] = self.xlabel
        if self.ylabel is not None:
            result['YLabel'] = self.ylabel
        if self.zlabel is not None:
            result['ZLabel'] = self.zlabel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChatType') is not None:
            self.chat_type = m.get('ChatType')
        if m.get('Data') is not None:
            temp_model = DescribeEventDetailResponseBodyEventDetailChartData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XLabel') is not None:
            self.xlabel = m.get('XLabel')
        if m.get('YLabel') is not None:
            self.ylabel = m.get('YLabel')
        if m.get('ZLabel') is not None:
            self.zlabel = m.get('ZLabel')
        return self


class DescribeEventDetailResponseBodyEventDetailContent(TeaModel):
    def __init__(self, label=None, name=None, value=None):
        # The title of the content in the anomalous event.
        self.label = label  # type: str
        self.name = name  # type: str
        # The description of the content in the anomalous event.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventDetailContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEventDetailResponseBodyEventDetailResourceInfo(TeaModel):
    def __init__(self, label=None, value=None):
        # The source title.
        self.label = label  # type: str
        # The source description.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventDetailResourceInfo, self).to_map()
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


class DescribeEventDetailResponseBodyEventDetail(TeaModel):
    def __init__(self, chart=None, content=None, resource_info=None):
        # An array that consists of the baseline behavior chart of the anomalous event.
        self.chart = chart  # type: list[DescribeEventDetailResponseBodyEventDetailChart]
        # An array that consists of the content in the anomalous event.
        self.content = content  # type: list[DescribeEventDetailResponseBodyEventDetailContent]
        # An array that consists of the source from which the information of the anomalous event is recorded.
        self.resource_info = resource_info  # type: list[DescribeEventDetailResponseBodyEventDetailResourceInfo]

    def validate(self):
        if self.chart:
            for k in self.chart:
                if k:
                    k.validate()
        if self.content:
            for k in self.content:
                if k:
                    k.validate()
        if self.resource_info:
            for k in self.resource_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chart'] = []
        if self.chart is not None:
            for k in self.chart:
                result['Chart'].append(k.to_map() if k else None)
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        result['ResourceInfo'] = []
        if self.resource_info is not None:
            for k in self.resource_info:
                result['ResourceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chart = []
        if m.get('Chart') is not None:
            for k in m.get('Chart'):
                temp_model = DescribeEventDetailResponseBodyEventDetailChart()
                self.chart.append(temp_model.from_map(k))
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeEventDetailResponseBodyEventDetailContent()
                self.content.append(temp_model.from_map(k))
        self.resource_info = []
        if m.get('ResourceInfo') is not None:
            for k in m.get('ResourceInfo'):
                temp_model = DescribeEventDetailResponseBodyEventDetailResourceInfo()
                self.resource_info.append(temp_model.from_map(k))
        return self


class DescribeEventDetailResponseBodyEventHandleInfoList(TeaModel):
    def __init__(self, current_value=None, disable_time=None, enable_time=None, handler_name=None,
                 handler_type=None, handler_value=None, id=None, status=None):
        # The account that is used to handle the anomalous event.
        self.current_value = current_value  # type: str
        # The point in time when the account was locked. The value is a UNIX timestamp. Unit: milliseconds.
        self.disable_time = disable_time  # type: long
        # The point in time when the account was unlocked. The value is a UNIX timestamp. Unit: milliseconds.
        self.enable_time = enable_time  # type: long
        # The handling method.
        self.handler_name = handler_name  # type: str
        # The type of the handling method.
        self.handler_type = handler_type  # type: str
        # The duration for which the handling operation takes effect. If you leave this parameter empty, the handling operation is permanently valid. Unit: minutes.
        self.handler_value = handler_value  # type: int
        # The ID of the handling record.
        self.id = id  # type: long
        # The status of the account that triggered the anomalous event. Valid values:
        # 
        # *   **0**: locked
        # *   **1**: unlocked
        # *   **-1**: failed to unlock the account
        # *   **-2**: failed to enable the account
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEventHandleInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name
        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type
        if self.handler_value is not None:
            result['HandlerValue'] = self.handler_value
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')
        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')
        if m.get('HandlerValue') is not None:
            self.handler_value = m.get('HandlerValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDetailResponseBodyEvent(TeaModel):
    def __init__(self, alert_time=None, backed=None, data_instance=None, deal_display_name=None,
                 deal_login_name=None, deal_reason=None, deal_time=None, deal_user_id=None, detail=None, display_name=None,
                 event_time=None, handle_info_list=None, id=None, log_detail=None, login_name=None, new_alarm=None,
                 product_code=None, status=None, status_name=None, sub_type_code=None, sub_type_name=None, type_code=None,
                 type_name=None, user_id=None):
        # The time when the alert for the anomalous event was generated. The value is a UNIX timestamp. Unit: milliseconds.
        self.alert_time = alert_time  # type: long
        # Indicates whether the handling result of the anomalous event is used to enhance the detection of anomalous events. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # > If you enhance the detection of anomalous events, the detection accuracy and the rate of triggering alerts for anomalous events are improved.
        self.backed = backed  # type: bool
        # The instance name of the service in which the anomalous event was detected.
        self.data_instance = data_instance  # type: str
        # The display name of the account that is used to handle the anomalous event.
        self.deal_display_name = deal_display_name  # type: str
        # The username of the account that is used to handle the anomalous event.
        self.deal_login_name = deal_login_name  # type: str
        # The reason why the anomalous event is handled.
        self.deal_reason = deal_reason  # type: str
        # The time when the anomalous event was handled. The value is a UNIX timestamp. Unit: milliseconds.
        self.deal_time = deal_time  # type: long
        # The ID of the account that is used to handle the anomalous event.
        self.deal_user_id = deal_user_id  # type: long
        # The content in the details of the anomalous event.
        self.detail = detail  # type: DescribeEventDetailResponseBodyEventDetail
        # The display name of the account that triggered the anomalous event.
        self.display_name = display_name  # type: str
        # The time when the anomalous event occurred. The value is a UNIX timestamp. Unit: milliseconds.
        self.event_time = event_time  # type: long
        # An array that consists of the handling records of the anomalous event.
        self.handle_info_list = handle_info_list  # type: list[DescribeEventDetailResponseBodyEventHandleInfoList]
        # The unique ID of the anomalous event.
        self.id = id  # type: long
        # The details of the alert logs.
        self.log_detail = log_detail  # type: str
        # The username of the account that triggered the anomalous event.
        self.login_name = login_name  # type: str
        self.new_alarm = new_alarm  # type: bool
        # The name of the service in which the anomalous event was detected. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The handling status for the anomalous event. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: confirmed
        # *   **2**: marked as false positive
        self.status = status  # type: int
        # The name of the handling status for the anomalous event.
        self.status_name = status_name  # type: str
        # The code of the anomalous event subtype.
        self.sub_type_code = sub_type_code  # type: str
        # The name of the anomalous event subtype.
        self.sub_type_name = sub_type_name  # type: str
        # The code of the anomalous event type.
        self.type_code = type_code  # type: str
        # The name of the anomalous event type. Valid values:
        # 
        # *   **01**: anomalous permission usage
        # *   **02**: anomalous data flow
        # *   **03**: anomalous data operation
        self.type_name = type_name  # type: str
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id  # type: long

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.handle_info_list:
            for k in self.handle_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventDetailResponseBodyEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.data_instance is not None:
            result['DataInstance'] = self.data_instance
        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name
        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name
        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        result['HandleInfoList'] = []
        if self.handle_info_list is not None:
            for k in self.handle_info_list:
                result['HandleInfoList'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.log_detail is not None:
            result['LogDetail'] = self.log_detail
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.new_alarm is not None:
            result['NewAlarm'] = self.new_alarm
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DataInstance') is not None:
            self.data_instance = m.get('DataInstance')
        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')
        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')
        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('Detail') is not None:
            temp_model = DescribeEventDetailResponseBodyEventDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        self.handle_info_list = []
        if m.get('HandleInfoList') is not None:
            for k in m.get('HandleInfoList'):
                temp_model = DescribeEventDetailResponseBodyEventHandleInfoList()
                self.handle_info_list.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogDetail') is not None:
            self.log_detail = m.get('LogDetail')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('NewAlarm') is not None:
            self.new_alarm = m.get('NewAlarm')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEventDetailResponseBody(TeaModel):
    def __init__(self, event=None, request_id=None):
        # The details of the anomalous event.
        self.event = event  # type: DescribeEventDetailResponseBodyEvent
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.event:
            self.event.validate()

    def to_map(self):
        _map = super(DescribeEventDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['Event'] = self.event.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Event') is not None:
            temp_model = DescribeEventDetailResponseBodyEvent()
            self.event = temp_model.from_map(m['Event'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEventDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventTypesRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, parent_type_id=None, resource_id=None, status=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The type of anomalous event for which you want to query the anomalous events of subtypes. Valid values:
        # 
        # *   **01**: anomalous permission usage
        # *   **02**: anomalous data flow
        # *   **03**: anomalous data operation
        self.parent_type_id = parent_type_id  # type: long
        # The type of the resource. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.resource_id = resource_id  # type: int
        # The status of the anomalous event. Valid values:
        # 
        # *   **1**: enabled
        # *   **2**: disabled
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.parent_type_id is not None:
            result['ParentTypeId'] = self.parent_type_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ParentTypeId') is not None:
            self.parent_type_id = m.get('ParentTypeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventTypesResponseBodyEventTypeListSubTypeList(TeaModel):
    def __init__(self, adapted_product=None, code=None, config_code=None, config_content_type=None,
                 config_description=None, config_value=None, description=None, event_hit_count=None, id=None, name=None, status=None):
        # The service to which the anomalous event detection rule applies. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.adapted_product = adapted_product  # type: str
        # The code of the anomalous event subtype.
        self.code = code  # type: str
        # The code of the configuration.
        self.config_code = config_code  # type: str
        # The content format of anomalous event detection rule. Valid values:
        # 
        # *   **0**: numeric values such as thresholds
        # *   **1**: text such as IP addresses
        self.config_content_type = config_content_type  # type: int
        # The description of the configuration.
        self.config_description = config_description  # type: str
        # The value of the configuration.
        self.config_value = config_value  # type: str
        # The description of the anomalous event subtype.
        self.description = description  # type: str
        # The number of times that the anomalous event hits the anomalous event detection rule.
        self.event_hit_count = event_hit_count  # type: int
        # The ID of the anomalous event subtype.
        self.id = id  # type: long
        # The name of the anomalous event subtype.
        self.name = name  # type: str
        # Indicates whether detection is enabled for the anomalous event subtype. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventTypesResponseBodyEventTypeListSubTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapted_product is not None:
            result['AdaptedProduct'] = self.adapted_product
        if self.code is not None:
            result['Code'] = self.code
        if self.config_code is not None:
            result['ConfigCode'] = self.config_code
        if self.config_content_type is not None:
            result['ConfigContentType'] = self.config_content_type
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.event_hit_count is not None:
            result['EventHitCount'] = self.event_hit_count
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptedProduct') is not None:
            self.adapted_product = m.get('AdaptedProduct')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigCode') is not None:
            self.config_code = m.get('ConfigCode')
        if m.get('ConfigContentType') is not None:
            self.config_content_type = m.get('ConfigContentType')
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventHitCount') is not None:
            self.event_hit_count = m.get('EventHitCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventTypesResponseBodyEventTypeList(TeaModel):
    def __init__(self, code=None, description=None, id=None, name=None, sub_type_list=None):
        # The code of the anomalous event type.
        self.code = code  # type: str
        # The description of the anomalous event type.
        self.description = description  # type: str
        # The ID of the anomalous event type.
        self.id = id  # type: long
        # The name of the anomalous event type.
        self.name = name  # type: str
        # An array that consists of anomalous event subtypes.
        self.sub_type_list = sub_type_list  # type: list[DescribeEventTypesResponseBodyEventTypeListSubTypeList]

    def validate(self):
        if self.sub_type_list:
            for k in self.sub_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventTypesResponseBodyEventTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        result['SubTypeList'] = []
        if self.sub_type_list is not None:
            for k in self.sub_type_list:
                result['SubTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sub_type_list = []
        if m.get('SubTypeList') is not None:
            for k in m.get('SubTypeList'):
                temp_model = DescribeEventTypesResponseBodyEventTypeListSubTypeList()
                self.sub_type_list.append(temp_model.from_map(k))
        return self


class DescribeEventTypesResponseBody(TeaModel):
    def __init__(self, event_type_list=None, request_id=None):
        # An array that consists of the types of anomalous events.
        # 
        # > If you leave the ParentTypeId parameter empty, anomalous event types are returned. If you set the ParentTypeId parameter, anomalous event subtypes under the specified anomalous event type are returned.
        self.event_type_list = event_type_list  # type: list[DescribeEventTypesResponseBodyEventTypeList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.event_type_list:
            for k in self.event_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventTypeList'] = []
        if self.event_type_list is not None:
            for k in self.event_type_list:
                result['EventTypeList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_type_list = []
        if m.get('EventTypeList') is not None:
            for k in m.get('EventTypeList'):
                temp_model = DescribeEventTypesResponseBodyEventTypeList()
                self.event_type_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEventTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventTypesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(self, current_page=None, deal_user_id=None, end_time=None, id=None, instance_name=None, lang=None,
                 page_size=None, product_code=None, start_time=None, status=None, sub_type_code=None,
                 target_product_code=None, type_code=None, user_id=None, user_name=None, warn_level=None):
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The ID of the account that handles the anomalous event.
        self.deal_user_id = deal_user_id  # type: str
        # The end of the time range during which the anomalous events are detected. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: str
        # The unique ID of the anomalous event.
        self.id = id  # type: long
        # The name of the data asset.
        self.instance_name = instance_name  # type: str
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the service to which the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The beginning of the time range during which the anomalous events are detected. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: str
        # The handling status of the anomalous event. Valid values:
        # 
        # *   0: unhandled
        # *   1: confirmed
        # *   2: marked as false positive
        self.status = status  # type: str
        # The name of the anomalous event subtype.
        # 
        # > You can call the **DescribeEventTypes** operation to query the name of the anomalous event subtype.
        self.sub_type_code = sub_type_code  # type: str
        # The name of the destination service in an anomalous data flow. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**\
        self.target_product_code = target_product_code  # type: str
        # The name of the anomalous event type. Valid values:
        # 
        # *   01: anomalous permission usage
        # *   02: anomalous data flow
        # *   03: anomalous data operation
        self.type_code = type_code  # type: str
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id  # type: long
        # The username of the RAM user.
        self.user_name = user_name  # type: str
        # The risk level of the alert that is triggered. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeEventsResponseBodyItems(TeaModel):
    def __init__(self, alert_time=None, backed=None, deal_display_name=None, deal_login_name=None, deal_time=None,
                 deal_user_id=None, display_name=None, event_time=None, id=None, login_name=None, product_code=None, status=None,
                 status_name=None, sub_type_code=None, sub_type_name=None, target_product_code=None, type_code=None,
                 type_name=None, user_id=None, warn_level=None):
        # The time when an alert was triggered for the anomalous event. The value is a UNIX timestamp. Unit: milliseconds.
        self.alert_time = alert_time  # type: long
        # Indicates whether the detection of anomalous events is enhanced. If the detection of anomalous events is enhanced, the detection accuracy and the rate of triggering alerts for anomalous events are improved. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.backed = backed  # type: bool
        # The display name of the account that is used to handle the anomalous event.
        self.deal_display_name = deal_display_name  # type: str
        # The username of the account that is used to handle the anomalous event.
        self.deal_login_name = deal_login_name  # type: str
        # The time when the anomalous event was handled. The value is a UNIX timestamp. Unit: milliseconds.
        self.deal_time = deal_time  # type: long
        # The ID of the account that is used to handle the anomalous event.
        self.deal_user_id = deal_user_id  # type: long
        # The display name of the account that triggered the anomalous event.
        self.display_name = display_name  # type: str
        # The time when the anomalous event occurred. The value is a UNIX timestamp. Unit: milliseconds.
        self.event_time = event_time  # type: long
        # The ID of the anomalous event.
        self.id = id  # type: long
        # The username of the account that triggered the anomalous event.
        self.login_name = login_name  # type: str
        # The name of the service in which the anomalous event was detected.
        self.product_code = product_code  # type: str
        # The handling status for the anomalous event. Valid values:
        # 
        # *   0: unhandled
        # *   1: confirmed
        # *   2: marked as false positive
        self.status = status  # type: int
        # The name of the handling status for the anomalous event.
        self.status_name = status_name  # type: str
        # The code of the anomalous event subtype.
        self.sub_type_code = sub_type_code  # type: str
        # The name of the anomalous event subtype.
        self.sub_type_name = sub_type_name  # type: str
        # The name of the destination service in an anomalous data flow.
        self.target_product_code = target_product_code  # type: str
        # The code of the anomalous event type.
        self.type_code = type_code  # type: str
        # The name of the anomalous event type.
        self.type_name = type_name  # type: str
        # The ID of the account that triggered the anomalous event.
        self.user_id = user_id  # type: long
        # The severity of the anomalous event.
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.deal_display_name is not None:
            result['DealDisplayName'] = self.deal_display_name
        if self.deal_login_name is not None:
            result['DealLoginName'] = self.deal_login_name
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.id is not None:
            result['Id'] = self.id
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.sub_type_code is not None:
            result['SubTypeCode'] = self.sub_type_code
        if self.sub_type_name is not None:
            result['SubTypeName'] = self.sub_type_name
        if self.target_product_code is not None:
            result['TargetProductCode'] = self.target_product_code
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DealDisplayName') is not None:
            self.deal_display_name = m.get('DealDisplayName')
        if m.get('DealLoginName') is not None:
            self.deal_login_name = m.get('DealLoginName')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('SubTypeCode') is not None:
            self.sub_type_code = m.get('SubTypeCode')
        if m.get('SubTypeName') is not None:
            self.sub_type_name = m.get('SubTypeName')
        if m.get('TargetProductCode') is not None:
            self.target_product_code = m.get('TargetProductCode')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the anomalous events.
        self.items = items  # type: list[DescribeEventsResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSourcesRequest(TeaModel):
    def __init__(self, audit_status=None, auth_status=None, current_page=None, engine_type=None, feature_type=None,
                 instance_id=None, lang=None, page_size=None, product_code=None, product_id=None, search_key=None,
                 search_type=None, service_region_id=None):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status  # type: int
        # Specifies whether DSC is authorized to access the data asset.
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auth_status = auth_status  # type: int
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page  # type: int
        # The type of the database engine. Valid values: **MySQL, MariaDB, Oracle, PostgreSQL, and SQLServer**.
        self.engine_type = engine_type  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The name of the service to which the data asset to query belongs. Valid values: **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The ID of the service to which the data asset to query belongs. Valid values: **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The content based on which a fuzzy search is performed.
        self.search_key = search_key  # type: str
        # The data asset type based on which a fuzzy search is performed.
        # 
        # *   **InstanceId**: the ID of the instance.
        # *   **InstanceName**: the name of the instance.
        # *   **DatabaseName**: the name of the database.
        self.search_type = search_type  # type: str
        # The region in which the data asset resides. For more information, see [Supported regions](~~214257~~).
        self.service_region_id = service_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeInstanceSourcesResponseBodyItems(TeaModel):
    def __init__(self, audit_status=None, auto_scan=None, can_modify_user_name=None, check_status=None,
                 datamask_status=None, db_name=None, enable=None, engine_type=None, error_message=None, gmt_create=None, id=None,
                 instance_description=None, instance_id=None, instance_size=None, last_modify_time=None, last_modify_user_id=None,
                 log_store_day=None, password_status=None, product_id=None, region_id=None, region_name=None, sampling_size=None,
                 tenant_id=None, tenant_name=None, user_name=None):
        # Indicates whether the security audit feature is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status  # type: int
        # Indicates whether the automatic scan feature is enabled to detect sensitive data. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auto_scan = auto_scan  # type: int
        # Indicates whether the username and password can be changed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.can_modify_user_name = can_modify_user_name  # type: bool
        # The data detection status. Valid values:
        # 
        # *   **0**: The data detection is ready.
        # *   **1**: The data detection is running.
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status  # type: int
        # Indicates whether DSC has the data de-identification permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.datamask_status = datamask_status  # type: int
        # The name of the database to which the data asset belongs.
        self.db_name = db_name  # type: str
        # Indicates whether sensitive data detection is enabled for the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable  # type: int
        # The type of the database engine. Valid values: **MySQL, MariaDB, Oracle, PostgreSQL, and SQLServer**.
        self.engine_type = engine_type  # type: str
        # The reason for the failure.
        self.error_message = error_message  # type: str
        # The time when the data asset was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The unique ID of the data asset.
        self.id = id  # type: long
        # The description of the instance.
        self.instance_description = instance_description  # type: str
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        # The storage space size of the instance. This parameter is valid only if the value of the ProductId parameter is 2. Unit: bytes.
        self.instance_size = instance_size  # type: long
        # The time when the data asset was last modified. Unit: milliseconds.
        self.last_modify_time = last_modify_time  # type: long
        # The ID of the account that is last used to modify the data asset.
        self.last_modify_user_id = last_modify_user_id  # type: str
        # The retention period of raw logs. Unit: days.
        self.log_store_day = log_store_day  # type: int
        # Indicates whether the password is used. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.password_status = password_status  # type: int
        # The ID of the service to which the data asset belongs. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The ID of the region where the instance resides.
        self.region_id = region_id  # type: str
        # The name of the region.
        self.region_name = region_name  # type: str
        # The number of sensitive data samples. Valid values: **0**, **5**, and **10**. Unit: data entries.
        self.sampling_size = sampling_size  # type: int
        # The ID of the tenant.
        self.tenant_id = tenant_id  # type: str
        # The name of the tenant.
        self.tenant_name = tenant_name  # type: str
        # The username of the account.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSourcesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.can_modify_user_name is not None:
            result['CanModifyUserName'] = self.can_modify_user_name
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.last_modify_user_id is not None:
            result['LastModifyUserId'] = self.last_modify_user_id
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.password_status is not None:
            result['PasswordStatus'] = self.password_status
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('CanModifyUserName') is not None:
            self.can_modify_user_name = m.get('CanModifyUserName')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LastModifyUserId') is not None:
            self.last_modify_user_id = m.get('LastModifyUserId')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('PasswordStatus') is not None:
            self.password_status = m.get('PasswordStatus')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeInstanceSourcesResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the queried data assets.
        self.items = items  # type: list[DescribeInstanceSourcesResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeInstanceSourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceSourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, current_page=None, feature_type=None, lang=None, name=None, page_size=None, product_code=None,
                 product_id=None, risk_level_id=None, rule_id=None, service_region_id=None):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page  # type: int
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The keyword that is used to search for data assets. DSC searches for data assets based on the keyword that you specify in fuzzy match mode. For example, if you specify data, all data assets whose names contain data are queried.
        self.name = name  # type: str
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The name of the service to which the data asset belongs, such as MaxCompute, OSS, and ApsaraDB RDS. For more information about the types of data assets from which DSC can scan for sensitive data, see [Supported data assets](~~212906~~).
        self.product_code = product_code  # type: str
        # The ID of the service to which the data asset belongs. You can call the [DescribeDataAssets](~~DescribeDataAssets~~) operation to query the ID of the service.
        self.product_id = product_id  # type: long
        # The sensitivity level ID of the data asset. A higher sensitivity level indicates that the identified data is more sensitive. Valid values:
        # 
        # *   **1**: No sensitive data is identified.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **4**: sensitive data at level 3
        # *   **5**: sensitive data at level 4.
        # *   **6**: sensitive data at level 5.
        # *   **7**: sensitive data at level 6.
        # *   **8**: sensitive data at level 7.
        # *   **9**: sensitive data at level 8.
        # *   **10**: sensitive data at level 9.
        # *   **11**: sensitive data at level 10.
        self.risk_level_id = risk_level_id  # type: long
        # The ID of the sensitive data detection rule that the data asset hits. You can call the [DescribeRules](~~DescribeRules~~) operation and obtain the ID of the sensitive data detection rule from the **Id** response parameter.
        self.rule_id = rule_id  # type: long
        # The region where the data asset resides. For more information, see [Supported regions](~~214257~~).
        self.service_region_id = service_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeInstancesResponseBodyItemsModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        # The ID of the tag. Valid values:
        # 
        # *   **101**: personal sensitive information
        # *   **102**: personal information
        # *   **107**: general information
        self.id = id  # type: long
        # The name of the tag. Valid values:
        # 
        # *   Personal sensitive information
        # *   Personal information
        # *   General information
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyItemsModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeInstancesResponseBodyItems(TeaModel):
    def __init__(self, creation_time=None, depart_name=None, id=None, instance_description=None, labelsec=None,
                 last_finish_time=None, model_tags=None, name=None, odps_risk_level_name=None, owner=None, product_code=None,
                 product_id=None, protection=None, risk_level_id=None, risk_level_name=None, rule_name=None, sensitive=None,
                 sensitive_count=None, tenant_name=None, total_count=None):
        # The time when the data asset was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.creation_time = creation_time  # type: long
        # The name of the department to which the data asset belongs.
        self.depart_name = depart_name  # type: str
        # The unique ID of the data asset in DSC.
        self.id = id  # type: long
        # The description of the data asset.
        self.instance_description = instance_description  # type: str
        # The security status of the data asset. Valid values:
        # 
        # *   **true**: The data asset is secure.
        # *   **false**: The data asset is insecure.
        self.labelsec = labelsec  # type: bool
        # The time when the data asset was last scanned. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_finish_time = last_finish_time  # type: long
        # A list of tags.
        self.model_tags = model_tags  # type: list[DescribeInstancesResponseBodyItemsModelTags]
        # The name of the data asset.
        self.name = name  # type: str
        # This parameter is deprecated.
        self.odps_risk_level_name = odps_risk_level_name  # type: str
        # The Alibaba Cloud account to which the data asset belongs.
        self.owner = owner  # type: str
        # The name of the service to which the data asset belongs, such as MaxCompute, OSS, and ApsaraDB RDS. For more information about the types of data assets that DSC can scan to detect sensitive data, see [Supported data assets](~~212906~~).
        self.product_code = product_code  # type: str
        # The ID of the service to which the data asset belongs.
        self.product_id = product_id  # type: str
        # The protection status of the data asset. Valid values:
        # 
        # *   **true**: The data asset is being protected.
        # *   **false**: The data asset is not protected.
        self.protection = protection  # type: bool
        # The ID of the sensitivity level for the data asset. A higher sensitivity level ID indicates that the identified data is more sensitive.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **4**: sensitive data at level 3.
        # *   **5**: sensitive data at level 4.
        # *   **6**: sensitive data at level 5.
        # *   **7**: sensitive data at level 6.
        # *   **8**: sensitive data at level 7.
        # *   **9**: sensitive data at level 8.
        # *   **10**: sensitive data at level 9.
        # *   **11**: sensitive data at level 10.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the data asset.
        self.risk_level_name = risk_level_name  # type: str
        # The name of the sensitive data detection rule that the data asset hits.
        self.rule_name = rule_name  # type: str
        # Indicates whether the data asset contains sensitive data. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.sensitive = sensitive  # type: bool
        # The number of sensitive data objects in the data asset. For example, if the data asset is an ApsaraDB RDS instance, the value indicates the number of sensitive tables in all databases of the instance.
        self.sensitive_count = sensitive_count  # type: int
        # The name of the tenant.
        self.tenant_name = tenant_name  # type: str
        # The total number of data objects in the data asset. For example, if the data asset is an ApsaraDB RDS instance, the value indicates the total number of tables in all databases of the instance.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.depart_name is not None:
            result['DepartName'] = self.depart_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.protection is not None:
            result['Protection'] = self.protection
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DepartName') is not None:
            self.depart_name = m.get('DepartName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeInstancesResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the data assets.
        self.items = items  # type: list[DescribeInstancesResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of data assets.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssObjectDetailRequest(TeaModel):
    def __init__(self, id=None, lang=None):
        # The ID of the OSS object.
        # 
        # >  You can call the [DescribeOssObjects](~~410152~~) operation to obtain the ID of the OSS object.
        self.id = id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        # The tag ID.
        # 
        # *   **101**: sensitive personal information
        # *   **102**: personal information
        # *   **103**: important information
        self.id = id  # type: long
        # The tag name.
        # 
        # *   Sensitive personal information
        # *   Personal information
        # *   Important information
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList(TeaModel):
    def __init__(self, category_name=None, count=None, model_tags=None, risk_level_id=None, risk_level_name=None,
                 rule_name=None):
        # The type of the OSS object.
        self.category_name = category_name  # type: str
        # The number of times that the OSS object hits the sensitive data detection rule.
        self.count = count  # type: long
        # A list of tags for data that hits the recognition model.
        self.model_tags = model_tags  # type: list[DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags]
        # The ID of the sensitivity level of the OSS object.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: indicates the low sensitivity level.
        # *   **3**: indicates the medium sensitivity level.
        # *   **4**: indicates the high sensitivity level.
        # *   **5**: indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the OSS object.
        self.risk_level_name = risk_level_name  # type: str
        # The name of the sensitive data detection rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.count is not None:
            result['Count'] = self.count
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeOssObjectDetailResponseBodyOssObjectDetail(TeaModel):
    def __init__(self, bucket_name=None, category_name=None, name=None, region_id=None, risk_level_name=None,
                 rule_list=None):
        # The name of the OSS bucket to which the OSS object belongs.
        self.bucket_name = bucket_name  # type: str
        # The type of the OSS object.
        self.category_name = category_name  # type: str
        # The name of the OSS object.
        self.name = name  # type: str
        # The region ID of the OSS object.
        self.region_id = region_id  # type: str
        # The name of the sensitivity level for the OSS object.
        self.risk_level_name = risk_level_name  # type: str
        # A list of the sensitive data detection rules that the OSS object hits.
        self.rule_list = rule_list  # type: list[DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailResponseBodyOssObjectDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeOssObjectDetailResponseBody(TeaModel):
    def __init__(self, oss_object_detail=None, request_id=None):
        # The details of the OSS object.
        self.oss_object_detail = oss_object_detail  # type: DescribeOssObjectDetailResponseBodyOssObjectDetail
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oss_object_detail:
            self.oss_object_detail.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_object_detail is not None:
            result['OssObjectDetail'] = self.oss_object_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssObjectDetail') is not None:
            temp_model = DescribeOssObjectDetailResponseBodyOssObjectDetail()
            self.oss_object_detail = temp_model.from_map(m['OssObjectDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOssObjectDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssObjectDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOssObjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssObjectDetailV2Request(TeaModel):
    def __init__(self, id=None, lang=None):
        self.id = id  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleListModelTags(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleListModelTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleList(TeaModel):
    def __init__(self, category_name=None, count=None, model_tags=None, risk_level_id=None, risk_level_name=None,
                 rule_name=None):
        self.category_name = category_name  # type: str
        self.count = count  # type: long
        self.model_tags = model_tags  # type: list[DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleListModelTags]
        self.risk_level_id = risk_level_id  # type: long
        self.risk_level_name = risk_level_name  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.model_tags:
            for k in self.model_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.count is not None:
            result['Count'] = self.count
        result['ModelTags'] = []
        if self.model_tags is not None:
            for k in self.model_tags:
                result['ModelTags'].append(k.to_map() if k else None)
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k in m.get('ModelTags'):
                temp_model = DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleListModelTags()
                self.model_tags.append(temp_model.from_map(k))
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeOssObjectDetailV2ResponseBodyOssObjectDetail(TeaModel):
    def __init__(self, bucket_name=None, category_name=None, name=None, region_id=None, risk_level_name=None,
                 rule_list=None):
        self.bucket_name = bucket_name  # type: str
        self.category_name = category_name  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.risk_level_name = risk_level_name  # type: str
        self.rule_list = rule_list  # type: list[DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2ResponseBodyOssObjectDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeOssObjectDetailV2ResponseBodyOssObjectDetailRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeOssObjectDetailV2ResponseBody(TeaModel):
    def __init__(self, oss_object_detail=None, request_id=None):
        self.oss_object_detail = oss_object_detail  # type: DescribeOssObjectDetailV2ResponseBodyOssObjectDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oss_object_detail:
            self.oss_object_detail.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_object_detail is not None:
            result['OssObjectDetail'] = self.oss_object_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssObjectDetail') is not None:
            temp_model = DescribeOssObjectDetailV2ResponseBodyOssObjectDetail()
            self.oss_object_detail = temp_model.from_map(m['OssObjectDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOssObjectDetailV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssObjectDetailV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssObjectDetailV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOssObjectDetailV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssObjectsRequest(TeaModel):
    def __init__(self, current_page=None, file_category_code=None, instance_id=None, lang=None,
                 last_scan_time_end=None, last_scan_time_start=None, name=None, page_size=None, risk_level_id=None, rule_id=None,
                 service_region_id=None, template_id=None):
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The code of the file type.
        self.file_category_code = file_category_code  # type: long
        # The ID of the instance to which the OSS object belongs.
        # 
        # > You can call the **DescribeInstances** operation to query the instance ID.
        self.instance_id = instance_id  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The end time of the last scan. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_scan_time_end = last_scan_time_end  # type: long
        # The start time of the last scan. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_scan_time_start = last_scan_time_start  # type: long
        # The search keyword. Fuzzy match is supported.
        self.name = name  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The sensitivity level of the OSS object. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: int
        # The ID of the sensitive data detection rule that the OSS object hits.
        # 
        # > You can call the **DescribeRules** operation to query the ID of the sensitive data detection rule.
        self.rule_id = rule_id  # type: long
        # The region in which the data asset resides.
        self.service_region_id = service_region_id  # type: str
        # The ID of the industry-specific rule template.
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.last_scan_time_end is not None:
            result['LastScanTimeEnd'] = self.last_scan_time_end
        if self.last_scan_time_start is not None:
            result['LastScanTimeStart'] = self.last_scan_time_start
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LastScanTimeEnd') is not None:
            self.last_scan_time_end = m.get('LastScanTimeEnd')
        if m.get('LastScanTimeStart') is not None:
            self.last_scan_time_start = m.get('LastScanTimeStart')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeOssObjectsResponseBodyItemsRuleList(TeaModel):
    def __init__(self, count=None, name=None, risk_level_id=None):
        # The number of times that the rule is hit.
        self.count = count  # type: long
        # The search keyword. Fuzzy match is supported.
        self.name = name  # type: str
        # The ID of the sensitivity level of the OSS object. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssObjectsResponseBodyItemsRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        return self


class DescribeOssObjectsResponseBodyItems(TeaModel):
    def __init__(self, bucket_name=None, category=None, category_name=None, file_category_code=None,
                 file_category_name=None, file_id=None, id=None, instance_id=None, name=None, region_id=None, risk_level_id=None,
                 risk_level_name=None, rule_count=None, rule_list=None, sensitive_count=None, size=None):
        # The name of the bucket.
        self.bucket_name = bucket_name  # type: str
        # The type of the OSS object. Valid values include **900001**, **800015**, or **800005**, which indicates the MP4 file, PDF file, or OSS configuration file, respectively.
        self.category = category  # type: long
        # The name of the file type.
        self.category_name = category_name  # type: str
        # The code of the file type.
        self.file_category_code = file_category_code  # type: long
        # The name of the file type.
        self.file_category_name = file_category_name  # type: str
        # The file ID of the OSS object.
        self.file_id = file_id  # type: str
        # The ID of the OSS object.
        self.id = id  # type: str
        # The ID of the instance to which the OSS object belongs.
        self.instance_id = instance_id  # type: long
        # The name of the OSS object.
        self.name = name  # type: str
        # The region ID of the OSS object.
        self.region_id = region_id  # type: str
        # The ID of the sensitivity level of the OSS object. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the OSS object.
        self.risk_level_name = risk_level_name  # type: str
        # The number of rules that are hit.
        self.rule_count = rule_count  # type: int
        # A list of rules.
        self.rule_list = rule_list  # type: list[DescribeOssObjectsResponseBodyItemsRuleList]
        # The number of fields that are hit.
        self.sensitive_count = sensitive_count  # type: int
        # The size of the file. Unit: bytes.
        self.size = size  # type: long

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.category is not None:
            result['Category'] = self.category
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code
        if self.file_category_name is not None:
            result['FileCategoryName'] = self.file_category_name
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')
        if m.get('FileCategoryName') is not None:
            self.file_category_name = m.get('FileCategoryName')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeOssObjectsResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeOssObjectsResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # A list of OSS objects.
        self.items = items  # type: list[DescribeOssObjectsResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssObjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeOssObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssObjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssObjectsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssObjectsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOssObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackagesRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, lang=None, name=None, page_size=None, product_id=None,
                 risk_level_id=None, rule_id=None):
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The ID of the instance to which the package belongs.
        # 
        # > You can call the **DescribeInstances** operation to query the ID of the instance.
        self.instance_id = instance_id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The search keyword. Fuzzy match is supported.
        self.name = name  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the service to which the package belongs.
        # 
        # > You can call the **DescribeDataAssets** operation to query the ID of the service.
        self.product_id = product_id  # type: long
        # The sensitivity level of the package. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The ID of the sensitive data detection rule that the package hits.
        # 
        # > You can call the **DescribeRules** operation to query the ID of the sensitive data detection rule.
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePackagesResponseBodyItems(TeaModel):
    def __init__(self, creation_time=None, id=None, instance_id=None, name=None, owner=None, risk_level_id=None,
                 risk_level_name=None, sensitive=None, sensitive_count=None, total_count=None):
        # The point in time when the MaxCompute package was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.creation_time = creation_time  # type: long
        # The ID of the package.
        self.id = id  # type: long
        # The ID of the instance to which the package belongs.
        self.instance_id = instance_id  # type: long
        # The name of the package.
        self.name = name  # type: str
        # The account of the user that owns the package.
        self.owner = owner  # type: str
        # The sensitivity level of the package. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the package.
        self.risk_level_name = risk_level_name  # type: str
        # Indicates whether the package contains sensitive data. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.sensitive = sensitive  # type: bool
        # The total volume of sensitive data in the package. For example, the value can be the total number of sensitive tables in the MaxCompute package.
        self.sensitive_count = sensitive_count  # type: int
        # The total volume of data in the package. For example, the value can be the total number of tables in the MaxCompute package.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackagesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePackagesResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the information about the packages.
        self.items = items  # type: list[DescribePackagesResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribePackagesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePackagesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePackagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentInstanceRequest(TeaModel):
    def __init__(self, auth_status=None, check_status=None, cluster_status=None, current_page=None, db_name=None,
                 engine_type=None, instance_id=None, lang=None, member_account=None, page_size=None, resource_type=None,
                 service_region_id=None):
        self.auth_status = auth_status  # type: int
        self.check_status = check_status  # type: int
        self.cluster_status = cluster_status  # type: str
        self.current_page = current_page  # type: int
        self.db_name = db_name  # type: str
        self.engine_type = engine_type  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.member_account = member_account  # type: long
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: long
        self.service_region_id = service_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        return self


class DescribeParentInstanceResponseBodyItems(TeaModel):
    def __init__(self, audit_status=None, auth_status=None, cluster_status=None, connect_node=None, db_num=None,
                 engine_type=None, instance_description=None, instance_id=None, instance_size=None, local_name=None,
                 member_account=None, parent_id=None, resource_type=None, support_connect_nodes=None, tenant_id=None,
                 tenant_name=None, un_connect_db_count=None, un_support_one_click_auth_reason=None):
        self.audit_status = audit_status  # type: int
        self.auth_status = auth_status  # type: int
        self.cluster_status = cluster_status  # type: str
        self.connect_node = connect_node  # type: str
        self.db_num = db_num  # type: str
        self.engine_type = engine_type  # type: str
        self.instance_description = instance_description  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_size = instance_size  # type: long
        self.local_name = local_name  # type: str
        self.member_account = member_account  # type: long
        self.parent_id = parent_id  # type: str
        self.resource_type = resource_type  # type: str
        self.support_connect_nodes = support_connect_nodes  # type: str
        self.tenant_id = tenant_id  # type: str
        self.tenant_name = tenant_name  # type: str
        self.un_connect_db_count = un_connect_db_count  # type: str
        self.un_support_one_click_auth_reason = un_support_one_click_auth_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentInstanceResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.connect_node is not None:
            result['ConnectNode'] = self.connect_node
        if self.db_num is not None:
            result['DbNum'] = self.db_num
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.member_account is not None:
            result['MemberAccount'] = self.member_account
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.support_connect_nodes is not None:
            result['SupportConnectNodes'] = self.support_connect_nodes
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.un_connect_db_count is not None:
            result['UnConnectDbCount'] = self.un_connect_db_count
        if self.un_support_one_click_auth_reason is not None:
            result['UnSupportOneClickAuthReason'] = self.un_support_one_click_auth_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ConnectNode') is not None:
            self.connect_node = m.get('ConnectNode')
        if m.get('DbNum') is not None:
            self.db_num = m.get('DbNum')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SupportConnectNodes') is not None:
            self.support_connect_nodes = m.get('SupportConnectNodes')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UnConnectDbCount') is not None:
            self.un_connect_db_count = m.get('UnConnectDbCount')
        if m.get('UnSupportOneClickAuthReason') is not None:
            self.un_support_one_click_auth_reason = m.get('UnSupportOneClickAuthReason')
        return self


class DescribeParentInstanceResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeParentInstanceResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParentInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeParentInstanceResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParentInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParentInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParentInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeParentInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskLevelsRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, template_id=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   zh_cn: Chinese (default)
        # *   en_us: English
        self.lang = lang  # type: str
        # The ID of the industry-specific rule template.
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskLevelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeRiskLevelsResponseBodyRiskLevelList(TeaModel):
    def __init__(self, description=None, id=None, name=None, reference_num=None):
        # The description of the sensitivity level. You can enter a custom description.
        # 
        # The following list describes the sensitivity level names and the corresponding default description:
        # 
        # *   **NA**: which indicates that no sensitive data is detected.
        # *   **S1**: which indicates the sensitive data at sensitivity level 1.
        # *   **S2**: which indicates the sensitive data at sensitivity level 2.
        # *   **S3**: which indicates the sensitive data at sensitivity level 3.
        # *   **S4**: which indicates the sensitive data at sensitivity level 4.
        # *   **S5**: which indicates the sensitive data at sensitivity level 5.
        # *   **S6**: which indicates the sensitive data at sensitivity level 6.
        # *   **S7**: which indicates the sensitive data at sensitivity level 7.
        # *   **S8**: which indicates the sensitive data at sensitivity level 8.
        # *   **S9**: which indicates the sensitive data at sensitivity level 9.
        # *   **S10**: which indicates the sensitive data at sensitivity level 10.
        self.description = description  # type: str
        # The unique ID of the sensitivity level. Valid values: 1 to 11. Each sensitivity level ID maps a sensitivity level. For example, the sensitivity level ID of 2 corresponds to the sensitivity level S1.
        # 
        # For more information, see the description of the Name parameter.
        self.id = id  # type: long
        # The name of the sensitivity level. The highest sensitivity level varies based on rule templates. The highest sensitivity level is S10. The highest sensitivity level of the **Built-in data security classification templates for Alibaba and Ant Group** is S4, and that of the **built-in classification templates for financial data** and **built-in classification templates for assets** is S5. For more information about the built-in classification templates for financial data, see Guidelines for Security Classification of Financial Data and Security Data - JRT 0197-2020. For a copied rule template, the highest sensitivity level is S10. The following list describes the sensitivity level names and the corresponding IDs:
        # 
        # *   **NA**: 1
        # *   **S1**: 2
        # *   **S2**: 3
        # *   **S3**: 4
        # *   **S4**: 5
        # *   **S5**: 6
        # *   **S6**: 7
        # *   **S7**: 8
        # *   **S8**: 9
        # *   **S9**: 10
        # *   **S10**: 11
        self.name = name  # type: str
        # The number of times that each sensitivity level is referenced in the rule template. Default value: 0.
        self.reference_num = reference_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskLevelsResponseBodyRiskLevelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reference_num is not None:
            result['ReferenceNum'] = self.reference_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReferenceNum') is not None:
            self.reference_num = m.get('ReferenceNum')
        return self


class DescribeRiskLevelsResponseBody(TeaModel):
    def __init__(self, request_id=None, risk_level_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of sensitivity levels.
        self.risk_level_list = risk_level_list  # type: list[DescribeRiskLevelsResponseBodyRiskLevelList]

    def validate(self):
        if self.risk_level_list:
            for k in self.risk_level_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRiskLevelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskLevelList'] = []
        if self.risk_level_list is not None:
            for k in self.risk_level_list:
                result['RiskLevelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_level_list = []
        if m.get('RiskLevelList') is not None:
            for k in m.get('RiskLevelList'):
                temp_model = DescribeRiskLevelsResponseBodyRiskLevelList()
                self.risk_level_list.append(temp_model.from_map(k))
        return self


class DescribeRiskLevelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRiskLevelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRiskLevelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRiskLevelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesRequest(TeaModel):
    def __init__(self, category=None, content_category=None, current_page=None, custom_type=None, feature_type=None,
                 group_id=None, keyword_compatible=None, lang=None, match_type=None, name=None, page_size=None,
                 product_code=None, product_id=None, risk_level_id=None, rule_type=None, status=None, support_form=None,
                 warn_level=None):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category  # type: int
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category  # type: int
        # The page number of the page to return.
        self.current_page = current_page  # type: int
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: built-in rule
        # *   **1**: custom rule
        self.custom_type = custom_type  # type: int
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The parent group type of the rule.
        self.group_id = group_id  # type: str
        # Specifies whether to allow earlier versions of request parameters to support keywords that are supported in later versions of request parameters. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # > To specify keywords as the content type of the sensitive data detection rule, you can set the Category parameter to 0 for earlier versions of request parameters and set the Category parameter to 5 for later versions of request parameters. You can specify the KeywordCompatible parameter based on your business requirements.
        self.keyword_compatible = keyword_compatible  # type: bool
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The match type. Valid values:
        # 
        # *   1: rule-based match
        # *   2: dictionary-based match
        self.match_type = match_type  # type: int
        # The name of the sensitive data detection rule. Fuzzy match is supported.
        self.name = name  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: int
        # The ID of the service to which the sensitive data detection rule is applied. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: sensitive data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        # *   **99**: custom rule
        self.rule_type = rule_type  # type: int
        # The status of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.status = status  # type: int
        # The type of the data asset. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data asset
        # *   **2**: unstructured data asset
        # 
        # > If you set the parameter to 1 or 2, rules that support all data assets and rules that support the queried data asset type are returned.
        self.support_form = support_form  # type: int
        # The severity level of the alert. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keyword_compatible is not None:
            result['KeywordCompatible'] = self.keyword_compatible
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.support_form is not None:
            result['SupportForm'] = self.support_form
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('KeywordCompatible') is not None:
            self.keyword_compatible = m.get('KeywordCompatible')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeRulesResponseBodyItems(TeaModel):
    def __init__(self, category=None, category_name=None, content=None, content_category=None, custom_type=None,
                 description=None, display_name=None, gmt_create=None, gmt_modified=None, group_id=None, hit_total_count=None,
                 id=None, login_name=None, major_key=None, match_type=None, name=None, product_code=None,
                 product_id=None, risk_level_id=None, risk_level_name=None, stat_express=None, status=None, support_form=None,
                 target=None, user_id=None, warn_level=None):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: keyword
        # *   **2**: regular expression
        self.category = category  # type: int
        # The name of the content type of the sensitive data detection rule.
        self.category_name = category_name  # type: str
        # The content in the sensitive data detection rule.
        # 
        # >  A built-in detection rule whose CustomType is 0 does not return the content of the rule.
        self.content = content  # type: str
        # The type of the content in the sensitive data detection rule. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates attempts to exploit SQL injections. The value 2 indicates bypass by using SQL injections. The value 3 indicates abuse of stored procedures. The value 4 indicates buffer overflow. The value 5 indicates SQL injections based on errors.
        self.content_category = content_category  # type: str
        # The type of the sensitive data detection rule.
        # 
        # *   0: built-in rule
        # *   1: custom rule
        self.custom_type = custom_type  # type: int
        # The description of the sensitive data detection rule.
        self.description = description  # type: str
        # The display name of the account that is used to create the sensitive data detection rule.
        self.display_name = display_name  # type: str
        # The time when the sensitive data detection rule is created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The time when the sensitive data detection rule is modified. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified  # type: long
        # The parent group type of the rule.
        self.group_id = group_id  # type: str
        # The number of times that the sensitive data detection rule is hit.
        self.hit_total_count = hit_total_count  # type: int
        # The ID of the sensitive data detection rule.
        self.id = id  # type: long
        # The username of the account that is used to create the sensitive data detection rule.
        self.login_name = login_name  # type: str
        # The key of the primary dimension.
        self.major_key = major_key  # type: str
        # The match type. Valid values:
        # 
        # *   **1**: rule-based match
        # *   **2**: dictionary-based match
        self.match_type = match_type  # type: int
        # The name of the sensitive data detection rule.
        self.name = name  # type: str
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The ID of the service to which the sensitive data detection rule is applied. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates OSS. The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The sensitivity level of data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name  # type: str
        # The statistical expression.
        self.stat_express = stat_express  # type: str
        # The status of the sensitive data detection rule. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.status = status  # type: int
        # The data asset type that is supported by the sensitive data detection rule. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data assets
        # *   **2**: unstructured data assets
        self.support_form = support_form  # type: int
        # The name of the service to which the data asset belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.target = target  # type: str
        # The ID of the account that is used to create the sensitive data detection rule.
        self.user_id = user_id  # type: long
        # The severity level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRulesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.content is not None:
            result['Content'] = self.content
        if self.content_category is not None:
            result['ContentCategory'] = self.content_category
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.hit_total_count is not None:
            result['HitTotalCount'] = self.hit_total_count
        if self.id is not None:
            result['Id'] = self.id
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.major_key is not None:
            result['MajorKey'] = self.major_key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        if self.stat_express is not None:
            result['StatExpress'] = self.stat_express
        if self.status is not None:
            result['Status'] = self.status
        if self.support_form is not None:
            result['SupportForm'] = self.support_form
        if self.target is not None:
            result['Target'] = self.target
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCategory') is not None:
            self.content_category = m.get('ContentCategory')
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HitTotalCount') is not None:
            self.hit_total_count = m.get('HitTotalCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('MajorKey') is not None:
            self.major_key = m.get('MajorKey')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        if m.get('StatExpress') is not None:
            self.stat_express = m.get('StatExpress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class DescribeRulesResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of the sensitive data detection rules.
        self.items = items  # type: list[DescribeRulesResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeRulesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablesRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, lang=None, name=None, package_id=None, page_size=None,
                 product_code=None, product_id=None, risk_level_id=None, rule_id=None, service_region_id=None, template_id=None):
        # The page number of the page to return. Default value: 1.
        self.current_page = current_page  # type: int
        # The ID of the data asset to which the table belongs. You can call the [DescribeInstances](~~DescribeInstances~~) operation to obtain the ID of the data asset.
        self.instance_id = instance_id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The search keyword. Fuzzy match is supported. For example, if you specify test, all tables whose names contain test are retrieved.
        self.name = name  # type: str
        # The ID of the package to which the table belongs. You can call the [DescribePackages](~~DescribePackages~~) operation to obtain the ID of the package.
        self.package_id = package_id  # type: long
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size  # type: int
        # The name of the service to which the table belongs, such as MaxCompute, OSS, and ApsaraDB RDS. For more information about the types of data assets from which Data Security Center (DSC) can scan for sensitive data, see [Supported data assets](~~212906~~).
        self.product_code = product_code  # type: str
        # The ID of the service to which the table belongs. You can call the [DescribeDataAssets](~~DescribeDataAssets~~) operation to obtain the ID of the service.
        self.product_id = product_id  # type: long
        # The sensitivity level of the table. Each sensitivity level ID corresponds to a sensitivity level name. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The ID of the sensitive data detection rule that the table hits. You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the ID of the sensitive data detection rule.
        self.rule_id = rule_id  # type: long
        # The region in which DSC is activated. For more information, see [Supported regions](~~214257~~).
        self.service_region_id = service_region_id  # type: str
        # The ID of the industry-specific rule template.
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeTablesResponseBodyItemsRuleList(TeaModel):
    def __init__(self, count=None, name=None, risk_level_id=None):
        # The total number of rules.
        self.count = count  # type: long
        # The name of the rule.
        self.name = name  # type: str
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTablesResponseBodyItemsRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.name is not None:
            result['Name'] = self.name
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        return self


class DescribeTablesResponseBodyItems(TeaModel):
    def __init__(self, creation_time=None, id=None, instance_description=None, instance_id=None, instance_name=None,
                 name=None, owner=None, product_code=None, product_id=None, risk_level_id=None, risk_level_name=None,
                 rule_list=None, sensitive=None, sensitive_count=None, sensitive_ratio=None, tenant_name=None,
                 total_count=None):
        # The point in time when the table was created. Unit: milliseconds.
        self.creation_time = creation_time  # type: long
        # The ID of the table.
        self.id = id  # type: long
        # The description of the data asset.
        self.instance_description = instance_description  # type: str
        # The ID of the data asset to which the table belongs.
        self.instance_id = instance_id  # type: long
        # The name of the data asset to which the table belongs.
        self.instance_name = instance_name  # type: str
        # The name of the table.
        self.name = name  # type: str
        # The Alibaba Cloud account to which the table belongs.
        self.owner = owner  # type: str
        # The name of the service to which the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**. For more information about the types of data assets from which DSC can scan for sensitive data, see [Supported data assets](~~212906~~).
        self.product_code = product_code  # type: str
        # The ID of the service to which the table belongs.
        self.product_id = product_id  # type: str
        # The sensitivity level of the table. Each sensitivity level ID corresponds to a sensitivity level name. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The name of the sensitivity level for the table. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name  # type: str
        # The information about the sensitive data detection rules that are hit.
        self.rule_list = rule_list  # type: list[DescribeTablesResponseBodyItemsRuleList]
        # Indicates whether the table contains sensitive fields. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sensitive = sensitive  # type: bool
        # The total number of sensitive fields in the table.
        self.sensitive_count = sensitive_count  # type: int
        # The percentage of sensitive fields in the table.
        self.sensitive_ratio = sensitive_ratio  # type: str
        # The name of the tenant.
        self.tenant_name = tenant_name  # type: str
        # The total number of fields in the table.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTablesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count
        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeTablesResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')
        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTablesResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # An array that consists of tables.
        self.items = items  # type: list[DescribeTablesResponseBodyItems]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTablesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTablesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateAllRulesRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, template_id=None):
        self.feature_type = feature_type  # type: int
        self.lang = lang  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateAllRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeTemplateAllRulesResponseBodyRuleList(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateAllRulesResponseBodyRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeTemplateAllRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_list=None):
        self.request_id = request_id  # type: str
        self.rule_list = rule_list  # type: list[DescribeTemplateAllRulesResponseBodyRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplateAllRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeTemplateAllRulesResponseBodyRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeTemplateAllRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTemplateAllRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplateAllRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTemplateAllRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeUserStatusResponseBodyUserStatus(TeaModel):
    def __init__(self, access_key_id=None, audit_closable=None, audit_releasable=None, authed=None,
                 charge_type=None, data_manager_role=None, instance_id=None, instance_num=None, instance_total_count=None,
                 lab_status=None, oss_total_size=None, protection_days=None, purchased=None, release_days=None,
                 release_time=None, remain_days=None, trail=None, use_agent_audit=None, use_instance_num=None, use_oss_size=None):
        # The AccessKey ID of the current account.
        self.access_key_id = access_key_id  # type: str
        # Indicates whether the SQL Explorer feature can be disabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.audit_closable = audit_closable  # type: bool
        # Indicates whether the audit resources can be released.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.audit_releasable = audit_releasable  # type: bool
        # Indicates whether DSC has permission to access user resources within the current account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.authed = authed  # type: bool
        # The billing method of DCS that is purchased by using the current account. Valid values:
        # 
        # *   **PREPAY**: subscription
        # *   **POSTPAY**: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The permissions that the current account has. Valid values:
        # 
        # *   **0**: The current account has the administrative permissions or read-only permissions on Data Security Center.
        # *   **1**: The current account has the permissions to manage data domains.
        self.data_manager_role = data_manager_role  # type: int
        # The ID of the data security center instance purchased by the main account.
        self.instance_id = instance_id  # type: str
        # The number of instances within the current account.
        self.instance_num = instance_num  # type: int
        # The total number of instances.
        self.instance_total_count = instance_total_count  # type: long
        # Indicates whether the data security lab feature is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.lab_status = lab_status  # type: int
        # OSS total storage capacity. Unit: Bytes.
        self.oss_total_size = oss_total_size  # type: long
        # Accumulate the number of days to protect user assets.
        self.protection_days = protection_days  # type: int
        # Indicates whether DSC is purchased. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.purchased = purchased  # type: bool
        # The grace period between when DSC is expired and when DSC is released. Unit: days.
        self.release_days = release_days  # type: int
        # The time when the audit resources are released. Unit: milliseconds.
        self.release_time = release_time  # type: long
        # The remaining period for which the data assets within the current account can be protected by DSC.
        self.remain_days = remain_days  # type: int
        # Indicates whether the current account uses a free trial of DSC. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.trail = trail  # type: bool
        # Indicates whether the agent audit feature is used. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.use_agent_audit = use_agent_audit  # type: bool
        # The number of instances that are used.
        self.use_instance_num = use_instance_num  # type: int
        # The occupied space of the Object Storage Service (OSS) bucket. Unit: bytes.
        self.use_oss_size = use_oss_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserStatusResponseBodyUserStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.audit_closable is not None:
            result['AuditClosable'] = self.audit_closable
        if self.audit_releasable is not None:
            result['AuditReleasable'] = self.audit_releasable
        if self.authed is not None:
            result['Authed'] = self.authed
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.data_manager_role is not None:
            result['DataManagerRole'] = self.data_manager_role
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.instance_total_count is not None:
            result['InstanceTotalCount'] = self.instance_total_count
        if self.lab_status is not None:
            result['LabStatus'] = self.lab_status
        if self.oss_total_size is not None:
            result['OssTotalSize'] = self.oss_total_size
        if self.protection_days is not None:
            result['ProtectionDays'] = self.protection_days
        if self.purchased is not None:
            result['Purchased'] = self.purchased
        if self.release_days is not None:
            result['ReleaseDays'] = self.release_days
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.remain_days is not None:
            result['RemainDays'] = self.remain_days
        if self.trail is not None:
            result['Trail'] = self.trail
        if self.use_agent_audit is not None:
            result['UseAgentAudit'] = self.use_agent_audit
        if self.use_instance_num is not None:
            result['UseInstanceNum'] = self.use_instance_num
        if self.use_oss_size is not None:
            result['UseOssSize'] = self.use_oss_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AuditClosable') is not None:
            self.audit_closable = m.get('AuditClosable')
        if m.get('AuditReleasable') is not None:
            self.audit_releasable = m.get('AuditReleasable')
        if m.get('Authed') is not None:
            self.authed = m.get('Authed')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DataManagerRole') is not None:
            self.data_manager_role = m.get('DataManagerRole')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('InstanceTotalCount') is not None:
            self.instance_total_count = m.get('InstanceTotalCount')
        if m.get('LabStatus') is not None:
            self.lab_status = m.get('LabStatus')
        if m.get('OssTotalSize') is not None:
            self.oss_total_size = m.get('OssTotalSize')
        if m.get('ProtectionDays') is not None:
            self.protection_days = m.get('ProtectionDays')
        if m.get('Purchased') is not None:
            self.purchased = m.get('Purchased')
        if m.get('ReleaseDays') is not None:
            self.release_days = m.get('ReleaseDays')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('RemainDays') is not None:
            self.remain_days = m.get('RemainDays')
        if m.get('Trail') is not None:
            self.trail = m.get('Trail')
        if m.get('UseAgentAudit') is not None:
            self.use_agent_audit = m.get('UseAgentAudit')
        if m.get('UseInstanceNum') is not None:
            self.use_instance_num = m.get('UseInstanceNum')
        if m.get('UseOssSize') is not None:
            self.use_oss_size = m.get('UseOssSize')
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, user_status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the current account.
        self.user_status = user_status  # type: DescribeUserStatusResponseBodyUserStatus

    def validate(self):
        if self.user_status:
            self.user_status.validate()

    def to_map(self):
        _map = super(DescribeUserStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_status is not None:
            result['UserStatus'] = self.user_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserStatus') is not None:
            temp_model = DescribeUserStatusResponseBodyUserStatus()
            self.user_status = temp_model.from_map(m['UserStatus'])
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableUserConfigRequest(TeaModel):
    def __init__(self, code=None, feature_type=None, lang=None):
        # The code of the configuration item. You can call the [DescribeConfigs](~~DescribeConfigs~~) operation to obtain the code of the configuration item.
        self.code = code  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Chinese (default)
        # *   **en_us**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableUserConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DisableUserConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableUserConfigResponseBody, self).to_map()
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


class DisableUserConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableUserConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableUserConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecDatamaskRequest(TeaModel):
    def __init__(self, data=None, feature_type=None, lang=None, template_id=None):
        # The sensitive data to be de-identified. The value is a JSON string that contains the following parameters:
        # 
        # *   **dataHeaderList**: the names of the columns in which data needs to be de-identified. Specify the column names in accordance with the order of data that needs to be de-identified.
        # *   **dataList**: the data that needs to be de-identified.
        # *   **ruleList**: the IDs of sensitive data detection rules used to detect data that needs to be de-identified. Specify the rule IDs in accordance with the order of data that needs to be de-identified. Each ID identifies a sensitive data detection rule that is used to detect a type of sensitive data. You can call the [DescribeRules](~~DescribeRules~~) operation to query the IDs of sensitive data detection rules.
        self.data = data  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The ID of the de-identification template. The ID is generated after you create the de-identification template in the [Data Security Center (DSC) console](https://yundun.console.aliyun.com/?\&p=sddpnext#/sddp/dm/template). You can choose **Data desensitization** > **Desensitization Template** in the left-side navigation pane and obtain the ID of the de-identification template from the **Desensitization Template** page.
        # 
        # *   If you select **Field name** as the matching mode of the template, DSC matches data based on the columns specified by the **dataHeaderList** parameter in the **Data** parameter.
        # *   If you select **Sensitive type** as the matching mode of the template, DSC matches data based on the sensitive data detection rules specified by the **ruleList** parameter in the **Data** parameter.
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecDatamaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ExecDatamaskResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The de-identified data, which is described in a JSON string. The JSON string contains the following parameters:
        # 
        # *   **dataHeaderList**: the names of columns that contain the de-identified data.
        # *   **dataList**: the de-identified data. The column order of the de-identified data is the same as that indicated by the dataHeaderList parameter.
        # *   **ruleList**: the IDs of sensitive data detection rules.
        self.data = data  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecDatamaskResponseBody, self).to_map()
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


class ExecDatamaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecDatamaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecDatamaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecDatamaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManualTriggerMaskingProcessRequest(TeaModel):
    def __init__(self, id=None, lang=None):
        # The ID of the de-identification task.
        # 
        # The ID of the de-identification task is a string. You can call the DescribeDataMaskingTasks operation to query the ID.
        self.id = id  # type: long
        # The language of the content within the request and response, default value zh_cn. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManualTriggerMaskingProcessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ManualTriggerMaskingProcessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManualTriggerMaskingProcessResponseBody, self).to_map()
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


class ManualTriggerMaskingProcessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ManualTriggerMaskingProcessResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ManualTriggerMaskingProcessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ManualTriggerMaskingProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataLimitRequest(TeaModel):
    def __init__(self, audit_status=None, auto_scan=None, engine_type=None, feature_type=None, id=None, lang=None,
                 log_store_day=None, modify_password=None, password=None, port=None, resource_type=None, sampling_size=None,
                 security_group_id_list=None, service_region_id=None, user_name=None, v_switch_id_list=None, vpc_id=None):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.audit_status = audit_status  # type: int
        # Specifies whether to automatically trigger a re-scan after a rule is modified. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # > When a re-scan is triggered, DSC scans all data in your data asset.
        self.auto_scan = auto_scan  # type: int
        # The database engine that is run by the instance. Valid values:
        # 
        # *   **MySQL**\
        # *   **SQLServer**\
        self.engine_type = engine_type  # type: str
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The unique ID of the data asset for which you want to modify configuration items.
        # 
        # > You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the ID of the data asset.
        self.id = id  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The retention period of raw logs after you enable the security audit feature. Unit: days. Valid values:
        # 
        # *   **30**\
        # *   **90**\
        # *   **180**\
        # *   **365**\
        self.log_store_day = log_store_day  # type: int
        # Specifies whether to change the username and password that are used to log on to the ApsaraDB RDS database. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.modify_password = modify_password  # type: bool
        # The password used to log on to the ApsaraDB RDS database that you authorize DSC to access.
        self.password = password  # type: str
        # The port that is used to connect to the database.
        self.port = port  # type: int
        # The name of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type  # type: int
        # The number of sensitive data samples tht are collected after sensitive data detection is enabled. Valid values:
        # 
        # *   **0**\
        # *   **5**\
        # *   **10**\
        self.sampling_size = sampling_size  # type: int
        # The security group that is used by PrivateLink when you install the DSC agent.
        self.security_group_id_list = security_group_id_list  # type: list[str]
        # The region in which the data asset resides. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-huhehaote**: China (Hohhot)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        self.service_region_id = service_region_id  # type: str
        # The username used to log on to the ApsaraDB RDS database that you authorize DSC to access.
        self.user_name = user_name  # type: str
        # The vSwitch that is used by PrivateLink when you install the DSC agent.
        self.v_switch_id_list = v_switch_id_list  # type: list[str]
        # The ID of the virtual private cloud (VPC) to which the data asset belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataLimitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day
        if self.modify_password is not None:
            result['ModifyPassword'] = self.modify_password
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size
        if self.security_group_id_list is not None:
            result['SecurityGroupIdList'] = self.security_group_id_list
        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')
        if m.get('ModifyPassword') is not None:
            self.modify_password = m.get('ModifyPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')
        if m.get('SecurityGroupIdList') is not None:
            self.security_group_id_list = m.get('SecurityGroupIdList')
        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ModifyDataLimitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataLimitResponseBody, self).to_map()
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


class ModifyDataLimitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataLimitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataLimitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDataLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefaultLevelRequest(TeaModel):
    def __init__(self, default_id=None, lang=None, sensitive_ids=None):
        # The default sensitivity level of data that Data Security Center (DSC) cannot classify as sensitive or insensitive. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.default_id = default_id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The sensitivity level ID of data that DSC classifies as sensitive. Separate multiple IDs with commas (,). Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.sensitive_ids = sensitive_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefaultLevelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_id is not None:
            result['DefaultId'] = self.default_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.sensitive_ids is not None:
            result['SensitiveIds'] = self.sensitive_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultId') is not None:
            self.default_id = m.get('DefaultId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SensitiveIds') is not None:
            self.sensitive_ids = m.get('SensitiveIds')
        return self


class ModifyDefaultLevelResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefaultLevelResponseBody, self).to_map()
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


class ModifyDefaultLevelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefaultLevelResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefaultLevelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDefaultLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEventStatusRequest(TeaModel):
    def __init__(self, backed=None, deal_reason=None, id=None, lang=None, status=None):
        # Specifies whether to enhance the detection of anomalous events. If you enhance the detection of anomalous events, the detection accuracy and the rate of triggering alerts for anomalous events are improved. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.backed = backed  # type: bool
        # The reason why the anomalous event is handled.
        self.deal_reason = deal_reason  # type: str
        # The ID of the anomalous event.
        # 
        # > You can call the **DescribeEvents** operation to query the ID of the anomalous event.
        self.id = id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The method to handle the anomalous event. Valid values:
        # 
        # *   **1**: marks the anomalous event as a false positive.
        # *   **2**: confirms and handles the anomalous event.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEventStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backed is not None:
            result['Backed'] = self.backed
        if self.deal_reason is not None:
            result['DealReason'] = self.deal_reason
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backed') is not None:
            self.backed = m.get('Backed')
        if m.get('DealReason') is not None:
            self.deal_reason = m.get('DealReason')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyEventStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEventStatusResponseBody, self).to_map()
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


class ModifyEventStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyEventStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyEventStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyEventStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEventTypeStatusRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, sub_type_ids=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Valid values: **zh** and **en**. The value zh indicates Chinese, and the value en indicates English.
        self.lang = lang  # type: str
        # The ID of the anomalous event subtype. Separate multiple IDs with commas (,).
        # 
        # > You can call the **DescribeEventTypes** operation to query the ID of anomalous event subtype.
        self.sub_type_ids = sub_type_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEventTypeStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.sub_type_ids is not None:
            result['SubTypeIds'] = self.sub_type_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SubTypeIds') is not None:
            self.sub_type_ids = m.get('SubTypeIds')
        return self


class ModifyEventTypeStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEventTypeStatusResponseBody, self).to_map()
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


class ModifyEventTypeStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyEventTypeStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyEventTypeStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyEventTypeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReportTaskStatusRequest(TeaModel):
    def __init__(self, feature_type=None, lang=None, report_task_status=None):
        # This parameter is deprecated.
        self.feature_type = feature_type  # type: int
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # Specifies the status of the report task. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # 
        # > This parameter is required.
        self.report_task_status = report_task_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReportTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')
        return self


class ModifyReportTaskStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReportTaskStatusResponseBody, self).to_map()
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


class ModifyReportTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyReportTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyReportTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyReportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleRequest(TeaModel):
    def __init__(self, category=None, content=None, id=None, lang=None, match_type=None, name=None, product_code=None,
                 product_id=None, risk_level_id=None, rule_type=None, support_form=None, warn_level=None):
        # The content type of the sensitive data detection rule. Valid values:
        # 
        # *   **2**: regular expression
        # *   **3**: algorithm
        # *   **5**: keyword
        self.category = category  # type: int
        # The content of the sensitive data detection rule. You can specify a regular expression, an algorithm, or keywords that are used to match sensitive fields or text.
        self.content = content  # type: str
        # The ID of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule ID.
        self.id = id  # type: long
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang  # type: str
        # The match type. Valid values:
        # 
        # *   **1**: rule-based match
        # *   **2**: dictionary-based match
        self.match_type = match_type  # type: int
        # The name of the sensitive data detection rule.
        # 
        # You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule name.
        self.name = name  # type: str
        # The service to which the sensitive data detection rule is applied. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code  # type: str
        # The ID of the service to which the sensitive data detection rule is applied. Valid values include **1**, **2**, **3**, **4**, and **5**. The value 1 indicates MaxCompute. The value 2 indicates Object Storage Service (OSS). The value 3 indicates AnalyticDB for MySQL. The value 4 indicates Tablestore. The value 5 indicates ApsaraDB RDS.
        self.product_id = product_id  # type: long
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id  # type: long
        # The type of the sensitive data detection rule. Valid values:
        # 
        # *   **1**: data detection rule
        # *   **2**: audit rule
        # *   **3**: anomalous event detection rule
        self.rule_type = rule_type  # type: int
        # The data assets supported by the sensitive data detection rule. Valid values:
        # 
        # *   **0**: all data assets
        # *   **1**: structured data assets
        # *   **2**: unstructured data assets
        self.support_form = support_form  # type: int
        # The risk level of the alert that is triggered by the sensitive data detection rule. Valid values:
        # 
        # *   **1**: low level
        # *   **2**: medium level
        # *   **3**: high level
        self.warn_level = warn_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.support_form is not None:
            result['SupportForm'] = self.support_form
        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SupportForm') is not None:
            self.support_form = m.get('SupportForm')
        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')
        return self


class ModifyRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleResponseBody, self).to_map()
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


class ModifyRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleStatusRequest(TeaModel):
    def __init__(self, id=None, ids=None, lang=None, status=None):
        # The ID of the sensitive data detection rule.
        # 
        # > You can query the ID of the sensitive data detection rule by calling the **DescribeRules** operation.
        self.id = id  # type: long
        # The ID of the sensitive data detection rule. Separate multiple IDs with commas (,).
        # 
        # > You can query the ID of the sensitive data detection rule by calling the **DescribeRules** operation.
        self.ids = ids  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # Specifies whether to enable or disable the sensitive data detection rule. Valid values:
        # 
        # *   **0**: disables the sensitive data detection rule.
        # *   **1**: enables the sensitive data detection rule.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyRuleStatusResponseBody(TeaModel):
    def __init__(self, failed_ids=None, request_id=None):
        # The IDs of sensitive data detection rules whose status failed to be changed. Multiple IDs are separated with commas (,).
        self.failed_ids = failed_ids  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRuleStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyRuleStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRuleStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMaskingProcessRequest(TeaModel):
    def __init__(self, id=None, lang=None):
        # The unique ID of the de-identification task. You can query the task ID by calling the [DescribeDataMaskingTasks](~~DescribeDataMaskingTasks~~) operation.
        self.id = id  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese (default)
        # *   **en_us**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMaskingProcessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class StopMaskingProcessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMaskingProcessResponseBody, self).to_map()
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


class StopMaskingProcessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopMaskingProcessResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopMaskingProcessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopMaskingProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


