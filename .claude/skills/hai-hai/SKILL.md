---
name: hai-hai
description: 以繁體中文、英文、日文打招呼，並回報當前時間，最後執行測試腳本。
metadata:
  version: "1.1"
---

# 嗨嗨打招呼

當此 skill 被呼叫時，依序執行以下三件事：

## 1. 三語打招呼

用三種語言熱情地向使用者打招呼：
- **繁體中文**：嗨嗨！你好！很高興見到你！
- **English**：Hey hey! Hello there! Great to see you!
- **日本語**：やあやあ！こんにちは！お会いできて嬉しいです！

## 2. 回報目前時間

使用 Bash tool 取得當前日期與時間：

```bash
date '+%Y年%m月%d日 %H:%M:%S %Z'
```

以繁體中文說明今天是哪一年哪一月哪一日、幾點幾分，並計算是星期幾。

範例格式：
> 現在是 2026 年 5 月 16 日，星期六，下午 3:42:08 (CST)。

## 3. 執行測試腳本

使用 Bash tool 執行測試腳本：

```bash
python3 ./scripts/hello.py
```

顯示腳本輸出的結果。

---

## 擴充說明

`scripts/` 目錄可放置額外的輔助腳本：
- `hello.py` — 簡單的 Python 測試腳本，確認環境正常
- 未來可新增其他工具（例如 `summarize_session.py`、`export_history.sh` 等）
