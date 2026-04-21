"""
Test script to verify Gemini 2.5 Flash-Lite and google-genai integration
"""
import os
from dotenv import load_dotenv
from app.services.embedding import EmbeddingService
from app.agent.digest_agent import DigestAgent
from app.agent.curator_agent import CuratorAgent
from app.profiles.user_profile import USER_PROFILE

load_dotenv()

def test_gemini_integration():
    print("=" * 60)
    print("Testing 2026 Gemini & google-genai Integration")
    print("=" * 60)

    # 1. Test Embedding Service
    print("\n[1/3] Testing EmbeddingService (text-embedding-004)...")
    try:
        embed_service = EmbeddingService()
        text = "Artificial Intelligence is transforming the world of software engineering."
        vector = embed_service.generate_embedding(text)
        if vector and len(vector) == 768:
            print(f"✅ Success! Generated {len(vector)}-dimensional vector.")
        else:
            print(f"❌ Failed: Vector length is {len(vector) if vector else 0}, expected 768.")
    except Exception as e:
        print(f"❌ Error in EmbeddingService: {e}")

    # 2. Test Digest Agent
    print("\n[2/3] Testing DigestAgent (gemini-2.5-flash-lite)...")
    try:
        digest_agent = DigestAgent()
        sample_title = "Google Unveils Gemini 2.5 Flash-Lite"
        sample_content = (
            "Google has released Gemini 2.5 Flash-Lite, the most cost-efficient "
            "and speed-optimized model in the Gemini family. It features a 1M token "
            "context window and is designed for high-volume, latency-sensitive tasks. "
            "It supports multimodal inputs and includes new 'thinking' controls for "
            "developers to toggle between extreme speed and deeper reasoning."
        )
        digest = digest_agent.generate_digest(sample_title, sample_content, "article")
        if digest and digest.title and digest.summary:
            print(f"✅ Success! Digest generated.")
            print(f"   Title: {digest.title}")
            print(f"   Summary: {digest.summary}")
        else:
            print(f"❌ Failed: Digest output is incomplete or null.")
    except Exception as e:
        print(f"❌ Error in DigestAgent: {e}")

    # 3. Test Curator Agent
    print("\n[3/3] Testing CuratorAgent (gemini-2.5-flash-lite)...")
    try:
        curator_agent = CuratorAgent(USER_PROFILE)
        sample_digests = [
            {
                "id": "article:1",
                "title": "Quantum Computing Breakthrough",
                "summary": "Researchers achieve stable qubits at room temperature using a new silicon-based approach.",
                "article_type": "article"
            },
            {
                "id": "youtube:2",
                "title": "Building RAG Systems with Gemini 2.5",
                "summary": "A deep dive into using Gemini's 1M context window for massive scale RAG applications.",
                "article_type": "youtube"
            }
        ]
        rankings = curator_agent.rank_digests(sample_digests)
        if rankings and len(rankings) > 0:
            print(f"✅ Success! Ranked {len(rankings)} items.")
            for r in rankings:
                print(f"   Rank {r.rank}: {r.digest_id} (Score: {r.relevance_score})")
                print(f"   Reasoning: {r.reasoning}")
        else:
            print(f"❌ Failed: No rankings returned.")
    except Exception as e:
        print(f"❌ Error in CuratorAgent: {e}")

    print("\n" + "=" * 60)
    print("Testing Complete!")
    print("=" * 60)

if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in environment or .env file.")
    else:
        test_gemini_integration()
