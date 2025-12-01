from fastapi import FastAPI

app = FastAPI(
    title="Shoof Smart API",
    description="أول نظام خدمة ذكي في المنطقة — منصة شوف الذكية",
    version="1.0.0"
)

providers = [
    {
        "company": "شركة الديكور الخليجية",
        "service": "ديكور",
        "rating": 4.8,
        "trust_index": 92,
        "phone": "+974 1234 567"
    },
    {
        "company": "نجار السالم",
        "service": "أعمال خشبية",
        "rating": 4.6,
        "trust_index": 88,
        "phone": "+974 2456 789"
    }
]

@app.get("/")
def home():
    return {"message": "Shoof Smart API is running!"}

@app.get("/providers")
def get_all_providers():
    return providers

@app.get("/provider/{service}")
def get_provider(service: str):
    result = [p for p in providers if p["service"] == service]
    return result if result else {"error": "No providers found"}
