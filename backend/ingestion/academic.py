import arxiv

def fetch_arxiv_papers(query="machine learning", max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = []
    for result in search.results():
        results.append({
            "title": result.title,
            "summary": result.summary,
            "link": result.entry_id
        })
    return results

if __name__ == "__main__":
    print(fetch_arxiv_papers("large language models"))
