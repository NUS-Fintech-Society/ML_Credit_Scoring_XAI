from fastapi import APIRouter, Path
from app.models import PredictionRequest
from typing import Annotated
from app.services.model_selector import predict_for_model
from app.services.model_selector import explain_for_model


router = APIRouter()

@router.post("/predict/{model}")
async def predict(
    model: Annotated[str, Path(title="The model to use for the prediction")],
    data: PredictionRequest
):
    return {
        "prediction": predict_for_model(model, data)
    }

@router.post("/explain/{model}")
async def predict(
    model: Annotated[str, Path(title="The model to use for the prediction")],
    data: PredictionRequest
):
    print(explain_for_model(model, data))
    return {
    }
