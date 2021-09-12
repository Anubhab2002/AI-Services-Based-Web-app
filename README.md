# AI-Services-Based-Web-app
A simple web application using AI based cognitive services for translation, speech-to-text, text-to-speech

# Brief about the project
1. The application is written in flask, a micro web framework written in python.
2. It does the following jobs:
    - translation of text from any recognised language to the language options available on the drop down menu using MS Azure Translator API. Link: https://azure.microsoft.com/en-in/services/cognitive-services/translator/
    - converting text to speech using IBM Watson text-to-speech API. Link: https://cloud.ibm.com/catalog/services/text-to-speech/
    - converting speech (make sure you allow the browser to use your microphone) to the closest possible text using Javascript SpeechRecognition interface of the Web Speech API
    
# Before you start
- I urge you to use a Virtual Environment while working on a flask project in order to avoid controvercies between versions of various dependencies used in a project. To know how to, follow https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ 
- All the required dependencies are listed in requirements.text file. In order to install them run the command ```pip install -r requirements.txt```
- Now create a ```.env``` file with the following details:
```
API_KEY=<api key from MS Azure Translator>
ENDPOINT=https://api.cognitive.microsofttranslator.com/
LOCATION=<location from MS Azure Translator>

TTS_API_KEY=<api key from IBM Watson text-to-speech service>
TTS_URL=<url from IBM Watson text-to-speech service>
```
You need to create an account in MS Azure as well as IBM cloud services to avail the required services.
You can use the services for free for a limited amount of time and for a limited amount of requests.

### Now you are all set to modify the project according to your needs.
### Also, don't forget to give a star.
