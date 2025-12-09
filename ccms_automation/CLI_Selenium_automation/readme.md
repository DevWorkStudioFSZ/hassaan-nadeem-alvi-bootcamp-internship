
🔍 PITC Complaint Portal Automation with Voice Transcription
📋 Overview

This Python automation script uses Selenium and Whisper AI to interact with Pakistan's PITC complaint portal, extract electricity bill information, and generate duplicate bills - all controlled by voice commands!
✨ Key Features
🎤 Voice-Activated Client Number Input

    Transcribes audio files containing spoken account numbers

    Supports multiple audio formats (OGG, WAV, MP3)

    Uses OpenAI's Whisper model for accurate transcription

    Automatic text cleaning for input compatibility

🤖 Smart Web Automation

    Automated login and navigation of PITC complaint portal

    Dynamic account selection based on available options

    Multi-window handling for duplicate bill generation

    Intelligent data extraction from HTML tables

📊 Data Processing & Visualization

    Structured extraction of consumer information

    Billing history collection and parsing

    Automatic PDF generation of duplicate bills

    Ready for data visualization integration

🔒 Professional Implementation

    Uses undetected-chromedriver to avoid bot detection

    Explicit waits for reliable element loading

    CDP commands for high-quality PDF export

    Comprehensive error handling

🛠️ Technical Stack
Core Libraries
Library	Purpose	Version
Selenium	Web automation	4.15+
undetected-chromedriver	Stealth browsing	3.5+
Whisper (OpenAI)	Speech-to-text	2023.09+
matplotlib	Future visualization	3.7+
Supporting Libraries

    base64 - PDF encoding/decoding

    time - Delays and timing

    WebDriverWait - Synchronization

📁 File Structure
text

pitc-automation/
├── main.py              # Main automation script
├── numbers.ogg          # Sample voice input
├── duplicate_bill.pdf   # Generated output
└── requirements.txt     # Dependencies

🚀 Installation & Setup
1. Prerequisites
bash

# Install Chrome/Chromium browser
sudo apt-get install chromium-browser  # Ubuntu/Debian
brew install --cask google-chrome     # macOS

2. Install Dependencies
bash

pip install -r requirements.txt

requirements.txt:
text

selenium>=4.15.0
undetected-chromedriver>=3.5.0
openai-whisper>=20230914
matplotlib>=3.7.0

3. Additional Setup
bash

# Install Whisper dependencies
pip install torch torchaudio

# Download Whisper model (optional, auto-downloads)
# whisper download small

🎯 Usage Guide
Basic Execution
python

python main.py

Step-by-Step Process

    Voice Transcription Phase 🎤

        Loads numbers.ogg audio file

        Transcribes spoken account number

        Cleans and formats for input

    Portal Interaction Phase 🌐

        Opens PITC complaint portal

        Enters transcribed account number

        Selects "Contact No" search type

        Executes search

    Account Selection Phase 👤

        Lists all available accounts

        Prompts user for selection

        Loads selected account details

    Data Extraction Phase 📋

        Extracts consumer information

        Captures billing history

        Stores reference number

    Bill Generation Phase 🧾

        Opens duplicate bill window

        Searches by reference number

        Generates PDF duplicate bill

Custom Audio Input
python

# Modify this line to use different audio files
audio_path = "your_audio_file.ogg"  # Supports .wav, .mp3, .ogg

📊 Output Examples
Console Output
text

Detected language: en
Account number: 03123456789

Available Accounts:
0. John Doe - Residential
1. John Doe - Commercial

Select account number: 0

Consumer Information:
Name: John Doe
Address: 123 Main Street
Meter No: ABC123
Reference No: REF-2024-001

Generated Files

    duplicate_bill.pdf - High-quality A4 format bill

    Console output with structured data

    Ready for database integration

⚙️ Configuration Options
Voice Model Selection
python

# Available models: tiny, base, small, medium, large
model = whisper.load_model("small")  # Balance of speed/accuracy

PDF Export Settings
python

pdf_settings = {
    "printBackground": True,
    "paperWidth": 8.27,    # A4 width
    "paperHeight": 11.69,  # A4 height
    "scale": 0.6           # Adjust for content fit
}

Wait Times Adjustment
python

# Adjust based on network speed
time.sleep(5)  # Currently 5 seconds, modify as needed

🛡️ Security & Best Practices
Credential Management
python

# Store sensitive data in environment variables
import os
account_number = os.getenv("PITC_ACCOUNT_NUMBER")

Anti-Detection Features

    Uses undetected-chromedriver

    Human-like delays between actions

    Realistic typing patterns

Error Handling

    Network timeout recovery

    Element not found exceptions

    Window switching validation

🔧 Troubleshooting
Common Issues & Solutions
Issue	Solution
Chrome not installed	Install Chrome/Chromium
Audio file not found	Check path and file extension
Element not clickable	Increase wait time
PDF generation fails	Check CDP command permissions
Debug Mode
python

# Add for debugging
import logging
logging.basicConfig(level=logging.DEBUG)

📈 Performance Tips

    Model Selection

        tiny: Fastest, lower accuracy

        small: Balanced (recommended)

        large: Most accurate, slowest

    Network Optimization

        Use faster internet for portal access

        Consider headless mode for speed

        Cache frequently used data

    Memory Management

        Close unused windows promptly

        Clear temporary variables

        Use context managers for files

🤝 Contributing
Development Setup
bash

# Clone and setup
git clone <repository>
cd pitc-automation
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

Testing
bash

# Run with test audio
python test_audio.py
# Validate output
python validate_output.py

📝 License & Attribution
Dependencies

    OpenAI Whisper: MIT License

    Selenium: Apache 2.0 License

    undetected-chromedriver: GPL v3

Usage Notes

    For educational purposes

    Respect PITC's terms of service

    Use responsibly and ethically

📞 Support & Contact
Getting Help

    Check troubleshooting section

    Review console error messages

    Verify audio file quality

Feature Requests

    Multi-language voice support

    Batch processing mode

    GUI interface

    API integration

⚠️ Disclaimer: This tool is for legitimate automation purposes only. Users are responsible for complying with PITC's terms of service and applicable laws.
