# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GenerateCosplayImageRequest(TeaModel):
    def __init__(self, face_image_url=None, style=None, template_image_url=None):
        self.face_image_url = face_image_url  # type: str
        self.style = style  # type: long
        self.template_image_url = template_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCosplayImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.style is not None:
            result['Style'] = self.style
        if self.template_image_url is not None:
            result['TemplateImageUrl'] = self.template_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('TemplateImageUrl') is not None:
            self.template_image_url = m.get('TemplateImageUrl')
        return self


class GenerateCosplayImageAdvanceRequest(TeaModel):
    def __init__(self, face_image_url_object=None, style=None, template_image_url_object=None):
        self.face_image_url_object = face_image_url_object  # type: READABLE
        self.style = style  # type: long
        self.template_image_url_object = template_image_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCosplayImageAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_image_url_object is not None:
            result['FaceImageUrl'] = self.face_image_url_object
        if self.style is not None:
            result['Style'] = self.style
        if self.template_image_url_object is not None:
            result['TemplateImageUrl'] = self.template_image_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceImageUrl') is not None:
            self.face_image_url_object = m.get('FaceImageUrl')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('TemplateImageUrl') is not None:
            self.template_image_url_object = m.get('TemplateImageUrl')
        return self


class GenerateCosplayImageResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCosplayImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateCosplayImageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateCosplayImageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateCosplayImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateCosplayImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCosplayImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateCosplayImageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateCosplayImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateCosplayImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTextDeformationRequest(TeaModel):
    def __init__(self, async=None, font_name=None, n=None, output_image_ratio=None, prompt=None, text_content=None,
                 ttf_url=None):
        # 1
        self.async = async  # type: bool
        self.font_name = font_name  # type: str
        self.n = n  # type: long
        self.output_image_ratio = output_image_ratio  # type: str
        self.prompt = prompt  # type: str
        self.text_content = text_content  # type: str
        self.ttf_url = ttf_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextDeformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async is not None:
            result['Async'] = self.async
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.n is not None:
            result['N'] = self.n
        if self.output_image_ratio is not None:
            result['OutputImageRatio'] = self.output_image_ratio
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.ttf_url is not None:
            result['TtfUrl'] = self.ttf_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('OutputImageRatio') is not None:
            self.output_image_ratio = m.get('OutputImageRatio')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('TtfUrl') is not None:
            self.ttf_url = m.get('TtfUrl')
        return self


class GenerateTextDeformationAdvanceRequest(TeaModel):
    def __init__(self, async=None, font_name=None, n=None, output_image_ratio=None, prompt=None, text_content=None,
                 ttf_url_object=None):
        # 1
        self.async = async  # type: bool
        self.font_name = font_name  # type: str
        self.n = n  # type: long
        self.output_image_ratio = output_image_ratio  # type: str
        self.prompt = prompt  # type: str
        self.text_content = text_content  # type: str
        self.ttf_url_object = ttf_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextDeformationAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async is not None:
            result['Async'] = self.async
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.n is not None:
            result['N'] = self.n
        if self.output_image_ratio is not None:
            result['OutputImageRatio'] = self.output_image_ratio
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.ttf_url_object is not None:
            result['TtfUrl'] = self.ttf_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('OutputImageRatio') is not None:
            self.output_image_ratio = m.get('OutputImageRatio')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('TtfUrl') is not None:
            self.ttf_url_object = m.get('TtfUrl')
        return self


class GenerateTextDeformationResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextDeformationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateTextDeformationResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateTextDeformationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateTextDeformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateTextDeformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateTextDeformationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateTextDeformationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateTextDeformationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateTextDeformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTextTextureRequest(TeaModel):
    def __init__(self, alpha_channel=None, font_name=None, image_short_size=None, image_url=None, n=None,
                 output_image_ratio=None, prompt=None, text_content=None, texture_style=None, ttf_url=None):
        self.alpha_channel = alpha_channel  # type: bool
        self.font_name = font_name  # type: str
        self.image_short_size = image_short_size  # type: long
        self.image_url = image_url  # type: str
        self.n = n  # type: long
        self.output_image_ratio = output_image_ratio  # type: str
        self.prompt = prompt  # type: str
        self.text_content = text_content  # type: str
        self.texture_style = texture_style  # type: str
        self.ttf_url = ttf_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextTextureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_channel is not None:
            result['AlphaChannel'] = self.alpha_channel
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.image_short_size is not None:
            result['ImageShortSize'] = self.image_short_size
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.n is not None:
            result['N'] = self.n
        if self.output_image_ratio is not None:
            result['OutputImageRatio'] = self.output_image_ratio
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.texture_style is not None:
            result['TextureStyle'] = self.texture_style
        if self.ttf_url is not None:
            result['TtfUrl'] = self.ttf_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaChannel') is not None:
            self.alpha_channel = m.get('AlphaChannel')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('ImageShortSize') is not None:
            self.image_short_size = m.get('ImageShortSize')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('OutputImageRatio') is not None:
            self.output_image_ratio = m.get('OutputImageRatio')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('TextureStyle') is not None:
            self.texture_style = m.get('TextureStyle')
        if m.get('TtfUrl') is not None:
            self.ttf_url = m.get('TtfUrl')
        return self


