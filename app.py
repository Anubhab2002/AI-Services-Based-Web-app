from flask import Flask, redirect, url_for, request, render_template, session
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests, os, uuid, json
# import pyaudio
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def translate_action():
    #reading data from form
    text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.environ['API_KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    #creating the translate path
    url = f'{endpoint}/translate?api-version=3.0&to={target_language}'

    # Request Header object
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Request Body object
    body = [{
        'text': text
    }]

    # the post request
    translator_request = requests.post(url, headers=headers, json=body)
    # the response object
    translator_response = translator_request.json()
    print(translator_response)
    # extract the translated text
    translated_text = translator_response[0]['translations'][0]['text']
    # rendering the response
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=text,
        target_language=target_language
    )

@app.route('/tts', methods=['GET'])
def tts():
    return render_template('tts.html')

@app.route('/tts', methods=['POST'])
def tts_action():
    #reading data from form
    text = request.form['text']

    # Load the values from .env
    key = os.environ['TTS_API_KEY']
    url = os.environ['TTS_URL']

    #creating the required text to speech object
    auth = IAMAuthenticator(key)
    tts = TextToSpeechV1(authenticator=auth)
    #setting service url
    tts.set_service_url(url)

    # reading the response file and writing into a .mp3 file in static folder
    with open('./static/audio.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
        audio_file.write(res.content)

    # rendering the response
    return render_template(
        'tts_results.html',
        original_text=text,
    )

@app.route('/stt', methods=['GET'])
def stt():
    return render_template('stt.html')

@app.route('/stt', methods=['POST'])
def stt_action():
    #reading data from form
    text = request.form['text']

    # rendering the response
    return render_template(
        'stt_results.html',
        text_generated=text,
    )