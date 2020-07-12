# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 01:01:31 2020

@author: Bibhupad
"""
#you will need the following library 
!pip install ibm_watson wget

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/ed114f51-86c5-4e0a-ad6c-af28995b283b"

iam_apikey_s2t = "4d5hpNR2AXU1vu80Nu9e_eYNg-drAuvHor0tViuWHdFa"

#wget retrieves content from web server.
!wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3

#We have the path of the wav file we would like to convert to text
filename='PolynomialRegressionandPipelines.mp3'

#We create the file object wav with the wav file using open ; we set the mode to "rb" , this is similar to read mode, but #it ensures the file is in binary mode.We use the method recognize to return the recognized text. The parameter audio is #the file object wav, the parameter content_type is the format of the audio file.

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

#The attribute result contains a dictionary that includes the translation:
response.result

from pandas.io.json import json_normalize
json_normalize(response.result['results'],"alternatives")

response

#recognized_text=response.result['results'][0]["alternatives"][0]["transcript"] --> 1st line of the result
#recognized_text=response.result['results'][1]["alternatives"][0]["transcript"] --> 2nd line of the result
recognized_text=response.result['results'][2]["alternatives"][0]["transcript"]
type(recognized_text)
recognized_text


#Language Translator

from ibm_watson import LanguageTranslatorV3

url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/48d49df0-8ddc-4233-8b79-d5fe586760e6'

apikey_lt='846fRd4_bBJmuHmK7pzcSvc08WQg1LakmMAqY0RY07Wh'

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas.io.json import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

#We can use the method translate this will translate the text. The parameter text is the text. Model_id is the type of #model we would like to use use we use list the the langwich . In this case, we set it to 'en-es' or English to Spanish. #We get a Detailed Response object translation_response

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation 

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

French_translation['translations'][0]['translation']
