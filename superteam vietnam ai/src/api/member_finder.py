from fastapi import FastAPI, HTTPExecution
from pydanti import BaseModel
from llm.semantic_search import SemanticSearch
from config import Config

app= FastAPI()
semantic_search = SemanticSearch()

class MemberQuery(BaseModel):
    query: str

@app.post("/memner/find")
async def find_member(query: MemberQuery):
    try:
        # Perform semantic search on the member database
        results = semantic_search.search(query.query)
        if not results:
            return {"status": "success", "response": "NO"}
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPExecution(status_code=500, detail=str(e))