# Brand comparison hub and sub-pages (imported by content/pages.py)

COMP = [("Compare brands", "/compare/")]

SRC_COMPARE = '''<h2>Sources</h2><ul class="sources">
<li>Garmin R10 manual: https://www8.garmin.com/manuals/webhelp/GUID-E2BBF6BE-4276-436F-B697-59ABEFD61933/EN-US/GUID-88F65277-47D4-403D-8F79-719CAA256D6B.html</li>
<li>Garmin R50 manual (PDF): https://www8.garmin.com/manuals/webhelp/GUID-D31AA1A2-C026-46EB-9699-FA94F1E8AF0B/EN-US/Approach_R50_OM_EN-US.pdf</li>
<li>Rapsodo golf FAQ (MLM2PRO): https://rapsodo.com/pages/frequently-asked-golf-questions-faq</li>
<li>SkyTrak plan your space and ST MAX guide: https://www.skytrakgolf.com/pages/plan-your-space</li>
<li>Shop Indoor Golf (retailer) Square Golf Omni specs: https://shopindoorgolf.com/products/square-omni-launch-monitor</li>
<li>Shot Scope LM1 UK specifications: https://shotscope.com/uk/shop/products/golf-launch-monitors/lm1-launch-monitor/</li>
<li>Bushnell Golf Europe Launch Pro specifications: https://bushnellgolfeurope.com/product/launch-pro/</li>
<li>Uneekor UK EYE MINI LITE &amp; EYE MINI specifications: https://uneekor.com/en-gb/products/eye-mini-lite-standalone</li>
<li>Uneekor EYE MINI LITE manual (PDF): https://download.uneekor.com/docs/EYE_MINI_LITE_Manual.pdf</li>
<li>FlightScope Mevo and Mevo+ FAQ: https://flightscope.com/pages/faq</li>
<li>BenQ AH700ST &amp; TH671ST specs: https://www.benq.com/en-us/projector/golf/ah700st/spec.html</li>
<li>Optoma GT1080HDR specs: https://www.optomausa.com/product/gt1080hdr</li>
<li>Amazon UK listings checked on [[checked]] (links tagged stewraw25-21).</li>
</ul>'''

