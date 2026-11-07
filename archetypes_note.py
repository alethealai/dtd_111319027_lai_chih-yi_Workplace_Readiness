"""11/6 系統基模（四）～（九）筆記內容，由 build.py 呼叫。"""

ARCHETYPES_DATE = '2026-11-06'
ARCHETYPES_SOURCE = 'https://irradiated-banjo-bc0.notion.site/40fc98d8903b80bc9a55dbb22b3434d7'

# 所有趨勢圖共用同一個座標框：橫軸為時間，縱軸只表示高低，不標數值。
AXIS = '<path d="M60 24 V212 H566" class="arc-axis"/><path d="m558 206 8 6-8 6" class="arc-axis"/><text x="566" y="242" text-anchor="end">時間</text>'


def figure(key, title, desc, body, legend, caption):
    items = ''.join(f'<span><b class="arc-key-{cls}"></b>{label}</span>' for cls, label in legend)
    return f'''<figure class="arc-figure" aria-labelledby="{key}-caption">
        <div class="arc-legend">{items}</div>
        <svg class="arc-chart" viewBox="0 0 600 252" role="img" aria-labelledby="{key}-title {key}-desc"><title id="{key}-title">{title}</title><desc id="{key}-desc">{desc}</desc>{AXIS}{body}</svg>
        <figcaption id="{key}-caption">{caption}</figcaption>
      </figure>'''


def bullets(items):
    return '<ul class="arc-list">' + ''.join(f'<li>{item}</li>' for item in items) + '</ul>'


def section(no, key, color, name, quote, traits, chart, examples, actions, extra=''):
    quote_html = f'<blockquote class="arc-quote"><p>{quote}</p></blockquote>' if quote else ''
    return f'''
    <section id="{key}" class="article-section arc-section">
      <p class="arc-no"><span class="arc-swatch arc-swatch-{color}" aria-hidden="true"></span>基模{no}</p>
      <h2>{name}</h2>
      {quote_html}
      <h3 class="arc-sub">特性</h3>
      {bullets(traits)}
      {chart}
      <h3 class="arc-sub">舉例</h3>
      {bullets(examples)}
      {f'<h3 class="arc-sub">對策</h3>{bullets(actions)}' if actions else ''}
      {extra}
    </section>'''


goal_chart = figure(
    'goal', '目標侵蝕趨勢示意',
    '目標標準線一階一階往下降，實際表現跟著標準一起往下滑。',
    '<path d="M60 62 H160 V90 H260 V118 H360 V146 H460 V172 H560" class="arc-line arc-ink"/>'
    '<path d="M60 168 C130 128 190 118 250 132 S390 170 560 196" class="arc-line arc-accent arc-dash"/>'
    '<text x="66" y="50" class="arc-ink-text">目標／標準</text><text x="290" y="184" class="arc-accent-text">實際表現</text>',
    [('ink', '目標／標準'), ('accent', '實際表現')],
    '圖 01／每次壓力一來就把標準調低一點，表現也跟著標準一起往下。示意圖，縱軸不標數值。')

escalation_chart = figure(
    'escalation', '惡性競爭趨勢示意',
    '甲方與乙方的行動強度交替往上加碼，兩條階梯線一路升高。',
    '<path d="M60 196 H140 V164 H260 V118 H380 V74 H500 V42 H560" class="arc-line arc-ink"/>'
    '<path d="M60 200 H200 V142 H320 V96 H440 V56 H560" class="arc-line arc-accent arc-dash"/>'
    '<text x="508" y="32" class="arc-ink-text">甲方</text><text x="520" y="80" class="arc-accent-text">乙方</text>',
    [('ink', '甲方的行動'), ('accent', '乙方的行動')],
    '圖 02／一方加碼，另一方就跟著加碼，雙方輪流把對立往上推。')

rich_chart = figure(
    'rich', '富者愈富趨勢示意',
    '兩條線從同一點出發，一條持續往上，另一條持續往下。',
    '<path d="M60 128 C200 118 350 76 560 36" class="arc-line arc-ink"/>'
    '<path d="M60 128 C200 140 350 176 560 202" class="arc-line arc-accent arc-dash"/>'
    '<circle cx="60" cy="128" r="5" class="arc-dot"/>'
    '<text x="474" y="30" class="arc-ink-text">A 愈來愈好</text><text x="430" y="170" class="arc-accent-text">B 愈來愈差</text>',
    [('ink', '先多拿到資源的一方'), ('accent', '另一方')],
    '圖 03／起點差不多，只因一開始多拿到一點資源，兩邊就往相反方向越拉越開。')

