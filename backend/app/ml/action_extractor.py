"""
action_extractor.py

Handles detection of action-item sentences using semantic similarity.

Uses sentence embeddings (MiniLM) to identify sentences that represent tasks.
"""

from sentence_transformers import SentenceTransformer, util
from app.ml.config import REFERENCE_ACTIONS, SIMILARITY_THRESHOLD

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert reference sentences to embeddings
reference_embeddings = model.encode(REFERENCE_ACTIONS, convert_to_tensor=True)


def is_action_item(sentence: str, threshold: float = SIMILARITY_THRESHOLD):
    """
    Check if a sentence is an action item.

    Args:
        sentence (str): Input sentence
        threshold (float): similarity threshold

    Returns:
        bool: True if action item, else False
    """

    sentence_embedding = model.encode(sentence, convert_to_tensor=True)

    # Compute similarity with reference actions
    similarities = util.cos_sim(sentence_embedding, reference_embeddings)

    max_score = similarities.max().item()

    return max_score > SIMILARITY_THRESHOLD


def filter_action_items(sentences):
    """
    Filter only action-item sentences from list.

    Args:
        sentences (list): list of sentence strings

    Returns:
        list: filtered action-item sentences
    """

    action_items = []

    for sentence in sentences:
        if is_action_item(sentence):
            action_items.append(sentence)

    return action_items