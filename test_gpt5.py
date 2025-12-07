"""
Test script to verify GPT-5.1 integration
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Test GPT-5.1 connection
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=" * 60)
print("Testing GPT-5.1 Integration")
print("=" * 60)

try:
    # Simple test with GPT-5.1
    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'GPT-5.1 is working!' in exactly 5 words."}
        ],
        max_tokens=20
    )
    
    result = response.choices[0].message.content
    print(f"\n✅ GPT-5.1 Response: {result}")
    print(f"✅ Model used: {response.model}")
    print(f"✅ Tokens used: {response.usage.total_tokens}")
    print("\n" + "=" * 60)
    print("SUCCESS! GPT-5.1 is working correctly!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nThis could mean:")
    print("1. GPT-5.1 model name might be different")
    print("2. Your API key doesn't have access to GPT-5.1")
    print("3. There might be a rate limit issue")
    print("\nLet's check what models are available...")
    
    # Try to list available models
    try:
        models = client.models.list()
        print("\nAvailable GPT-5 models:")
        for model in models.data:
            if "gpt-5" in model.id.lower():
                print(f"  - {model.id}")
    except:
        print("Could not list models")
