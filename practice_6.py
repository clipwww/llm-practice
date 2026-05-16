# 需要：pip install openai
# 前置：LM Studio 已 serve、qwen2.5:3b 已 pull
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="LM Studio",  # LM Studio 不檢查、隨便填
)

r = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": "用 3 句話介紹什麼是 ReAct。"}],
)

text = r.choices[0].message.content
print("回應：", text)

# === 自我驗證 ===
assert len(text) > 10, "回應太短、LM Studio 可能沒跑起來"
print(f"✅ 練習 6 通過 — 你的本機 LM Studio 已能透過 OpenAI-compatible API 呼叫")
print(f"💡 跑這次完全沒花錢（除了你的電力）")