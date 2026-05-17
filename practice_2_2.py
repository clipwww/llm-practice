# 需要：pip install openai
# 前置：ollama pull gemma4:e4b && ollama serve
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="ollama")

# 中文情緒分類（正面 / 負面 / 中立）
TEST_SET = [
    ("這部電影超讚、看完想再看一次！", "正面"),
    ("劇情無聊、演員演技尷尬。", "負面"),
    ("這是一部 2019 年的電影。", "中立"),
    ("我不確定喜不喜歡、可能再想想。", "中立"),
    ("第一集很不錯但第二集就崩了。", "負面"),
    ("看完心情很好、推薦！", "正面"),
]

FEW_SHOT_EXAMPLES = """範例：
input: 這家餐廳的牛排好吃到讓我哭出來。
output: 正面

input: 服務生態度很差、我再也不會來了。
output: 負面

input: 這家店位於新北市三重區。
output: 中立
"""


def classify(text: str, *, use_few_shot: bool) -> str:
    prefix = FEW_SHOT_EXAMPLES + "\n" if use_few_shot else ""
    prompt = f"{prefix}input: {text}\noutput:"
    r = client.chat.completions.create(
        model="gemma4:e4b",
        max_tokens=10,
        messages=[{"role": "user", "content": prompt}],
    )
c    return r.choices[0].message.content.strip().splitlines()[0]


def evaluate(use_few_shot: bool) -> tuple[int, int]:
    correct = 0
    for text, label in TEST_SET:
        pred = classify(text, use_few_shot=use_few_shot)
        ok = label in pred
        print(f" {'✓' if ok else '✗'} [{label}] {text[:30]}... → '{pred}'")
        if ok:
            correct += 1
    return correct, len(TEST_SET)


print("=== 0-shot ===")
c0, n = evaluate(use_few_shot=False)
print(f"正確 {c0}/{n} = {c0/n:.0%}")

print("\n=== 3-shot ===")
c3, _ = evaluate(use_few_shot=True)
print(f"正確 {c3}/{n} = {c3/n:.0%}")

# === 自我驗證 ===
assert c3 >= c0, f"預期 3-shot 不比 0-shot 差、實際 {c3} < {c0}（小 model 樣本小、跑幾次比較）"
print(f"\n✅ 練習 2 通過 — 0-shot {c0}/{n}、3-shot {c3}/{n}（本機 $0）")
print("💡 觀察：'中立' 在 0-shot 容易被誤判成正面或負面、3-shot 後改善明顯")
print("💡 小 model（gemma4:e4b）通常 0-shot 表現比 Claude 差更多、所以 few-shot 改善幅度更大")