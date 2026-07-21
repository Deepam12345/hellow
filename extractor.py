import re

def extract_information(text):

    diagnosis = re.findall(r"Diagnosis:(.*)", text)

    medicines = re.findall(r"Medicine:(.*)", text)

    lab = re.findall(r"[A-Za-z ]+:\s*\d+", text)

    return {
        "diagnosis": diagnosis,
        "medicines": medicines,
        "lab_results": lab
    }