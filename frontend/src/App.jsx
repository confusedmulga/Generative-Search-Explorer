import { useState } from "react";
import SearchBar from "./components/SearchBar";

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState("");

  const handleSearch = async (query) => {
    setLoading(true);
    setError("");
    setResults(null);

    try {
      const res = await fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const data = await res.json();
      setResults(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Generative Search Explorer
      </h1>

      <SearchBar onSearch={handleSearch} />

      {loading && <p className="text-center">Loading…</p>}
      {error && <p className="text-red-600 text-center">{error}</p>}

      {results && (
        <div className="space-y-6">
          <div>
            <h2 className="text-xl font-semibold">Answer:</h2>
            <p className="mt-2">{results.generated_answer}</p>
          </div>

          <div>
            <h2 className="text-xl font-semibold">Top Matches:</h2>
            <ul className="list-disc list-inside mt-2 space-y-1">
              {results.top_matches.map((doc, i) => (
                <li key={i}>{doc}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
