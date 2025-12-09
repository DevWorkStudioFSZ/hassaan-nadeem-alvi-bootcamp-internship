
📄 PITC Duplicate Bill Generator

A modern, voice-enabled web application for generating duplicate bills from the Pakistan Telecommunication Company (PITC) portal with automated data extraction and visualization capabilities.
✨ Features
🎯 Core Functionality

    Voice Recognition: Speak phone numbers instead of typing

    Automated Scraping: Extracts consumer information and billing history

    PDF Generation: Creates downloadable duplicate bills

    Session Management: Maintains active scraping sessions

    Multi-Account Support: Handles multiple accounts per contact number

📊 Data Visualization

    Interactive Charts: Generates billing trend graphs using Matplotlib

    Monthly Analysis: Visualizes consumption patterns over time

    Color-coded UI: Modern gradient design with smooth transitions

🔒 Security & Reliability

    Anti-detection: Bypasses bot protection using Playwright with custom headers

    Error Handling: Comprehensive exception management

    Session Expiry: Automatic cleanup of inactive sessions

    Async Operations: Non-blocking I/O for better performance

🏗️ Architecture
Backend Stack

    Framework: Quart (async Flask-compatible)

    Server: Hypercorn (ASGI server)

    Scraping: Playwright with Chromium

    Visualization: Matplotlib

    Data Format: JSON API responses

Frontend Stack

    UI Framework: Bootstrap 5

    Interactivity: Vanilla JavaScript

    Voice API: Web Speech API

    Responsive Design: Mobile-friendly interface

📁 Project Structure
text

pitc-bill-generator/
├── app.py                 # Main Quart application
├── scraper.py            # Async web scraping logic
├── requirements.txt      # Python dependencies
├── readme.md            # This file
├── static/
│   ├── css/
│   │   └── style.css    # Custom styles
│   └── js/
│       └── main.js      # Frontend logic
├── templates/
│   └── index.html       # Main HTML template
└── bills/               # Generated PDF storage

🚀 Installation
Prerequisites

    Python 3.8+

    Node.js (for Playwright browser installation)

    1GB+ RAM for browser automation

Step 1: Clone and Setup
bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

Step 2: Configure Application
bash

# Create necessary directories
mkdir -p static/{css,js} templates bills

# Set up static files (copy provided CSS/JS)
# (Files should be placed in respective directories)

Step 3: Run Application
bash

# Development mode
python app.py

# Production mode (recommended)
hypercorn app:app --bind 0.0.0.0:5000

The application will be available at http://localhost:5000
📋 Usage Guide
Step 1: Phone Number Input

    Enter 10+ digit contact number

    Or click "Speak" to use voice input

    Click "Search" to begin

Step 2: Account Selection

    View all accounts associated with the number

    Click on desired account card

    System fetches billing data automatically

Step 3: Data Review & Download

    Review consumer information

    View billing history and visualization

    Click "Generate PDF" to download duplicate bill

🔧 Configuration
Environment Variables

Add to .env file:
env

SECRET_KEY=your_secret_key_here
DEBUG=False
HOST=0.0.0.0
PORT=5000

Browser Settings (in scraper.py)

    headless=True - Run browser in background

    Viewport: 1920x1080

    Custom user agent to avoid detection

    Disabled sandbox for container compatibility

🛠️ Technical Details
Session Management

    Each search creates unique session ID

    Sessions stored in memory dictionary

    Automatic cleanup on bill generation

    Timeout handling for long operations

Scraping Logic

    Navigates to PITC complaint portal

    Fills contact number and selects search type

    Waits for account list to load

    Extracts account options (skipping "Select" placeholder)

    Retrieves consumer information from table

    Clicks billing details tab

    Parses billing history data

Graph Generation

    Extracts month/year from billing data

    Converts to standardized date format

    Sorts chronologically

    Creates line chart with fill effect

    Returns base64-encoded PNG

📊 API Endpoints
Endpoint	Method	Description	Request Body
/	GET	Main page	-
/search	POST	Start session	{"contact_no": "923001234567"}
/select_account	POST	Fetch account data	{"session_id": "id", "account_value": "value"}
/generate_bill	POST	Generate PDF	{"session_id": "id", "reference_no": "ref"}
/download/<filename>	GET	Download PDF	-
🧪 Testing
Manual Testing
bash

# Test voice input
- Click "Speak" button and say phone number
- Verify number appears in input field

# Test search functionality
- Enter valid PITC contact number
- Verify accounts appear

# Test bill generation
- Select account
- Verify data loads
- Click generate and download PDF

Automated Testing (Future)
bash

# Install test dependencies
pip install pytest pytest-asyncio pytest-playwright

# Run tests
pytest tests/

⚠️ Limitations & Considerations
Legal & Ethical

    Authorized Use Only: Ensure you have permission to access the data

    Rate Limiting: Implement delays to avoid overwhelming PITC servers

    Data Privacy: Generated bills contain sensitive information

    Terms of Service: Check PITC's terms regarding automated access

Technical Limitations

    Requires stable internet connection

    PITC website changes may break scraping logic

    Voice recognition only works in supported browsers

    PDF generation depends on PITC's duplicate bill functionality

🔮 Future Enhancements
Planned Features

    User authentication system

    Database integration for history tracking

    Scheduled bill generation

    Email notifications with attachments

    Mobile app version

Technical Improvements

    Docker containerization

    Redis session storage

    Proxy rotation for scraping

    Headless browser pooling

    Performance monitoring dashboard

🤝 Contributing

    Fork the repository

    Create feature branch (git checkout -b feature/amazing)

    Commit changes (git commit -m 'Add amazing feature')

    Push to branch (git push origin feature/amazing)

    Open Pull Request

Development Guidelines

    Follow PEP 8 for Python code

    Use async/await patterns consistently

    Add docstrings for new functions

    Update requirements.txt for new dependencies

    Test changes thoroughly before submitting

📄 License

This project is for educational purposes only. Use responsibly and in compliance with PITC's terms of service and applicable laws.
🆘 Support
Common Issues

    Browser doesn't launch
    bash

# Reinstall Playwright
playwright install --force chromium

    Session timeout errors

        Increase timeout values in scraper.py

        Check network connectivity to PITC

    Voice recognition not working

        Ensure HTTPS is used (required for Speech API)

        Check browser permissions for microphone

    PDF generation fails

        Verify reference number format

        Check PITC bill availability for selected account

Debug Mode

Enable debug logging:
python

# In app.py
app.config['DEBUG'] = True

📞 Contact

For technical support or questions:

    Open an issue on GitHub repository

    Ensure to include error logs and steps to reproduce

Disclaimer: This tool automates access to PITC's portal. Users are responsible for ensuring their usage complies with PITC's terms of service and applicable laws. The developers assume no liability for misuse or damages resulting from this software.
📦 Dependencies

Create requirements.txt:
txt

quart==0.18.0
hypercorn==0.14.3
playwright==1.35.0
matplotlib==3.7.2
python-dotenv==1.0.0

Install with:
bash

pip install -r requirements.txt

Additional system dependencies (Ubuntu/Debian):
bash

sudo apt-get install -y libpangocairo-1.0-0 libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libcups2 libxss1 libxrandr2 libasound2 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0

