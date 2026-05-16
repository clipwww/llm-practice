# 需要：pip install openai      (用 OpenAI-compatible SDK 跟 LM Studio 溝通)
# 前置：LM Studio pull gemma4:e4b && LM Studio serve
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="LM Studio",  # LM Studio 不檢查、隨便填
)

r = client.chat.completions.create(
    model="gemma4:e4b",   # 換成 qwen2.5:3b / llama3.2:3b 也可
    max_tokens=256,
    messages=[
        {"role": "system", "content": "直接回答，不要輸出思考過程。"},
        {"role": "user", "content": "用一句話自我介紹。"},
    ],
)

# === 自我驗證 ===
# print("回應原始資料：", r)
text = r.choices[0].message.content
print("回應：", text)
print("usage:", r.usage)

assert r.choices[0].finish_reason in ("stop", "length"), f"非預期 finish_reason: {r.choices[0].finish_reason}"
assert len(text) > 0, "回應不應為空"
assert r.usage.completion_tokens > 0, "output token 應 > 0"
print("✅ 練習 1 通過 — LM Studio gemma4:e4b 已能本機回應、$0/次")