commons_chart = figure(
    'commons', '共同的悲劇趨勢示意',
    '大家的活動量先快速上升，共用資源同時下降，資源耗盡後活動量一起崩落。',
    '<path d="M60 196 C190 192 270 74 350 62 C410 54 450 150 560 200" class="arc-line arc-ink"/>'
    '<path d="M60 48 C240 52 330 96 390 146 S510 202 560 206" class="arc-line arc-accent arc-dash"/>'
    '<text x="300" y="50" class="arc-ink-text">大家的收益</text><text x="74" y="38" class="arc-accent-text">共用資源</text>',
    [('ink', '個體收益加總'), ('accent', '共用資源存量')],
    '圖 04／一開始大家一起成長，資源被用到見底之後，所有人一起受害。')

fix_chart = figure(
    'fix', '飲鴆止渴趨勢示意',
    '每次採取短期對策，問題就暫時下降，但之後反彈得更高，整體一路惡化。',
    '<path d="M60 150 L120 176 L170 132 L230 160 L280 108 L340 138 L390 80 L450 112 L500 52 L560 40" class="arc-line arc-ink"/>'
    '<path d="M120 188 v-8 M230 172 v-8 M340 150 v-8 M450 124 v-8" class="arc-tick"/>'
    '<text x="120" y="204" text-anchor="middle" class="arc-accent-text arc-small">對策</text>'
    '<text x="230" y="188" text-anchor="middle" class="arc-accent-text arc-small">對策</text>'
    '<text x="340" y="166" text-anchor="middle" class="arc-accent-text arc-small">對策</text>'
    '<text x="450" y="140" text-anchor="middle" class="arc-accent-text arc-small">對策</text>'
    '<text x="430" y="40" class="arc-ink-text">問題嚴重度</text>',
    [('ink', '問題嚴重度'), ('accent', '採取短期對策')],
    '圖 05／每用一次短期對策，問題就暫時好一點，但很快又反彈得更高。')

invest_chart = figure(
    'invest', '投資與成長不足趨勢示意',
    '需求快速上升，產能成長緩慢跟不上，最後需求反轉下滑。',
    '<path d="M60 200 C190 192 270 76 370 64 C440 56 490 112 560 152" class="arc-line arc-accent arc-dash"/>'
    '<path d="M60 190 C250 178 400 156 560 140" class="arc-line arc-ink"/>'
    '<text x="300" y="54" class="arc-accent-text">需求（急驚風）</text><text x="410" y="176" class="arc-ink-text">產能（慢郎中）</text>',
    [('accent', '需求'), ('ink', '產能')],
    '圖 06／產能沒有提早擴充，需求衝上去之後品質變差，成長反而掉頭往下。')

talent_chart = figure(
    'talent', '老師畫的 IC 產業與人力成長曲線',
    '產業曲線很快衝到上限，人力曲線成長較慢、較早走平並下滑，training 曲線幾乎平平往前。',
    '<path d="M250 40 H540" class="arc-ceiling"/><text x="546" y="44" class="arc-small">上限</text>'
    '<path d="M60 210 C150 186 230 66 300 46 C360 32 430 52 490 84" class="arc-line arc-ink"/>'
    '<path d="M60 210 C200 184 320 122 400 120 C450 120 500 146 540 172" class="arc-line arc-accent arc-dash"/>'
    '<path d="M60 210 C200 206 320 198 420 192" class="arc-line arc-green arc-dot-dash"/>'
    '<path d="m412 186 10 6-11 4" class="arc-line arc-green"/>'
    '<text x="120" y="112" class="arc-ink-text">IC 產業</text><text x="410" y="110" class="arc-accent-text">HR／人力</text><text x="432" y="200" class="arc-green-text">training</text>',
    [('ink', 'IC 產業'), ('accent', 'HR／人力'), ('green', 'training')],
    '圖 07／依白板重畫。IC 產業很快衝到上限，人力跟培訓的曲線卻追不上，最後人才變成瓶頸。')

