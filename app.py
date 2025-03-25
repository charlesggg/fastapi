import fastapi
import wikipediaapi

app = fastapi.FastAPI()
wiki_wiki = wikipediaapi.Wikipedia('en')

@app.get("/search")
def search_wikipedia(query: str):
    page = wiki_wiki.page(query)
    
    if not page.exists():
        return {"query": query, "result": "No results found."}
    
    return {
        "query": query,
        "title": page.title,
        "summary": page.summary[:500],  # Limit to 500 chars
        "url": page.fullurl
    }