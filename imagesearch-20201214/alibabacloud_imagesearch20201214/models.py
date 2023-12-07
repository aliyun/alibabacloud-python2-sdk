# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddImageRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, custom_content=None, instance_name=None, int_attr=None,
                 int_attr_2=None, pic_content=None, pic_name=None, product_id=None, region=None, str_attr=None, str_attr_2=None):
        # The category of the image. For more information, see [Category reference](~~179184~~).
        # 
        # > *   For product image search, if you specify a category for an image, the specified category prevails. If you do not specify a category for an image, the system predicts the category, and returns the prediction result in the response.
        # >*   For generic image search, only 88888888 may be returned for this parameter in the response regardless of whether a category is specified.
        self.category_id = category_id  # type: int
        # Specifies whether to identify the subject in the image and search for images based on the subject identification result. Default value: true. Valid values:
        # 
        # *   true: The system identifies the subject in the image, and searches for images based on the subject identification result. The subject identification result is included in the response.
        # *   false: The system does not identify the subject in the image, and searches for images based on the entire image.
        self.crop = crop  # type: bool
        # The user-defined content. The value can be up to 4,096 characters in length.
        # 
        # > If you specify this parameter, the response includes this parameter and its value. You can add text such as an image description.
        self.custom_content = custom_content  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length. If an Image Search instance is purchased, you can log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance. If no Image Search instance is purchased, you must purchase an instance. For more information, see [Activate Image Search](~~179178~~) and [Create an instance](~~66569~~).
        # 
        # > The instance name is not the instance ID.
        self.instance_name = instance_name  # type: str
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr = int_attr  # type: int
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr_2 = int_attr_2  # type: int
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For product and generic image searches, the length and width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # > *   If you use SDKs to call this operation, you do not need to specify **PicContent**. The SDKs encapsulate this parameter and automatically encode its value in Base64. For more information about how to use Image Search SDK for Java, see [Java SDK](~~179188~~).
        # >*   If you use OpenAPI Explorer to call this operation, you can select only the **2019-03-25** version. If you call this operation of other versions, the value of **PicContent** cannot be encoded in Base64.
        self.pic_content = pic_content  # type: str
        # The name of the image. The name can be up to 512 characters in length.
        # 
        # > *   An image is uniquely identified by the values of ProductId and PicName.
        # >*   If you add an image whose product ID (ProductId) and image name (PicName) are the same as those of an existing image, the newly added image overwrites the existing image.
        self.pic_name = pic_name  # type: str
        # The ID of the product. The ID can be up to 512 characters in length.
        # 
        # > A product may have multiple images.
        self.product_id = product_id  # type: str
        # The subject area of the image, in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels.
        # 
        # > *   If you specify Region, the system searches for images based on the value of Region regardless of the value of Crop.
        # >*   The value of Region does not have a unit. The value is generated based on the length and width of the image. If the length and width of the image are scaled, the value of Region must be proportionally adjusted.
        self.region = region  # type: str
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \ ¥ $ & %\
        self.str_attr = str_attr  # type: str
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \ ¥ $ & %\
        self.str_attr_2 = str_attr_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, custom_content=None, instance_name=None, int_attr=None,
                 int_attr_2=None, pic_content_object=None, pic_name=None, product_id=None, region=None, str_attr=None,
                 str_attr_2=None):
        # The category of the image. For more information, see [Category reference](~~179184~~).
        # 
        # > *   For product image search, if you specify a category for an image, the specified category prevails. If you do not specify a category for an image, the system predicts the category, and returns the prediction result in the response.
        # >*   For generic image search, only 88888888 may be returned for this parameter in the response regardless of whether a category is specified.
        self.category_id = category_id  # type: int
        # Specifies whether to identify the subject in the image and search for images based on the subject identification result. Default value: true. Valid values:
        # 
        # *   true: The system identifies the subject in the image, and searches for images based on the subject identification result. The subject identification result is included in the response.
        # *   false: The system does not identify the subject in the image, and searches for images based on the entire image.
        self.crop = crop  # type: bool
        # The user-defined content. The value can be up to 4,096 characters in length.
        # 
        # > If you specify this parameter, the response includes this parameter and its value. You can add text such as an image description.
        self.custom_content = custom_content  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length. If an Image Search instance is purchased, you can log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance. If no Image Search instance is purchased, you must purchase an instance. For more information, see [Activate Image Search](~~179178~~) and [Create an instance](~~66569~~).
        # 
        # > The instance name is not the instance ID.
        self.instance_name = instance_name  # type: str
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr = int_attr  # type: int
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr_2 = int_attr_2  # type: int
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For product and generic image searches, the length and width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # > *   If you use SDKs to call this operation, you do not need to specify **PicContent**. The SDKs encapsulate this parameter and automatically encode its value in Base64. For more information about how to use Image Search SDK for Java, see [Java SDK](~~179188~~).
        # >*   If you use OpenAPI Explorer to call this operation, you can select only the **2019-03-25** version. If you call this operation of other versions, the value of **PicContent** cannot be encoded in Base64.
        self.pic_content_object = pic_content_object  # type: READABLE
        # The name of the image. The name can be up to 512 characters in length.
        # 
        # > *   An image is uniquely identified by the values of ProductId and PicName.
        # >*   If you add an image whose product ID (ProductId) and image name (PicName) are the same as those of an existing image, the newly added image overwrites the existing image.
        self.pic_name = pic_name  # type: str
        # The ID of the product. The ID can be up to 512 characters in length.
        # 
        # > A product may have multiple images.
        self.product_id = product_id  # type: str
        # The subject area of the image, in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels.
        # 
        # > *   If you specify Region, the system searches for images based on the value of Region regardless of the value of Crop.
        # >*   The value of Region does not have a unit. The value is generated based on the length and width of the image. If the length and width of the image are scaled, the value of Region must be proportionally adjusted.
        self.region = region  # type: str
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \ ¥ $ & %\
        self.str_attr = str_attr  # type: str
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \ ¥ $ & %\
        self.str_attr_2 = str_attr_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        return self


