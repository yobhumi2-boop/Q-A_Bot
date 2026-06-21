import os
import sys
from groq import Groq

def main():
    # Verify API key
    if not os.environ.get("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY environment variable not set.")
        print("Please check your terminal setup or .env configuration.")
        sys.exit(1)

    print("⚡ Initializing Groq Client...")

    # Initialize Groq client
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    # Available models:
    # llama-3.3-70b-versatile
    # llama-3.1-8b-instant
    # deepseek-r1-distill-llama-70b
    model_id = "llama-3.3-70b-versatile"

    print(f"🤖 Q&A Bot Ready ({model_id}). Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("❓ Ask me anything: ")

            if user_input.strip().lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            print("\n🤖 Thinking...", end="\r")

            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                temperature=0.7,
                max_tokens=2048
            )

            answer = response.choices[0].message.content

            print(f"🤖 Answer:\n{answer}\n")
            print("-" * 50)

        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()