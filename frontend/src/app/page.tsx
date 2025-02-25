import SearchBar from "@/components/SearchBar"
import ResultsDisplay from "@/components/ResultsDisplay"

export default function Home() {
  return (
    <main className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8 text-center">Twitter Sentiment Analysis</h1>
      <SearchBar />
      <ResultsDisplay />
    </main>
  )
}

