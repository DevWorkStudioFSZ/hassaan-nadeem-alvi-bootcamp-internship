
Multilingual Voice Assistant for Electricity Outage Reporting

A Flask-based voice assistant that processes Urdu/English voice notes to report electricity outages, check status, and provide localized responses for Rawalpindi streets.
Features

    Multilingual Transcription: Uses Whisper for Urdu/English audio transcription

    Smart Street Matching: Cleans and matches street names with Romanization support

    Intent Detection: Identifies outage reports or status inquiries

    Session Memory: Remembers user's street across interactions

    Realistic Responses: Provides context-aware outage reasons and ETAs

    Web Interface: Flask server with upload endpoint

Requirements

    Python 3.7+

    Flask

    OpenAI Whisper

    rawalpindi_streets.json (street database)

Installation
bash

pip install flask openai-whisper
python final_boy.py

Endpoints

    GET /: Web interface (index.html)

    POST /upload: Upload audio file for processing

Response Format
json

{
  "transcribed_text": "original transcription",
  "detected_language": "UR/EN",
  "intent": "outage/status/unknown",
  "location": {"street": "street_name"},
  "response": "localized_response",
  "memory": "remembered_street",
  "success": true
}

Example Usage
bash

curl -X POST -F "audio=@voice_note.ogg" http://localhost:5000/upload

