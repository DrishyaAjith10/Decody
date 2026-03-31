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