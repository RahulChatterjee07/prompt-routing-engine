# prompt-routing-engine

This project simulates an intelligent routing engine that automatically directs various document types (e.g., forms, reports, assessments, correspondence) to appropriate LLM prompt templates. Inspired by real-world enterprise applications, it uses mocked Textract outputs and a simple rule engine to demonstrate the concept.

## 🔧 Features
- Simulates document type detection using keyword + layout heuristics
- Routes documents to specific LLM prompt templates
- YAML-based prompt templates for flexibility
- Modular, extensible Python code

## 📁 Project Structure
```
prompt-routing-engine/
├── data/
│   ├── sample_documents/          # Simulated text-based input files
│   └── textract_outputs/         # Mock layout + content JSONs
├── prompts/                      # YAML prompt templates
├── routing_engine/               # Rule engine + routing logic
├── notebooks/                    # Jupyter demo
├── README.md                     # You are here
└── requirements.txt              # Python dependencies
```

## ▶️ Example Workflow
1. Input a mock document (form, report, etc.)
2. Load corresponding Textract-like layout + content data
3. Run rule engine to detect document type
4. Load the correct LLM prompt template
5. (Optional) Print or send the filled prompt to an LLM

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🚀 Run Demo (Jupyter Notebook)
```bash
cd notebooks
jupyter notebook demo.ipynb
```

## 🧠 Future Extensions
- Integrate real Textract APIs
- Add Streamlit UI
- Introduce fuzzy layout matching

---

Made with ❤️ by Rahul Chatterjee
