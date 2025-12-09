import os
import json
import whisper
import re
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

print("Loading Whisper model...")
model = whisper.load_model("small")

# ===================== LOAD & CLEAN STREETS =====================
with open("rawalpindi_streets.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Filter out garbage: only keep streets that look real
VALID_STREETS = []
for item in raw_data:
    name = item["name"].strip()
    # Skip junk: too short OR single letter OR just "Block" etc.
    if (len(name) < 4 and " " not in name) or name.lower() in ["a","b","c","d","e","f","g","block","lane","road","street"]:
        continue
    if any(char.isdigit() and len(name) < 6 for char in name):  # Skip "Lane 7" alone
        continue
    VALID_STREETS.append(name)

print(f"Cleaned: {len(VALID_STREETS)} real streets loaded (garbage like A/B/C removed)")

# Romanization map
ROMAN_MAP = {
    "ہارلی":"harley","سکس":"sixth","ایڈیالہ":"adiala","سٹلائٹ":"satellite",
    "سدر":"saddar","صدر":"saddar","چکلالہ":"chaklala","بنک روڈ":"bank road",
    "کمرسیل":"commercial","چوک":"chowk","مارکیٹ":"market","روڈ":"road"
}

def romanize(text):
    t = text.lower()
    for u, e in ROMAN_MAP.items():
        t = t.replace(u, e)
    return t

# Build smart lookup
STREET_LOOKUP = {}
for name in VALID_STREETS:
    STREET_LOOKUP[name.lower()] = name
    roman = romanize(name)
    if roman != name.lower():
        STREET_LOOKUP[roman] = name

# ===================== OUTAGE REASONS =====================
OUTAGE_REASONS = [
    "فیڈر پر فنی خرابی کی وجہ سے",
    "ٹرانسفارمر اوورلوڈ ہو گیا ہے",
    "مین لائن میں فالٹ آ گیا ہے",
    "پلانڈ لوڈشیڈنگ جاری ہے",
    "گرڈ اسٹیشن سے سپلائی بند ہے",
    "تار ٹوٹ گئی ہے",
    "سب سٹیشن میں مرمت چل رہی ہے",
    "برقی کیبل خراب ہو گئی ہے"
]

OUTAGE_KEYWORDS = ["بجلی نہیں","لوڈشیڈنگ","بجلی گئی","اندھیرا","no electricity","power cut","بجلی غائب","لائٹ نہیں","no light","bijli nahi"]
STATUS_KEYWORDS = ["سٹیٹس","کب آئے گی","status","when","کتنے بجے"]

user_sessions = {}

def transcribe_audio(path):
    r = model.transcribe(path, language="en")
    return {"text": r["text"].strip(), "lang": r.get("language", "ur").upper()}

def detect_intent(text):
    t = text.lower()
    if any(k in t for k in OUTAGE_KEYWORDS): return "outage"
    if any(k in t for k in STATUS_KEYWORDS): return "status"
    return "unknown"

def extract_street(text):
    t = romanize(text).lower()
    # Try full word match first
    for key in STREET_LOOKUP:
        if key in t or key in text.lower():
            # Making it's not just a letter inside a word
            if len(key) >= 4 or " " in key:
                return STREET_LOOKUP[key]
    return None

def generate_response(intent, street, text, sid):
    mem = user_sessions.get(sid, {})

    if intent == "outage" and street:
        user_sessions[sid] = {"street": street}
        reason = random.choice(OUTAGE_REASONS)
        return f"{street} میں {reason} بجلی بند ہے۔\nتقریباً 3-4 گھنٹے لگ سکتے ہیں، صبر کریں"

    if intent == "status" and (street or mem.get("street")):
        final = street or mem["street"]
        user_sessions[sid] = {"street": final}
        return f"{final}آپ کی بجلی تقریباً 15 منٹ میں واپس آجائے گی۔"

    if street:
        user_sessions[sid] = {"street": street}
        return f"{street} سے بول رہے ہیں؟ بجلی نہیں ہے یا سٹیٹس پوچھنا ہے؟"

    if mem.get("street"):
        if intent == "outage":
            reason = random.choice(OUTAGE_REASONS)
            return f"{mem['street']} میں {reason} بجلی بند ہے"
        if intent == "status":
            return f"{mem['street']} میں بجلی آ چکی ہے"

    return "معاف کیجیے! کون سی سٹریٹ یا محلہ ہے؟\nمثال: ہارلی اسٹریٹ، سکس روڈ، صدر"

def process_voice_note(path, sid):
    trans = transcribe_audio(path)
    text = trans["text"]
    intent = detect_intent(text)
    street = extract_street(text)
    response = generate_response(intent, street, text, sid)

    memory_street = user_sessions.get(sid, {}).get("street", "None")

    return {
        "transcribed_text": text,
        "detected_language": trans["lang"],
        "intent": intent,
        "location": {"street": street or "Not found"},
        "response": response,
        "memory": memory_street,
        "success": True
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio"}), 400
    file = request.files["audio"]
    ext = file.filename.rsplit(".", 1)[-1] if "." in file.filename else "webm"
    path = f"temp_audio.{ext}"
    file.save(path)
    sid = request.remote_addr

    try:
        result = process_voice_note(path, sid)
        os.remove(path)
        return jsonify(result)
    except Exception as e:
        if os.path.exists(path): os.remove(path)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Urdu + English + Memory + Real reasons")
    print("http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), threaded=True)
