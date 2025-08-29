from fastapi import FastAPI, Query
from typing import List

# (later we'll import our recommender model pipeline)
# from src.news_recommender.pipeline import RecommenderPipeline

app = FastAPI(
    title="News Recommender API",
    description="A personalized news recommendation system",
    version="0.1.0",
)

# Initialize model/pipeline here (placeholder for now)
# recommender = RecommenderPipeline()


@app.get("/")
def read_root():
    """Root endpoint for health check"""
    return {"message": "News Recommender API is running!"}


@app.get("/recommend")
def recommend_articles(user_id: int = Query(None), text: str = Query(None)) -> List[str]:
    """
    Get recommended articles.
    - If `user_id` is provided → recommend based on past interactions
    - If `text` is provided → recommend similar articles
    """
    if user_id:
        # Example dummy response (replace with recommender.get_by_user(user_id))
        return [f"Recommended article A for user {user_id}", f"Article B for user {user_id}"]

    if text:
        # Example dummy response (replace with recommender.get_by_text(text))
        return [f"Similar to '{text}': Article X", f"Similar to '{text}': Article Y"]

    return ["Please provide either user_id or text to get recommendations."]
