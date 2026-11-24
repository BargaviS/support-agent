from fastapi import FastAPI                      # import the framework

app = FastAPI(title="Support Agent API")         # create the application object

@app.get("/health")                              # when someone opens GET /health...
def health():                                    # ...run this function
    return {"status": "ok"}                      # ...and reply with this JSON