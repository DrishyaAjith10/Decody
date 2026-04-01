"""
Decody API
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.utils.cleaner import clean_transcript
from app.utils.parser import parse_vtt

from app.ml.nlp import split_by_speaker
from app.ml.entity_extractor import extract_details
from app.ml.decision_extractor import extract_decision
from app.ml.retriever import build_embeddings, retrieve

from app.utils.export import convert_to_csv


app = FastAPI()


# ------------------------
# REQUEST MODELS
# ------------------------

class TranscriptRequest(BaseModel):
    text: str


class SearchRequest(BaseModel):
    text: str
    query: str


# ------------------------
# ROUTES
# ------------------------

@app.get("/")
def serve_home():
    return FileResponse("app/static/index.html")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    if file.filename.endswith(".vtt"):
        text = parse_vtt(text)

    text = clean_transcript(text)

    return {
        "filename": file.filename,
        "text": text
    }


@app.post("/search")
def search(request: SearchRequest):
    text = clean_transcript(request.text)
    query = request.query.lower()

    sentences = split_by_speaker(text)

    if not sentences:
        return {"action_items": [], "decisions": []}

    results = [{"sentence": s} for s in sentences]

    action_items = []
    decisions = []

    # 🔥 FIX: deduplicate at source
    unique_sentences = list({item["sentence"] for item in results})

    for sentence in unique_sentences:

        extracted = extract_details(sentence)
        if extracted and extracted.get("who"):
            action_items.append(extracted)


        decision_data = extract_decision(sentence)

        if decision_data:
            decisions.append(decision_data)

    return {
        "action_items": action_items,
        "decisions": decisions
    }


@app.post("/export")
def export(request: TranscriptRequest):
    text = clean_transcript(request.text)

    sentences = split_by_speaker(text)

    structured = [
        extract_details(s)
        for s in sentences
        if extract_details(s).get("who")
    ]

    csv_data = convert_to_csv(structured)

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=decody_output.csv"
        }
    )


# ------------------------
# STATIC FILES
# ------------------------

app.mount("/static", StaticFiles(directory="app/static"), name="static")