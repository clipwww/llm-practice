# 需要：pip install openai
# 前置：LM Studio pull gemma4:e4b && LM Studio serve
import sys, time
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="LM Studio")

# 量 5 次 latency
latencies = []
for _ in range(5):
    t0 = time.time()
    r = client.chat.completions.create(
        model="gemma4:e4b",
        max_tokens=200,
        messages=[{"role": "user", "content": "你好！自我介紹一下。"}],
    )
    latencies.append(time.time() - t0)

# 統計
avg_latency = sum(latencies) / len(latencies)
out_tok_avg = r.usage.completion_tokens  # 末次當代表
tps = out_tok_avg / avg_latency if avg_latency > 0 else 0

print(f"model: gemma4:e4b (本機)")
print(f"5 次 latency (sec): min={min(latencies):.2f} max={max(latencies):.2f} mean={avg_latency:.2f}")
print(f"avg output: {out_tok_avg} tokens、約 {tps:.1f} tokens/sec")
print(f"\n1000 次成本: $0 (本機)、預計時長: {avg_latency * 1000 / 60:.1f} 分鐘")

# === 自我驗證 ===
assert avg_latency > 0, "latency 應 > 0"
assert out_tok_avg > 0, "output token 應 > 0"
print(f"\n✅ 練習 3 通過 — 本機 model $0 但要花 {avg_latency * 1000 / 60:.0f} 分鐘跑 1000 次")
print("💡 對照 Path B Anthropic：1000 次只要 ~10-20 分鐘但要 $0.25（haiku）")