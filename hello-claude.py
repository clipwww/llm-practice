from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic() # 自動讀取 ANTHROPIC_API_KEY

msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hello, who are you?"}],
)

print(msg.content[0].text)