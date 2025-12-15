// Utility to fetch and manage book content from docs folder
// This is kept for potential future use but not currently used in the RAG chatbot
interface BookChapter {
  id: string;
  title: string;
  content: string;
  module: string;
  path: string;
}

export const getBookContent = async (): Promise<BookChapter[]> => {
  // Fetch the processed book content from static JSON
  try {
    const response = await fetch('/book-content.json');
    if (!response.ok) {
      console.error('Failed to fetch book content:', response.statusText);
      // Return empty array if fetch fails
      return [];
    }
    return response.json();
  } catch (error) {
    console.error('Error fetching book content:', error);
    return [];
  }
};

export const searchBookContent = async (query: string): Promise<BookChapter[]> => {
  try {
    const content = await getBookContent();

    // Simple search implementation - in a real app, you'd want more sophisticated search
    const lowerQuery = query.toLowerCase();

    return content.filter(chapter =>
      chapter.title.toLowerCase().includes(lowerQuery) ||
      chapter.content.toLowerCase().includes(lowerQuery) ||
      chapter.module.toLowerCase().includes(lowerQuery)
    );
  } catch (error) {
    console.error('Error searching book content:', error);
    return [];
  }
};