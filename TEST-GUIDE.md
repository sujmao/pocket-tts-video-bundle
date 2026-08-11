Pocket TTS Portable — 手動測試指南
=====================================

## 測試 A：分層 ZIP（4 檔案 → 手動組裝）

### A1. 準備
  1. 開一個全新的空資料夾，例如 C:\test-zip\
  2. 把 release\ 底下 4 個 ZIP 全部複製過去

### A2. 組裝
  1. 解壓 pocket-tts-core-v1.0.zip      → C:\test-zip\
  2. 解壓 pocket-tts-deps-v1.0.zip      → C:\test-zip\  (覆蓋提示：Yes)
  3. 解壓 pocket-tts-models-v1.0.zip    → C:\test-zip\  (覆蓋提示：Yes)
  4. 解壓 pocket-tts-voices-v1.0.zip    → C:\test-zip\  (覆蓋提示：Yes)

### A3. 驗證目錄結構
  C:\test-zip\ 應該有：
  ├── start.bat
  ├── python\
  ├── tools\ffmpeg\bin\ffmpeg.exe
  ├── site-packages\
  ├── models\model.safetensors
  ├── models\embeddings\
  ├── voices-celebrities\
  ├── pocket_tts_api.py
  ├── video_generator.py
  ├── voice_metadata.py
  └── templates\index.html

### A4. 啟動
  雙擊 start.bat → 等 30-60 秒載入模型
  瀏覽器開 http://localhost:8000

### A5. 功能測試
  □ WebUI 顯示正常
  □ 語音選擇器有語言/性別/風格標籤
  □ 語音庫篩選器可正常過濾
  □ TTS 文字轉語音正常
  □ Video Generator：輸入文字+標題+選聲音 → 產生 MP4
  □ 影片播放正常，有波形+標題


## 測試 B：7z SFX 單一 EXE（一個檔案 → 自動解壓）

### B1. 準備
  1. 開一個全新的空資料夾，例如 C:\test-sfx\
  2. 把 dist\pocket-tts-portable.exe 複製過去

### B2. 執行 SFX
  雙擊 pocket-tts-portable.exe
  → 跳出「Choose where to extract」對話框
  → 選擇 C:\test-sfx\
  → 解壓完成後自動執行 start.bat

### B3. 驗證目錄結構
  同 A3

### B4-B5. 功能測試
  同 A4-A5


## 測試結果記錄

測試 A (分層 ZIP):
  □ 組裝成功
  □ 啟動成功
  □ TTS 正常
  □ Video Generator 正常
  問題：________________________________

測試 B (SFX EXE):
  □ 解壓成功
  □ 自動啟動
  □ TTS 正常
  □ Video Generator 正常
  問題：________________________________
