# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateQueueRequest(TeaModel):
    def __init__(self, delay_seconds=None, enable_logging=None, maximum_message_size=None,
                 message_retention_period=None, polling_wait_seconds=None, queue_name=None, visibility_timeout=None):
        self.delay_seconds = delay_seconds  # type: long
        self.enable_logging = enable_logging  # type: bool
        self.maximum_message_size = maximum_message_size  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.polling_wait_seconds = polling_wait_seconds  # type: long
        self.queue_name = queue_name  # type: str
        self.visibility_timeout = visibility_timeout  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class CreateQueueResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueueResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: CreateQueueResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateQueueResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequest(TeaModel):
    def __init__(self, enable_logging=None, max_message_size=None, topic_name=None):
        self.enable_logging = enable_logging  # type: bool
        self.max_message_size = max_message_size  # type: long
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class CreateTopicResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTopicResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: CreateTopicResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTopicResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(self, queue_name=None):
        self.queue_name = queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class DeleteQueueResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: DeleteQueueResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteQueueResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(self, topic_name=None):
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTopicResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueAttributesRequest(TeaModel):
    def __init__(self, queue_name=None):
        self.queue_name = queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueueAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class GetQueueAttributesResponseBodyData(TeaModel):
    def __init__(self, active_messages=None, create_time=None, delay_messages=None, delay_seconds=None,
                 inactive_messages=None, last_modify_time=None, logging_enabled=None, maximum_message_size=None,
                 message_retention_period=None, polling_wait_seconds=None, queue_internal_url=None, queue_name=None, queue_url=None,
                 visibility_timeout=None):
        self.active_messages = active_messages  # type: long
        self.create_time = create_time  # type: long
        self.delay_messages = delay_messages  # type: long
        self.delay_seconds = delay_seconds  # type: long
        self.inactive_messages = inactive_messages  # type: long
        self.last_modify_time = last_modify_time  # type: long
        self.logging_enabled = logging_enabled  # type: bool
        self.maximum_message_size = maximum_message_size  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.polling_wait_seconds = polling_wait_seconds  # type: long
        self.queue_internal_url = queue_internal_url  # type: str
        self.queue_name = queue_name  # type: str
        self.queue_url = queue_url  # type: str
        self.visibility_timeout = visibility_timeout  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueueAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_internal_url is not None:
            result['QueueInternalUrl'] = self.queue_internal_url
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_url is not None:
            result['QueueUrl'] = self.queue_url
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayMessages') is not None:
            self.delay_messages = m.get('DelayMessages')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueInternalUrl') is not None:
            self.queue_internal_url = m.get('QueueInternalUrl')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueUrl') is not None:
            self.queue_url = m.get('QueueUrl')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class GetQueueAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: GetQueueAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueueAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQueueAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueueAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionAttributesRequest(TeaModel):
    def __init__(self, subscription_name=None, topic_name=None):
        self.subscription_name = subscription_name  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, endpoint=None, filter_tag=None, last_modify_time=None,
                 notify_content_format=None, notify_strategy=None, subscription_name=None, subscription_url=None, topic_name=None,
                 topic_owner=None):
        self.create_time = create_time  # type: long
        self.endpoint = endpoint  # type: str
        self.filter_tag = filter_tag  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.notify_content_format = notify_content_format  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.subscription_name = subscription_name  # type: str
        self.subscription_url = subscription_url  # type: str
        self.topic_name = topic_name  # type: str
        self.topic_owner = topic_owner  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.subscription_url is not None:
            result['SubscriptionURL'] = self.subscription_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('SubscriptionURL') is not None:
            self.subscription_url = m.get('SubscriptionURL')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')
        return self


class GetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: GetSubscriptionAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSubscriptionAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubscriptionAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubscriptionAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicAttributesRequest(TeaModel):
    def __init__(self, topic_name=None):
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicAttributesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, last_modify_time=None, logging_enabled=None, max_message_size=None,
                 message_count=None, message_retention_period=None, topic_inner_url=None, topic_name=None, topic_url=None):
        self.create_time = create_time  # type: long
        self.last_modify_time = last_modify_time  # type: long
        self.logging_enabled = logging_enabled  # type: bool
        self.max_message_size = max_message_size  # type: long
        self.message_count = message_count  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.topic_inner_url = topic_inner_url  # type: str
        self.topic_name = topic_name  # type: str
        self.topic_url = topic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopicAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.topic_inner_url is not None:
            result['TopicInnerUrl'] = self.topic_inner_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('TopicInnerUrl') is not None:
            self.topic_inner_url = m.get('TopicInnerUrl')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')
        return self


class GetTopicAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: GetTopicAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTopicAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTopicAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTopicAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTopicAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, queue_name=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.queue_name = queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class ListQueueResponseBodyDataPageData(TeaModel):
    def __init__(self, active_messages=None, create_time=None, delay_messages=None, delay_seconds=None,
                 inactive_messages=None, last_modify_time=None, logging_enabled=None, maximum_message_size=None,
                 message_retention_period=None, polling_wait_seconds=None, queue_internal_url=None, queue_name=None, queue_url=None,
                 visibility_timeout=None):
        self.active_messages = active_messages  # type: long
        self.create_time = create_time  # type: long
        self.delay_messages = delay_messages  # type: long
        self.delay_seconds = delay_seconds  # type: long
        self.inactive_messages = inactive_messages  # type: long
        self.last_modify_time = last_modify_time  # type: long
        self.logging_enabled = logging_enabled  # type: bool
        self.maximum_message_size = maximum_message_size  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.polling_wait_seconds = polling_wait_seconds  # type: long
        self.queue_internal_url = queue_internal_url  # type: str
        self.queue_name = queue_name  # type: str
        self.queue_url = queue_url  # type: str
        self.visibility_timeout = visibility_timeout  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_internal_url is not None:
            result['QueueInternalUrl'] = self.queue_internal_url
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_url is not None:
            result['QueueUrl'] = self.queue_url
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayMessages') is not None:
            self.delay_messages = m.get('DelayMessages')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueInternalUrl') is not None:
            self.queue_internal_url = m.get('QueueInternalUrl')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueUrl') is not None:
            self.queue_url = m.get('QueueUrl')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class ListQueueResponseBodyData(TeaModel):
    def __init__(self, page_data=None, page_num=None, page_size=None, pages=None, size=None, total=None):
        self.page_data = page_data  # type: list[ListQueueResponseBodyDataPageData]
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.pages = pages  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueueResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListQueueResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQueueResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: ListQueueResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQueueResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionByTopicRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, subscription_name=None, topic_name=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.subscription_name = subscription_name  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionByTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListSubscriptionByTopicResponseBodyDataPageData(TeaModel):
    def __init__(self, create_time=None, endpoint=None, filter_tag=None, last_modify_time=None,
                 notify_content_format=None, notify_strategy=None, subscription_name=None, subscription_url=None, topic_name=None,
                 topic_owner=None):
        self.create_time = create_time  # type: long
        self.endpoint = endpoint  # type: str
        self.filter_tag = filter_tag  # type: str
        self.last_modify_time = last_modify_time  # type: long
        self.notify_content_format = notify_content_format  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.subscription_name = subscription_name  # type: str
        self.subscription_url = subscription_url  # type: str
        self.topic_name = topic_name  # type: str
        self.topic_owner = topic_owner  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionByTopicResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.subscription_url is not None:
            result['SubscriptionURL'] = self.subscription_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('SubscriptionURL') is not None:
            self.subscription_url = m.get('SubscriptionURL')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')
        return self