class GenerateTextTextureAdvanceRequest(TeaModel):
    def __init__(self, alpha_channel=None, font_name=None, image_short_size=None, image_url_object=None, n=None,
                 output_image_ratio=None, prompt=None, text_content=None, texture_style=None, ttf_url_object=None):
        self.alpha_channel = alpha_channel  # type: bool
        self.font_name = font_name  # type: str
        self.image_short_size = image_short_size  # type: long
        self.image_url_object = image_url_object  # type: READABLE
        self.n = n  # type: long
        self.output_image_ratio = output_image_ratio  # type: str
        self.prompt = prompt  # type: str
        self.text_content = text_content  # type: str
        self.texture_style = texture_style  # type: str
        self.ttf_url_object = ttf_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextTextureAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_channel is not None:
            result['AlphaChannel'] = self.alpha_channel
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.image_short_size is not None:
            result['ImageShortSize'] = self.image_short_size
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.n is not None:
            result['N'] = self.n
        if self.output_image_ratio is not None:
            result['OutputImageRatio'] = self.output_image_ratio
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.texture_style is not None:
            result['TextureStyle'] = self.texture_style
        if self.ttf_url_object is not None:
            result['TtfUrl'] = self.ttf_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaChannel') is not None:
            self.alpha_channel = m.get('AlphaChannel')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('ImageShortSize') is not None:
            self.image_short_size = m.get('ImageShortSize')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('OutputImageRatio') is not None:
            self.output_image_ratio = m.get('OutputImageRatio')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('TextureStyle') is not None:
            self.texture_style = m.get('TextureStyle')
        if m.get('TtfUrl') is not None:
            self.ttf_url_object = m.get('TtfUrl')
        return self


class GenerateTextTextureResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateTextTextureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class GenerateTextTextureResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: GenerateTextTextureResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateTextTextureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GenerateTextTextureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateTextTextureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateTextTextureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateTextTextureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateTextTextureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InteractiveFullSegmentationRequest(TeaModel):
    def __init__(self, image_url=None, return_format=None):
        self.image_url = image_url  # type: str
        self.return_format = return_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveFullSegmentationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.return_format is not None:
            result['ReturnFormat'] = self.return_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ReturnFormat') is not None:
            self.return_format = m.get('ReturnFormat')
        return self


class InteractiveFullSegmentationAdvanceRequest(TeaModel):
    def __init__(self, image_url_object=None, return_format=None):
        self.image_url_object = image_url_object  # type: READABLE
        self.return_format = return_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveFullSegmentationAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.return_format is not None:
            result['ReturnFormat'] = self.return_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('ReturnFormat') is not None:
            self.return_format = m.get('ReturnFormat')
        return self


class InteractiveFullSegmentationResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveFullSegmentationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class InteractiveFullSegmentationResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None):
        self.data = data  # type: InteractiveFullSegmentationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InteractiveFullSegmentationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = InteractiveFullSegmentationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InteractiveFullSegmentationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InteractiveFullSegmentationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InteractiveFullSegmentationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InteractiveFullSegmentationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InteractiveScribbleSegmentationRequest(TeaModel):
    def __init__(self, edge_feathering=None, image_url=None, integrated_mask_url=None, mask_image_url=None,
                 neg_scribble_image_url=None, pos_scribble_image_url=None, postprocess_option=None, return_form=None, return_format=None):
        self.edge_feathering = edge_feathering  # type: str
        self.image_url = image_url  # type: str
        self.integrated_mask_url = integrated_mask_url  # type: str
        self.mask_image_url = mask_image_url  # type: str
        self.neg_scribble_image_url = neg_scribble_image_url  # type: str
        self.pos_scribble_image_url = pos_scribble_image_url  # type: str
        self.postprocess_option = postprocess_option  # type: str
        self.return_form = return_form  # type: str
        self.return_format = return_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveScribbleSegmentationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_feathering is not None:
            result['EdgeFeathering'] = self.edge_feathering
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.integrated_mask_url is not None:
            result['IntegratedMaskUrl'] = self.integrated_mask_url
        if self.mask_image_url is not None:
            result['MaskImageUrl'] = self.mask_image_url
        if self.neg_scribble_image_url is not None:
            result['NegScribbleImageUrl'] = self.neg_scribble_image_url
        if self.pos_scribble_image_url is not None:
            result['PosScribbleImageUrl'] = self.pos_scribble_image_url
        if self.postprocess_option is not None:
            result['PostprocessOption'] = self.postprocess_option
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        if self.return_format is not None:
            result['ReturnFormat'] = self.return_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EdgeFeathering') is not None:
            self.edge_feathering = m.get('EdgeFeathering')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IntegratedMaskUrl') is not None:
            self.integrated_mask_url = m.get('IntegratedMaskUrl')
        if m.get('MaskImageUrl') is not None:
            self.mask_image_url = m.get('MaskImageUrl')
        if m.get('NegScribbleImageUrl') is not None:
            self.neg_scribble_image_url = m.get('NegScribbleImageUrl')
        if m.get('PosScribbleImageUrl') is not None:
            self.pos_scribble_image_url = m.get('PosScribbleImageUrl')
        if m.get('PostprocessOption') is not None:
            self.postprocess_option = m.get('PostprocessOption')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        if m.get('ReturnFormat') is not None:
            self.return_format = m.get('ReturnFormat')
        return self


