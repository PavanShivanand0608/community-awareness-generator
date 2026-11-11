
from fastapi import FastAPI, HTTPException

from api.schemas import PredictionRequest, CampaignResponse
from src.predictor import predict_sdgs
from src.campaign_generator import generate_campaign


app = FastAPI(
    title="AI-Assisted Community Awareness Campaign Generator",
    description=(
        "An AI application that identifies relevant SDGs "
        "and generates community awareness campaigns."
    ),
    version="2.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Community Awareness Campaign Generator is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/generate-campaign", response_model=CampaignResponse)
def create_campaign(request: PredictionRequest):

    try:
        # Step 1: Predict relevant SDG using the trained ML model
        predicted_labels = predict_sdgs(request.text)

        if not predicted_labels:
            raise HTTPException(
                status_code=422,
                detail="The model could not identify a relevant SDG."
            )

        # Step 2: Use the first predicted SDG for campaign generation
        selected_sdg = predicted_labels[0]

        # Step 3: Generate campaign using OpenRouter AI
        campaign = generate_campaign(
            problem=request.text,
            sdg_id=selected_sdg
        )

        # Step 4: Return complete result
        return CampaignResponse(
            input_text=request.text,
            predicted_sdgs=predicted_labels,
            campaign=campaign,
            message="SDG prediction and campaign generation completed successfully."
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"Campaign generation service failed: {str(error)}"
        )
