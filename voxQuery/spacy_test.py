import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Pattern: optional adjectives + noun + 'bill'
# Add more patterns for different bill types
patterns = [
    [{"POS": "NOUN"}, {"LOWER": "bill"}],      # water bill
    [{"POS": "NOUN"}, {"LOWER": "invoice"}],   # water invoice
    [{"POS": "NOUN"}, {"LOWER": "statement"}]  # water statement
]
for name, pattern in zip(["BILL", "INVOICE", "STATEMENT"], patterns):
    matcher.add(name, [pattern])


text = "Hi, can you send me my electricity invoice?"
doc = nlp(text)

entities = {}
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    entities["service_type"] = span[0].text  # take the first word (the service)

print(entities)
# Output: {'service_type': 'water'}
