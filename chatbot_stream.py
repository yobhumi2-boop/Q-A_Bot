import os
import sys
from groq import Groq

def main():
    if not os.environ.get("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY environment variable not set.")
        sys.exit(1)

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    model_id = "llama-3.3-70b-versatile"

    print(f"🤖 Q&A Bot Ready ({model_id}). Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("❓ Ask me anything: ")

            if user_input.lower() in ["exit", "quit"]:
                break

            print("\n🤖 Answer:")

            stream = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "user", "content": user_input}
                ],
                stream=True
            )

            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="", flush=True)

            print("\n" + "-" * 50)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()

