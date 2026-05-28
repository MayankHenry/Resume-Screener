from fastapi import FastAPI

router = FastAPI()
@router.get("/analyze")
def analyze_resume():
    return {"status": "analyze route is working"}