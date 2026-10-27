# 職場即戰力｜Workplace Readiness

115-1 學期課程學習作品集。

- 作者：alethealai
- 儲存庫：[GitHub](https://github.com/alethealai/dtd_111319027_lai_chih-yi_Workplace_Readiness)
- 預定網站網址（Pages 啟用後生效）：https://alethealai.github.io/dtd_111319027_lai_chih-yi_Workplace_Readiness/

米白、海軍藍與琥珀橘的靜態課程作品集。宋體標題、清楚的黑體內文，搭配較寬的留白。首頁只顯示三個入口；每週筆記需點入列表，再點選文章。

## 頁面

- `index.html`：首頁
- `notes.html`：每週筆記列表
- `notes/beer-game.html`：啤酒遊戲筆記
- `notes/pine-inn.html`：松林客棧個案筆記
- `notes/swot.html`：10/2 SWOT 與策略選擇筆記，含響應式四格圖、方案路徑及紡織產業流程
- `notes/people-express.html`：10/16 人民航空課堂筆記與經營成果，含作業回答、趨勢圖與 CSV 下載
- `people_express_note.py`：人民航空內容產生器，由 `build.py` 呼叫；成果讀取 `assets/people-express/` 內封存報表
- `project.html`：期末專題
- `exercise.html`：彈性週作業
- `assets/styles.css`：字體、配色及手機版樣式
- `assets/site.js`：手機選單與圖表切換
- `assets/beer-game-data.json`：課堂照片轉錄資料
- `build.py`：頁面內容來源與靜態頁面產生器

## 本機預覽

在此資料夾執行 `python3 -m http.server 4173 --bind 127.0.0.1`，瀏覽 `http://127.0.0.1:4173`。

不需要 npm 安裝。網站可直接託管在 GitHub Pages。字體使用 Google Fonts；離線時以系統宋體／明體與黑體替代。

## 修改內容

編輯 `build.py`，執行 `python3 build.py`，再一併提交產生的 HTML 與資料檔。

啤酒遊戲、松林客棧及 SWOT 的上課日期分別由 `BEER_GAME_DATE`、`PINE_INN_DATE`、`SWOT_DATE` 設定，使用 ISO 日期格式。新增筆記時，在 `build.py` 加入新文章內容與列表連結。期末題目尚未提供，頁面保留待補標示。

## GitHub Pages 部署

1. 將此資料夾內容上傳到 GitHub 儲存庫的根目錄（含 `.nojekyll`）。
2. Settings → Pages → Build and deployment → Source 選擇 Deploy from a branch。
3. Branch 選擇 main，資料夾選擇 / (root)，儲存。
4. 等待 Pages 建置完成，開啟 Settings → Pages 顯示的網址。

使用相對連結，可部署在 `https://帳號.github.io/儲存庫名稱/` 子路徑。

官方說明：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## 資料說明

啤酒遊戲數據從使用者提供的課堂照片 IMG_8218、IMG_8217 人工轉錄，記錄的是課堂工廠角色報表，不宣稱是個人操作結果。第 13 週訂購量空白，以 null 表示，圖表不補零。負庫存依照片紅色括號轉為負號。所有數字應以老師的原始報表為準。

啤酒遊戲頁面保留課堂週報告照片及轉錄數據。SWOT 頁面依 2026/10/2 白板照片（IMG_9310–IMG_9314）重繪圖解，未加入原始白板照片。路徑圖為概念示意，沒有量化縱軸；紡織流程僅呈現板書中的環節。講義延伸以可展開的區塊標示，心得以重新整理筆記的角度撰寫。人民航空頁面在可展開區塊附上 10/16 課堂白板照片三張（`assets/people-express/whiteboard-1016-*.jpg`）。

## 作品使用

© 2026 alethealai。個人原創內容保留所有權利；未提供開源授權。引用之教材與第三方資料權利歸原作者，請依來源規定使用。
