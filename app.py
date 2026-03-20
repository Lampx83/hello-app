from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from uploaded build!"}


@app.get("/metadata")
def get_metadata():
    return {
        "name": "Admission",
        "description": "Tra loi cau hoi ve tuyen sinh, quy che tuyen sinh va tai lieu lien quan. Du lieu lay tu collection Admission trong Qdrant.",
        "version": "1.0.0",
        "developer": "LakeFlow",
        "capabilities": [
            "admission",
            "tuyen sinh",
            "quy che",
            "tai lieu"
        ],
        "supported_models": [
            {
                "model_id": "qwen3:8b",
                "name": "Qwen3 8B",
                "description": "Mo hinh Ollama cho hoi dap dua tren tai lieu Admission",
                "accepted_file_types": []
            }
        ],
        "sample_prompts": [
            "Dieu kien tuyen sinh dai hoc chinh quy la gi?",
            "Thoi gian nop ho so tuyen sinh nam nay?",
            "Cac nganh dao tao va chi tieu tuyen sinh?"
        ],
        "provided_data_types": [
            {
                "type": "qdrant_collection",
                "description": "Collection Admission trong Qdrant"
            }
        ],
        "contact": "",
        "status": "active"
    }