from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from agents.recommendation_agent import get_recommendation
from agents.chat_agent import get_chat_response  # New import
from models.schemas import ProductQuery, ProductInfo, EcoScore, RecyclingOptions, Recommendation, ChatMessage
from utils.search import search_product_url  # New import for auto-search

app = FastAPI(title="Eco-Conscious Shopping Assistant")

# CORS for frontend (even though frontend is not implemented)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/recommendation", response_model=Recommendation)
async def recommendation_endpoint(product_info: ProductInfo, eco_score: EcoScore, recycling_options: RecyclingOptions):
    try:
        return await get_recommendation(product_info, eco_score, recycling_options)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# New conversational endpoint
@app.post("/chat", response_model=dict)
async def chat_endpoint(chat: ChatMessage):
    try:
        return await get_chat_response(chat.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))