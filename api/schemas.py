
from pydantic import BaseModel, Field
from typing import List


class PredictionRequest(BaseModel):
    text: str = Field(
        ...,
        description="Community problem to analyze and generate a campaign for"
    )


class PredictionResponse(BaseModel):
    input_text: str
    predicted_sdgs: List[int]
    message: str


class CampaignResponse(BaseModel):
    input_text: str
    predicted_sdgs: List[int]
    campaign: dict
    message: str
