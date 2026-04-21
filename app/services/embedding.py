import os
from typing import List, Optional
from google import genai
from dotenv import load_dotenv

load_dotenv()

class EmbeddingService:
    def __init__(self):
        # The new unified SDK uses a Client object
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        # Modern 2026 text embedding model
        self.model_name = "gemini-embedding-001" # Consolidated 2026 embedding model
        self.dimensions = 768

    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        Generates a 768-dimensional vector using the 2026 unified google-genai SDK.
        """
        try:
            if not text:
                return None
            
            clean_text = text.replace("\n", " ")[:10000]
            
            response = self.client.models.embed_content(
                model=self.model_name,
                contents=clean_text,
                config={'output_dimensionality': self.dimensions}
            )
            # Accessing the first embedding in the new response structure
            return response.embeddings[0].values
        except Exception as e:
            print(f"Error generating 2026 Google embedding: {e}")
            return None

    def generate_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generates embeddings for a batch of texts.
        """
        try:
            response = self.client.models.embed_content(
                model=self.model_name,
                contents=texts,
                config={'output_dimensionality': self.dimensions}
            )
            return [e.values for e in response.embeddings]
        except Exception as e:
            print(f"Error generating 2026 Google batch embeddings: {e}")
            return []
