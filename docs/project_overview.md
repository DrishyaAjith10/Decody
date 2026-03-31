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


🔧 Step 7: Semantic Search Integration
Implemented MiniLM-based semantic retrieval
Converted transcript sentences into vector embeddings
Enabled query-based retrieval of relevant sentences
Used cosine similarity to rank importance

🧠 Step 8: Query-Based Insight Extraction
Added /search endpoint
Accepts:
transcript text
user query (e.g., "action items", "decisions")
Retrieves only relevant sentences before processing
Improves efficiency and accuracy

⚖️ Step 9: Decision Extraction
Implemented rule-based decision detection
Identifies sentences containing:
"agreed", "decided", "approved", etc.
Cleans and normalizes decision statements
Outputs structured decisions separately from tasks

🔀 Step 10: Multi-Output System
System now returns:
action_items
decisions
Avoids forcing all sentences into one category
Handles empty cases gracefully

🎨 Step 11: Frontend Integration
Built UI using HTML, CSS, and JavaScript
Added:
transcript input
query input
structured results display
Separated:
Action Items (table)
Decisions (list)


## Final Pipeline

Transcript  
→ Cleaning  
→ Sentence Splitting (spaCy)  
→ Embedding (MiniLM)  
→ Semantic Retrieval (Query-based)  
→ Action Extraction (spaCy + rules)  
→ Decision Extraction (rule-based)  
→ Structured Output  
→ API Response / CSV Export  
→ UI Display

## Result

The system successfully:

- Identifies action items with:
  - responsible person
  - task
  - deadline

- Detects and extracts key decisions from discussions

- Uses semantic search to retrieve relevant transcript segments

- Supports query-based interaction for dynamic insights

- Provides output in:
  - structured JSON
  - downloadable CSV
  - user-friendly UI