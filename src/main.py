"""Care Loop - Main entry point for agent orchestration."""

from fastapi import FastAPI

app = FastAPI(title="Care Loop", description="Multi-agent care coordination")

@app.get("/")
def root():
    return {"status": "Care Loop online", "agents": ["triage", "scheduler", "coordinator"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
