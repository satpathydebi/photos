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
    elif "optum" in text and "vm" in text and "details" in text:
        # Assume token is last word (you can enhance this with regex if needed)
        token = text.split()[-1]
        return ("optum_vm_details", token)
    return ("unknown", None)
