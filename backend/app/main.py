from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .repository import analytics

app=FastAPI(title="LMS Analytics API",version="2.0.0",description="Production-style analytics API for the LMS Star Schema.")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@app.get("/health")
def health(): return {"status":"healthy","service":"LMS Analytics API","version":"2.0.0"}

@app.get("/api/overview")
def overview(): return analytics.overview()

@app.get("/api/enrollments")
def enrollments(): return analytics.enrollments()

@app.get("/api/course-performance")
def course_performance(): return analytics.course_performance()

@app.get("/api/activity")
def activity(): return analytics.activity()

@app.get("/api/assessments")
def assessments(): return analytics.assessments()

@app.get("/api/learner-activity")
def learner_activity(): return analytics.learner_activity()

@app.get("/api/data-model")
def data_model(): return analytics.data_model()

@app.get("/api/data-dictionary")
def data_dictionary(): return analytics.data_dictionary()

@app.post("/api/events")
def ingest_event(event: dict):
    required=["event_id","event_name","occurred_at","user_id","session_id"]
    missing=[x for x in required if x not in event]
    return {"accepted":not missing,"missing_fields":missing,"event":event}
