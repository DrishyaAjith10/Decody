"""
Decody API

Provides endpoint to extract action items from transcript.
"""
from pydantic import BaseModel
from fastapi import FastAPI
from app.ml.nlp import process_text, get_sentences
from app.ml.action_extractor import filter_action_items
from app.ml.entity_extractor import extract_details
from fastapi.responses import Response
from app.utils.export import convert_to_csv

app = FastAPI()

class TranscriptRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Decody API is running"}


@app.post("/analyze")
def analyze_transcript(request: TranscriptRequest):
    text = request.text
    """
    Analyze transcript and return structured action items
    """

    doc = process_text(text)
    sentences = get_sentences(doc)
    actions = filter_action_items(sentences)

    structured = []

    for a in actions:
        structured.append(extract_details(a))

    return {
        "action_items": structured
    }

@app.post("/export")
def export(request: TranscriptRequest):
    text = request.text
    doc = process_text(text)
    sentences = get_sentences(doc)
    actions = filter_action_items(sentences)

    structured = []

    for a in actions:
        structured.append(extract_details(a))

    csv_data = convert_to_csv(structured)

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=decody_output.csv"
        }
    )

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")