class ListSubscriptionByTopicResponseBodyData(TeaModel):
    def __init__(self, page_data=None, page_num=None, page_size=None, pages=None, size=None, total=None):
        self.page_data = page_data  # type: list[ListSubscriptionByTopicResponseBodyDataPageData]
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.pages = pages  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubscriptionByTopicResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListSubscriptionByTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSubscriptionByTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: ListSubscriptionByTopicResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListSubscriptionByTopicResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSubscriptionByTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSubscriptionByTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubscriptionByTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubscriptionByTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubscriptionByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, topic_name=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTopicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListTopicResponseBodyDataPageData(TeaModel):
    def __init__(self, create_time=None, last_modify_time=None, logging_enabled=None, max_message_size=None,
                 message_count=None, message_retention_period=None, topic_inner_url=None, topic_name=None, topic_url=None):
        self.create_time = create_time  # type: long
        self.last_modify_time = last_modify_time  # type: long
        self.logging_enabled = logging_enabled  # type: bool
        self.max_message_size = max_message_size  # type: long
        self.message_count = message_count  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.topic_inner_url = topic_inner_url  # type: str
        self.topic_name = topic_name  # type: str
        self.topic_url = topic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTopicResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.topic_inner_url is not None:
            result['TopicInnerUrl'] = self.topic_inner_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('TopicInnerUrl') is not None:
            self.topic_inner_url = m.get('TopicInnerUrl')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')
        return self


class ListTopicResponseBodyData(TeaModel):
    def __init__(self, page_data=None, page_num=None, page_size=None, total=None):
        self.page_data = page_data  # type: list[ListTopicResponseBodyDataPageData]
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTopicResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTopicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: ListTopicResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTopicResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTopicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTopicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTopicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQueueAttributesRequest(TeaModel):
    def __init__(self, delay_seconds=None, enable_logging=None, maximum_message_size=None,
                 message_retention_period=None, polling_wait_seconds=None, queue_name=None, visibility_timeout=None):
        self.delay_seconds = delay_seconds  # type: long
        self.enable_logging = enable_logging  # type: bool
        self.maximum_message_size = maximum_message_size  # type: long
        self.message_retention_period = message_retention_period  # type: long
        self.polling_wait_seconds = polling_wait_seconds  # type: long
        self.queue_name = queue_name  # type: str
        self.visibility_timeout = visibility_timeout  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetQueueAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class SetQueueAttributesResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetQueueAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: SetQueueAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SetQueueAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetQueueAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetQueueAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSubscriptionAttributesRequest(TeaModel):
    def __init__(self, notify_strategy=None, subscription_name=None, topic_name=None):
        self.notify_strategy = notify_strategy  # type: str
        self.subscription_name = subscription_name  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSubscriptionAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSubscriptionAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: SetSubscriptionAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SetSubscriptionAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetSubscriptionAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetSubscriptionAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTopicAttributesRequest(TeaModel):
    def __init__(self, enable_logging=None, max_message_size=None, topic_name=None):
        self.enable_logging = enable_logging  # type: bool
        self.max_message_size = max_message_size  # type: long
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTopicAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetTopicAttributesResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTopicAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: SetTopicAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SetTopicAttributesResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetTopicAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetTopicAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeRequest(TeaModel):
    def __init__(self, endpoint=None, message_tag=None, notify_content_format=None, notify_strategy=None,
                 push_type=None, subscription_name=None, topic_name=None):
        self.endpoint = endpoint  # type: str
        self.message_tag = message_tag  # type: str
        self.notify_content_format = notify_content_format  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.push_type = push_type  # type: str
        self.subscription_name = subscription_name  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SubscribeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubscribeResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscribeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubscribeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubscribeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeRequest(TeaModel):
    def __init__(self, subscription_name=None, topic_name=None):
        self.subscription_name = subscription_name  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnsubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UnsubscribeResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnsubscribeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: UnsubscribeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UnsubscribeResponseBody, self).to_map()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UnsubscribeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnsubscribeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnsubscribeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnsubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


