Whisper Transcription & Entity Extraction

**PLEASE USE YOUR OWN AUDIO FILE**
This Python script uses OpenAI Whisper for speech-to-text transcription and spaCy for named entity recognition (NER) to extract service-related terms like "water bill" from an Urdu audio file.
Features

    Transcribes Urdu audio using Whisper (small model)

    Uses spaCy's matcher to extract entities (bill, invoice, statement)

    Extracts service types (e.g., "water") from transcribed text

Requirements

    Python 3.7+

    OpenAI Whisper

    spaCy with en_core_web_sm model

Installation
bash

pip install openai-whisper spacy
python -m spacy download en_core_web_sm

Usage

    Place your audio file in audio/urdu2.ogg

    Run:

bash

python whisper_test.py

Output

    Prints the transcribed text

    Extracts and prints service entities (e.g., {'service_type': 'water'})