class AddImageResponseBodyPicInfo(TeaModel):
    def __init__(self, category_id=None, region=None):
        # The result of category prediction. If a category is specified in the request, the specified category prevails.
        self.category_id = category_id  # type: int
        # The result of subject identification. The subject area of the image is in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageResponseBodyPicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, pic_info=None, request_id=None, success=None):
        # The code returned.
        # 
        # *   A value of 0 indicates that the request was successful.
        # *   Values other than 0 indicate that the request failed.
        self.code = code  # type: int
        # The error message returned if the request failed.
        # 
        # > No value is returned if the request was successful, and an error message is returned if the request failed.
        self.message = message  # type: str
        # The results of category prediction and subject identification.
        self.pic_info = pic_info  # type: AddImageResponseBodyPicInfo
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super(AddImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
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
        if m.get('PicInfo') is not None:
            temp_model = AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, instance_name=None, pic_name=None, product_id=None):
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The name of the image.
        # 
        # *   If this parameter is not set, the system deletes all the images that correspond to the specified ProductId parameter.
        # *   If this parameter is set, the system deletes only the image that is specified by the ProductId and PicName parameters.
        self.pic_name = pic_name  # type: str
        # The ID of the commodity.
        # 
        # >  A commodity may have multiple images.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteImageResponseBodyData(TeaModel):
    def __init__(self, pic_names=None):
        # The name (PicName) of the deleted image.
        self.pic_names = pic_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: int
        # The information about the deleted images.
        self.data = data  # type: DeleteImageResponseBodyData
        # The error message returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
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
            temp_model = DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailRequest(TeaModel):
    def __init__(self, instance_name=None):
        # The name of the instance.
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailRequest, self).to_map()
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


class DetailResponseBodyInstance(TeaModel):
    def __init__(self, capacity=None, name=None, qps=None, region=None, service_type=None, total_count=None,
                 utc_create=None, utc_expire_time=None):
        # The capacity of the plan. Unit: × 10,000 images.
        self.capacity = capacity  # type: int
        # The name of the instance.
        self.name = name  # type: str
        # The number of queries per second supported by the plan.
        self.qps = qps  # type: int
        # The information about the region.
        self.region = region  # type: str
        # The Image Search model.
        # 
        # 0: commodity search. 1: generic image search.
        self.service_type = service_type  # type: int
        # The number of images.
        self.total_count = total_count  # type: long
        # The time when the instance was created. Unit: milliseconds.
        self.utc_create = utc_create  # type: str
        # The time when the instance expires. Unit: milliseconds.
        self.utc_expire_time = utc_expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.name is not None:
            result['Name'] = self.name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class DetailResponseBody(TeaModel):
    def __init__(self, instance=None, request_id=None, success=None):
        # The details about the instance.
        self.instance = instance  # type: DetailResponseBodyInstance
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(DetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DetailResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaRequest(TeaModel):
    def __init__(self, instance_name=None):
        # The name of the instance.
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DumpMetaRequest, self).to_map()
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


