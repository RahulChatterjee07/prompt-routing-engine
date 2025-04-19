import json
import os
from routing_engine.rules import classify_document
from routing_engine.prompt_loader import load_prompt_template


def route_document(json_path, prompt_dir="prompts"):
    """
    Route a document based on its Textract-style JSON to the correct prompt.
    """
    with open(json_path, "r") as f:
        textract_data = json.load(f)

    doc_type = classify_document(textract_data)
    print(f"📄 Detected Document Type: {doc_type}")

    if doc_type == "unknown":
        print("⚠️ No matching rules found.")
        return None

    prompt_path = os.path.join(prompt_dir, f"{doc_type}_prompt.yaml")

    if not os.path.exists(prompt_path):
        print(f"⚠️ Prompt template not found: {prompt_path}")
        return None

    prompt_template = load_prompt_template(prompt_path)
    print(f"\n🧠 Loaded Prompt Template for '{doc_type}':\n")
    print(prompt_template)
    return prompt_template


if __name__ == "__main__":
    # Example run
    route_document("data/textract_outputs/form.json")
