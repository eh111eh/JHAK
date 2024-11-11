import requests

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = '4a1e91d71c07a607b7634c37afd12fbe85e28d34'

# URL of the audio file or local file path
AUDIO_FILE_PATH = 'test.mp3'

# Deepgram API endpoint
url = "https://api.deepgram.com/v1/listen"

# Prepare headers
headers = {'Authorization': f'Token {DEEPGRAM_API_KEY}', 'Content-Type': 'audio/wav' }

# Open the audio file in binary mode
with open(AUDIO_FILE_PATH, 'rb') as audio_file:
    response = requests.post(url, headers=headers, data=audio_file)

# Check for success and print the response
if response.status_code == 200:
    transcription_result = response.json()
    print("Transcription:", transcription_result.get('results', {}).get('channels', [])[0].get('alternatives', [])[0].get('transcript'))
else:
    print(f"Error: {response.status_code} - {response.text}")