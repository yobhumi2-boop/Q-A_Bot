import os
import sys
from groq import Groq

def main():
    if not os.environ.get("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY environment variable not set.")
        sys.exit(1)

    print("⚡ Initializing Groq Client...")

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    model_id = "llama-3.3-70b-versatile"

    # Conversation memory
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

    print(f"🤖 Chat Assistant Ready ({model_id}). Type 'exit' to stop.\n")

    while True:
        try:
            user_input = input("❓ You: ")

            if user_input.strip().lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            print("\n🤖 Thinking...", end="\r")

            # Add user message to memory
            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            response = client.chat.completions.create(
                model=model_id,
                messages=messages,
                temperature=0.7,
                max_tokens=2048
            )

            assistant_reply = response.choices[0].message.content

            # Add assistant reply to memory
            messages.append(
                {
                    "role": "assistant",
                    "content": assistant_reply
                }
            )

            print(f"🤖 Assistant:\n{assistant_reply}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
