# Decody

Decody is an intelligent system designed to analyze meeting transcripts and extract meaningful insights such as action items and decisions.

## 🚀 Problem
Meeting transcripts are long and unstructured, making it difficult to quickly identify key decisions and assigned tasks.

## 💡 Solution
Decody processes transcripts using NLP techniques to:
- Identify action items
- Extract responsible person (Who)
- Extract task description (What)
- Extract deadlines (By When)

## 🧠 Current Features
- Sentence segmentation
- Named Entity Recognition (NER) using spaCy
- Structured extraction of PERSON and DATE entities

## 🏗️ Tech Stack
- Python
- spaCy (NLP)
- Sentence Transformers (for semantic understanding - upcoming)
- FastAPI (planned)
- React (planned)
- Supabase (planned)

## 🔄 Pipeline (Current)
Transcript → NLP Processing → Sentences + Entities

## 🔮 Future Scope
- Action item detection using semantic models
- Decision extraction
- Question-answering over transcripts
- Export to CSV/PDF



## ✅ Current Progress

Decody can now:
- Identify action items from meeting transcripts
- Use semantic similarity (MiniLM)
- Extract meaningful sentences from unstructured text

### Example Output

Input:
John will prepare the project report by Friday.

Output:
✔ Action Item Detected

## 🚀 Features Implemented

- Action Item Detection using semantic similarity (MiniLM)
- Entity Extraction (Who, What, When)
- FastAPI backend for processing
- CSV export functionality

## 🔗 API Endpoints

### POST /analyze
Returns structured action items

### POST /export
Downloads results as CSV file

## 📊 Example Output

| Who  | What                        | When       |
|------|-----------------------------|------------|
| John | prepare project report      | Friday     |
| Sarah| finalize UI design          | next week  |