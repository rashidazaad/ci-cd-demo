from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>CI/CD Demo</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
                h1 { color: #333; }
                .status { color: #2ecc71; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>🚀 CI/CD Test Application</h1>
            <p>Pipeline Status: <span class="status">SUCCESSFULLY DEPLOYED & RUNNING!</span></p>
        </body>
    </html>
    """