class DumpMetaResponseBodyData(TeaModel):
    def __init__(self, dump_meta_status=None, id=None):
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.dump_meta_status = dump_meta_status  # type: str
        # The ID of the export task.
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DumpMetaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dump_meta_status is not None:
            result['DumpMetaStatus'] = self.dump_meta_status
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DumpMetaStatus') is not None:
            self.dump_meta_status = m.get('DumpMetaStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DumpMetaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        # The information about the export task.
        self.data = data  # type: DumpMetaResponseBodyData
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DumpMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DumpMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DumpMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DumpMetaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaListRequest(TeaModel):
    def __init__(self, id=None, instance_name=None, page_number=None, page_size=None):
        # The ID of the export task.
        self.id = id  # type: long
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of images to return on each page. Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DumpMetaListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DumpMetaListResponseBodyDataDumpMetaList(TeaModel):
    def __init__(self, code=None, id=None, meta_url=None, msg=None, status=None, utc_create=None, utc_modified=None):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: str
        # The ID of the task.
        self.id = id  # type: long
        # The address where you can download the metadata. The address is valid for 2 hours.
        self.meta_url = meta_url  # type: str
        # The error message returned.
        self.msg = msg  # type: str
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status  # type: str
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create  # type: str
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DumpMetaListResponseBodyDataDumpMetaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class DumpMetaListResponseBodyData(TeaModel):
    def __init__(self, dump_meta_list=None, page_number=None, page_size=None, total_count=None):
        # A list of tasks that are used to export metadata.
        self.dump_meta_list = dump_meta_list  # type: list[DumpMetaListResponseBodyDataDumpMetaList]
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The total number of tasks.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.dump_meta_list:
            for k in self.dump_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DumpMetaListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k in self.dump_meta_list:
                result['DumpMetaList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k in m.get('DumpMetaList'):
                temp_model = DumpMetaListResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DumpMetaListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The information about the task that is used to export metadata.
        self.data = data  # type: DumpMetaListResponseBodyData
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DumpMetaListResponseBody, self).to_map()
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
            temp_model = DumpMetaListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DumpMetaListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DumpMetaListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DumpMetaListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseInstanceRequest(TeaModel):
    def __init__(self, bucket_name=None, callback_address=None, instance_name=None, path=None):
        # The name of the Object Storage Service (OSS) bucket.
        # 
        # >  The bucket must be in the same region as the Image Search instance.
        self.bucket_name = bucket_name  # type: str
        # The callback address.
        self.callback_address = callback_address  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseInstanceResponseBodyData(TeaModel):
    def __init__(self, id=None, increment_status=None):
        # The ID of the task.
        self.id = id  # type: str
        # The status of the task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.increment_status = increment_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.increment_status is not None:
            result['IncrementStatus'] = self.increment_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncrementStatus') is not None:
            self.increment_status = m.get('IncrementStatus')
        return self


class IncreaseInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        # The information about the task.
        self.data = data  # type: IncreaseInstanceResponseBodyData
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(IncreaseInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = IncreaseInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IncreaseInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IncreaseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IncreaseInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseListRequest(TeaModel):
    def __init__(self, bucket_name=None, id=None, instance_name=None, page_number=None, page_size=None, path=None):
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name  # type: str
        # The ID of the batch task.
        self.id = id  # type: long
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of images to return on each page. Default value: 10.
        self.page_size = page_size  # type: int
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseListResponseBodyDataIncrementsInstance(TeaModel):
    def __init__(self, bucket_name=None, callback_address=None, code=None, error_url=None, id=None, msg=None,
                 path=None, status=None, utc_create=None, utc_modified=None):
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name  # type: str
        # The callback address.
        self.callback_address = callback_address  # type: str
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: str
        # The address where you can download the result. The address is valid for 2 hours.
        self.error_url = error_url  # type: str
        # The ID of the task.
        self.id = id  # type: long
        # The error message returned.
        self.msg = msg  # type: str
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path  # type: str
        # The status of the batch task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status  # type: str
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create  # type: str
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(IncreaseListResponseBodyDataIncrementsInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.code is not None:
            result['Code'] = self.code
        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url
        if self.id is not None:
            result['Id'] = self.id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class IncreaseListResponseBodyDataIncrements(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[IncreaseListResponseBodyDataIncrementsInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IncreaseListResponseBodyDataIncrements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = IncreaseListResponseBodyDataIncrementsInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class IncreaseListResponseBodyData(TeaModel):
    def __init__(self, increments=None, page_number=None, page_size=None, total_count=None):
        # A list of batch tasks.
        self.increments = increments  # type: IncreaseListResponseBodyDataIncrements
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The total number of tasks.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.increments:
            self.increments.validate()

    def to_map(self):
        _map = super(IncreaseListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.increments is not None:
            result['Increments'] = self.increments.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Increments') is not None:
            temp_model = IncreaseListResponseBodyDataIncrements()
            self.increments = temp_model.from_map(m['Increments'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class IncreaseListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The information about the batch task.
        self.data = data  # type: IncreaseListResponseBodyData
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(IncreaseListResponseBody, self).to_map()
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
            temp_model = IncreaseListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IncreaseListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IncreaseListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IncreaseListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(self, category_id=None, filter=None, instance_name=None, num=None, pic_name=None, product_id=None,
                 start=None):
        # The category of the product. For more information, see [Category references](~~179184~~).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id  # type: int
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   int_attr=1000 AND str_attr="value1"
        self.filter = filter  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num  # type: int
        # The name of the image.
        self.pic_name = pic_name  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByNameResponseBodyAuctions(TeaModel):
    def __init__(self, category_id=None, custom_content=None, int_attr=None, int_attr_2=None, pic_name=None,
                 product_id=None, score=None, sort_expr_values=None, str_attr=None, str_attr_2=None):
        # The category of the image.
        self.category_id = category_id  # type: int
        # The user-defined content.
        self.custom_content = custom_content  # type: str
        # The attribute, which is an integer.
        self.int_attr = int_attr  # type: int
        self.int_attr_2 = int_attr_2  # type: int
        # The name of the image.
        self.pic_name = pic_name  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The similarity score of the returned image. Valid values: 0 to 1.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.score = score  # type: float
        # The score information about the image.
        # 
        # > *   This parameter is not supported. We recommend that you use the Score parameter.
        # >*   The SortExprValues parameter indicates a 2-tuple in which values are separated by a semicolon (;). The first value indicates the correlation score of the returned image. A greater value indicates a higher correlation with the sample image. Different algorithms are used.
        # >*   If the value of CategoryId is within the value range from 0 to 2, the value range of SortExprValues is from 0 to 7.33136443711219e+24.
        # >*   If the value of CategoryId is not within the value range from 0 to 2, the value range of SortExprValues is from 0 to 5.37633353624177e+24. If the returned image is identical with the sample image, the highest correlation score is generated.
        self.sort_expr_values = sort_expr_values  # type: str
        # The attribute, which is a string.
        self.str_attr = str_attr  # type: str
        self.str_attr_2 = str_attr_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyAuctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        return self


class SearchImageByNameResponseBodyHead(TeaModel):
    def __init__(self, docs_found=None, docs_return=None, search_time=None):
        # The number of images returned.
        self.docs_found = docs_found  # type: int
        # The number of images that match the search conditions on the Image Search instance.
        self.docs_return = docs_return  # type: int
        # The time it takes to complete the search process. Unit: milliseconds.
        self.search_time = search_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyHead, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByNameResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(self, id=None, name=None):
        # The ID of the category.
        self.id = id  # type: int
        # The name of the category.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyPicInfoAllCategories, self).to_map()
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


class SearchImageByNameResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(self, region=None):
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyPicInfoMultiRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBodyPicInfo(TeaModel):
    def __init__(self, all_categories=None, category_id=None, multi_region=None, region=None):
        # The categories that are supported by the system.
        self.all_categories = all_categories  # type: list[SearchImageByNameResponseBodyPicInfoAllCategories]
        # The category selected by the system.
        # 
        # If a category is specified in the request, the specified category prevails.
        self.category_id = category_id  # type: int
        # The recognized subjects.
        self.multi_region = multi_region  # type: list[SearchImageByNameResponseBodyPicInfoMultiRegion]
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region  # type: str

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponseBodyPicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByNameResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByNameResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(self, auctions=None, code=None, head=None, msg=None, pic_info=None, request_id=None, success=None):
        # The product descriptions returned.
        self.auctions = auctions  # type: list[SearchImageByNameResponseBodyAuctions]
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: int
        # The summary of the search result.
        self.head = head  # type: SearchImageByNameResponseBodyHead
        # The error message returned.
        self.msg = msg  # type: str
        # The information such as the system-selected category and result of subject recognition.
        self.pic_info = pic_info  # type: SearchImageByNameResponseBodyPicInfo
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByNameResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByNameResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByNameResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageByNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageByNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, filter=None, instance_name=None, num=None, pic_content=None,
                 region=None, start=None):
        # The category of the product. For more information, see [Category references](~~179184~~).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id  # type: int
        # Specifies whether to recognize the subject in the image and search for images based on the recognized subject. Valid values: true and false. Default value: true.
        # 
        # *   true: The system recognizes the subject in the image, and searches for images based on the recognized subject. The recognition result is included in the response.
        # *   false: The system does not recognize the subject of the image, and searches for images based on the entire image.
        self.crop = crop  # type: bool
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   Example: int_attr=1000 AND str_attr="value1"
        self.filter = filter  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num  # type: int
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For brand image searches, the length and the width of the image must range from 200 pixels to 4,096 pixels.
        # *   For cloth image searches, the length and the width of the image must range from 448 pixels to 4,096 pixels.
        # *   For product and generic image searches, the length and the width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        self.pic_content = pic_content  # type: str
        # The subject area of the image. Specify the subject area in the following format: `x1,x2,y1,y2`. `x1 and y1` represent the upper-left corner pixel. `x2 and y2` represent the lower-right corner pixel.
        # 
        # >*   If you set the Region parameter, the system searches for images based on the value of Region regardless of the value of the Crop parameter.
        self.region = region  # type: str
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(self, category_id=None, crop=None, filter=None, instance_name=None, num=None,
                 pic_content_object=None, region=None, start=None):
        # The category of the product. For more information, see [Category references](~~179184~~).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id  # type: int
        # Specifies whether to recognize the subject in the image and search for images based on the recognized subject. Valid values: true and false. Default value: true.
        # 
        # *   true: The system recognizes the subject in the image, and searches for images based on the recognized subject. The recognition result is included in the response.
        # *   false: The system does not recognize the subject of the image, and searches for images based on the entire image.
        self.crop = crop  # type: bool
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   Example: int_attr=1000 AND str_attr="value1"
        self.filter = filter  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num  # type: int
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For brand image searches, the length and the width of the image must range from 200 pixels to 4,096 pixels.
        # *   For cloth image searches, the length and the width of the image must range from 448 pixels to 4,096 pixels.
        # *   For product and generic image searches, the length and the width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        self.pic_content_object = pic_content_object  # type: READABLE
        # The subject area of the image. Specify the subject area in the following format: `x1,x2,y1,y2`. `x1 and y1` represent the upper-left corner pixel. `x2 and y2` represent the lower-right corner pixel.
        # 
        # >*   If you set the Region parameter, the system searches for images based on the value of Region regardless of the value of the Crop parameter.
        self.region = region  # type: str
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicResponseBodyAuctions(TeaModel):
    def __init__(self, category_id=None, custom_content=None, int_attr=None, int_attr_2=None, pic_name=None,
                 product_id=None, score=None, sort_expr_values=None, str_attr=None, str_attr_2=None):
        # The category of the image.
        self.category_id = category_id  # type: int
        # The user-defined content.
        self.custom_content = custom_content  # type: str
        # The attribute, which is an integer.
        self.int_attr = int_attr  # type: int
        self.int_attr_2 = int_attr_2  # type: int
        # The name of the image.
        self.pic_name = pic_name  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The similarity score of the searched image. Valid values: 0 to 1.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.score = score  # type: float
        # The score information about the image.
        # 
        # > *   This parameter is not supported. We recommend that you use the Score parameter.
        # >*   The SortExprValues parameter indicates a 2-tuple in which values are separated by a semicolon (;). The first value indicates the correlation score of the returned image. A greater value indicates a higher correlation with the sample image. Different algorithms are used.
        # >*   If the value of CategoryId is within the value range from 0 to 2, the value range of SortExprValues is from 0 to 7.33136443711219e+24.
        # >*   If the value of CategoryId is not within the value range from 0 to 2, the value range of SortExprValues is from 0 to 5.37633353624177e+24. If the returned image is identical with the sample image, the highest correlation score is generated.
        self.sort_expr_values = sort_expr_values  # type: str
        # The attribute, which is a string.
        self.str_attr = str_attr  # type: str
        self.str_attr_2 = str_attr_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyAuctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        return self


class SearchImageByPicResponseBodyHead(TeaModel):
    def __init__(self, docs_found=None, docs_return=None, search_time=None):
        # The number of images returned.
        self.docs_found = docs_found  # type: int
        # The number of images that match the search conditions on the Image Search instance.
        self.docs_return = docs_return  # type: int
        # The time it takes to complete the search process. Unit: milliseconds.
        self.search_time = search_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyHead, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByPicResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(self, id=None, name=None):
        # The ID of the category.
        self.id = id  # type: int
        # The name of the category.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyPicInfoAllCategories, self).to_map()
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


class SearchImageByPicResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(self, region=None):
        # The result of subject recognition. The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyPicInfoMultiRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBodyPicInfo(TeaModel):
    def __init__(self, all_categories=None, category_id=None, multi_region=None, region=None):
        # The categories that are supported by the system.
        self.all_categories = all_categories  # type: list[SearchImageByPicResponseBodyPicInfoAllCategories]
        # The category selected by the system. If a category is specified in the request, the specified category prevails.
        self.category_id = category_id  # type: int
        # The recognized subjects.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.multi_region = multi_region  # type: list[SearchImageByPicResponseBodyPicInfoMultiRegion]
        # The result of subject recognition. The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region  # type: str

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponseBodyPicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByPicResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(self, auctions=None, code=None, head=None, msg=None, pic_info=None, request_id=None, success=None):
        # The product descriptions returned.
        self.auctions = auctions  # type: list[SearchImageByPicResponseBodyAuctions]
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: int
        # The summary of the search result.
        self.head = head  # type: SearchImageByPicResponseBodyHead
        # The error message returned.
        self.msg = msg  # type: str
        # The information such as the system-selected category and result of subject recognition.
        self.pic_info = pic_info  # type: SearchImageByPicResponseBodyPicInfo
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByPicResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByPicResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageByPicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageByPicResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(self, custom_content=None, instance_name=None, int_attr=None, int_attr_2=None, pic_name=None,
                 product_id=None, str_attr=None, str_attr_2=None):
        # The user-defined content. The value can be up to 4,096 characters in length.
        # 
        # >  If you set this parameter, the response includes this parameter and its value. You can add text such as an image description.
        self.custom_content = custom_content  # type: str
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        self.instance_name = instance_name  # type: str
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you set this parameter, the response includes this parameter and its value.
        self.int_attr = int_attr  # type: int
        self.int_attr_2 = int_attr_2  # type: int
        # The name of the image. The name can be up to 512 characters in length.
        # 
        # > *   An image is uniquely identified by the values of the ProductId and PicName parameters.
        # >*   If you add an image whose product ID (ProductId) and image name (PicName) are the same as those of an existing image, the newly added image overwrites the existing image.
        self.pic_name = pic_name  # type: str
        # The ID of the product. The ID can be up to 512 characters in length.
        # 
        # >  A product may have multiple images.
        self.product_id = product_id  # type: str
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images. If you set this parameter, the response includes this parameter and its value.
        self.str_attr = str_attr  # type: str
        self.str_attr_2 = str_attr_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code  # type: int
        # Id of the request
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


