"""Build a dependency-free Traditional Chinese course portfolio for GitHub Pages."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent
COURSE = 'https://irradiated-banjo-bc0.notion.site/115-1-375c98d8903b809bbe0dd273e1cf6a1d'
GAME = 'https://www.top-boss.com.tw/beer-game/'
PINE_INN = 'https://irradiated-banjo-bc0.notion.site/3ddc98d8903b8092b89ad8e8674925f3'
BEER_GAME_DATE = '2026-09-11'
PINE_INN_DATE = '2026-09-18'
SWOT_DATE = '2026-10-02'
beer_game_date_label = BEER_GAME_DATE if BEER_GAME_DATE else '上課日期待補'
pine_inn_date_label = PINE_INN_DATE
data = [
    [1,10,10,10,10],[2,10,10,10,10],[3,10,10,10,15],
    [4,10,10,10,20],[5,15,15,10,20],[6,20,-5,40,30],
    [7,20,-55,70,80],[8,30,-95,70,90],[9,80,-65,50,10],
    [10,90,-5,30,20],[11,10,-25,30,30],[12,20,-35,30,5],
    [13,30,-25,20,None]
]

def page(title, content, active='home', depth=0, description='職場即戰力課程的學習紀錄、每週筆記與學期成果。'):
    prefix = '../' * depth
    links = [('home','index.html','首頁'),('notes','notes.html','每週筆記'),('project','project.html','期末專題'),('exercise','exercise.html','彈性週作業')]
    nav = ''.join(f'<a href="{prefix}{path}"'+(' aria-current="page"' if key==active else '')+f'>{label}</a>' for key,path,label in links)
    return f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#faf7f0"><meta name="description" content="{html.escape(description)}"><title>{title}｜職場即戰力</title><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/styles.css"><script defer src="{prefix}assets/site.js"></script></head>
<body><a class="skip" href="#main">跳至主要內容</a><header class="site-header"><div class="wrap header-inner"><a href="{prefix}index.html" class="brand" aria-label="職場即戰力首頁">職場即戰力<small>LEARNING PORTFOLIO</small></a><button class="menu-button" aria-expanded="false" aria-controls="main-nav">選單</button><nav class="nav" id="main-nav" data-open="false" aria-label="主要導覽">{nav}</nav></div></header>
<main class="wrap" id="main">{content}</main><footer class="site-footer"><div class="wrap footer-inner"><span>職場即戰力 · 115-1 學期學習紀錄</span><a href="{COURSE}" target="_blank" rel="noopener noreferrer">老師的課程網站 ↗</a></div></footer></body></html>'''

def save(path, text):
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8')

save('index.html',page('學期學習紀錄','''
<section class="home-hero" aria-labelledby="home-title"><div><div class="eyebrow">115-1 · 學期學習紀錄</div><h1 id="home-title">從課堂體驗，<br>到職場思考。</h1><p class="lead">記錄每一次決策、觀察與成長。</p><dl class="profile"><div><dt>學生</dt><dd>數位三甲　111319027　賴芷翊</dd></div><div><dt>授課教師</dt><dd>張朝清 教授</dd></div></dl></div><div class="term-note"><strong>學習・思考</strong>從實作中理解，<br>在反思中累積。</div></section>
<section aria-label="學習成果目錄"><p class="section-label">CONTENTS / 學習目錄</p><div class="entry-list">
<a class="entry" href="notes.html"><span class="entry-no">01</span><div><h2>每週筆記</h2><p>課堂重點、操作紀錄與學習反思</p></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="entry" href="project.html"><span class="entry-no">02</span><div><h2>期末專題</h2><p>從問題出發，整理分析與研究成果</p></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="entry" href="exercise.html"><span class="entry-no">03</span><div><h2>彈性週作業</h2><p>自主學習與 WFH-Q&A 作業紀錄</p></div><span class="arrow" aria-hidden="true">↗</span></a>
</div></section>'''))

save('notes.html',page('每週筆記',f'''
<header class="page-intro"><div class="eyebrow">01 / CLASS NOTES</div><h1>每週筆記</h1><p>把課堂中的提問、嘗試與發現，<br>整理成可以回看的學習紀錄。</p></header>
<section aria-label="課堂筆記列表">
<a class="note-row" href="notes/people-express.html"><div class="note-date">2026-10-16</div><div><h2>人民航空：成長、擴張與獲利</h2><p>從解除管制與服務能力，走進40季經營練習：擴張、修正，再找回獲利。</p><div class="tags"><span>系統思考</span><span>經營模擬</span><span>成長限制</span></div></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="note-row" href="notes/swot.html"><div class="note-date">{SWOT_DATE}</div><div><h2>SWOT：從方案到策略選擇</h2><p>先有方案，再進行評估。從內外部條件、未來路徑與產業位置，整理決策的依據。</p><div class="tags"><span>SWOT 分析</span><span>策略選擇</span><span>產業價值鏈</span></div></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="note-row" href="notes/pine-inn.html"><div class="note-date">{pine_inn_date_label}</div><div><h2>松林客棧：營運管理與決策</h2><p>從顧客需求與營運資料，思考餐廳應如何找出問題並制定策略。</p><div class="tags"><span>經營管理</span><span>顧客需求</span><span>數據決策</span></div></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="note-row" href="notes/beer-game.html"><div class="note-date">{beer_game_date_label}</div><div><h2>啤酒遊戲：供需與訂貨決策</h2><p>從 13 週的模擬紀錄，觀察需求、訂貨與庫存之間的關係。</p><div class="tags"><span>供應鏈</span><span>庫存管理</span><span>長鞭效應</span></div></div><span class="arrow" aria-hidden="true">↗</span></a>
</section><p class="list-end">其餘課堂筆記將隨課程進度陸續整理。</p>''','notes'))

def chart(series, minimum, maximum, title):
    w,h=680,280
    left,right,top,bottom=45,19,19,42
    def x(index): return left+index*(w-left-right)/12
    def y(value): return top+(maximum-value)*(h-top-bottom)/(maximum-minimum)
    lines=[]
    for tick in range(minimum,maximum+1,20):
        lines.append(f'<line x1="{left}" y1="{y(tick):.1f}" x2="{w-right}" y2="{y(tick):.1f}" class="{"zero" if tick==0 else "grid"}"/><text x="{left-10}" y="{y(tick)+4:.1f}" text-anchor="end">{tick}</text>')
    for i in range(13):
        lines.append(f'<text x="{x(i):.1f}" y="{h-17}" text-anchor="middle">{i+1}</text>')
    for col,color,dashed in series:
        points=' '.join(f'{x(i):.1f},{y(row[col]):.1f}' for i,row in enumerate(data) if row[col] is not None)
        lines.append(f'<polyline points="{points}" class="line" stroke="{color}"'+(' stroke-dasharray="6 5"' if dashed else '')+'/>')
        for i,row in enumerate(data):
            if row[col] is not None: lines.append(f'<circle cx="{x(i):.1f}" cy="{y(row[col]):.1f}" r="3" fill="{color}"/>')
    return f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{title}，橫軸為遊戲第1至13週，縱軸單位為箱"><title>{title}</title>'+''.join(lines)+'</svg>'

orders=chart([(3,'#172d46',False),(4,'#a95312',True)],0,100,'工廠收到的需求量與訂購量')
inventory=chart([(2,'#172d46',False)],-100,20,'工廠庫存變化，第8週最低為負95箱')
article=f'''
<nav class="breadcrumbs" aria-label="麵包屑"><a href="../notes.html">每週筆記</a><span aria-hidden="true">/</span><span>課堂紀錄</span></nav>
<header class="article-head"><p class="article-meta">{beer_game_date_label} · 課堂模擬紀錄</p><h1>啤酒遊戲</h1><p class="article-subtitle">供需與訂貨決策</p><div class="tags"><span>供應鏈</span><span>庫存管理</span><span>長鞭效應</span></div><p class="article-intro">需求增加時，究竟該多訂多少貨？透過啤酒遊戲，觀察訂貨決策如何影響整條供應鏈。</p></header>
<div class="article-layout"><nav class="article-toc" aria-label="本篇目錄"><p class="section-label">IN THIS NOTE</p><a href="#class">課堂內容</a><a href="#concepts">重點整理</a><a href="#results">操作與成果</a><a href="#reflection">我的反思</a><a href="#sources">參考資料</a></nav><article class="article-content">
<section id="class" class="article-section"><h2>課堂內容</h2><p>這堂課透過啤酒遊戲模擬供應鏈的運作，觀察供需狀況，練習決定每次應該訂購多少貨。訂貨時需要同時考慮需求、目前庫存，以及尚未到貨的訂單。</p><p>遊戲中的角色包含工廠、配銷商、大盤商與零售商。貨品沿著供應鏈往下游流動，訂單則往上游傳遞；生產、交貨與訂單傳遞都可能有時間延遲。</p><div class="flow" aria-label="貨品流向：工廠到配銷商到大盤商到零售商"><span>工廠</span><i aria-hidden="true">→</i><span>配銷商</span><i aria-hidden="true">→</i><span>大盤商</span><i aria-hidden="true">→</i><span>零售商</span></div><p class="source-note">本篇數據取自課堂照片中的「工廠週報告」，屬於課堂展示紀錄；尚未確認個人實際操作角色。規則說明參考 Top-BOSS 官方介紹。</p></section>
<section id="concepts" class="article-section"><h2>重點整理</h2><dl class="concepts"><div><dt>01　庫存與缺貨</dt><dd>庫存過多會增加持有成本，庫存不足則可能產生欠貨。訂貨決策需要在兩者之間取得平衡。</dd></div><div><dt>02　到貨延遲</dt><dd>下訂後不會立刻收到貨。如果只看當下缺貨，而忽略已經下訂、還沒送到的貨，可能重複追加訂單。</dd></div><div><dt>03　長鞭效應</dt><dd>下游需求的小幅變化，可能隨著各角色的訂貨調整，轉變成上游更大的波動。判斷時應比較各角色與市場的紀錄，不能只看單一角色。</dd></div></dl></section>
<section id="results" class="article-section"><h2>操作與成果</h2>
<div class="chart-panel"><div class="chart-toolbar"><h3 id="chart-title">需求與訂購量</h3><div class="chart-switch" aria-label="選擇圖表"><button data-chart-mode="orders" aria-pressed="true">需求與訂貨</button><button data-chart-mode="inventory" aria-pressed="false">庫存變化</button></div></div><div data-chart-panel="orders"><div class="legend"><span><b></b>工廠收到的需求量</span><span><b class="amber"></b>工廠訂購量</span></div>{orders}<p class="chart-desc">橫軸：遊戲週次 · 單位：箱。第 13 週訂購量未記錄，曲線於第 12 週結束。此處的需求量並非終端市場需求。</p></div><div data-chart-panel="inventory" hidden><div class="legend"><span><b></b>工廠庫存量</span></div>{inventory}<p class="chart-desc">橫軸：遊戲週次 · 單位：箱。負值表示照片報表中的欠貨狀態。</p></div></div>
<noscript><p class="no-script">啟用 JavaScript 後可切換庫存圖表；下方仍可查看課堂紀錄照片。</p></noscript>
<ul class="observations"><li><strong>第 6 週，庫存開始轉負。</strong>收到的需求由 10 箱升至 40 箱，當週到貨 20 箱，報表庫存為 −5 箱。</li><li><strong>第 8 週，欠貨達到 95 箱。</strong>工廠需求為 70 箱，當週到貨僅 30 箱，訂購量提高到 90 箱。</li><li><strong>第 10 週到貨增加，欠貨縮小。</strong>到貨 90 箱、需求 30 箱，庫存從前一週的 −65 箱回升至 −5 箱；到第 13 週仍有 25 箱欠貨。</li></ul>
<figure class="class-photo"><img src="../assets/beer-game-week13.jpeg" alt="課堂啤酒遊戲第 13 週工廠週報告" loading="lazy"><figcaption>課堂啤酒遊戲第 13 週工廠報告紀錄。</figcaption></figure></section>
<section id="reflection" class="article-section"><h2>我的反思</h2><div class="reflection"><p>這是我第一次接觸這類供應鏈模擬遊戲，一開始，我以為只要顧好自己這一端收到的需求，再決定相對應的訂貨量就可以。實際進行幾回合後才發現，下游零售商的需求不斷變動，加上資訊傳遞與到貨都有延遲，我的庫存常在短缺與過剩之間擺盪：需要貨時沒有庫存，不需要時卻累積了很多貨。</p><p>老師提醒我們，訂貨後要兩週才會到貨，而下游的需求傳到上游也需要時間，做決策不能只看自己眼前收到的需求，還要持續觀察下游的需求趨勢，並把已經下單、尚未到貨的數量一起納入判斷。這次的遊戲真的讓我親身體會到：供應鏈中每個角色看似各自做決定，其實彼此的決策會互相影響；如果只處理眼前的問題，很容易讓缺貨與庫存過剩反覆出現。</p><p>最後在檢視遊戲結果的折線圖時，老師提醒我們，不要只看每條線上升或下降，而要觀察各個高峰出現的先後順序：哪一條線先出現高峰、它影響了哪一條線，以及是否接著造成另一個高峰。從高峰之間的時間差，可以更清楚地看見需求與訂貨變化如何沿著供應鏈傳遞。有了圖表的幫助，讓我們更能判斷在第幾週時哪些決策需要修正，也能看出一個錯誤決策所帶來的連鎖反應可能延續多久。透過圖表與數字，我們可以更理性、客觀地找出最佳解。</p></div></section>
<section id="sources" class="article-section"><h2>參考資料</h2><ol class="sources"><li><a href="{COURSE}" target="_blank" rel="noopener noreferrer">張朝清老師｜115-1 職場即戰力課程網站 ↗</a></li><li><a href="{GAME}" target="_blank" rel="noopener noreferrer">Top-BOSS｜啤酒供應鏈管理介紹 ↗</a></li><li>課堂照片：工廠週報告與供應鏈訂購量、庫存量圖表。</li></ol></section><a class="back-link" href="../notes.html">← 返回每週筆記</a></article></div>'''
save('notes/beer-game.html',page('啤酒遊戲：供需與訂貨決策',article,'notes',1,'從課堂照片中的13週工廠紀錄，整理啤酒遊戲的供需變化、訂貨決策與庫存管理。'))

pine_inn_article=f'''
<nav class="breadcrumbs" aria-label="麵包屑"><a href="../notes.html">每週筆記</a><span aria-hidden="true">/</span><span>課堂個案</span></nav>
<header class="article-head"><p class="article-meta">{pine_inn_date_label} · 課堂個案分析</p><h1>松林客棧</h1><p class="article-subtitle">營運管理與決策</p><div class="tags"><span>經營管理</span><span>顧客需求</span><span>數據決策</span></div><p class="article-intro">當顧客與營業額都在成長，利潤為什麼反而下降？從松林客棧的經營方式，重新思考顧客需求與決策依據。</p></header>
<div class="article-layout"><nav class="article-toc" aria-label="本篇目錄"><p class="section-label">IN THIS NOTE</p><a href="#class">個案概要</a><a href="#concepts">課堂重點</a><a href="#proposals">問題與提案</a><a href="#reflection">我的反思</a><a href="#sources">參考資料</a></nav><article class="article-content">
<section id="class" class="article-section"><h2>個案概要</h2><p>松林客棧擁有穩定的老主顧，夏季也會迎來大量觀光客。雖然營業額與顧客人數持續成長，客棧的利潤卻逐漸下降，投資報酬率只有約 3%。這個個案讓我們從顧客需求、存貨紀錄與經營決策等角度，思考生意興隆卻沒有帶來理想獲利的可能原因。</p></section>
<section id="concepts" class="article-section"><h2>課堂重點</h2>
<div class="lesson-block"><h3>營業額與利潤公式</h3><div class="formula-list">
<div><div class="formula-equation"><code>TR = Q × @p</code></div><div class="formula-meaning">總營業額（Total Revenue）＝銷售量 × 客單價。<small>筆記寫法：Q * @p</small></div></div>
<div><div class="formula-equation"><code>π = TR − TC</code></div><div class="formula-meaning">利潤＝總營業額－總成本。</div></div>
<div><div class="formula-equation"><code>TC = VC + FC</code></div><div class="formula-meaning">總成本＝變動成本＋固定成本。</div></div>
<div><div class="formula-equation"><code>π = (@p − c) × Q − FC</code></div><div class="formula-meaning">其中 <code>c</code> 為每份變動成本，所以 <code>VC = c × Q</code>。</div></div>
</div><p class="source-note">符號：TR＝總營業額、Q＝銷售量、@p＝客單價、TC＝總成本、VC＝變動成本、FC＝固定成本、π＝利潤。</p><p class="source-note">Net profit＝扣除費用與稅後的淨利。</p></div>
<div class="lesson-block"><h3>市場區隔與營運數據</h3><ul class="lesson-list"><li><strong>區分常客與夏季觀光客：</strong>比較兩群人的來店時間、餐點選擇與客單價，再分別設計常客方案及觀光客套餐。</li><li><strong>追蹤三項效率：</strong>翻桌率看座位使用速度，存貨週轉率看食材運用效率，坪效看每坪空間帶來的營業額。</li><li><strong>建立每日盤點：</strong>記錄期初存貨、進貨、銷售、報廢、員工領用及期末存貨；搭配隨機抽查，判斷差異來自耗損、份量、記帳或其他原因。</li></ul></div>
<div class="lesson-block"><h3>成本分類</h3><ul class="lesson-list"><li><strong>直接材料：</strong>可直接追溯到餐點的食材成本（可以均攤到每次使用）。</li><li><strong>直接人工：</strong>可直接歸屬於餐點製作的人工（可以均攤到每次使用）。</li><li><strong>間接費用：</strong>租金、水電及共用設備等成本（不能直接均攤到每次使用）。</li></ul></div>
</section>
<section id="proposals" class="article-section"><h2>問題與提案</h2>
<div class="proposal-group"><h3>大家都點雞排怎麼辦？</h3><ul class="proposal-list"><li><strong>先確認雞排是否真的比較不賺。</strong><div class="proposal-detail">比較雞排與牛排的單位邊際貢獻、銷量和製作時間；如果雞排的總貢獻較高，就不必強迫顧客改點牛排。</div></li><li><strong>提高雞排顧客的客單價。</strong><div class="proposal-detail">保留受歡迎的雞排，提供飲料、湯品或甜點升級套餐，增加每位顧客的消費。</div></li><li><strong>降低顧客嘗試牛排的門檻。</strong><div class="proposal-detail">推出小份牛排、雞牛雙拼或觀光客特色套餐，再比較調整前後的牛排銷量。</div></li></ul></div>
<div class="proposal-group"><h3>人員流動怎麼辦？</h3><ul class="proposal-list"><li><strong>先建立明確的管理責任。</strong><div class="proposal-detail">指定一位廚房負責人，管理食材領用、盤點、報廢及工作分配。</div></li><li><strong>把個人經驗變成餐廳的制度。</strong><div class="proposal-detail">記錄標準配方、作業流程與交接方式，避免某位員工離職後工作無法繼續。</div></li><li><strong>培養替補人力，再判斷是否增聘副手。</strong><div class="proposal-detail">讓重要工作至少有兩個人會做；若泰德仍無法兼顧採購與成本管理，再聘請職責明確的營運副手。</div></li></ul></div>
<div class="proposal-group"><h3>冬天怎麼辦？</h3><ul class="proposal-list"><li><strong>先確認冬季是否真的是淡季。</strong><div class="proposal-detail">比較各月份的來客數、營業額與餐點銷量，再決定需要縮減多少採購與人力。</div></li><li><strong>用常客與預約穩定冬季需求。</strong><div class="proposal-detail">推出常客方案，並設計會議多人套餐、家庭聚餐套餐與團體預約方案；搭配冬季限定菜色，增加顧客在淡季來店的理由。</div></li><li><strong>把餐券當成引導回訪的工具。</strong><div class="proposal-detail">設定合理折扣、兌換期限與使用時段，並保留日後供餐需要的成本。</div></li><li><strong>依需求同步調整支出。</strong><div class="proposal-detail">減少肉品採購、調整排班，並精簡銷量低、耗損高的菜色。</div></li></ul></div></section>
<section id="reflection" class="article-section"><h2>我的反思</h2><div class="reflection"><p>在松林客棧的個案中，我發現老闆在意的事情，不一定就是顧客真正重視的事情。露絲非常在意服務人員是否立刻收走餐盤、補充咖啡或備妥餐具，但真正因服務不佳而抱怨的顧客並不多。如果經營者沒有先了解顧客的需求，只是一心追求自己認為重要的細節，最後可能只會打造出自己心目中的完美環境，而不一定是讓顧客感到舒服、願意再次光臨的環境。</p><p>此外，經營決策應該建立在客觀資料上，而不能只依靠老闆的感覺。露絲發現廚房存貨短缺後，便懷疑員工把食材帶回家，甚至考慮在廚房後門加鎖。但是，如果沒有每日盤點、進貨、銷售、報廢及員工領用等紀錄，就無法確定存貨短缺究竟來自偷竊、浪費、份量不一致，還是記帳錯誤。</p><p>數據的用途也不只是找出問題的成因或追究責任。透過不同餐點的銷量、食材消耗量及季節變化，泰德也可以進一步了解餐廳的供需關係，判斷各種肉品應該訂購多少，以及哪些餐點可能需要調整或精簡。這些資料能幫助他比較老主顧與觀光客的消費習慣，進而規劃菜單、定價及淡旺季的發展策略。</p><p>這個個案讓我明白，經營者除了注意眼前的服務與異常，也需要退一步觀察整體營運。只有了解顧客真正重視的價值，並透過資料檢查自己的判斷，才能找到問題的根源，做出適合餐廳長期發展的決策。</p></div></section>
<section id="sources" class="article-section"><h2>參考資料</h2><ol class="sources"><li><a href="{PINE_INN}" target="_blank" rel="noopener noreferrer">張朝清老師｜松林客棧個案 ↗</a></li><li>個人課堂筆記。</li></ol></section><a class="back-link" href="../notes.html">← 返回每週筆記</a></article></div>'''
save('notes/pine-inn.html',page('松林客棧：營運管理與決策',pine_inn_article,'notes',1,'從松林客棧個案整理顧客需求、營運資料與經營決策之間的關係。'))

swot_article=f'''
<nav class="breadcrumbs" aria-label="麵包屑"><a href="../notes.html">每週筆記</a><span aria-hidden="true">/</span><span>SWOT 與策略</span></nav>
<header class="article-head swot-head">
  <p class="article-meta"><time datetime="{SWOT_DATE}">{SWOT_DATE}</time> · 課堂筆記</p>
  <h1>SWOT：從方案到策略選擇</h1>
  <p class="article-subtitle">先有方案，再進行評估。</p>
  <div class="tags"><span>SWOT 分析</span><span>策略選擇</span><span>產業價值鏈</span></div>
  <p class="article-intro">這週老師用 SWOT 講策略選擇：先想清楚有哪些方案，再看自己的條件和外在環境。這篇是我依 10/2 的白板照片整理的筆記，也加上複習後的想法。</p>
</header>
<div class="article-layout">
  <nav class="article-toc" aria-label="本篇目錄"><p class="section-label">IN THIS NOTE</p><a href="#concepts">課堂重點</a><a href="#pathways">從現在到未來</a><a href="#value-chain">紡織產業案例</a><a href="#reflection">我的反思</a><a href="#sources">參考資料</a></nav>
  <article class="article-content swot-note">
    <section id="concepts" class="article-section">
      <h2>課堂重點：先確定評估的對象</h2>
      <blockquote class="swot-key"><p class="swot-kicker">白板上的核心句</p><p>先有方案 Alt.<br>才進行評估 SWOT。</p></blockquote>
      <p>SWOT 不是憑空分析自己，而是要先有一個具體的方案，再看自己的條件和外在環境對這個方案有利還是不利。</p>
      <figure class="swot-figure" aria-labelledby="swot-grid-caption">
        <div class="swot-grid">
          <div class="swot-cell"><span class="swot-letter" aria-hidden="true">S</span><div><p class="swot-category">內部條件 · 有利</p><h3>優勢 <span lang="en">Strengths</span></h3><p>自身已有、能支持方案的能力與資源。</p><p class="swot-prompt">我有哪些條件可以運用？</p></div></div>
          <div class="swot-cell"><span class="swot-letter" aria-hidden="true">W</span><div><p class="swot-category">內部條件 · 不利</p><h3>劣勢 <span lang="en">Weaknesses</span></h3><p>自身的不足，或執行方案時的限制。</p><p class="swot-prompt">我還缺少哪些能力或資源？</p></div></div>
          <div class="swot-cell"><span class="swot-letter" aria-hidden="true">O</span><div><p class="swot-category">外部環境 · 有利</p><h3>機會 <span lang="en">Opportunities</span></h3><p>環境中有利於方案發展的條件。</p><p class="swot-prompt">外界有哪些機會可以掌握？</p></div></div>
          <div class="swot-cell"><span class="swot-letter" aria-hidden="true">T</span><div><p class="swot-category">外部環境 · 不利</p><h3>威脅 <span lang="en">Threats</span></h3><p>環境中可能妨礙方案的因素。</p><p class="swot-prompt">哪些外在變化可能造成影響？</p></div></div>
        </div>
        <figcaption id="swot-grid-caption">圖 01／SWOT 四格。格子裡的問題是我複習時寫給自己的提示。</figcaption>
      </figure>
      <div class="swot-fit"><span class="swot-kicker">另一個板書關鍵字 · P–E fit</span><h3>人與環境的適配</h3><p>白板上把 People、Job Environment 和 P–E fit 寫在一起。我的理解是：人的能力和特質，要和工作環境的要求對得上。所以評估的時候，不能只看自己有什麼，也要看環境需要什麼。</p></div>
    </section>
    <section id="pathways" class="article-section">
      <h2>從現在到未來：比較不同路徑</h2>
      <p>老師在白板上畫了 Now 和 Future，中間有好幾條不同的曲線，代表不同方案會走出不同的路。選方案的時候，除了看現在的條件和想達到的目標，也要想從現在走到未來的過程。</p>
      <figure class="swot-figure swot-pathways" aria-labelledby="pathways-caption">
        <div class="swot-diagram-heading"><span>NOW → FUTURE</span><span>不同方案 · 不同路徑</span></div>
        <svg class="swot-path-chart" viewBox="0 0 600 320" role="img" aria-labelledby="pathways-title pathways-desc">
          <title id="pathways-title">從現在出發的三種方案路徑</title>
          <desc id="pathways-desc">三條曲線從現在向未來延伸，分別標為方案 A、B、C。橫向代表時間。白板上沒有標縱軸，所以這張圖只看路徑的走向，不比較好壞。</desc>
          <path d="M48 35 V242 H554" class="swot-axis"/>
          <path d="m546 236 8 6-8 6" class="swot-axis"/>
          <path d="M90 242 V266 M470 242 V266" class="swot-axis"/>
          <path d="M470 32 V231" class="swot-guide"/>
          <path d="M90 242 C195 233 313 114 470 53" class="swot-route swot-route-a"/>
          <path d="M90 242 C213 245 330 189 470 128" class="swot-route swot-route-b"/>
          <path d="M90 242 C237 251 350 237 470 200" class="swot-route swot-route-c"/>
          <circle cx="90" cy="242" r="6" class="swot-origin"/>
          <circle cx="470" cy="53" r="5" class="swot-dot-a"/><circle cx="470" cy="128" r="5" class="swot-dot-b"/><circle cx="470" cy="200" r="5" class="swot-dot-c"/>
          <text x="489" y="62" class="swot-path-a">方案 A</text><text x="489" y="137" class="swot-path-b">方案 B</text><text x="489" y="209" class="swot-path-c">方案 C</text>
          <text x="90" y="300" text-anchor="middle">現在</text><text x="470" y="300" text-anchor="middle">未來</text>
        </svg>
        <figcaption id="pathways-caption">圖 02／我依白板重畫的示意圖，A、B、C 是我自己加的代號。白板上沒有標縱軸，所以這張圖只看路徑的走向，不比較好壞。</figcaption>
      </figure>
      <h3 class="swot-subheading">我整理的思考順序</h3>
      <ol class="swot-steps"><li><span>01</span><strong>釐清目標</strong><p>想走到哪裡？</p></li><li><span>02</span><strong>提出方案</strong><p>有哪些選擇？</p></li><li><span>03</span><strong>SWOT 評估</strong><p>各有什麼條件？</p></li><li><span>04</span><strong>比較與選擇</strong><p>哪個較符合目標？</p></li></ol>
      <p class="source-note">這是我把板書的「方案、評估、抉擇」和講義的策略思考程序合在一起整理的順序。</p>
      <details class="swot-supplement"><summary>講義補充：策略形態與策略勢態</summary><dl><div><dt>策略形態</dt><dd>某一時點上的策略狀態，也就是當時的經營形貌。</dd></div><div><dt>策略勢態</dt><dd>不同時點間，策略變化的方向與速度。</dd></div></dl><p>所以除了寫出現在和未來的樣子，我也要想清楚中間是怎麼變過去的。</p><p class="source-note">依〈從策略形態到策略矩陣〉第 1–3 頁補充。</p></details>
    </section>
    <section id="value-chain" class="article-section">
      <h2>紡織產業案例：看見上下游</h2>
      <p>老師用紡織業當例子，從人造纖維、紡紗、織布到成衣，把上下游串起來。先看懂每個環節在哪裡、彼此怎麼連，才能想企業可以往哪裡發展。</p>
      <figure class="swot-figure" aria-labelledby="value-chain-caption">
        <div class="swot-chain-direction"><span>上游</span><span aria-hidden="true">→</span><span>下游</span></div>
        <ol class="swot-chain" aria-label="白板紡織產業流程"><li><span>01</span><strong>人造纖維</strong></li><li><span>02</span><strong>紡紗</strong></li><li><span>03</span><strong>織布</strong></li><li><span>04</span><strong>成衣</strong></li></ol>
        <figcaption id="value-chain-caption">圖 03／我依白板重畫的簡化流程，沒有畫出所有價值活動。</figcaption>
      </figure>
      <p>白板照片沒有拍到這個案例完整的方案和 SWOT 分析，所以我先記下產業流程，方案的細節還要再確認。</p>
      <details class="swot-supplement"><summary>講義延伸：價值鏈、垂直整合與策略矩陣</summary><p>講義把產業價值鏈看成從上游到下游一連串的價值單元。垂直整合程度是策略形態的構面之一，用來思考企業要參與哪些上下游環節。</p><p>策略矩陣是把策略形態的六個構面，沿著產業價值鏈展開。六個構面是：產品線廣度與特色、目標市場區隔與選擇、垂直整合程度、相對規模與規模經濟、地理涵蓋範圍，以及競爭優勢。</p><p class="source-note">整理自講義第 5、8–11 頁，是我複習時的延伸閱讀。</p></details>
    </section>
    <section id="reflection" class="article-section">
      <h2>我的反思</h2>
      <div class="reflection"><p>整理完這份筆記，我印象最深的是「先有方案，才進行評估」。如果之後要比較兩份實習，我會先寫清楚兩份工作各做什麼、我想從中累積什麼能力，再分別寫 SWOT。而且只寫「缺乏經驗」太籠統，我要寫出缺的是哪種經驗、會影響哪份工作，還有能不能先準備補起來。</p><p>P–E fit 也提醒我，評估自己一定要有一個具體的環境來對照。就算我很熟某個工具，也要看職缺是不是真的需要它，才知道這項能力對選擇有沒有幫助。這是我複習時想到的例子，也讓我更明白為什麼要先把方案寫清楚。</p></div>
    </section>
    <section id="sources" class="article-section">
      <h2>參考資料</h2>
      <ol class="sources"><li>2026/10/2 課堂白板照片（IMG_9310–IMG_9314）。圖表是我依照片重畫的，文字和提問是複習時整理的。</li><li>課堂講義〈從策略形態到策略矩陣〉：第 1–3 頁的策略定義與思考程序、第 5 頁的策略形態構面，以及第 8–11 頁的價值鏈與策略矩陣。</li><li><a href="{COURSE}" target="_blank" rel="noopener noreferrer">張朝清老師｜115-1 職場即戰力課程網站 ↗</a></li></ol>
    </section>
    <a class="back-link" href="../notes.html">← 返回每週筆記</a>
  </article>
</div>'''
save('notes/swot.html',page('SWOT：從方案到策略選擇',swot_article,'notes',1,'10/2 課堂筆記：以 SWOT 四格、未來方案路徑與紡織產業流程，整理策略評估、環境適配與複習心得。'))

save('project.html',page('期末專題','''<header class="page-intro empty-page"><div class="eyebrow">02 / FINAL PROJECT</div><h1>期末專題</h1><p>從一個值得探究的問題出發，<br>把課堂所學轉化為有依據的分析。</p></header><section class="empty-body"><span class="status-label">準備中</span><h2>研究題目，持續醞釀中。</h2><p>題目與作業細節確認後，將在這裡整理研究動機、分析過程、結論與簡報。</p><div class="outline" aria-label="預計整理架構"><div class="outline-item"><span>01</span><div><h3>問題與動機</h3><p>研究什麼，以及為什麼值得研究。</p></div></div><div class="outline-item"><span>02</span><div><h3>資料與分析</h3><p>整理資料來源，運用課堂概念進行分析。</p></div></div><div class="outline-item"><span>03</span><div><h3>結論與成果</h3><p>提出發現、建議與研究限制，彙整報告簡報。</p></div></div></div></section>''','project'))
save('exercise.html',page('彈性週作業','''<header class="page-intro empty-page"><div class="eyebrow">03 / INDEPENDENT LEARNING</div><h1>彈性週作業</h1><p>延伸課堂中的問題，<br>留下自主學習與思考的過程。</p></header><section class="empty-body"><span class="status-label">準備中</span><h2>等待本學期作業題目。</h2><p>收到老師的 WFH-Q&A 題目後，將在這裡整理題目、回答、參考資料與作業簡報。</p><div class="outline" aria-label="預計整理架構"><div class="outline-item"><span>01</span><div><h3>題目與回答</h3><p>記錄問題，說明思考與回答的依據。</p></div></div><div class="outline-item"><span>02</span><div><h3>資料與成果</h3><p>保留參考來源，彙整完成的簡報。</p></div></div></div></section>''','exercise'))
save('404.html',page('找不到頁面','''<header class="page-intro"><div class="eyebrow">404</div><h1>這一頁尚未收錄。</h1><p>連結可能已變更，請回到首頁繼續閱讀。</p></header><a class="back-link" href="index.html">← 返回首頁</a>'''))
save('assets/beer-game-data.json',json.dumps({'source':'課堂照片 IMG_8218、IMG_8217，工廠週報告','columns':['week','arrivals','inventory','demand','orders'],'rows':data},ensure_ascii=False,indent=2))
from people_express_note import render_note
save('notes/people-express.html', page('人民航空：成長、擴張與獲利', render_note(ROOT), 'notes', 1, '10/16 課堂筆記與人民航空40季模擬：策略組合、擴張轉折、最終成果與學習反思。'))
print('Built 9 static pages and classroom data. No external build dependencies.')
