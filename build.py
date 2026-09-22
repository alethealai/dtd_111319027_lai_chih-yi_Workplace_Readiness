"""Build a dependency-free Traditional Chinese course portfolio for GitHub Pages."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent
COURSE = 'https://irradiated-banjo-bc0.notion.site/115-1-375c98d8903b809bbe0dd273e1cf6a1d'
GAME = 'https://www.top-boss.com.tw/beer-game/'
DATE = None  # Set to the confirmed class date, for example '2026-09-15'.
date_label = DATE if DATE else '上課日期待補'
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
<section class="home-hero" aria-labelledby="home-title"><div><div class="eyebrow">115-1 · 學期學習紀錄</div><h1 id="home-title">從課堂體驗，<br>到職場思考。</h1><p class="lead">記錄每一次決策、觀察與成長。</p></div><div class="term-note"><strong>學習・思考</strong>從實作中理解，<br>在反思中累積。</div></section>
<section aria-label="學習成果目錄"><p class="section-label">CONTENTS / 學習目錄</p><div class="entry-list">
<a class="entry" href="notes.html"><span class="entry-no">01</span><div><h2>每週筆記</h2><p>課堂重點、操作紀錄與學習反思</p></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="entry" href="project.html"><span class="entry-no">02</span><div><h2>期末專題</h2><p>從問題出發，整理分析與研究成果</p></div><span class="arrow" aria-hidden="true">↗</span></a>
<a class="entry" href="exercise.html"><span class="entry-no">03</span><div><h2>彈性週作業</h2><p>自主學習與 WFH-Q&A 作業紀錄</p></div><span class="arrow" aria-hidden="true">↗</span></a>
</div></section>'''))

save('notes.html',page('每週筆記',f'''
<header class="page-intro"><div class="eyebrow">01 / CLASS NOTES</div><h1>每週筆記</h1><p>把課堂中的提問、嘗試與發現，<br>整理成可以回看的學習紀錄。</p></header>
<section aria-label="課堂筆記列表"><a class="note-row" href="notes/beer-game.html"><div class="note-date">{date_label}</div><div><h2>啤酒遊戲：供需與訂貨決策</h2><p>從 13 週的模擬紀錄，觀察需求、訂貨與庫存之間的關係。</p><div class="tags"><span>供應鏈</span><span>庫存管理</span><span>長鞭效應</span></div></div><span class="arrow" aria-hidden="true">↗</span></a></section><p class="list-end">其餘課堂筆記將隨課程進度陸續整理。</p>''','notes'))

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
<header class="article-head"><p class="article-meta">{date_label} · 課堂模擬紀錄</p><h1>啤酒遊戲</h1><p class="article-subtitle">供需與訂貨決策</p><div class="tags"><span>供應鏈</span><span>庫存管理</span><span>長鞭效應</span></div><p class="article-intro">需求增加時，究竟該多訂多少貨？透過啤酒遊戲，觀察訂貨決策如何影響整條供應鏈。</p></header>
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

save('project.html',page('期末專題','''<header class="page-intro empty-page"><div class="eyebrow">02 / FINAL PROJECT</div><h1>期末專題</h1><p>從一個值得探究的問題出發，<br>把課堂所學轉化為有依據的分析。</p></header><section class="empty-body"><span class="status-label">準備中</span><h2>研究題目，持續醞釀中。</h2><p>題目與作業細節確認後，將在這裡整理研究動機、分析過程、結論與簡報。</p><div class="outline" aria-label="預計整理架構"><div class="outline-item"><span>01</span><div><h3>問題與動機</h3><p>研究什麼，以及為什麼值得研究。</p></div></div><div class="outline-item"><span>02</span><div><h3>資料與分析</h3><p>整理資料來源，運用課堂概念進行分析。</p></div></div><div class="outline-item"><span>03</span><div><h3>結論與成果</h3><p>提出發現、建議與研究限制，彙整報告簡報。</p></div></div></div></section>''','project'))
save('exercise.html',page('彈性週作業','''<header class="page-intro empty-page"><div class="eyebrow">03 / INDEPENDENT LEARNING</div><h1>彈性週作業</h1><p>延伸課堂中的問題，<br>留下自主學習與思考的過程。</p></header><section class="empty-body"><span class="status-label">準備中</span><h2>等待本學期作業題目。</h2><p>收到老師的 WFH-Q&A 題目後，將在這裡整理題目、回答、參考資料與作業簡報。</p><div class="outline" aria-label="預計整理架構"><div class="outline-item"><span>01</span><div><h3>題目與回答</h3><p>記錄問題，說明思考與回答的依據。</p></div></div><div class="outline-item"><span>02</span><div><h3>資料與成果</h3><p>保留參考來源，彙整完成的簡報。</p></div></div></div></section>''','exercise'))
save('404.html',page('找不到頁面','''<header class="page-intro"><div class="eyebrow">404</div><h1>這一頁尚未收錄。</h1><p>連結可能已變更，請回到首頁繼續閱讀。</p></header><a class="back-link" href="index.html">← 返回首頁</a>'''))
save('assets/beer-game-data.json',json.dumps({'source':'課堂照片 IMG_8218、IMG_8217，工廠週報告','columns':['week','arrivals','inventory','demand','orders'],'rows':data},ensure_ascii=False,indent=2))
print('Built 6 static pages and classroom data. No external build dependencies.')
