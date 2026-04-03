# Decody — Meeting Intelligence System

Decody is a lightweight Meeting Intelligence System that processes meeting transcripts and extracts meaningful insights such as **Action Items** and **Decisions** using a hybrid NLP approach.

---

## 🚀 Features

* Extracts **Action Items** (Who, What, By When)
* Identifies **Decisions** from discussions
* Semantic **Search using MiniLM embeddings**
* Handles **messy transcripts** (timestamps, fillers, speaker tags)
* Export results as **CSV**
* Query-based retrieval (e.g., “action items”, “decisions”)

---

## 🧠 System Architecture

Decody follows a hybrid NLP pipeline:

```
Transcript
   ↓
Cleaning (remove noise, timestamps)
   ↓
Sentence Segmentation (spaCy)
   ↓
Embedding (MiniLM)
   ↓
Semantic Retrieval
   ↓
Extraction (Rule-based NLP)
   ↓
Structured Output
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **NLP:** spaCy
* **Embeddings:** Sentence Transformers (MiniLM)
* **Frontend:** HTML + JavaScript
* **Export:** CSV

---

## 🔍 How It Works

### 1. Cleaning

Removes:

* timestamps
* speaker labels
* filler words

---

### 2. Retrieval (MiniLM)

* Converts sentences into embeddings
* Matches query with relevant sentences using cosine similarity

---

### 3. Extraction

#### Action Items

* Detects tasks using semantic similarity + rules
* Extracts:

  * **Who**
  * **What**
  * **When**

#### Decisions

* Identifies sentences with keywords like:

  * "agreed"
  * "decided"
  * "approved"

---

### 4. Output

Returns:

```json
{
  "action_items": [...],
  "decisions": [...]
}
```

---

## 🧪 Example

### Input:

```
John will prepare the report by Friday.
The team agreed to revise pricing.
```

### Output:

```json
{
  "action_items": [
    {
      "who": "John",
      "what": "prepare the report",
      "when": "Friday"
    }
  ],
  "decisions": [
    {
      "decision": "The team agreed to revise pricing."
    }
  ]
}
```

---

## 📡 API Endpoints

### `/analyze`

Extracts action items from transcript

### `/search`

Query-based retrieval + extraction

### `/export`

Exports results as CSV


---

## 🚀 Future Improvements

* Add conversational chatbot (RAG)
* Improve decision detection using ML models
* Multi-file transcript support
* UI enhancements and visualization

---

## 👩‍💻 Author

Drishya Ajith

