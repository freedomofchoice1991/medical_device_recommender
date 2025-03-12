from fastapi import APIRouter
from .services import get_grouped_by_classification, find_similar_devices

router = APIRouter()

@router.get("/grouped")
def get_grouped_devices():
    """Returns medical devices grouped by classification code."""
    data = get_grouped_by_classification()
    return {"grouped_devices": data}

@router.get("/recommend/{product_code}")
def recommend_alternatives(product_code: str):
    """Finds alternative devices based on classification criteria."""
    result = find_similar_devices(product_code)
    return result