sections = ''.join([
    section('四', 'goal', 'green', '目標侵蝕', '努力不一定會成功，但不努力一定很輕鬆。',
        ['結構跟「捨本逐末」很像，但被犧牲的是<strong>目標本身</strong>：每遇到壓力就把標準降低一點，長期目標就慢慢被侵蝕掉。',
         '早期警訊：「把標準降低一點先應付過去，以後再來嚴格要求。」'],
        goal_chart,
        ['<strong>企業</strong>：一家高科技公司生產進度一落後，就把交貨期標準拉長一點，還一直說「我們維持 90% 準時交貨率」。結果客戶早就不滿意，轉向競爭對手購買。',
         '<strong>生活</strong>：躺平、內卷、「及格就好」。原本有成就的人降低了自我期許，能做到的就越來越少。',
         '<strong>產品開發</strong>：上市日期快到了卻還有 bug，只能選「降規格先上市」或「維持規格但延後上市」。',
         '<strong>公共政策</strong>：政府放寬就業、赤字或汙染管制的標準。'],
        ['堅持目標、標準和願景。']),
    section('五', 'escalation', 'blue', '惡性競爭', '你有你的張良計，我有我的過牆梯。',
        ['雙方都覺得要勝過對方才安全，於是一方領先，另一方就感到威脅而加碼，對立就不斷升高。',
         '雙方都認為自己只是在<strong>防衛</strong>，最後局面卻升高到誰都不想要的程度。',
         '早期警訊：「要是對手慢下來，我們就能停止這場仗。」'],
        escalation_chart,
        ['<strong>企業</strong>：兩家嬰兒車公司輪流降價搶市佔率，最後兩家都只能勉強損益兩平，好產品也可能就此消失。',
         '價格戰、廣告戰、專利戰、口水戰、訴訟戰、軍備競賽。',
         '歷史上的外戚 vs. 宦官、中央 vs. 地方、地主 vs. 佃農。',
         '公司內部的預算灌水：一個部門灌水，其他部門有樣學樣。',
         '夫妻爭執、兩代衝突、自行車 vs. 行人。'],
        ['找雙贏的做法，把對方的目標也納入考量。可以先主動釋出善意，降低對方的威脅感。',
         '「相互容忍」（Mutual Forbearance）假說：敵不動，我不動。']),
    section('六', 'rich', 'purple', '富者愈富', '馬太效應，強者愈強、弱者愈弱。「朱門酒肉臭，路有凍死骨。」',
        ['兩個實力相近的活動在搶<strong>同一份有限的資源</strong>。一方一開始只多拿到一點，表現就比較好，接著拿到更多資源，形成增強環路。另一方則陷入反方向的增強環路，越來越差。',
         '資源有限，落後的一方幾乎沒有翻身的機會。',
         '早期警訊：兩個共用資源的活動，一個蒸蒸日上，另一個在掙扎求生。'],
        rich_chart,
        ['<strong>企業</strong>：主管有兩位能力相當的部屬。其中一位請病假一週，主管就把機會給了另一位。後來一位越做越有幹勁，另一位越來越沒安全感，最後離職了。',
         '公司內兩項產品搶預算，先成功的那項拿到更多投資，另一項越來越困難。',
         '害羞的學生一開始成績不好，被貼上「學習遲緩」的標籤，得到的關注越來越少。',
         '工作越忙越少回家，家庭關係就越差，回家也越來越痛苦。'],
        [],
        '''<details class="arc-supplement"><summary>課堂延伸：金觀濤《興盛與危機》，體制失靈造成的死循環</summary>
        <ul class="arc-list">
          <li><strong>基模 = Architectures = 骨架</strong>：基模是看問題用的結構骨架。</li>
          <li><strong>東方的大一統</strong>：分久必合，合久必分。中國傳統是由儒家意識形態、官僚體系、宗法與地主經濟三者綁在一起的「一體化」結構。</li>
          <li><strong>地主 vs. 佃農</strong>：資源越來越集中在地主手上，佃農越來越窮，最後變成流民。這就是富者愈富的增強環路。</li>
          <li><strong>無組織力量</strong>：流民累積成無組織的力量，衝垮整個體制。崩潰之後重組，但結構沒變，貧富差距又慢慢拉開，所以一直陷在同一個循環裡。</li>
          <li><strong>西方沒有大一統</strong>：從城堡到莊園再到邦聯，是由下往上組成的。United States 因為不信任中央，各州聯合起來；參議院每州 2 席，眾議院依人口分配席次，用制度來避免大州吃掉小州。United Kingdom 則是由不同王國重組而成。</li>
        </ul></details>'''),
    section('七', 'commons', 'brown', '共同的悲劇（公地悲劇）', '',
        ['很多人各自為了自己的需求，共用一項<strong>看起來很充裕、其實有上限</strong>的資源。',
         '一開始大家都成長得很快，後來收益開始遞減，越努力成長越慢，最後資源耗盡，大家一起受害。',
         '早期警訊：「以前很充裕，現在越來越難，我得更努力才拿得到。」'],
        commons_chart,
        ['<strong>企業</strong>：好幾個部門共用一組銷售人員，一開始效果很好。後來每個部門都要人支援，業務員過勞（Burnout！）大量離職，結果所有部門的銷售力都大減。',
         '同一家公司六個部門的業務員輪流向同一位客戶推銷互相競爭的產品，損害的是公司形象這項共有資源。',
         '濫採礦產、過度捕撈；酸雨、臭氧層破洞、溫室效應。'],
        ['透過教育、自我節制和同儕壓力，或由參與者共同設計調節機制。',
         '禁止與管制：公開限制、開罰。',
         '配額（Quota）分配。',
         '使用者付費，提高使用的代價。',
         '想辦法增加資源的總量。']),
    section('八', 'fix', 'black', '飲鴆止渴', '短期有效，長期更糟，而且會越來越依賴這個解法。',
        ['這個對策當下確實有效，但後遺症越來越嚴重，問題反而更惡化，最後變成對解方本身上癮。',
         '早期警訊：「以前一直都有效，為什麼現在不靈了？」'],
        fix_chart,
        ['<strong>企業</strong>：總裁為了讓投資報酬率好看，延後購買新的生產機器。帳面數字馬上變好看，但製造品質下滑、口碑變差，需求跟著下跌，總裁就更不願意投資。',
         '<strong>讀書</strong>：不求理解、瘋狂刷題，甚至只背答案。',
         '借錢付利息，之後要付更多利息。',
         '砍維修預算來省成本，結果故障更多、成本更高。',
         '景氣不好就裁員、砍預算，支出降了，組織的動力也沒了。'],
        ['把眼光放在長期。如果可以，就完全不用短期對策。',
         '除非它只是「緩兵之計」，用空間換取時間，去找更好的長期解法。']),
    section('九', 'invest', 'white', '投資與成長不足', '深根才能成長，設限才能茁壯。',
        ['由「成長上限」加上「捨本逐末」組合而成。',
         '成長快碰到上限時，應該<strong>提早而且積極地</strong>投資產能，才能突破上限。但多數人會降低目標或標準，把投資不足合理化。',
         '結果產能擴充像「慢郎中」，需求成長卻像「急驚風」，服務品質下降、競爭者進場、士氣低落，成長甚至會反轉。',
         '重點：投資不足的是<strong>能帶動未來成長的產能（capacity）</strong>，不是眼前的成長活動。',
         '早期警訊：「我們一直是最好的，以後會更好，但現在要先保留資源，不要過度投資。」'],
        invest_chart + talent_chart + bullets([
            '<strong>Emerging Growth</strong>：突然爆紅，就放棄現在的、跑去做新的項目。原本的核心沒有繼續投資，新的項目也還沒站穩。',
            '<strong>事業 vs. 身體</strong>：老師畫了事業曲線一路往上、身體曲線往下。個人事業快速成長，卻沒有投資在健康和家庭上，最後反過來拖垮事業。']),
        ['<strong>小吃店</strong>：一開始座位少、服務好。客人變多以後排隊變長、環境變亂，服務品質越來越差。',
         '只有很壯觀的願景，卻從來不評估要多少時間和努力才做得到。',
         '經濟快速成長時，交通、水電、通訊、人力、法規這些需要長時間建設的基礎沒有提早投資。',
         '<strong>《小，是我故意的》（Small Giants）</strong>：書裡的公司不是做不大，而是刻意選擇不擴張，把力氣放在做好自己的核心。我喜歡「小剛剛好」這個想法。老師上課提到 Apple，它的技術不一定是市場上最早出現的，但它不會被新項目牽著走，而是專心把核心產品做到最好，做出別人沒有的特色。這讓我想到老師說的「深根才能成長，設限才能茁壯」：先往下扎根，成長才站得穩；替自己設下界線，才不會被一時的機會拉走。老師也說，有些產業本來就沒有發大財的機會，別人不想進場投資，自己在裡面的市佔率又高到別人進不來，「小」反而成了保護。'],
        ['如果確實有成長潛力，就在需求來之前擴充產能。',
         '也可以刻意不成長或放慢成長，例如限時、限量供應。',
         '如果成長已經開始變慢，就不要再硬推成長，應該把力氣放在擴充產能上。']),
])

