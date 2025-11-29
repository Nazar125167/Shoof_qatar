
# 📁 shoof-qatar-demo (Public)
@app.get("/")
def demo_home():
    return {
        "message": "نظام شوف التجريبي",
        "note": "النظام الكامل يعمل على السيرفر",
        "demo": True
    }

@app.get("/demo-recommend")
def demo_recommend():
    return {
        "company": "شركة تجريبية",
        "phone": "+974 XXXXXXXX",
        "trust_score": "9.0/10",
        "note": "بيانات حقيقية في النظام الكامل"
    }
