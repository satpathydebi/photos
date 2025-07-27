# nlp_parser.py

import spacy

nlp = spacy.load("en_core_web_sm")

def parse_command(text):
    doc = nlp(text.lower())
    if "list" in text and "vm" in text:
        return ("list_vms", None)
    elif "power on" in text or "start" in text:
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PRODUCT":
                return ("power_on", ent.text)
    elif "power off" in text or "shutdown" in text:
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PRODUCT":
                return ("power_off", ent.text)
    return ("unknown", None)