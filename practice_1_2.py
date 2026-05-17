# 需要：pip install openai     (OpenAI-compatible SDK 跟 LM Studio 溝通)
# 前置：LM Studio pull gemma4:e4b && LM Studio serve
import sys, statistics
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="LM Studio")

PROMPTS = {
    "中文": "用一句話描述一隻貓在做什麼。",
    "English": "Describe in one sentence what a cat is doing.",
}

N = 10  # 本機慢、N 小一點；確認 OK 後加大
for label, prompt in PROMPTS.items():
    output_tokens = []
    for _ in range(N):
        r = client.chat.completions.create(
            model="gemma4:e4b",
            max_tokens=80,
            temperature=1.0,  # 拉高 temperature 看 variance
            messages=[{"role": "user", "content": prompt}],
        )
        output_tokens.append(r.usage.completion_tokens)
    print(f"\n[{label}] prompt: {prompt}")
    print(f"  input tokens: {r.usage.prompt_tokens}")
    print(f"  output tokens — min={min(output_tokens)} max={max(output_tokens)} mean={statistics.mean(output_tokens):.1f} stdev={statistics.stdev(output_tokens):.1f}")

# === 自我驗證 ===
assert max(output_tokens) > min(output_tokens), "temperature=1.0 下、output 長度應該有 variance"
print("\n✅ 練習 2 通過 — 觀察到 temperature 對 output token 的 variance、本機跑 $0")
print("💡 中文 prompt 通常 input tokens 比 English 多（中文 token 化通常一字 ≈ 2 tokens）")