COMPARE_PAGE = dict(
    path="/compare/",
    title="Compare Golf Simulator & Launch Monitor Brands (UK)",
    short="Compare brands",
    crumbs=[],
    type="article",
    js=True,
    description="Compare 8 golf launch monitor brands (Garmin, Rapsodo, SkyTrak, Bushnell, Uneekor, FlightScope, Square, Shot Scope) plus UK nets, mats and projectors.",
    h1="Compare home simulator brands side by side",
    hero=dict(
        variant="hero-compare",
        eyebrow="Brand-by-brand hub",
        lede="Compare tracking technology, placement, subscription rules and verified UK price bands across launch monitors, enclosures, hitting mats, projectors and sim racing hardware.",
        cta_primary=("Jump to launch monitor table", "#launch-monitor-matrix"),
        cta_secondary=("Check room sizes", "/golf/room-size-guide/"),
        stats=[("8", "launch monitor brands"), ("10", "net, mat & projector brands"), ("7", "sim racing brands")],
        svg="compare-hero",
    ),
    itemlist=[
        ("Garmin Approach launch monitors", "/golf/launch-monitors/#garmin-approach-r10"),
        ("Rapsodo MLM2PRO", "/golf/launch-monitors/#rapsodo-mlm2pro"),
        ("SkyTrak ST MAX", "/golf/launch-monitors/#skytrak-st-max"),
        ("Square Golf launch monitors", "/golf/launch-monitors/#square-golf-indoor"),
        ("Shot Scope LM1", "/golf/launch-monitors/#shot-scope-lm1"),
        ("SimSpace nets and enclosures", "/golf/simulators/#simspace-enclosure"),
        ("BenQ short-throw projectors", "/golf/simulators/#benq-ah700st"),
    ],
    faq=[
        ("Which launch monitor brands need the least room depth?", "Photometric camera units that sit beside the ball — including Garmin Approach R50, SkyTrak ST MAX, Square Golf, Bushnell Launch Pro, Foresight GC3 and Uneekor EYE MINI / EYE MINI LITE — do not need 1.8 to 2.7 m of open floor behind the golfer. You still need safe ball-to-screen distance and full swing clearance."),
        ("Which launch monitor brands have no mandatory subscription?", "Shot Scope LM1 uses the free Shot Scope mobile app with no subscription. Foresight GC3 (sold in the UK at £7,500) includes FSX Play software with no recurring fee. FlightScope Mevo+ includes bundled E6 courses and supports direct GSPro connection without a FlightScope subscription, though third-party sim software licences still apply separately."),
        ("Which launch monitors work without a gaming PC?", "Shot Scope LM1 has its own 3.5 inch screen and mobile app. Garmin Approach R50 has a built-in 10 inch touchscreen. Garmin R10, Rapsodo MLM2PRO and Uneekor EYE MINI support mobile or iPad apps (Uneekor EYE MINI LITE requires a wired Windows PC)."),
        ("Are Amazon product prices on this page live?", "No. Amazon UK prices shown here were checked on 24 Nov 2026 and change frequently. Always check Amazon UK or the maker's UK store for the current price before buying."),
        ("Do you test these simulator brands hands-on?", "No. We research every figure from makers' manuals, official UK product pages and Amazon UK listings, and we have not tested these products ourselves."),
    ],
    related=[
        ("/compare/radar-vs-camera-launch-monitors/", "Radar vs camera launch monitors", "How placement, room depth and left/right-handed bays differ by brand."),
        ("/compare/launch-monitor-subscriptions/", "Launch monitor subscriptions compared", "Free apps vs annual software memberships across 8 brands."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Compare Shot Scope LM1, Garmin R10, Rapsodo MLM2PRO and Square Golf indoor."),
    ],
    body='''<p class="lede">Start by filtering the category you are pricing up. Launch monitor brands differ mostly on where the unit sits (behind the ball vs beside it), whether simulator play needs an annual subscription, and whether you need a gaming PC.</p>
<h2>Quick brand comparisons</h2>
<div class="cards two">
  <a class="card tile" href="[[BP]]/compare/radar-vs-camera-launch-monitors/"><div><span class="card-tag">Deep dive</span><h3>Radar vs camera brands</h3><p>Behind-the-ball depth vs beside-the-ball side clearance, plus dual-handed play.</p></div><span class="tile-cta">Compare placement &rarr;</span></a>
  <a class="card tile" href="[[BP]]/compare/launch-monitor-subscriptions/"><div><span class="card-tag gold">Running costs</span><h3>Subscriptions &amp; software compared</h3><p>Which brands include free software vs annual fees for courses and GSPro.</p></div><span class="tile-cta">Compare software terms &rarr;</span></a>
</div>
<div class="filter-bar" role="group" aria-label="Filter brand categories" data-filter-group data-target="#brand-sections">
  <button type="button" class="filter-btn is-active" data-filter="all" aria-pressed="true">All brands</button>
  <button type="button" class="filter-btn" data-filter="lm" aria-pressed="false">Launch monitors (8)</button>
  <button type="button" class="filter-btn" data-filter="nets" aria-pressed="false">Nets &amp; enclosures (5)</button>
  <button type="button" class="filter-btn" data-filter="mats" aria-pressed="false">Hitting mats (3)</button>
  <button type="button" class="filter-btn" data-filter="proj" aria-pressed="false">Projectors (2)</button>
  <button type="button" class="filter-btn" data-filter="racing" aria-pressed="false">Sim racing (7)</button>
</div>

<div id="brand-sections">
<section data-cat="lm">
<h2 id="launch-monitor-matrix">Launch monitor &amp; simulator brands compared</h2>
<p>Every figure below comes from the maker's manual, official UK store page, or the Amazon UK listing checked on [[checked]] (Square Golf Omni room figure from retailer Shop Indoor Golf).</p>
<div class="tbl"><table>
<thead><tr>
  <th>Brand &amp; models</th>
  <th>Tracking tech</th>
  <th>Placement</th>
  <th>Subscription / software notes</th>
  <th>UK price band</th>
  <th>Where to check</th>
</tr></thead>
<tbody>
<tr>
  <td><strong>Shot Scope</strong><br><span class="small">LM1</span></td>
  <td><span class="badge badge-radar">Doppler radar</span></td>
  <td>Behind ball (~1.4–1.5 m)</td>
  <td><span class="badge badge-free">Free app</span> Shot Scope mobile app included; built-in 3.5" screen</td>
  <td>[[price:shot-scope-lm1]] (Amazon UK) / £179.99 RRP</td>
  <td>[[buy:shot-scope-lm1|Amazon UK]]</td>
</tr>
<tr>
  <td><strong>Garmin</strong><br><span class="small">Approach R10 / R50</span></td>
  <td><span class="badge badge-radar">R10: Radar</span><br><span class="badge badge-camera">R50: 3-camera</span></td>
  <td>R10: 1.8–2.4 m behind<br>R50: ~0.5 m beside tee</td>
  <td><span class="badge badge-sub">Subscription for sim</span> Virtual rounds require active Garmin Golf membership</td>
  <td>[[price:garmin-approach-r10]] (R10) to [[price:garmin-approach-r50]] (R50)</td>
  <td>[[buy:garmin-approach-r10|R10 Amazon]] &middot; [[buy:garmin-approach-r50|R50 Amazon]]</td>
</tr>
<tr>
  <td><strong>Rapsodo</strong><br><span class="small">MLM2PRO</span></td>
  <td><span class="badge badge-hybrid">Radar + 2 cameras</span></td>
  <td>6.5–8.5 ft behind ball (~14 ft+ total indoor depth)</td>
  <td><span class="badge badge-sub">Membership</span> Simulation &amp; impact vision tiers via Rapsodo</td>
  <td>[[price:rapsodo-mlm2pro]] (Amazon UK)</td>
  <td>[[buy:rapsodo-mlm2pro|Amazon UK]]</td>
</tr>
<tr>
  <td><strong>Square Golf</strong><br><span class="small">Indoor / Omni</span></td>
  <td><span class="badge badge-camera">Camera</span></td>
  <td>Beside tee (~14–20 in for Omni, retailer figure)</td>
  <td><span class="badge badge-sub">Check bundle</span> Indoor simulation software included or per-round credits</td>
  <td>[[price:square-golf-indoor]] to [[price:square-golf-omni]]</td>
  <td>[[buy:square-golf-indoor|Indoor]] &middot; [[buy:square-golf-omni|Omni Amazon]]</td>
</tr>
<tr>
  <td><strong>SkyTrak</strong><br><span class="small">ST MAX</span></td>
  <td><span class="badge badge-camera">Photometric + radar</span></td>
  <td>Beside ball (10x10 ft min area; 16–17 ft depth recommended)</td>
  <td><span class="badge badge-sub">Annual plan</span> Amazon listing includes 1-year software; renewal after year 1</td>
  <td>[[price:skytrak-st-max]] (Amazon UK)</td>
  <td>[[buy:skytrak-st-max|Amazon UK]]</td>
</tr>
<tr>
  <td><strong>Uneekor</strong><br><span class="small">EYE MINI LITE / EYE MINI</span></td>
  <td><span class="badge badge-camera">2-camera IR</span></td>
  <td>Beside ball (~40 cm / 16 in, parallel to target)</td>
  <td><span class="badge badge-sub">Tiered software</span> Player Package included; 3rd-party sim (GSPro) &amp; AI need paid tier</td>
  <td>£1,699–£1,999 (LITE) / £2,999 (EYE MINI, Uneekor UK)</td>
  <td>https://uneekor.com/en-gb/products/eye-mini-lite-standalone</td>
</tr>
<tr>
  <td><strong>FlightScope</strong><br><span class="small">Mevo Gen2 / Mevo+</span></td>
  <td><span class="badge badge-radar">3D Doppler radar</span></td>
  <td>7–9 ft behind tee (8–13 ft indoor ball flight)</td>
  <td><span class="badge badge-free">No FlightScope sub</span> E6 courses included on Mevo+; direct GSPro support</td>
  <td>~£1,199 (Gen2) to £1,759 (Mevo+, UK retailers)</td>
  <td>https://flightscope.com/products/mevo-plus</td>
</tr>
<tr>
  <td><strong>Bushnell / Foresight</strong><br><span class="small">Launch Pro / GC3</span></td>
  <td><span class="badge badge-camera">3-camera IR</span></td>
  <td>Beside ball (7" x 10" hitting zone)</td>
  <td>Launch Pro: Foresight+ sub for club data/sim (note: US region check every 45 days). GC3: FSX Play included, no sub</td>
  <td>£2,490 (Launch Pro EU) / £7,500 (GC3 UK)</td>
  <td>https://bushnellgolfeurope.com/product/launch-pro/</td>
</tr>
</tbody>
</table></div>

<h2>PC, screen &amp; ball requirements by brand</h2>
<div class="tbl"><table>
<thead><tr>
  <th>Brand &amp; model</th>
  <th>Built-in display</th>
  <th>PC required</th>
  <th>Special ball / stickers indoors</th>
  <th>Budget band (UK)</th>
</tr></thead>
<tbody>
<tr><td><strong>Shot Scope LM1</strong></td><td>Yes (3.5" colour)</td><td>No (phone app)</td><td>No special balls needed for ball/club speed</td><td>Under £500</td></tr>
<tr><td><strong>Garmin Approach R10</strong></td><td>No (LED indicator)</td><td>No (Garmin Golf app)</td><td>Works with standard balls; Titleist RCT option</td><td>Under £500</td></tr>
<tr><td><strong>Rapsodo MLM2PRO</strong></td><td>No (app device)</td><td>No (mobile/tablet)</td><td>Rapsodo RPT balls for spin metrics</td><td>Under £500</td></tr>
<tr><td><strong>Square Golf indoor / Omni</strong></td><td>Check listing</td><td>No / Windows &amp; mobile</td><td>Marked balls / club stickers per model</td><td>£500 – £2,000</td></tr>
<tr><td><strong>SkyTrak ST MAX</strong></td><td>No</td><td>PC / iPad / Mac</td><td>Standard golf balls</td><td>£500 – £2,000</td></tr>
<tr><td><strong>FlightScope Mevo+</strong></td><td>No</td><td>No (mobile/iPad or PC)</td><td>Metallic dot stickers or Titleist RCT balls for indoor spin</td><td>£500 – £2,000</td></tr>
<tr><td><strong>Uneekor EYE MINI LITE</strong></td><td>No (LED status)</td><td>Yes (Windows PC + Ethernet)</td><td>Standard balls (club stickers for club data)</td><td>£500 – £2,000</td></tr>
<tr><td><strong>Uneekor EYE MINI</strong></td><td>Yes (on-unit)</td><td>Optional (iOS VIEW Air or PC)</td><td>Standard balls (club stickers for club data)</td><td>£2,000+</td></tr>
<tr><td><strong>Bushnell Launch Pro</strong></td><td>Yes (3" x 2" LCD)</td><td>Optional (PC for Premier sim)</td><td>Standard balls (club markers for club data)</td><td>£2,000+</td></tr>
<tr><td><strong>Garmin Approach R50</strong></td><td>Yes (10" touchscreen)</td><td>No (standalone display)</td><td>Standard balls (club sticker for face-to-path)</td><td>£2,000+</td></tr>
<tr><td><strong>Foresight GC3</strong></td><td>Yes (on-unit LCD)</td><td>Optional (PC for FSX Play)</td><td>Standard balls (club markers for club data)</td><td>£2,000+</td></tr>
</tbody>
</table></div>

<h2>Launch monitor brand profiles</h2>
<div class="filter-bar" role="group" aria-label="Filter launch monitor brands by setup" data-filter-group data-attr="data-lm" data-target="#lm-cards">
  <button type="button" class="filter-btn is-active" data-filter="all" aria-pressed="true">All 8 brands</button>
  <button type="button" class="filter-btn" data-filter="beside" aria-pressed="false">Beside ball (saves depth)</button>
  <button type="button" class="filter-btn" data-filter="behind" aria-pressed="false">Behind ball (radar)</button>
  <button type="button" class="filter-btn" data-filter="under1k" aria-pressed="false">Under £1,000 options</button>
  <button type="button" class="filter-btn" data-filter="nosub" aria-pressed="false">No mandatory sub option</button>
</div>
<div class="brand-grid" id="lm-cards">
  <div class="brand-card" data-lm="behind beside under1k">
    <div>
      <div class="brand-top"><h3>Garmin (R10 &amp; R50)</h3><span class="badge badge-hybrid">Radar &amp; Camera</span></div>
      <p class="small">Covers both entry-level portable radar and standalone touchscreen camera simulation.</p>
      <ul class="brand-specs">
        <li><strong>Approach R10 ([[price:garmin-approach-r10]]):</strong> IPX7 radar, 10h battery, 1.8–2.4 m behind tee. Amazon listing notes international version sold from abroad.</li>
        <li><strong>Approach R50 ([[price:garmin-approach-r50]]):</strong> 3-camera unit beside tee (~0.5 m) with built-in 10" colour touchscreen and 4h battery.</li>
        <li><strong>Software note:</strong> Virtual rounds require a Garmin Golf subscription.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn" href="https://www.amazon.co.uk/dp/B095QX1FSR?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">R10 on Amazon &rarr;</a>
      <a class="btn-outline" href="[[BP]]/golf/garmin-r50-vs-skytrak-st-max/">R50 vs ST MAX</a>
    </div>
  </div>

  <div class="brand-card" data-lm="behind under1k">
    <div>
      <div class="brand-top"><h3>Rapsodo (MLM2PRO)</h3><span class="badge badge-hybrid">Dual Camera + Radar</span></div>
      <p class="small">Combines Doppler radar behind the golfer with dual optical cameras for shot &amp; impact video.</p>
      <ul class="brand-specs">
        <li><strong>MLM2PRO ([[price:rapsodo-mlm2pro]]):</strong> Sits 6.5–8.5 ft behind the ball, with at least 8 ft to net (over 14 ft total depth).</li>
        <li><strong>Key feature:</strong> Shot Vision and Impact Vision swing replay in the Rapsodo app.</li>
        <li><strong>Ceiling guidance:</strong> Rapsodo notes 9 ft may fit players around 5 ft 8 in and under; taller players may need 10–11 ft.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn" href="https://www.amazon.co.uk/dp/B0BTPZMCSF?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">MLM2PRO on Amazon &rarr;</a>
      <a class="btn-outline" href="[[BP]]/golf/launch-monitors-under-1000/">Under £1,000 guide</a>
    </div>
  </div>

  <div class="brand-card" data-lm="beside">
    <div>
      <div class="brand-top"><h3>SkyTrak (ST MAX)</h3><span class="badge badge-camera">Beside-Ball Photometric</span></div>
      <p class="small">Long-standing indoor simulator brand placing sensors beside the tee to save room depth.</p>
      <ul class="brand-specs">
        <li><strong>ST MAX ([[price:skytrak-st-max]]):</strong> Dual Doppler radar + photometric cameras; Amazon UK listing includes 1-year software and GOLFTEC speed training.</li>
        <li><strong>Space requirement:</strong> SkyTrak lists a 10 ft x 10 ft minimum unobstructed area and 16–17 ft depth for full enclosures.</li>
        <li><strong>Left/right handers:</strong> Unit moves to the opposite side of the mat for left-handed golfers.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn" href="https://www.amazon.co.uk/dp/B0FXNBJFG3?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">ST MAX on Amazon &rarr;</a>
      <a class="btn-outline" href="[[BP]]/golf/garmin-r50-vs-skytrak-st-max/">Compare with R50</a>
    </div>
  </div>

  <div class="brand-card" data-lm="beside under1k">
    <div>
      <div class="brand-top"><h3>Square Golf (Indoor &amp; Omni)</h3><span class="badge badge-camera">Compact Camera</span></div>
      <p class="small">Dedicated indoor camera units priced between entry radar monitors and higher-end commercial units.</p>
      <ul class="brand-specs">
        <li><strong>Square Golf indoor ([[price:square-golf-indoor]]):</strong> Compact indoor unit under £700 when checked.</li>
        <li><strong>Square Golf Omni ([[price:square-golf-omni]]):</strong> Beside-the-golfer placement (~14–20 in from tee; retailer Shop Indoor Golf suggests 9 ft H x 10 ft W x 12 ft D).</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn" href="https://www.amazon.co.uk/dp/B0DD83PR5L?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">Square Indoor on Amazon &rarr;</a>
      <a class="btn-outline" href="https://www.amazon.co.uk/dp/B0HLDR2FBB?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">Omni on Amazon</a>
    </div>
  </div>

  <div class="brand-card" data-lm="behind under1k nosub">
    <div>
      <div class="brand-top"><h3>Shot Scope (LM1)</h3><span class="badge badge-radar">Entry Doppler Radar</span></div>
      <p class="small">UK golf-tech brand offering a compact screen-equipped radar monitor with no app subscription.</p>
      <ul class="brand-specs">
        <li><strong>LM1 ([[price:shot-scope-lm1]]):</strong> K-band 24 GHz radar placed ~1.4–1.5 m (55 in) behind the ball; 300 g, ~5h USB-C battery, IPX3 rated.</li>
        <li><strong>Display &amp; data:</strong> 3.5" colour screen showing ball speed, club speed, smash factor, carry and total distance.</li>
        <li><strong>Software note:</strong> Free lifetime Shot Scope mobile app; built for range and net practice rather than full course simulation.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn" href="https://www.amazon.co.uk/dp/B0GP22ZYY5?tag=stewraw25-21" rel="sponsored nofollow noopener" target="_blank">LM1 on Amazon &rarr;</a>
      <a class="btn-outline" href="[[BP]]/golf/launch-monitors-under-1000/">Under £1,000 guide</a>
    </div>
  </div>

  <div class="brand-card" data-lm="beside">
    <div>
      <div class="brand-top"><h3>Uneekor (EYE MINI &amp; LITE)</h3><span class="badge badge-camera">Dual IR Cameras</span></div>
      <p class="small">Known for high-speed impact video (Club Optix) and dimple-reading ball tracking without marked balls.</p>
      <ul class="brand-specs">
        <li><strong>EYE MINI LITE (£1,699–£1,999 Uneekor UK):</strong> Indoor-only wired unit (mains power + CAT-6 Ethernet to Windows PC); 19 data points; 12" x 8" hitting zone.</li>
        <li><strong>EYE MINI (£2,999 Uneekor UK):</strong> Portable version with 6–8h battery, on-unit display and iOS VIEW Air support.</li>
        <li><strong>Software note:</strong> Includes Player Package; GSPro / 3rd-party simulation and AI Trainer require a paid tier.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn-outline" href="https://uneekor.com/en-gb/products/eye-mini-lite-standalone" rel="noopener" target="_blank">Uneekor UK specs &rarr;</a>
    </div>
  </div>

  <div class="brand-card" data-lm="behind nosub">
    <div>
      <div class="brand-top"><h3>FlightScope (Mevo Gen2 &amp; Mevo+)</h3><span class="badge badge-radar">3D Doppler Radar</span></div>
      <p class="small">Radar systems placed behind the tee, suited to dual-handed bays because nothing sits beside the mat.</p>
      <ul class="brand-specs">
        <li><strong>Mevo+ (£1,759 UK retail) &amp; Gen2 (~£1,199):</strong> Placed 7–9 ft behind the tee with 8–13 ft indoor ball flight recommended.</li>
        <li><strong>Ball requirement:</strong> Uses metallic dot stickers or Titleist RCT balls indoors for spin measurement.</li>
        <li><strong>Software note:</strong> No mandatory FlightScope subscription; Mevo+ bundles E6 courses and integrates directly with GSPro.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn-outline" href="https://flightscope.com/products/mevo-plus" rel="noopener" target="_blank">FlightScope Mevo+ specs &rarr;</a>
    </div>
  </div>

  <div class="brand-card" data-lm="beside nosub">
    <div>
      <div class="brand-top"><h3>Bushnell &amp; Foresight (Launch Pro / GC3)</h3><span class="badge badge-camera">Triscopic 3-Camera</span></div>
      <p class="small">Sibling hardware platforms built on Foresight's three-camera infrared tracking beside the ball.</p>
      <ul class="brand-specs">
        <li><strong>Bushnell Launch Pro (£2,490 Bushnell Europe):</strong> Lower upfront hardware cost; club data and simulation require an annual Foresight+ membership. Check UK/EU vs US unit terms carefully (Bushnell notes US Launch Pro units require a US internet check every 45 days).</li>
        <li><strong>Foresight GC3 (£7,500 UK retail):</strong> Unlocked outright purchase with FSX Play included and no recurring subscription.</li>
      </ul>
    </div>
    <div class="brand-foot">
      <a class="btn-outline" href="https://bushnellgolfeurope.com/product/launch-pro/" rel="noopener" target="_blank">Bushnell Europe specs &rarr;</a>
    </div>
  </div>
</div>
</section>

<section data-cat="nets">
<h2>Nets, enclosures &amp; impact screen brands</h2>
<p>Checked on Amazon UK on [[checked]]. Always leave the net or screen maker's stated clearance behind the fabric so the wall is never struck.</p>
<div class="tbl"><table>
<thead><tr><th>Brand</th><th>Checked products</th><th>Sizes from listing</th><th>Price checked</th><th>Category</th></tr></thead>
<tbody>
<tr><td><strong>SimSpace</strong></td><td>Deluxe Driving Net / Simulator Enclosure / Impact Screen</td><td>Net 2.5 x 2.5 x 3.84 m; Screen 2.4 x 2.5 m</td><td>[[price:simspace-impact-screen]] – [[price:simspace-enclosure]]</td><td>Nets, bays &amp; screens</td></tr>
<tr><td><strong>Hillman PGM</strong></td><td>3m Practice Cage &amp; Net</td><td>3 m x 3 m cage</td><td>[[price:hillman-pgm-3m-cage]]</td><td>Full cage</td></tr>
<tr><td><strong>FORZA</strong></td><td>7ft x 7ft Pop-Up Golf Net</td><td>7 ft x 7 ft (approx. 2.1 x 2.1 m)</td><td>[[price:forza-7ft-net]]</td><td>Garden pop-up net</td></tr>
<tr><td><strong>GoSports</strong></td><td>Golf Simulator Impact Screen</td><td>See Amazon UK listing</td><td>[[price:gosports-impact-screen]]</td><td>Impact screen</td></tr>
<tr><td><strong>Amazon Basics</strong></td><td>Portable Golf Practice Net</td><td>2.44 m x 2.44 m</td><td>[[price:amazon-basics-golf-net]]</td><td>Portable practice net</td></tr>
</tbody>
</table></div>
<p>See full product cards in [[link:/golf/nets-and-mats/|Nets and mats]], [[link:/golf/golf-nets-for-the-garden/|Garden golf nets]], and [[link:/golf/simulators/|Home simulator bays]].</p>
</section>

<section data-cat="mats">
<h2>Hitting mat brands</h2>
<div class="tbl"><table>
<thead><tr><th>Brand</th><th>Model</th><th>Dimensions / note</th><th>Price checked</th><th>Amazon UK</th></tr></thead>
<tbody>
<tr><td><strong>Spurk</strong></td><td>Winter Strike Mat</td><td>Compact strike strip</td><td>[[price:spurk-winter-strike-mat]]</td><td>[[buy:spurk-winter-strike-mat|Check price]]</td></tr>
<tr><td><strong>COSTWAY</strong></td><td>Golf Hitting Mat</td><td>Multi-turf practice mat</td><td>[[price:costway-hitting-mat]]</td><td>[[buy:costway-hitting-mat|Check price]]</td></tr>
<tr><td><strong>GIRAFFYCO</strong></td><td>1.5 x 1.2 m Hitting Mat</td><td>1.5 m x 1.2 m stance + hitting area</td><td>[[price:giraffyco-hitting-mat]]</td><td>[[buy:giraffyco-hitting-mat|Check price]]</td></tr>
</tbody>
</table></div>
</section>

<section data-cat="proj">
<h2>Short-throw projector brands</h2>
<p>Short-throw projectors sit closer to the impact screen so the golfer does not cast a shadow across the image. Verify exact throw distance against your bay depth on each maker's throw calculator.</p>
<div class="tbl"><table>
<thead><tr><th>Brand &amp; model</th><th>Resolution &amp; light</th><th>Brightness</th><th>Throw ratio (maker)</th><th>Price checked</th><th>Amazon UK</th></tr></thead>
<tbody>
<tr><td><strong>BenQ TH671ST</strong></td><td>1080p Lamp</td><td>3,000 ANSI lm</td><td>0.69–0.83 (1.2x zoom)</td><td>[[price:benq-th671st]]</td><td>[[buy:benq-th671st|TH671ST]]</td></tr>
<tr><td><strong>Optoma GT1080HDR</strong></td><td>1080p Lamp</td><td>3,800 lm</td><td>0.49:1 (fixed lens)</td><td>[[price:optoma-gt1080hdr]]</td><td>[[buy:optoma-gt1080hdr|GT1080HDR]]</td></tr>
<tr><td><strong>BenQ AH700ST</strong></td><td>1080p Laser</td><td>4,000 ANSI lm</td><td>0.69–0.83 (1.2x zoom)</td><td>[[price:benq-ah700st]]</td><td>[[buy:benq-ah700st|AH700ST]]</td></tr>
</tbody>
</table></div>
<p>See our dedicated [[link:/golf/golf-simulator-projectors/|golf simulator projector throw guide]] for 2.4 m and 3.0 m screen placement distances.</p>
</section>

<section data-cat="racing">
<h2>Sim racing hardware brands</h2>
<p>Comparing the wheel base, pedal and cockpit brands listed across our [[link:/racing/|Sim racing guides]]:</p>
<div class="tbl"><table>
<thead><tr><th>Brand</th><th>Role</th><th>Checked models</th><th>Price band ([[checked]])</th><th>Guide</th></tr></thead>
<tbody>
<tr><td><strong>Logitech G</strong></td><td>Wheels, direct drive &amp; pedals</td><td>G923, G RS50, PRO Racing Pedals</td><td>[[price:logitech-g923]] – [[price:logitech-rs50]]</td><td>[[link:/racing/direct-drive-wheels/|Wheels &amp; pedals]]</td></tr>
<tr><td><strong>Thrustmaster</strong></td><td>Belt-driven wheel + 3-pedal set</td><td>T300 RS GT</td><td>[[price:thrustmaster-t300-rs-gt]]</td><td>[[link:/racing/direct-drive-wheels/|Wheels &amp; pedals]]</td></tr>
<tr><td><strong>Fanatec</strong></td><td>Direct drive bases &amp; pedals</td><td>CSL DD, GT DD Pro, CSL Elite Pedals V2</td><td>[[price:fanatec-csl-elite-pedals-v2]] – [[price:fanatec-gt-dd-pro]]</td><td>[[link:/racing/direct-drive-wheels/|Wheels &amp; pedals]]</td></tr>
<tr><td><strong>MOZA Racing</strong></td><td>Direct drive bundle</td><td>MOZA R5 bundle</td><td>[[price:moza-r5-bundle]]</td><td>[[link:/racing/direct-drive-wheels/|Wheels &amp; pedals]]</td></tr>
<tr><td><strong>Playseat</strong></td><td>Foldable &amp; tubular cockpits</td><td>Challenge ActiFit, Trophy Logitech G</td><td>[[price:playseat-challenge]] – [[price:playseat-trophy]]</td><td>[[link:/racing/cockpits-and-rigs/|Cockpits &amp; rigs]]</td></tr>
<tr><td><strong>Next Level Racing</strong></td><td>Cockpits &amp; monitor stands</td><td>GTLite Pro, F-GT, F-GT &amp; Elite monitor stands</td><td>[[price:nlr-f-gt-monitor-stand]] – [[price:nlr-f-gt]]</td><td>[[link:/racing/cockpits-and-rigs/|Cockpits &amp; rigs]]</td></tr>
<tr><td><strong>GT Omega</strong></td><td>Aluminium profile frame &amp; seat</td><td>PRIME Lite frame, INERTIA bucket seat</td><td>[[price:gt-omega-inertia-seat]] – [[price:gt-omega-prime-lite]]</td><td>[[link:/racing/cockpits-and-rigs/|Cockpits &amp; rigs]]</td></tr>
</tbody>
</table></div>
</section>
</div>
''' + SRC_COMPARE,
)

RADAR_VS_CAMERA_PAGE = dict(
    path="/compare/radar-vs-camera-launch-monitors/",
    title="Radar vs camera golf launch monitors compared (UK)",
    short="Radar vs camera",
    crumbs=COMP,
    type="article",
    description="Radar vs photometric camera golf launch monitors compared for UK rooms: Garmin, Rapsodo, FlightScope, Shot Scope, SkyTrak, Uneekor, Square Golf and Bushnell.",
    faq=[
        ("Which launch monitor type works for both left- and right-handed players without moving the unit?", "Behind-the-ball radar units such as the Garmin Approach R10, Rapsodo MLM2PRO and FlightScope Mevo+ sit centred behind the golfer, so left- and right-handed players do not need to move the hardware between shots."),
        ("Why do camera launch monitors need less room depth?", "Photometric camera units sit 0.4 to 0.5 m beside the hitting zone instead of 1.8 to 2.7 m behind the golfer, saving roughly 2 m of floor depth."),
    ],
    related=[
        ("/compare/", "Compare all 8 brands", "Full matrix with UK prices, software notes and Amazon UK links."),
        ("/golf/room-size-guide/", "Interactive room size checker", "Enter your room height, width and depth to see what fits."),
        ("/compare/launch-monitor-subscriptions/", "Launch monitor subscriptions", "Compare ongoing software fees by brand."),
    ],
    body='''<p class="lede">Choosing a launch monitor brand starts with where the hardware sits. Behind-the-ball radar and beside-the-ball camera units place different demands on room depth, lighting and dual-handed setups.</p>
[[svg:radar-vs-camera]]
<h2>Side-by-side comparison</h2>
<div class="tbl"><table>
<thead><tr><th>Factor</th><th>Behind-the-ball radar</th><th>Beside-the-ball camera</th></tr></thead>
<tbody>
<tr><td>Example brands</td><td>Garmin R10, Rapsodo MLM2PRO, Shot Scope LM1, FlightScope Mevo+</td><td>Garmin R50, SkyTrak ST MAX, Square Golf, Uneekor EYE MINI / LITE, Bushnell Launch Pro, Foresight GC3</td></tr>
<tr><td>Unit placement</td><td>1.4 m to 2.7 m (5 to 9 ft) behind the ball</td><td>~0.4 m to 0.5 m to the side of the tee</td></tr>
<tr><td>Total indoor depth</td><td>Needs behind-tee space plus 2.4 m+ ball flight (often 4.3 m+ total)</td><td>Saves behind-golfer depth; still needs swing + ball-to-screen room</td></tr>
<tr><td>Left &amp; right-handed play</td><td>Unit stays put behind the hitting line</td><td>Unit must be moved across the mat unless using an overhead rig</td></tr>
<tr><td>Indoor spin measurement</td><td>FlightScope Mevo+ and Rapsodo MLM2PRO note dot/RCT/RPT balls indoors for spin</td><td>Reads standard golf balls directly via high-speed cameras</td></tr>
</tbody>
</table></div>
<h2>Checked Amazon UK models</h2>
<p>If you have 4.5 m+ of depth in a UK garage, behind-the-ball models keep entry costs lower: [[buy:shot-scope-lm1|Shot Scope LM1]] ([[price:shot-scope-lm1]]), [[buy:garmin-approach-r10|Garmin Approach R10]] ([[price:garmin-approach-r10]]) and [[buy:rapsodo-mlm2pro|Rapsodo MLM2PRO]] ([[price:rapsodo-mlm2pro]]).</p>
<p>In shorter spare rooms where behind-golfer depth is limited, beside-the-ball camera models include [[buy:square-golf-indoor|Square Golf indoor]] ([[price:square-golf-indoor]]), [[buy:square-golf-omni|Square Golf Omni]] ([[price:square-golf-omni]]), [[buy:skytrak-st-max|SkyTrak ST MAX]] ([[price:skytrak-st-max]]) and [[buy:garmin-approach-r50|Garmin Approach R50]] ([[price:garmin-approach-r50]]).</p>
''' + SRC_COMPARE,
)

SUBSCRIPTIONS_PAGE = dict(
    path="/compare/launch-monitor-subscriptions/",
    title="Golf launch monitor subscriptions & software compared (UK)",
    short="Subscriptions compared",
    crumbs=COMP,
    type="article",
    description="Which golf launch monitor brands require an annual subscription in the UK: Shot Scope, Garmin, Rapsodo, SkyTrak, Uneekor, FlightScope and Bushnell/Foresight.",
    faq=[
        ("Which launch monitors work out of the box with no ongoing fee?", "Shot Scope LM1 includes the Shot Scope mobile app free for life. FlightScope Mevo+ charges no FlightScope subscription and bundles E6 courses. Foresight GC3 (£7,500 UK retail) includes FSX Play with no recurring subscription."),
        ("Does GSPro require a brand subscription as well?", "It depends on the brand. FlightScope Mevo+ supports direct GSPro connection without a FlightScope fee, whereas Uneekor EYE MINI / LITE and Bushnell Launch Pro require an active paid software tier from the hardware maker in addition to a GSPro licence."),
    ],
    related=[
        ("/compare/", "Compare all 8 brands", "Full hardware, placement and UK price matrix."),
        ("/compare/radar-vs-camera-launch-monitors/", "Radar vs camera brands", "Compare room depth and dual-handed setup."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Compare budget units and what software comes included."),
    ],
    body='''<p class="lede">Upfront hardware price is only part of the cost of a home golf simulator. Several brands gate virtual courses, club data or third-party simulator access behind annual subscriptions.</p>
<h2>Software &amp; subscription rules by brand</h2>
<div class="tbl"><table>
<thead><tr><th>Brand &amp; model</th><th>Included out of the box</th><th>What requires a paid subscription</th><th>Source</th></tr></thead>
<tbody>
<tr><td><strong>Shot Scope LM1</strong> ([[price:shot-scope-lm1]])</td><td>On-unit 3.5" screen + free Shot Scope mobile app</td><td>No subscription required (range/net data only, not course sim)</td><td>Shot Scope UK product page</td></tr>
<tr><td><strong>FlightScope Mevo+</strong> (£1,759 UK retail)</td><td>FS Golf app + bundled E6 courses; direct GSPro link</td><td>No FlightScope hardware fee (3rd-party GSPro licence separate)</td><td>FlightScope / UK retail docs</td></tr>
<tr><td><strong>Foresight GC3</strong> (£7,500 UK retail)</td><td>Full ball &amp; club data + FSX Play software</td><td>No recurring Foresight fee</td><td>Foresight UK retail specs</td></tr>
<tr><td><strong>Garmin R10 / R50</strong> ([[price:garmin-approach-r10]] / [[price:garmin-approach-r50]])</td><td>Shot metrics &amp; practice range</td><td>Garmin Golf membership required for virtual rounds</td><td>Amazon UK listings</td></tr>
<tr><td><strong>Rapsodo MLM2PRO</strong> ([[price:rapsodo-mlm2pro]])</td><td>Core launch monitor session data</td><td>Rapsodo membership for full simulation &amp; replay tiers</td><td>Rapsodo FAQ</td></tr>
<tr><td><strong>SkyTrak ST MAX</strong> ([[price:skytrak-st-max]])</td><td>Amazon UK listing includes 1-year software</td><td>Annual renewal required after year 1 for sim packages</td><td>Amazon UK listing</td></tr>
<tr><td><strong>Uneekor EYE MINI / LITE</strong> (£1,699–£2,999 UK)</td><td>Player Package (range &amp; core data)</td><td>Paid Uneekor tier required for 3rd-party sim (GSPro) &amp; AI Trainer</td><td>Uneekor UK product pages</td></tr>
<tr><td><strong>Bushnell Launch Pro</strong> (£2,490 Europe)</td><td>Ball data + 30-day trial</td><td>Foresight+ Silver/Gold membership required for club data &amp; simulation</td><td>Bushnell Golf Europe</td></tr>
</tbody>
</table></div>
<h2>Before you commit</h2>
<ul>
<li>Check whether the software needs a Windows gaming PC (for example, Uneekor EYE MINI LITE requires a Windows PC and Ethernet cable) or runs on a tablet or built-in screen.</li>
<li>Check regional terms: Bushnell notes that US-spec Launch Pro units require a US internet connection every 45 days, so UK buyers should check UK/EU sourcing.</li>
<li>Verify current annual subscription pricing directly on the maker's UK page before ordering hardware.</li>
</ul>
''' + SRC_COMPARE,
)

COMPARE_PAGES = [COMPARE_PAGE, RADAR_VS_CAMERA_PAGE, SUBSCRIPTIONS_PAGE]