class InteractiveScribbleSegmentationAdvanceRequest(TeaModel):
    def __init__(self, edge_feathering=None, image_url_object=None, integrated_mask_url_object=None,
                 mask_image_url_object=None, neg_scribble_image_url_object=None, pos_scribble_image_url_object=None,
                 postprocess_option=None, return_form=None, return_format=None):
        self.edge_feathering = edge_feathering  # type: str
        self.image_url_object = image_url_object  # type: READABLE
        self.integrated_mask_url_object = integrated_mask_url_object  # type: READABLE
        self.mask_image_url_object = mask_image_url_object  # type: READABLE
        self.neg_scribble_image_url_object = neg_scribble_image_url_object  # type: READABLE
        self.pos_scribble_image_url_object = pos_scribble_image_url_object  # type: READABLE
        self.postprocess_option = postprocess_option  # type: str
        self.return_form = return_form  # type: str
        self.return_format = return_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveScribbleSegmentationAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_feathering is not None:
            result['EdgeFeathering'] = self.edge_feathering
        if self.image_url_object is not None:
            result['ImageUrl'] = self.image_url_object
        if self.integrated_mask_url_object is not None:
            result['IntegratedMaskUrl'] = self.integrated_mask_url_object
        if self.mask_image_url_object is not None:
            result['MaskImageUrl'] = self.mask_image_url_object
        if self.neg_scribble_image_url_object is not None:
            result['NegScribbleImageUrl'] = self.neg_scribble_image_url_object
        if self.pos_scribble_image_url_object is not None:
            result['PosScribbleImageUrl'] = self.pos_scribble_image_url_object
        if self.postprocess_option is not None:
            result['PostprocessOption'] = self.postprocess_option
        if self.return_form is not None:
            result['ReturnForm'] = self.return_form
        if self.return_format is not None:
            result['ReturnFormat'] = self.return_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EdgeFeathering') is not None:
            self.edge_feathering = m.get('EdgeFeathering')
        if m.get('ImageUrl') is not None:
            self.image_url_object = m.get('ImageUrl')
        if m.get('IntegratedMaskUrl') is not None:
            self.integrated_mask_url_object = m.get('IntegratedMaskUrl')
        if m.get('MaskImageUrl') is not None:
            self.mask_image_url_object = m.get('MaskImageUrl')
        if m.get('NegScribbleImageUrl') is not None:
            self.neg_scribble_image_url_object = m.get('NegScribbleImageUrl')
        if m.get('PosScribbleImageUrl') is not None:
            self.pos_scribble_image_url_object = m.get('PosScribbleImageUrl')
        if m.get('PostprocessOption') is not None:
            self.postprocess_option = m.get('PostprocessOption')
        if m.get('ReturnForm') is not None:
            self.return_form = m.get('ReturnForm')
        if m.get('ReturnFormat') is not None:
            self.return_format = m.get('ReturnFormat')
        return self


class InteractiveScribbleSegmentationResponseBodyData(TeaModel):
    def __init__(self, result_url=None):
        self.result_url = result_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InteractiveScribbleSegmentationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        return self


class InteractiveScribbleSegmentationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: InteractiveScribbleSegmentationResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InteractiveScribbleSegmentationResponseBody, self).to_map()
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
            temp_model = InteractiveScribbleSegmentationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InteractiveScribbleSegmentationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InteractiveScribbleSegmentationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InteractiveScribbleSegmentationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InteractiveScribbleSegmentationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


