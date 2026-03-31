# Decody - Meeting Transcript Analyzer

## Step 1: NLP Setup
- Used spaCy for:
  - Sentence segmentation
  - Named Entity Recognition (PERSON, DATE)

## Step 2: Action Item Detection
- Used Sentence Transformers (MiniLM)
- Converted sentences into embeddings
- Compared with predefined reference action patterns
- Used cosine similarity to filter action items

## Result (Current)
System can:
- Read transcript
- Split into sentences
- Identify action-item sentences

Example:

Input:
John will prepare the project report by Friday.

Output:
Identified as Action Item

## Pipeline (Current)

Transcript  
→ Sentence Splitting (spaCy)  
→ Semantic Filtering (MiniLM)  
→ Action Items  

## Observations
- Threshold tuning affects detection accuracy
- Reference patterns improve semantic understanding

## Next Step
- Extract structured data:
  - Who (PERSON)
  - What (Task)
  - When (DATE)


## Step 3: API Development

- Built FastAPI backend
- Created /analyze endpoint
- Returns structured action items in JSON format

## Result
System is now accessible via API and ready for frontend integration


## Step 4: Structured Extraction

- Extracted:
  - Who (PERSON)
  - What (Task description)
  - When (DATE)
- Used spaCy for entity recognition
- Applied rule-based cleaning for task extraction

## Step 5: API Development

- Built FastAPI backend
- Created endpoints:
  - `/analyze` → returns structured JSON
  - `/export` → downloads CSV file

## Step 6: Export Feature

- Implemented CSV export functionality
- Converted structured data into tabular format
- Enabled file download via API

## Final Pipeline

Transcript  
→ Sentence Splitting (spaCy)  
→ Action Detection (MiniLM)  
→ Entity Extraction (spaCy)  
→ Structured Output  
→ API Response / CSV Export

## Result

The system successfully:
- Identifies action items
- Extracts responsible person, task, and deadline
- Provides output in both JSON and downloadable formats