TOC = [('goal', '基模四 目標侵蝕'), ('escalation', '基模五 惡性競爭'), ('rich', '基模六 富者愈富'),
       ('commons', '基模七 共同的悲劇'), ('fix', '基模八 飲鴆止渴'), ('invest', '基模九 投資與成長不足'), ('reflection', '我的反思'), ('sources', '參考資料')]


def render_note(course_url):
    toc = ''.join(f'<a href="#{key}">{label}</a>' for key, label in TOC)
    return f'''
<nav class="breadcrumbs" aria-label="麵包屑"><a href="../notes.html">每週筆記</a><span aria-hidden="true">/</span><span>系統基模</span></nav>
<header class="article-head arc-head">
  <p class="article-meta"><time datetime="{ARCHETYPES_DATE}">{ARCHETYPES_DATE}</time> · 課堂筆記</p>
  <h1>系統基模（四）～（九）</h1>
  <p class="article-subtitle">看懂問題背後反覆出現的結構。</p>
  <div class="tags"><span>系統思考</span><span>系統基模</span><span>增強環路</span></div>
  <p class="article-intro">這週老師介紹了基模四到基模九。我依老師的課程頁面和課堂白板，把每個基模的特性、例子和對策整理在一起，並畫了趨勢圖來看它們隨時間怎麼變化。</p>
</header>
<div class="article-layout">
  <nav class="article-toc" aria-label="本篇目錄"><p class="section-label">IN THIS NOTE</p>{toc}</nav>
  <article class="article-content arc-note">
    <p class="source-note">每張趨勢圖都是我自己畫的示意圖，橫軸是時間，縱軸只看高低、不標數值；只有圖 07 是依老師白板重畫的。</p>
    {sections}
    <section id="reflection" class="article-section">
      <h2>我的反思</h2>
      <div class="reflection"><p>這週的六個基模裡，最顛覆我認知的是「投資與成長不足」。之前在<a href="people-express.html">人民航空的經營模擬</a>中，我前期擴張得很快，營收和利潤也逐年上升，我一度以為這樣就是對的。直到後來淨利開始下跌，我才發現問題不是成長不夠，而是投資跟不上成長。後來我改變策略，先暫停擴張，把現有的規模和服務品質顧好，公司才慢慢走出困境。現在回頭看，這就是休養生息、韜光養晦的智慧：穩穩地長大，比轟動一時就結束更重要。</p><p>我發現這也出現在我的生活裡。我常常心血來潮，突然想做很多事，把時間表排得滿滿的。現在我覺得那也是一種「成長過快」：目標一下子拉得太高，能力卻還跟不上，最後事事力不從心，堅持沒多久就放棄了。這讓我學會，有時候要替自己的成長設限，先把能做好的事做好，再一步步往上加。這也是我對「深根才能成長，設限才能茁壯」最真實的體會。</p></div>
    </section>
    <section id="sources" class="article-section">
      <h2>參考資料</h2>
      <ol class="sources"><li>2026/11/6 課堂白板與 iPad 筆記照片。圖 07 依白板重畫，其餘趨勢圖是我整理時畫的示意圖。</li><li><a href="{ARCHETYPES_SOURCE}" target="_blank" rel="noopener noreferrer">張朝清老師｜系統基模九式 ↗</a></li><li>金觀濤、劉青峰《興盛與危機：論中國社會超穩定結構》（課堂口述延伸）。</li><li>Bo Burlingham《小，是我故意的》（Small Giants），課堂介紹的延伸閱讀。</li><li><a href="{course_url}" target="_blank" rel="noopener noreferrer">張朝清老師｜115-1 職場即戰力課程網站 ↗</a></li></ol>
    </section>
    <a class="back-link" href="../notes.html">← 返回每週筆記</a>
  </article>
</div>'''
