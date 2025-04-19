import json

# Define keyword and layout-based rules
DOCUMENT_RULES = {
    "form": {
        "keywords": ["Form", "Medical History Intake", "Patient Name"],
        "layout": ["KEY_VALUE_SET", "TABLE"]
    },
    "report": {
        "keywords": ["Clinical Evaluation", "symptoms", "physical exam", "imaging"],
        "layout": []
    },
    "assessment": {
        "keywords": ["Functional Capacity Assessment", "Checklist"],
        "layout": ["TABLE"]
    },
    "correspondence": {
        "keywords": ["Dear", "Regards", "To Whom It May Concern"],
        "layout": []
    }
}


def extract_text_and_layout(textract_json):
    """
    Given a Textract-style dictionary, extract all text lines and block types.
    """
    text_lines = []
    layouts = []

    for block in textract_json.get("Blocks", []):
        if block["BlockType"] == "LINE" and "Text" in block:
            text_lines.append(block["Text"])
        elif block["BlockType"] in {"KEY_VALUE_SET", "TABLE", "FORM"}:
            layouts.append(block["BlockType"])

    return text_lines, layouts


def classify_document(textract_json):
    """
    Classify the document type based on content and layout rules.
    """
    text_lines, layouts = extract_text_and_layout(textract_json)
    text_blob = " ".join(text_lines).lower()

    for doc_type, rule in DOCUMENT_RULES.items():
        # Check if any of the keywords appear in text
        keyword_match = any(keyword.lower() in text_blob for keyword in rule["keywords"])
        layout_match = all(layout in layouts for layout in rule["layout"])

        if keyword_match and (not rule["layout"] or layout_match):
            return doc_type

    return "unknown"
