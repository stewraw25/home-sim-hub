# Page content for Home Sim Hub. Markers:
#   [[SITE_NAME]] -> config.json site_name
#   [[p:slug]] -> Amazon UK product card
#   [[buy:slug|text]] -> inline Amazon UK affiliate link
#   [[price:slug]] -> checked price
#   [[link:/path/|text]] -> internal link
#   [[svg:key]] -> inline technical SVG diagram
#   [[checked]] -> price_checked date
#   [[BP]] -> base path

import os, importlib.util
_dir = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("pages_compare", os.path.join(_dir, "pages_compare.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
COMPARE_PAGES = _mod.COMPARE_PAGES

GOLF = [("Home golf", "/golf/")]
RACE = [("Sim racing", "/racing/")]

SRC_GOLF = '''<h2>Sources</h2><ul class="sources">
<li>Garmin Approach R10 owner's manual, "Preparing for a Shot": https://www8.garmin.com/manuals/webhelp/GUID-E2BBF6BE-4276-436F-B697-59ABEFD61933/EN-US/GUID-88F65277-47D4-403D-8F79-719CAA256D6B.html</li>
<li>Garmin Approach R50 owner's manual (PDF): https://www8.garmin.com/manuals/webhelp/GUID-D31AA1A2-C026-46EB-9699-FA94F1E8AF0B/EN-US/Approach_R50_OM_EN-US.pdf</li>
<li>Garmin forum reply from Garmin staff on R50 room space: https://forums.garmin.com/outdoor-recreation/golf/f/approach-r50/404415/room-dimensions</li>
<li>Rapsodo golf FAQ (MLM2PRO set-up and indoor space): https://rapsodo.com/pages/frequently-asked-golf-questions-faq</li>
<li>Rapsodo, recommended ceiling height for golf simulators: https://rapsodo.com/blogs/golf/recommended-ceiling-height-for-golf-simulator</li>
<li>SkyTrak ST MAX user guide (PDF): https://resources.skytrakgolf.com/hubfs/ST%20MAX%20USER%20GUIDE.pdf</li>
<li>SkyTrak, plan your space: https://www.skytrakgolf.com/pages/plan-your-space</li>
<li>Shop Indoor Golf (retailer) Square Golf Omni specs: https://shopindoorgolf.com/products/square-omni-launch-monitor</li>
<li>Shot Scope LM1 UK product page and specifications: https://shotscope.com/uk/shop/products/golf-launch-monitors/lm1-launch-monitor/</li>
</ul>'''

PAGES = [
# ---------------- HOME ----------------
dict(
    path="/",
    title="[[SITE_NAME]]: UK Home Golf Bays, Brand Hub & Sim Racing",
    short="Home",
    description="UK guides to home golf simulators and sim racing rigs: compare 8 launch monitor brands, check room sizes from makers' manuals, and compare Amazon UK gear.",
    h1="Plan a home golf bay or sim rig that actually fits your room",
    hero=dict(
        eyebrow="UK Home Simulator Guides",
        lede="[[SITE_NAME]] compares launch monitor brands, room dimensions and Amazon UK bay hardware using makers' own manuals and verified listings — with zero guesswork and zero fake reviews.",
        cta_primary=("Compare golf brands", "/compare/"),
        cta_secondary=("Room size guide", "/golf/room-size-guide/"),
        stats=[("8", "launch monitor brands"), ("37", "Amazon UK items checked"), ("0", "invented scores or ratings")],
        svg="bay-hero",
    ),
    related=[
        ("/compare/", "Compare brands hub", "Side-by-side matrix of Garmin, Rapsodo, SkyTrak, Bushnell/Foresight, Uneekor, FlightScope, Square Golf and Shot Scope."),
        ("/golf/room-size-guide/", "Golf room size guide", "Ceiling height, width and depth from Garmin, Rapsodo and SkyTrak manuals."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Budget-friendly radar and indoor units listed on Amazon UK."),
    ],
    body='''<h2>Compare brands before you buy</h2>
<div class="callout"><strong>New:</strong> Use our [[link:/compare/|Compare brands hub]] to compare radar vs camera launch monitors, subscription policies, room depth needs, and UK price bands across Garmin, Rapsodo, SkyTrak, Square Golf, Shot Scope, Bushnell/Foresight, Uneekor and FlightScope, plus nets, mats and projectors.</div>
<h2>Choose your simulator path</h2>
<div class="cards three">
<a class="card tile" href="[[BP]]/compare/">
  <div><span class="card-tag gold">Brand hub</span><h3>Compare brands</h3><p>Side-by-side comparison of 8 launch monitor brands plus nets, enclosures, hitting mats and projectors.</p></div>
  <span class="tile-cta">Open brand matrix &rarr;</span>
</a>
<a class="card tile" href="[[BP]]/golf/">
  <div><span class="card-tag">Golf bay</span><h3>Home golf guides</h3><p>Launch monitors, indoor bays, impact screens, garden nets, hitting mats and UK room clearances.</p></div>
  <span class="tile-cta">Explore home golf &rarr;</span>
</a>
<a class="card tile" href="[[BP]]/racing/">
  <div><span class="card-tag slate">Motorsport</span><h3>Sim racing rigs</h3><p>Geared vs direct drive wheel bases, load-cell pedals, folding stands, cockpits and monitor mounts.</p></div>
  <span class="tile-cta">Explore sim racing &rarr;</span>
</a>
</div>
<h2>Popular UK planning guides</h2>
<div class="cards two">
<a class="card tile" href="[[BP]]/golf/room-size-guide/"><div><h3>How much room do you need for a golf simulator?</h3><p>Metre and foot clearances for ceilings, swing width, radar depth behind the ball and camera units beside the tee.</p></div><span class="tile-cta">Check room sizes &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/garage-golf-simulator/"><div><h3>Setting up a golf simulator in a UK garage</h3><p>Step-by-step check for garage door tracks, launch monitor placement, padded enclosures and short-throw projectors.</p></div><span class="tile-cta">Read garage guide &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/garmin-r50-vs-skytrak-st-max/"><div><h3>Garmin Approach R50 vs SkyTrak ST MAX</h3><p>Camera launch monitors beside the ball compared on price, screen, software terms and footprint.</p></div><span class="tile-cta">Compare both models &rarr;</span></a>
<a class="card tile" href="[[BP]]/racing/room-and-setup-guide/"><div><h3>Sim racing room and set-up guide</h3><p>Exact footprints from Playseat, Next Level Racing and wheel stand listings.</p></div><span class="tile-cta">Check rig footprints &rarr;</span></a>
</div>
<h2>How we research every page</h2>
<p>We work from makers' published user manuals, official UK product pages and Amazon UK listings checked on [[checked]]. We do not test products ourselves, do not publish star ratings, and name the exact source for every dimension and price.</p>'''),

*COMPARE_PAGES,

# ---------------- GOLF HUB ----------------
dict(
    path="/golf/",
    title="Home golf simulators and practice set-ups (UK)",
    short="Home golf",
    description="Everything that goes into a home golf bay in the UK: launch monitors, nets and impact screens, hitting mats, enclosures, projectors and room sizes.",
    h1="Home golf bays, launch monitors and practice set-ups",
    hero=dict(
        eyebrow="Home Golf Section",
        lede="Whether you want a garden net and mat or a full indoor bay with an impact screen and projector, start with the room dimensions and choose hardware that fits.",
        cta_primary=("Compare golf brands", "/compare/"),
        cta_secondary=("Room size guide", "/golf/room-size-guide/"),
        stats=[("20", "Amazon UK golf items checked"), ("7", "launch monitors"), ("6", "nets & enclosures")],
        svg="bay-hero",
    ),
    related=[
        ("/compare/", "Compare golf simulator brands", "Side-by-side matrix of Garmin, Rapsodo, SkyTrak, Uneekor, FlightScope and Bushnell."),
        ("/golf/room-size-guide/", "Room size guide", "Ceiling height, width and depth from official manuals."),
        ("/golf/garage-golf-simulator/", "Garage golf simulator guide", "Step-by-step check for UK garages."),
    ],
    body='''<p class="lede">A home golf set-up can be as simple as a net and a mat in the garden, or a full indoor bay with a launch monitor, impact screen and projector. This section covers each part.</p>
<div class="cards two">
<a class="card tile" href="[[BP]]/golf/launch-monitors/"><div><h3>Launch monitors</h3><p>The device that measures each shot. Radar units sit behind you; camera units sit beside the ball.</p></div><span class="tile-cta">See launch monitors &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/simulators/"><div><h3>Home simulator bays</h3><p>Enclosures, impact screens and projectors that turn a launch monitor into a simulator.</p></div><span class="tile-cta">See simulator bays &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/nets-and-mats/"><div><h3>Nets and mats</h3><p>Practice nets for the garden or garage, and hitting mats.</p></div><span class="tile-cta">See nets and mats &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/room-size-guide/"><div><h3>Room size guide</h3><p>Ceiling height, width and depth, using the makers' published figures.</p></div><span class="tile-cta">Check room sizes &rarr;</span></a>
</div>
<h2>Buying guides &amp; comparisons</h2>
<div class="cards two">
<a class="card tile" href="[[BP]]/compare/"><div><span class="card-tag gold">Brand matrix</span><h3>Compare all golf simulator brands</h3><p>Garmin, Rapsodo, SkyTrak, Square Golf, Shot Scope, Bushnell/Foresight, Uneekor and FlightScope compared.</p></div><span class="tile-cta">Compare brands &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/launch-monitor-vs-simulator/"><div><h3>Launch monitor vs simulator explained</h3><p>What comes in the box with a launch monitor vs what you add for projected course play.</p></div><span class="tile-cta">Read guide &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/launch-monitors-under-1000/"><div><h3>Launch monitors under £1,000</h3><p>Shot Scope LM1, Garmin R10, Rapsodo MLM2PRO and Square Golf indoor compared.</p></div><span class="tile-cta">Read guide &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/garage-golf-simulator/"><div><h3>Setting up a golf simulator in a garage</h3><p>Step-by-step plan for garage ceiling clearance, enclosures, mats and projectors.</p></div><span class="tile-cta">Read guide &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/garmin-r50-vs-skytrak-st-max/"><div><h3>Garmin Approach R50 vs SkyTrak ST MAX</h3><p>Two beside-the-ball camera systems compared on price, screen and software.</p></div><span class="tile-cta">Read comparison &rarr;</span></a>
<a class="card tile" href="[[BP]]/golf/golf-nets-for-the-garden/"><div><h3>Golf nets for the garden</h3><p>Pop-up nets and 3m practice cages compared by listing size.</p></div><span class="tile-cta">Read guide &rarr;</span></a>
</div>'''),

# ---------------- LAUNCH MONITORS HUB ----------------
dict(
    path="/golf/launch-monitors/",
    title="Golf launch monitors on Amazon UK",
    short="Launch monitors",
    crumbs=GOLF,
    type="article",
    description="How home golf launch monitors differ, where each one sits, and the launch monitors listed on Amazon UK with prices checked 24 Nov 2026.",
    itemlist=[
        ("Shot Scope LM1", "/golf/launch-monitors/#shot-scope-lm1"),
        ("Garmin Approach R10", "/golf/launch-monitors/#garmin-approach-r10"),
        ("Rapsodo MLM2PRO", "/golf/launch-monitors/#rapsodo-mlm2pro"),
        ("Square Golf indoor launch monitor", "/golf/launch-monitors/#square-golf-indoor"),
        ("Square Golf Omni", "/golf/launch-monitors/#square-golf-omni"),
        ("SkyTrak ST MAX", "/golf/launch-monitors/#skytrak-st-max"),
        ("Garmin Approach R50", "/golf/launch-monitors/#garmin-approach-r50"),
    ],
    faq=[
        ("Where does a radar launch monitor sit compared with a camera unit?", "Radar units such as the Garmin R10, Rapsodo MLM2PRO and Shot Scope LM1 sit 1.4 to 2.6 m behind the ball. Camera units such as the Garmin R50, SkyTrak ST MAX and Square Golf Omni sit beside the ball."),
        ("Do all launch monitors need a subscription?", "No. Shot Scope LM1 uses the free Shot Scope app with no subscription. Other units, such as the Garmin R10 and R50, require an active subscription for virtual course play."),
    ],
    related=[
        ("/compare/", "Compare all 8 launch monitor brands", "Includes Bushnell/Foresight, Uneekor and FlightScope alongside Amazon UK models."),
        ("/golf/room-size-guide/", "Room size guide", "Full ceiling, width and depth checklist."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Focused look at entry-level units."),
    ],
    body='''<p class="lede">A launch monitor measures what happens when you hit the ball, such as ball speed and launch angle. Many also link to simulator software so you can play virtual courses.</p>
[[svg:radar-vs-camera]]
<h2>Behind the ball or beside it</h2>
<p>Where a launch monitor sits decides how much room it needs.</p>
<ul>
<li>Radar units such as the Garmin Approach R10, Rapsodo MLM2PRO and Shot Scope LM1 sit on the floor behind the golfer. Garmin's R10 manual says to place it 1.8 to 2.4 m (6 to 8 ft) behind the tee. Rapsodo says 6.5 to 8.5 ft behind the ball for the MLM2PRO. Shot Scope's UK spec puts the LM1 around 1.4 to 1.5 m (55 in) behind the ball.</li>
<li>Camera units such as the Garmin Approach R50, SkyTrak ST MAX and Square Golf Omni sit beside the ball. Garmin's R50 manual says about 0.5 m (1.5 ft) to the side of the tee, facing it.</li>
</ul>
<p>See the [[link:/golf/room-size-guide/|room size guide]] for each maker's figures, or open the [[link:/compare/|brand comparison hub]] to include Uneekor, FlightScope and Bushnell/Foresight.</p>
<h2>Launch monitors listed on Amazon UK</h2>
<div class="tbl"><table><thead><tr><th>Model</th><th>Price checked [[checked]]</th><th>Where it sits (maker)</th></tr></thead><tbody>
<tr><td>[[buy:shot-scope-lm1|Shot Scope LM1]]</td><td>[[price:shot-scope-lm1]]</td><td>1.4 to 1.5 m (55 in) behind the ball (Shot Scope UK spec)</td></tr>
<tr><td>[[buy:garmin-approach-r10|Garmin Approach R10]]</td><td>[[price:garmin-approach-r10]]</td><td>1.8 to 2.4 m behind the tee</td></tr>
<tr><td>[[buy:rapsodo-mlm2pro|Rapsodo MLM2PRO]]</td><td>[[price:rapsodo-mlm2pro]]</td><td>6.5 to 8.5 ft behind the ball</td></tr>
<tr><td>[[buy:square-golf-indoor|Square Golf indoor launch monitor]]</td><td>[[price:square-golf-indoor]]</td><td>Beside the ball (check maker guide)</td></tr>
<tr><td>[[buy:square-golf-omni|Square Golf Omni]]</td><td>[[price:square-golf-omni]]</td><td>Beside the golfer, about 14 to 20 in from the tee (retailer figure)</td></tr>
<tr><td>[[buy:skytrak-st-max|SkyTrak ST MAX]]</td><td>[[price:skytrak-st-max]]</td><td>Beside the ball</td></tr>
<tr><td>[[buy:garmin-approach-r50|Garmin Approach R50]]</td><td>[[price:garmin-approach-r50]]</td><td>About 0.5 m to the side of the tee</td></tr>
</tbody></table></div>
<p class="small">Prices are as checked on [[checked]] and change often. Check Amazon for the current price.</p>
[[p:garmin-approach-r10]][[p:rapsodo-mlm2pro]][[p:shot-scope-lm1]][[p:square-golf-indoor]][[p:square-golf-omni]][[p:skytrak-st-max]][[p:garmin-approach-r50]]
<h2>Subscriptions</h2>
<p>Some features need a paid subscription. For example, the Amazon listings for the Garmin R10 and R50 say virtual rounds need an active Garmin Golf membership or subscription. By contrast, Shot Scope states its LM1 mobile app is free with no subscription. Check each maker's current terms before you buy.</p>
''' + SRC_GOLF),

# ---------------- SIMULATOR HUB ----------------
dict(
    path="/golf/simulators/",
    faq=[
        ("Do I need a short-throw projector for a home golf bay?", "Short-throw projectors such as the BenQ AH700ST, BenQ TH671ST and Optoma GT1080HDR mount closer to the impact screen so your body does not cast a shadow over the image."),
        ("How much space should be left behind an impact screen or net?", "Leave at least 30 cm (and always follow the screen or enclosure maker's stated clearance) so the stretched screen does not strike the wall behind it."),
    ],
    title="Home golf simulator bays: enclosures, screens and projectors",
    short="Simulator bays",
    crumbs=GOLF,
    type="article",
    description="What goes into a home golf simulator bay in the UK: launch monitor, impact screen or net, enclosure, hitting mat, projector and software.",
    itemlist=[
        ("SimSpace golf simulator enclosure", "/golf/simulators/#simspace-enclosure"),
        ("SimSpace Deluxe impact screen", "/golf/simulators/#simspace-impact-screen"),
        ("GoSports golf simulator impact screen", "/golf/simulators/#gosports-impact-screen"),
        ("BenQ AH700ST projector", "/golf/simulators/#benq-ah700st"),
        ("BenQ TH671ST projector", "/golf/simulators/#benq-th671st"),
        ("Optoma GT1080HDR projector", "/golf/simulators/#optoma-gt1080hdr"),
    ],
    related=[
        ("/golf/garage-golf-simulator/", "Garage golf simulator guide", "Fitting a full bay inside a UK garage."),
        ("/golf/room-size-guide/", "Room size guide", "Ceiling height and ball-to-screen clearances."),
        ("/compare/", "Compare bay brands", "SimSpace, GoSports, BenQ and Optoma side by side."),
    ],
    body='''<p class="lede">A home simulator bay puts a picture of the shot in front of you. It needs a launch monitor plus a few other parts.</p>
[[svg:bay-dimensions]]
<h2>The parts of a home bay</h2>
<ol>
<li><strong>Launch monitor</strong> to measure the shot. See [[link:/golf/launch-monitors/|launch monitors]].</li>
<li><strong>Impact screen or net</strong> to stop the ball. A screen also takes the projected picture.</li>
<li><strong>Enclosure</strong>, a frame with side netting that holds the screen and catches mishits.</li>
<li><strong>Hitting mat</strong> to protect the floor. See [[link:/golf/nets-and-mats/|nets and mats]].</li>
<li><strong>Projector</strong>, usually a short-throw model so it can sit close to the screen.</li>
<li><strong>Software</strong>, from the launch monitor maker or a third party, sometimes on subscription.</li>
</ol>
<p>Garmin's launch monitor manuals ask for adequate free space behind the net or screen, a net or screen high and wide enough for high or wayward shots, and padding on enclosure frames to reduce ricochet.</p>
<h2>Enclosures</h2>
[[p:simspace-enclosure]]
<h2>Impact screens</h2>
[[p:simspace-impact-screen]][[p:gosports-impact-screen]]
<h2>Projectors</h2>
<p>Check the projector maker's throw distance and mounting guidance against your room before buying.</p>
[[p:benq-ah700st]][[p:benq-th671st]][[p:optoma-gt1080hdr]]
<p>Next: [[link:/golf/garage-golf-simulator/|setting up a simulator in a garage]] and the [[link:/golf/room-size-guide/|room size guide]].</p>
''' + SRC_GOLF),

# ---------------- NETS AND MATS HUB ----------------
dict(
    path="/golf/nets-and-mats/",
    faq=[
        ("Where should a radar launch monitor sit relative to a hitting mat?", "Garmin's Approach R10 manual notes that the bottom edge of the launch monitor should sit above the top surface of the hitting mat."),
        ("Do I need a hitting mat if I use a golf net in the garden?", "Yes. A hitting mat protects your lawn from divots and gives a level, repeatable surface for launch monitor shots."),
    ],
    title="Golf nets, practice cages and hitting mats (UK)",
    short="Nets and mats",
    crumbs=GOLF,
    type="article",
    description="Golf practice nets, cages and hitting mats listed on Amazon UK, with sizes from each listing and prices checked 24 Nov 2026.",
    itemlist=[
        ("Amazon Basics portable golf net", "/golf/nets-and-mats/#amazon-basics-golf-net"),
        ("FORZA 7ft x 7ft pop-up net", "/golf/nets-and-mats/#forza-7ft-net"),
        ("SimSpace Deluxe Home Driving Net", "/golf/nets-and-mats/#simspace-deluxe-net"),
        ("Hillman PGM 3m practice cage", "/golf/nets-and-mats/#hillman-pgm-3m-cage"),
        ("Spurk Winter Strike Mat", "/golf/nets-and-mats/#spurk-winter-strike-mat"),
        ("COSTWAY golf hitting mat", "/golf/nets-and-mats/#costway-hitting-mat"),
        ("GIRAFFYCO 1.5 x 1.2 m hitting mat", "/golf/nets-and-mats/#giraffyco-hitting-mat"),
    ],
    related=[
        ("/golf/golf-nets-for-the-garden/", "Garden golf nets", "Outdoor sizing and safety tips."),
        ("/golf/simulators/", "Simulator bays & screens", "Stepping up from a net to a projected bay."),
        ("/compare/", "Compare brands hub", "Compare net and mat brands alongside launch monitors."),
    ],
    body='''<p class="lede">A net and a mat are the simplest home practice set-up, and they're also part of most indoor simulator bays.</p>
<h2>Nets and practice cages</h2>
<p>Sizes below are from each Amazon listing. Check the net maker's guidance on how much free space to leave behind the net.</p>
[[p:amazon-basics-golf-net]][[p:forza-7ft-net]][[p:simspace-deluxe-net]][[p:hillman-pgm-3m-cage]]
<h2>Hitting mats</h2>
<p>If you use a radar launch monitor on a mat, Garmin's R10 manual notes that the bottom edge of the launch monitor should sit above the mat.</p>
[[p:spurk-winter-strike-mat]][[p:costway-hitting-mat]][[p:giraffyco-hitting-mat]]
<p>More: [[link:/golf/golf-nets-for-the-garden/|golf nets for the garden]].</p>
''' + SRC_GOLF),

# ---------------- ROOM SIZE GUIDE ----------------
dict(
    path="/golf/room-size-guide/",
    title="How much room do you need for a golf simulator? (UK guide)",
    short="Room size guide",
    crumbs=GOLF,
    type="article",
    js=True,
    description="Ceiling height, width and depth for a home golf simulator, using Garmin, Rapsodo and SkyTrak published figures, converted to metres for UK rooms.",
    faq=[
        ("What ceiling height do you need for an indoor golf simulator?", "SkyTrak says a 10 ft (3.05 m) ceiling typically offers ample clearance and many golfers manage with 9 ft (2.74 m). Rapsodo says 9 ft may suit golfers around 5 ft 8 in and under, while taller players may need 10 or 11 ft. Measure from the top of your hitting mat to the lowest overhead obstruction."),
        ("How much room depth does a radar unit need vs a camera unit?", "Radar monitors like the Garmin R10 and Rapsodo MLM2PRO sit 6 to 8.5 ft behind the ball plus at least 8 ft of ball flight (14 ft+ total). Camera units sit beside the ball, saving behind-the-golfer depth, though SkyTrak still recommends 16 to 17 ft overall depth for full simulator enclosures."),
        ("What extra width is needed for both left- and right-handed golfers?", "SkyTrak suggests adding 1 to 2 ft of extra width when both left- and right-handed golfers use the bay. Beside-the-ball camera units also need moving to the opposite side of the hitting area."),
    ],
    related=[
        ("/compare/", "Compare launch monitor brands", "See placement and room space across 8 brands."),
        ("/golf/garage-golf-simulator/", "Garage golf simulator guide", "Practical UK garage measurements and layout."),
        ("/golf/launch-monitors/", "Launch monitors on Amazon UK", "Compare behind-the-ball vs beside-the-ball units."),
    ],
    body='''<p class="lede">Three measurements decide whether a golf simulator fits: ceiling height, room width and room depth. Each launch monitor maker publishes its own figures, so start with the one you're considering.</p>
<div class="callout">The quickest check, which SkyTrak suggests: stand where you'd hit, take a slow practice swing with your driver, and see whether you clear the ceiling, walls and lights.</div>
<div class="room-tool" id="room-checker">
<h3>Check your room against makers' published figures</h3>
<p class="small">Enter your room dimensions in metres (measured from the top of the hitting mat to the lowest beam or door track) or pick a UK preset:</p>
<div class="preset-row">
  <button type="button" class="preset-btn" data-room-preset="2.40,2.80,5.00">UK single garage (2.4 × 2.8 × 5.0 m)</button>
  <button type="button" class="preset-btn" data-room-preset="2.80,5.00,5.40">Double garage (2.8 × 5.0 × 5.4 m)</button>
  <button type="button" class="preset-btn" data-room-preset="2.40,3.20,3.80">Spare room (2.4 × 3.2 × 3.8 m)</button>
  <button type="button" class="preset-btn" data-room-preset="3.10,3.80,5.20">Garden cabin / studio (3.1 × 3.8 × 5.2 m)</button>
</div>
<div class="room-inputs">
  <div class="room-field"><label for="rm-h">Ceiling height (m)</label><input id="rm-h" type="number" step="0.05" min="1.5" max="6" value="2.80"></div>
  <div class="room-field"><label for="rm-w">Room width (m)</label><input id="rm-w" type="number" step="0.1" min="1.5" max="10" value="3.50"></div>
  <div class="room-field"><label for="rm-d">Room depth (m)</label><input id="rm-d" type="number" step="0.1" min="1.5" max="12" value="4.90"></div>
</div>
<div class="room-results" id="room-fit-results"><p class="small">Enable JavaScript to compare your measurements live against the table below.</p></div>
</div>
[[svg:radar-vs-camera]]
<h2>Makers' published figures</h2>
<div class="tbl"><table><thead><tr><th>Launch monitor</th><th>Where it sits</th><th>Ball to net or screen</th><th>Other figures</th></tr></thead><tbody>
<tr><td>Garmin Approach R10</td><td>On the ground 6 to 8 ft (1.8 to 2.4 m) behind the tee</td><td>At least 8 ft (2.4 m) indoors</td><td>Garmin asks for adequate ceiling height and nothing obstructing the backswing or follow-through</td></tr>
<tr><td>Rapsodo MLM2PRO</td><td>6.5 to 8.5 ft behind the ball</td><td>At least 8 ft</td><td>Rapsodo says a little more than 14 ft in total indoors, and taller players may need the unit further back</td></tr>
<tr><td>Garmin Approach R50</td><td>About 1.5 ft (0.5 m) to the side of the tee, facing it</td><td>Not stated in the manual</td><td>A Garmin staff reply says the room needs space for a full swing with each club plus 2 x 2 ft clear in front of the R50</td></tr>
<tr><td>SkyTrak ST MAX</td><td>Beside the ball</td><td>Not stated in the user guide</td><td>Minimum unobstructed area 10 ft long by 10 ft wide; ceiling height varies with your height and club length</td></tr>
<tr><td>Square Golf Omni</td><td>Beside the golfer, about 14 to 20 in from the tee</td><td>Not stated</td><td>Retailer Shop Indoor Golf recommends a room 9 ft high, 10 ft wide and 12 ft deep</td></tr>
</tbody></table></div>
<p class="small">Feet are the makers' units. Metric conversions are ours: 8 ft is about 2.4 m, 9 ft about 2.7 m, 10 ft about 3.05 m and 12 ft about 3.7 m.</p>
<h2>Ceiling height</h2>
<p>None of these makers gives one ceiling height that suits everyone, because it depends on your height, your swing and the club. SkyTrak says a 10 ft ceiling typically offers ample clearance and that many golfers say 9 ft is enough. Rapsodo says a 9 ft ceiling may suit golfers about 5 ft 8 in and under, taller golfers may need 10 or 11 ft, and suggests allowing 6 to 9 in above the highest point of your swing.</p>
<p>Measure from the top of your hitting mat, not the floor, and to the lowest thing overhead, such as a beam, light or garage door track.</p>
<h2>Width</h2>
<p>SkyTrak says its screens and nets range from 8 to 13 ft wide and suggests a 12 ft room width for a more spacious feel, plus an extra 1 to 2 ft if both left- and right-handed golfers will use it. Camera units that sit beside the ball need moving to the other side for a left-handed golfer.</p>
<h2>Depth</h2>
<p>Depth is where radar and camera units differ most.</p>
<ul>
<li>Radar behind the golfer: add the space behind the ball for the unit to the ball-to-net distance. For the Garmin R10, that's 6 to 8 ft plus at least 8 ft. For the Rapsodo MLM2PRO, Rapsodo puts the indoor total at a little more than 14 ft.</li>
<li>Camera beside the ball: the unit takes no extra depth behind you, but you still need room for your stance and backswing, the ball-to-screen distance, and the screen maker's clearance behind the screen. SkyTrak suggests 17 ft of room depth for a comfortable set-up, and gives a minimum of 16 ft for its Studio 10 enclosure.</li>
</ul>
<h2>Before you buy</h2>
<ol>
<li>Measure ceiling height, width and depth in metres and feet.</li>
<li>Check the launch monitor maker's set-up page for the exact model.</li>
<li>Check the net, screen or enclosure listing for its own size and the space it needs behind it.</li>
<li>Do the slow driver swing test in the space.</li>
</ol>
<p>Related: [[link:/golf/launch-monitor-vs-simulator/|launch monitor vs simulator]], [[link:/golf/garage-golf-simulator/|garage simulator set-up]].</p>
''' + SRC_GOLF),

# ---------------- LM vs SIM ----------------
dict(
    path="/golf/launch-monitor-vs-simulator/",
    title="Launch monitor vs golf simulator: what's the difference?",
    short="Launch monitor vs simulator",
    crumbs=GOLF,
    type="article",
    description="A launch monitor measures your shots; a golf simulator adds an impact screen, software and an enclosure. See how they differ and what you need in the UK.",
    faq=[
        ("Can I start with a launch monitor and net, then add a screen later?", "Yes. Many golfers start with a launch monitor, hitting mat and practice net using a phone or tablet, then add an impact screen, enclosure and short-throw projector later."),
        ("Do launch monitors include simulator courses?", "Some include trial or bundled driving range features, while full virtual course play often requires an active brand subscription or third-party simulator software."),
    ],
    related=[
        ("/compare/", "Compare launch monitor brands", "See subscription policies and bundled software by brand."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Entry-level options to start with."),
        ("/golf/simulators/", "Home simulator bays", "Enclosures, impact screens and short-throw projectors."),
    ],
    body='''<p class="lede">A launch monitor is the measuring device. A simulator is a full set-up built around one, with a screen and software that show the shot and let you play virtual courses.</p>
<h2>Launch monitor on its own</h2>
<p>On its own, a launch monitor shows numbers, such as ball speed, launch angle and carry, on its own screen or a phone app. You can use one at a driving range, or at home into a net.</p>
<h2>A full simulator</h2>
<p>A home simulator adds an impact screen or net, an enclosure to catch mishits, a hitting mat, a projector or TV, and software. Some launch monitors include simulator features, sometimes on a subscription. For example, the Rapsodo MLM2PRO listing describes it as a "mobile launch monitor + golf simulator", and the Garmin R50 listing says it has a built-in 10 inch touchscreen and that virtual rounds need a subscription.</p>
<div class="tbl"><table><thead><tr><th></th><th>Launch monitor only</th><th>Full simulator</th></tr></thead><tbody>
<tr><td>What you see</td><td>Shot numbers on a device or phone</td><td>The shot on a screen, plus numbers</td></tr>
<tr><td>Space</td><td>Depends on the unit; radar units need room behind the ball</td><td>The unit's space plus room for the screen or enclosure</td></tr>
<tr><td>Extra parts</td><td>Net and mat for home use</td><td>Screen, enclosure, mat, projector, software</td></tr>
</tbody></table></div>
<h2>Which to start with</h2>
<p>You can start with a launch monitor, a net and a mat, and add a screen and projector later. If you plan to build a bay, check the [[link:/golf/room-size-guide/|room size guide]] first, then the [[link:/golf/simulators/|simulator bay parts]].</p>
''' + SRC_GOLF),

# ---------------- GUIDE: UNDER 1000 ----------------
dict(
    path="/golf/launch-monitors-under-1000/",
    faq=[
        ("Which launch monitor under £1,000 has no subscription?", "Shot Scope LM1 uses the free Shot Scope mobile app with no subscription and includes a 3.5 inch colour screen on the unit."),
        ("Which under-£1,000 unit saves the most room depth?", "The Square Golf indoor unit is a camera launch monitor rather than a behind-the-ball radar unit, though you should verify its exact set-up guide before ordering."),
    ],
    title="Golf launch monitors under £1,000 on Amazon UK",
    short="Under £1,000",
    crumbs=GOLF,
    type="article",
    description="Launch monitors under £1,000 listed on Amazon UK, compared by where they sit and how much room the maker says they need. Prices checked 24 Nov 2026.",
    itemlist=[
        ("Shot Scope LM1", "/golf/launch-monitors-under-1000/#shot-scope-lm1"),
        ("Garmin Approach R10", "/golf/launch-monitors-under-1000/#garmin-approach-r10"),
        ("Rapsodo MLM2PRO", "/golf/launch-monitors-under-1000/#rapsodo-mlm2pro"),
        ("Square Golf indoor launch monitor", "/golf/launch-monitors-under-1000/#square-golf-indoor"),
    ],
    related=[
        ("/compare/", "Compare all 8 brands", "See how budget models stack up against SkyTrak, Uneekor and FlightScope."),
        ("/golf/room-size-guide/", "Room size guide", "Check depth before buying a behind-the-ball unit."),
        ("/golf/nets-and-mats/", "Nets and mats", "Pair an entry launch monitor with a net and mat."),
    ],
    body='''<p class="lede">These four launch monitors were listed on Amazon UK under £1,000 when we checked on [[checked]]. We've set out where each one sits and what the maker says about space, so you can check them against your room.</p>
<div class="tbl"><table><thead><tr><th>Model</th><th>Price checked</th><th>Placement</th><th>Indoor space (maker)</th></tr></thead><tbody>
<tr><td>Shot Scope LM1</td><td>[[price:shot-scope-lm1]]</td><td>Behind the ball, ~1.4 to 1.5 m (55 in)</td><td>Check Shot Scope guide + net clearance</td></tr>
<tr><td>Garmin Approach R10</td><td>[[price:garmin-approach-r10]]</td><td>Behind the ball, 1.8 to 2.4 m</td><td>Ball at least 2.4 m from the net</td></tr>
<tr><td>Rapsodo MLM2PRO</td><td>[[price:rapsodo-mlm2pro]]</td><td>Behind the ball, 6.5 to 8.5 ft</td><td>A little more than 14 ft in total</td></tr>
<tr><td>Square Golf indoor</td><td>[[price:square-golf-indoor]]</td><td>Beside the ball (check maker guide)</td><td>Check maker set-up guide</td></tr>
</tbody></table></div>
<h2>The four models</h2>
[[p:shot-scope-lm1]][[p:garmin-approach-r10]][[p:rapsodo-mlm2pro]][[p:square-golf-indoor]]
<h2>Things to check</h2>
<ul>
<li>Room depth, if the unit sits behind you. See the [[link:/golf/room-size-guide/|room size guide]].</li>
<li>Whether simulator features need a subscription.</li>
<li>Which phone or tablet the app works with.</li>
<li>Seller and returns details on the Amazon listing.</li>
</ul>
''' + SRC_GOLF),

# ---------------- GUIDE: GARAGE ----------------
dict(
    path="/golf/garage-golf-simulator/",
    title="Setting up a golf simulator in a UK garage",
    short="Garage simulator",
    crumbs=GOLF,
    type="article",
    description="A step-by-step guide to fitting a home golf simulator into a UK garage: measuring, picking a launch monitor for the depth, screens, mats and projectors.",
    faq=[
        ("Does a golf simulator fit in a standard UK single garage?", "A typical UK single garage is narrow (around 2.4 to 3 m wide) and often has low beams or an up-and-over door track. Always test a slow driver swing from your intended hitting spot before ordering an enclosure."),
        ("Why use a short-throw projector in a garage bay?", "Short-throw models like the BenQ AH700ST mount closer to the impact screen, reducing the chance of your body or club casting a shadow on the image."),
    ],
    related=[
        ("/golf/room-size-guide/", "Room size guide", "Full ceiling, width and depth checklist."),
        ("/compare/", "Compare brands hub", "Compare beside-the-ball camera units vs radar units for garage layouts."),
        ("/golf/simulators/", "Enclosures & projectors", "Full list of screens, bays and short-throw projectors."),
    ],
    body='''<p class="lede">A garage can have more depth than a spare room, which helps with launch monitors that sit behind the golfer. Check the ceiling height carefully, including any garage door track or opener.</p>
[[svg:bay-dimensions]]
<h2>1. Measure the space</h2>
<p>Measure the lowest point overhead, including any garage door track, opener or beam, then the width and depth. Use the [[link:/golf/room-size-guide/|room size guide]] to compare your figures with each maker's.</p>
<h2>2. Pick a launch monitor that suits the depth</h2>
<p>Radar units sit behind the golfer and need more depth. Garmin's R10 manual puts it 1.8 to 2.4 m behind the tee, with the ball at least 2.4 m from the net. Camera units such as the Garmin R50 or SkyTrak ST MAX sit beside the ball, which saves depth.</p>
[[p:garmin-approach-r10]][[p:skytrak-st-max]]
<h2>3. Choose a screen or enclosure</h2>
<p>An enclosure holds the impact screen and side netting. Check its frame size against your width and height, and leave the clearance the maker asks for behind the screen.</p>
[[p:simspace-enclosure]][[p:gosports-impact-screen]]
<h2>4. Add a mat</h2>
[[p:giraffyco-hitting-mat]]
<h2>5. Add a projector</h2>
<p>A short-throw projector can sit nearer the screen. Check the projector maker's throw distance for your screen size.</p>
[[p:benq-ah700st]]
<h2>6. Safety checks</h2>
<ul>
<li>Garmin's manuals ask for adequate ceiling height, nothing obstructing the swing, free space behind the net or screen, and padding on enclosure frames.</li>
<li>Keep cars, windows and anything fragile away from the hitting area.</li>
</ul>
''' + SRC_GOLF),

# ---------------- GUIDE: R50 vs ST MAX ----------------
dict(
    path="/golf/garmin-r50-vs-skytrak-st-max/",
    faq=[
        ("Do you need a separate PC or tablet for the Garmin Approach R50?", "The Amazon UK listing notes the Garmin Approach R50 includes a built-in 10 inch colour touchscreen display, though virtual course rounds still require an active Garmin Golf membership."),
        ("What software is included with the SkyTrak ST MAX?", "The Amazon UK listing checked on 24 Nov 2026 states 1 year of software is included with the SkyTrak ST MAX."),
    ],
    title="Garmin Approach R50 vs SkyTrak ST MAX",
    short="R50 vs ST MAX",
    crumbs=GOLF,
    type="article",
    description="Garmin Approach R50 and SkyTrak ST MAX compared side by side using Amazon UK listing details and each maker's set-up guidance. Prices checked 24 Nov 2026.",
    related=[
        ("/compare/", "Compare all 8 launch monitor brands", "See how R50 and ST MAX compare with Uneekor, Bushnell, FlightScope and Square Golf."),
        ("/golf/room-size-guide/", "Room size guide", "Room clearance rules for camera units."),
    ],
    body='''<p class="lede">Both of these are camera-based launch monitors that sit beside the ball. Here's how they compare on the details their makers and Amazon UK listings publish.</p>
<div class="tbl"><table><thead><tr><th></th><th>Garmin Approach R50</th><th>SkyTrak ST MAX</th></tr></thead><tbody>
<tr><td>Price checked [[checked]]</td><td>[[price:garmin-approach-r50]]</td><td>[[price:skytrak-st-max]]</td></tr>
<tr><td>Where it sits</td><td>About 0.5 m to the side of the tee, facing it (Garmin manual)</td><td>Beside the ball (SkyTrak)</td></tr>
<tr><td>Space figures</td><td>Room for a full swing with each club plus 2 x 2 ft clear in front of the unit (Garmin staff)</td><td>Minimum unobstructed area 10 ft by 10 ft; ceiling varies (SkyTrak user guide)</td></tr>
<tr><td>Screen</td><td>Built-in 10 inch touchscreen (Amazon listing)</td><td>Not stated in the listing</td></tr>
<tr><td>Measuring system (listing)</td><td>3-camera system</td><td>Dual Doppler radar plus photometric cameras</td></tr>
<tr><td>Software</td><td>Virtual rounds need an active Garmin Golf membership (listing)</td><td>Listing title says 1 year of software included</td></tr>
<tr><td>Size and weight (listing)</td><td>26.9 x 19.1 x 41.9 cm; 9 lb</td><td>Package 34.11 x 29.39 x 14.1 cm; 2.27 kg</td></tr>
</tbody></table></div>
[[p:garmin-approach-r50]][[p:skytrak-st-max]]
<h2>How to choose between them</h2>
<ul>
<li>Price: the R50 was more than twice the ST MAX's price when we checked.</li>
<li>Screen: the R50 has its own screen; check what device the ST MAX needs for its software.</li>
<li>Subscriptions: compare each maker's current software terms.</li>
<li>Left- and right-handed players: both sit beside the ball, so the unit moves to the other side for a left-hander.</li>
</ul>
''' + SRC_GOLF),

# ---------------- GUIDE: GARDEN NETS ----------------
dict(
    path="/golf/golf-nets-for-the-garden/",
    faq=[
        ("How wide should a garden golf net be for full swings?", "Checked Amazon UK listings range from 7 ft x 7 ft (FORZA pop-up) and 2.44 m x 2.44 m (Amazon Basics) up to 2.5 m x 2.5 m x 3.84 m (SimSpace) and 3 m x 3 m (Hillman PGM cage)."),
        ("Can a pop-up garden net stay outside all year?", "Check each maker's listing: lighter pop-up nets are typically designed to pack away between sessions, whereas heavier steel-framed cages are built for semi-permanent garden use."),
    ],
    title="Golf nets for the garden: sizes and options on Amazon UK",
    short="Garden golf nets",
    crumbs=GOLF,
    type="article",
    description="Golf practice nets and cages for UK gardens, compared by the sizes given in each Amazon UK listing, with prices checked 24 Nov 2026.",
    itemlist=[
        ("Amazon Basics portable golf net", "/golf/golf-nets-for-the-garden/#amazon-basics-golf-net"),
        ("FORZA 7ft x 7ft pop-up net", "/golf/golf-nets-for-the-garden/#forza-7ft-net"),
        ("SimSpace Deluxe Home Driving Net", "/golf/golf-nets-for-the-garden/#simspace-deluxe-net"),
        ("Hillman PGM 3m practice cage", "/golf/golf-nets-for-the-garden/#hillman-pgm-3m-cage"),
    ],
    related=[
        ("/golf/nets-and-mats/", "All nets and hitting mats", "Includes hitting mats to protect your lawn."),
        ("/golf/launch-monitors-under-1000/", "Launch monitors under £1,000", "Portable radar monitors to pair with a garden net."),
    ],
    body='''<p class="lede">A net is the simplest way to practise full swings at home. These are listed on Amazon UK, from pop-up nets to steel-framed cages.</p>
<div class="tbl"><table><thead><tr><th>Net</th><th>Size (listing)</th><th>Price checked</th></tr></thead><tbody>
<tr><td>Amazon Basics portable golf net</td><td>2.44 m x 2.44 m</td><td>[[price:amazon-basics-golf-net]]</td></tr>
<tr><td>FORZA pop-up net</td><td>7 ft x 7 ft</td><td>[[price:forza-7ft-net]]</td></tr>
<tr><td>SimSpace Deluxe Home Driving Net</td><td>2.5 m x 2.5 m x 3.84 m</td><td>[[price:simspace-deluxe-net]]</td></tr>
<tr><td>Hillman PGM practice cage</td><td>3 m x 3 m</td><td>[[price:hillman-pgm-3m-cage]]</td></tr>
</tbody></table></div>
[[p:amazon-basics-golf-net]][[p:forza-7ft-net]][[p:simspace-deluxe-net]][[p:hillman-pgm-3m-cage]]
<h2>Before you buy</h2>
<ul>
<li>Leave free space behind the net, as the net maker advises.</li>
<li>Think about neighbours, windows and anything a wayward shot could reach.</li>
<li>Check whether the net is meant to stay up outdoors or to be packed away.</li>
<li>Add a [[link:/golf/nets-and-mats/|hitting mat]] to protect the lawn.</li>
</ul>'''),

# ---------------- RACING HUB ----------------
dict(
    path="/racing/",
    title="Sim racing at home: wheels, pedals, cockpits and stands (UK)",
    short="Sim racing",
    description="UK guides to a home sim racing set-up: wheel bases, pedals, cockpits and rigs, seats and monitor stands, with Amazon UK prices checked 24 Nov 2026.",
    h1="Sim racing wheels, pedals and cockpits for UK rooms",
    hero=dict(
        variant="hero-racing",
        eyebrow="Sim Racing Section",
        lede="From a folding seat that tucks into a corner to an aluminium profile rig with direct drive force feedback, compare footprints and Amazon UK hardware.",
        cta_primary=("Room & set-up guide", "/racing/room-and-setup-guide/"),
        cta_secondary=("Direct drive wheels", "/racing/direct-drive-wheels/"),
        stats=[("17", "Amazon UK racing items checked"), ("~136x54 cm", "folding seat footprint"), ("7", "racing brands")],
        svg="racing-hero",
    ),
    related=[
        ("/compare/", "Compare all brands", "Includes Logitech, Thrustmaster, Fanatec, MOZA, Playseat, NLR and GT Omega."),
        ("/golf/", "Home golf bays", "Explore launch monitors, nets and simulator bays."),
    ],
    body='''<p class="lede">A sim racing set-up needs a wheel and pedals, something solid to mount them on, and a screen in front of you. This section covers each part and how much room it takes.</p>
<div class="cards two">
<a class="card tile" href="[[BP]]/racing/room-and-setup-guide/"><div><h3>Room and set-up guide</h3><p>Floor space for desk, stand and cockpit set-ups, using makers' dimensions.</p></div><span class="tile-cta">Check footprints &rarr;</span></a>
<a class="card tile" href="[[BP]]/racing/direct-drive-wheels/"><div><h3>Wheels and pedals</h3><p>Direct drive and geared wheels on Amazon UK, plus pedal sets.</p></div><span class="tile-cta">See wheels &amp; pedals &rarr;</span></a>
<a class="card tile" href="[[BP]]/racing/cockpits-and-rigs/"><div><h3>Cockpits, seats and stands</h3><p>Foldable seats, full cockpits, wheel stands and monitor stands.</p></div><span class="tile-cta">See cockpits &rarr;</span></a>
</div>
<h2>The parts of a sim racing set-up</h2>
<ol>
<li><strong>Wheel base and wheel</strong>, either geared or belt-driven, or direct drive.</li>
<li><strong>Pedals</strong>, often bundled with the wheel; some upgrades use a load cell brake.</li>
<li><strong>Mount</strong>: a desk clamp, a wheel stand, or a full cockpit with a seat.</li>
<li><strong>Screen</strong>: a TV, one monitor or three, often on a monitor stand.</li>
<li><strong>Extras</strong> such as a shifter or handbrake.</li>
</ol>
<p>Check that each part works with your console or PC. Platform details are in each Amazon listing title.</p>'''),

# ---------------- RACING ROOM GUIDE ----------------
dict(
    path="/racing/room-and-setup-guide/",
    title="Sim racing room and set-up guide: how much space you need",
    short="Room and set-up guide",
    crumbs=RACE,
    type="article",
    description="How much floor space a sim racing set-up takes, from a wheel stand to a full cockpit, using Playseat, Next Level Racing and Amazon UK listing dimensions.",
    faq=[
        ("How much floor space does a foldable racing cockpit take?", "Playseat lists the Challenge ActiFit at 136 x 54 x 96 cm (L x W x H) when unfolded, weighing 9 kg, and folds away between sessions."),
        ("Can a folding stand handle a direct drive wheel?", "Some folding frames flex under high torque. Next Level Racing states its F-GT includes wheel and pedal strengthening kits for direct drive wheels; always verify wheel base compatibility on the cockpit maker's site."),
    ],
    related=[
        ("/racing/direct-drive-wheels/", "Wheels and pedals", "Compare geared kits vs direct drive bases."),
        ("/racing/cockpits-and-rigs/", "Cockpits, seats and stands", "Full comparison of stands, folding seats and frames."),
    ],
    body='''<p class="lede">A sim racing set-up takes much less space than a golf bay. The floor space depends on how you mount the wheel, from a folding stand to a full cockpit.</p>
<h2>Footprints from makers and listings</h2>
<div class="tbl"><table><thead><tr><th>Set-up</th><th>Dimensions</th><th>Source</th></tr></thead><tbody>
<tr><td>Grefinity height-adjustable wheel stand</td><td>57.4 x 48 x 80 cm; 10.1 kg</td><td>Amazon UK listing</td></tr>
<tr><td>Playseat Challenge ActiFit (foldable)</td><td>136 x 54 x 96 cm (L x W x H); 9 kg; recommended driver length at least 120 cm</td><td>Playseat FAQ</td></tr>
<tr><td>Next Level Racing F-GT, Formula position</td><td>170 x 60 x 100 cm; maximum supported weight 130 kg</td><td>Next Level Racing support page</td></tr>
<tr><td>Next Level Racing F-GT, GT position</td><td>140 x 60 x 125 cm</td><td>Next Level Racing support page</td></tr>
<tr><td>Next Level Racing F-GT monitor stand</td><td>20.32 x 60.96 x 114.3 cm; 9.07 kg</td><td>Amazon UK listing</td></tr>
</tbody></table></div>
<p class="small">Add room to get in and out of the seat, and the depth of your screen or monitor stand in front of the wheel.</p>
<h2>Three ways to mount a wheel</h2>
<h3>Desk clamp</h3>
<p>Many geared wheels clamp to a desk. It takes no extra floor space, but the desk needs to stay put under force, and your chair needs to stay still when you brake.</p>
<h3>Wheel stand</h3>
<p>A folding stand holds the wheel and pedals and can be stored away. You sit on your own chair or sofa.</p>
[[p:grefinity-wheel-stand]]
<h3>Cockpit</h3>
<p>A cockpit fixes the seat, wheel and pedals together, so nothing moves under braking. Next Level Racing says the F-GT now includes pedal and wheel strengthening kits for direct drive wheels and high-load brake pedals.</p>
[[p:playseat-challenge]][[p:nlr-f-gt]]
<h2>Screens</h2>
<p>Single and triple monitor stands sit in front of the cockpit. The Next Level Racing Elite triple stand listing says it holds three 21 to 43 inch screens.</p>
[[p:nlr-f-gt-monitor-stand]]
<h2>Before you buy</h2>
<ol>
<li>Measure the floor area and leave space to get in and out.</li>
<li>Check the cockpit's supported wheel bases and pedals on the maker's page.</li>
<li>Check the cockpit's weight limit and recommended driver height.</li>
<li>Check console or PC compatibility for the wheel and pedals.</li>
</ol>
<h2>Sources</h2><ul class="sources">
<li>Playseat Challenge ActiFit FAQ: https://www.playseat.com/en-us/pages/faq-challenge-actifit</li>
<li>Next Level Racing F-GT Cockpit (NLR-S010) support page: https://support.nextlevelracing.com/hc/en-us/articles/13018208861199-Next-Level-Racing-F-GT-Cockpit-NLR-S010</li>
<li>Amazon UK listings linked on this page, checked [[checked]].</li>
</ul>'''),

# ---------------- RACING: WHEELS ----------------
dict(
    path="/racing/direct-drive-wheels/",
    faq=[
        ("What is the difference between geared and direct drive sim racing wheels?", "In a direct drive base such as the Fanatec CSL DD, MOZA R5 or Logitech G RS50, the wheel rim mounts directly to the motor shaft. Entry kits like the Logitech G923 drive the rim through internal gears."),
        ("Do direct drive wheel bases work on PS5 as well as PC?", "Only console-licensed models such as the Fanatec Gran Turismo DD Pro and Logitech G RS50 list PS5/PS4 compatibility; PC-only bases like the Fanatec CSL DD (PC) do not."),
    ],
    title="Direct drive and geared sim racing wheels on Amazon UK",
    short="Wheels and pedals",
    crumbs=RACE,
    type="article",
    description="Sim racing wheel bases and pedal sets on Amazon UK, from geared wheels to direct drive bases, with listing details and prices checked 24 Nov 2026.",
    itemlist=[
        ("Logitech G923", "/racing/direct-drive-wheels/#logitech-g923"),
        ("Thrustmaster T300 RS GT", "/racing/direct-drive-wheels/#thrustmaster-t300-rs-gt"),
        ("Fanatec CSL DD", "/racing/direct-drive-wheels/#fanatec-csl-dd"),
        ("MOZA R5 bundle", "/racing/direct-drive-wheels/#moza-r5-bundle"),
        ("Logitech G RS50", "/racing/direct-drive-wheels/#logitech-rs50"),
        ("Fanatec Gran Turismo DD Pro", "/racing/direct-drive-wheels/#fanatec-gt-dd-pro"),
    ],
    related=[
        ("/racing/cockpits-and-rigs/", "Cockpits and rigs", "Pair your wheel base with a suitable stand or rig."),
        ("/racing/room-and-setup-guide/", "Sim racing room guide", "Check floor footprint before ordering."),
    ],
    body='''<p class="lede">A direct drive wheel base has the wheel mounted straight onto the motor. Other wheels drive the rim through gears or a belt. The table shows how each Amazon UK listing describes the product.</p>
<h2>Wheels and bases compared</h2>
<div class="tbl"><table><thead><tr><th>Product</th><th>Type (listing)</th><th>Platforms (listing title)</th><th>Price checked</th></tr></thead><tbody>
<tr><td>Logitech G923</td><td>Wheel and pedals kit</td><td>PS5, PC</td><td>[[price:logitech-g923]]</td></tr>
<tr><td>Thrustmaster T300 RS GT</td><td>Wheel and 3-pedal set</td><td>PS5, PS4, PC</td><td>[[price:thrustmaster-t300-rs-gt]]</td></tr>
<tr><td>Fanatec CSL DD</td><td>Direct drive wheel base</td><td>PC</td><td>[[price:fanatec-csl-dd]]</td></tr>
<tr><td>MOZA R5 bundle</td><td>Direct drive base with pedals</td><td>See listing</td><td>[[price:moza-r5-bundle]]</td></tr>
<tr><td>Logitech G RS50</td><td>Direct drive 8Nm base and wheel</td><td>PS5, PC</td><td>[[price:logitech-rs50]]</td></tr>
<tr><td>Fanatec Gran Turismo DD Pro</td><td>Direct drive bundle</td><td>PC, PS5, PS4</td><td>[[price:fanatec-gt-dd-pro]]</td></tr>
</tbody></table></div>
<h2>Wheel and pedal kits</h2>
[[p:logitech-g923]][[p:thrustmaster-t300-rs-gt]]
<h2>Direct drive</h2>
<p>Before buying a direct drive base, check that your cockpit, stand or desk maker lists it as supported.</p>
[[p:fanatec-csl-dd]][[p:moza-r5-bundle]][[p:logitech-rs50]][[p:fanatec-gt-dd-pro]]
<h2>Pedals</h2>
[[p:fanatec-csl-elite-pedals-v2]][[p:logitech-g-pro-pedals]]
<h2>Things to check</h2>
<ul>
<li>Console or PC compatibility, from the listing title and the maker's page.</li>
<li>Whether the wheel rim and pedals are included or sold separately.</li>
<li>How you'll mount it: see the [[link:/racing/room-and-setup-guide/|room and set-up guide]].</li>
</ul>'''),

# ---------------- RACING: COCKPITS ----------------
dict(
    path="/racing/cockpits-and-rigs/",
    faq=[
        ("Which sim racing cockpits come without a seat?", "Frames such as the GT Omega PRIME Lite and wheel stands like the Grefinity stand are sold without a seat, so you either use your own chair or add a separate bucket seat."),
        ("Can a foldable cockpit store away after racing?", "Yes. Both the Playseat Challenge ActiFit and Next Level Racing GTLite Pro are designed to fold between sessions."),
    ],
    title="Sim racing cockpits, rigs, seats and monitor stands on Amazon UK",
    short="Cockpits and rigs",
    crumbs=RACE,
    type="article",
    description="Sim racing cockpits, foldable seats, wheel stands, seats and monitor stands on Amazon UK, with makers' dimensions and prices checked 24 Nov 2026.",
    itemlist=[
        ("Grefinity wheel stand", "/racing/cockpits-and-rigs/#grefinity-wheel-stand"),
        ("Playseat Challenge ActiFit", "/racing/cockpits-and-rigs/#playseat-challenge"),
        ("Next Level Racing GTLite Pro", "/racing/cockpits-and-rigs/#nlr-gtlite-pro"),
        ("Next Level Racing F-GT", "/racing/cockpits-and-rigs/#nlr-f-gt"),
        ("Playseat Trophy Logitech G Edition", "/racing/cockpits-and-rigs/#playseat-trophy"),
        ("GT Omega PRIME Lite", "/racing/cockpits-and-rigs/#gt-omega-prime-lite"),
    ],
    related=[
        ("/racing/direct-drive-wheels/", "Wheels and pedals", "Check direct drive torque vs cockpit support."),
        ("/racing/room-and-setup-guide/", "Sim racing room guide", "Dimensions and clearance checks."),
    ],
    body='''<p class="lede">From a folding seat that stores against a wall to an aluminium profile rig, these are the cockpit options listed on Amazon UK when we checked.</p>
<div class="tbl"><table><thead><tr><th>Product</th><th>Type</th><th>Price checked</th></tr></thead><tbody>
<tr><td>Grefinity wheel stand</td><td>Height-adjustable stand, no seat</td><td>[[price:grefinity-wheel-stand]]</td></tr>
<tr><td>Playseat Challenge ActiFit</td><td>Foldable seat cockpit</td><td>[[price:playseat-challenge]]</td></tr>
<tr><td>Next Level Racing GTLite Pro</td><td>Foldable cockpit</td><td>[[price:nlr-gtlite-pro]]</td></tr>
<tr><td>Next Level Racing F-GT</td><td>Formula and GT cockpit</td><td>[[price:nlr-f-gt]]</td></tr>
<tr><td>GT Omega PRIME Lite</td><td>Cockpit frame, no seat</td><td>[[price:gt-omega-prime-lite]]</td></tr>
<tr><td>Playseat Trophy Logitech G Edition</td><td>Cockpit</td><td>[[price:playseat-trophy]]</td></tr>
</tbody></table></div>
<h2>Stands and foldable options</h2>
[[p:grefinity-wheel-stand]][[p:playseat-challenge]][[p:nlr-gtlite-pro]]
<h2>Full cockpits</h2>
[[p:nlr-f-gt]][[p:playseat-trophy]][[p:gt-omega-prime-lite]]
<h2>Seats</h2>
<p>Frames sold without a seat, such as the GT Omega PRIME Lite listed here, need a separate seat.</p>
[[p:gt-omega-inertia-seat]]
<h2>Monitor stands</h2>
[[p:nlr-f-gt-monitor-stand]][[p:nlr-elite-triple-stand]]
<p>For floor space, see the [[link:/racing/room-and-setup-guide/|room and set-up guide]].</p>'''),

# ---------------- ABOUT ----------------
dict(
    path="/about/",
    title="About [[SITE_NAME]]",
    short="About",
    description="Who runs [[SITE_NAME]], how we research products, and how the site makes money.",
    body='''<p>[[SITE_NAME]] is a UK website about setting up home simulators, starting with golf and sim racing.</p>
<h2>How we research</h2>
<ul>
<li>We use makers' manuals and set-up pages, and Amazon UK listings. Every figure on the site names its source.</li>
<li>We have not tested, reviewed hands-on or owned the products we list.</li>
<li>We don't give star ratings or scores.</li>
<li>Prices are shown as checked on a stated date, because they change often.</li>
</ul>
<h2>How the site is paid for</h2>
<p>We earn a commission from Amazon when you buy through some links, at no extra cost to you. See the [[link:/affiliate-disclosure/|affiliate disclosure]].</p>
<p>Spotted something out of date? See the [[link:/contact/|contact page]].</p>'''),

# ---------------- DISCLOSURE ----------------
dict(
    path="/affiliate-disclosure/",
    title="Affiliate disclosure",
    short="Affiliate disclosure",
    description="[[SITE_NAME]] is a participant in the Amazon Associates Programme for Amazon.co.uk. Here's how our affiliate links work.",
    body='''<p>[[SITE_NAME]] is a participant in the Amazon Associates Programme for Amazon.co.uk, an affiliate advertising programme that lets sites earn advertising fees by linking to Amazon.co.uk.</p>
<p>As an Amazon Associate, [[SITE_NAME]] earns from qualifying purchases.</p>
<ul>
<li>Links to Amazon on this site are affiliate links. If you buy after clicking one, we may earn a commission. The price you pay is the same.</li>
<li>Affiliate links are marked as sponsored in the page code.</li>
<li>Prices and availability were checked on the date shown on each page and may have changed. The price on Amazon at the time of purchase applies.</li>
<li>Commissions don't change what we include. We list products that are relevant to the guide and available on Amazon UK when checked.</li>
</ul>'''),

# ---------------- PRIVACY ----------------
dict(
    path="/privacy/",
    title="Privacy",
    short="Privacy",
    description="How [[SITE_NAME]] handles privacy: no accounts, no analytics, no forms, and what happens when you click through to Amazon.",
    body='''<p>Last updated [[checked]].</p>
<h2>What this site collects</h2>
<p>This site has no accounts, no comments and no forms, and it doesn't use analytics or advertising cookies of its own.</p>
<h2>Hosting</h2>
<p>The site is hosted on GitHub Pages. GitHub may log technical information such as your IP address when you visit, as described in GitHub's privacy statement: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement</p>
<h2>Amazon links</h2>
<p>When you click a link to Amazon, Amazon may set cookies to track the visit so that a commission can be paid. That's covered by Amazon's own privacy notice: https://www.amazon.co.uk/gp/help/customer/display.html?nodeId=201909010</p>
<h2>Changes</h2>
<p>If we add a contact form or any analytics, we'll update this page first.</p>'''),

# ---------------- CONTACT ----------------
dict(
    path="/contact/",
    title="Contact",
    short="Contact",
    description="How to contact [[SITE_NAME]] to report an out-of-date UK price, broken link or product update.",
    body='''<p>A contact form is coming soon.</p>
<p>When it's ready, you'll be able to use it to tell us about an out-of-date price, a broken link or a product listing that has changed.</p>'''),

# ---------------- 404 ----------------
dict(
    path="/404.html",
    title="Page not found",
    short="Not found",
    disclosure=False,
    description="This page could not be found on [[SITE_NAME]]. Browse home golf bays, brand comparisons or sim racing.",
    body='''<p>That page couldn't be found. Try the [[link:/|home page]], [[link:/compare/|compare brands]], [[link:/golf/|home golf]] or [[link:/racing/|sim racing]].</p>'''),
]
