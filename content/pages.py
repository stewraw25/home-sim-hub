# Page content for Home Sim Hub. Markers: [[p:slug]] product card, [[buy:slug|text]] inline affiliate link,
# [[price:slug]] checked price, [[link:/path/|text]] internal link, [[checked]] price-check date.
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
</ul>'''

PAGES = [
# ---------------- HOME ----------------
dict(path="/", title="Home Sim Hub: UK guides to home golf bays and sim racing rigs", short="Home",
 description="Plain-English UK guides to setting up a home golf simulator or sim racing rig: room sizes, what you need, and Amazon UK products with prices checked.",
 h1="Build a home simulator that fits your room",
 body='''<p class="lede">Home Sim Hub explains what you need for a home golf bay or a sim racing setup, how much room each one takes, and which Amazon UK products fit each part of the job.</p>
<p>We work from the makers' own manuals and set-up pages and from Amazon UK listings. We don't test products ourselves, and we say where each figure comes from.</p>
<div class="cards two">
<a class="card tile" href="[[BP]]/golf/"><h3>Home golf</h3><p>Launch monitors, home simulator bays, nets, mats and how much room you need.</p></a>
<a class="card tile" href="[[BP]]/racing/"><h3>Sim racing</h3><p>Wheels, pedals, cockpits, seats and monitor stands, and how much floor space a rig takes.</p></a>
</div>
<h2>Start here</h2>
<ul>
<li>[[link:/golf/room-size-guide/|How much room do you need for a golf simulator?]]</li>
<li>[[link:/golf/launch-monitor-vs-simulator/|Launch monitor or full simulator: what's the difference?]]</li>
<li>[[link:/golf/launch-monitors-under-1000/|Launch monitors under £1,000 on Amazon UK]]</li>
<li>[[link:/racing/room-and-setup-guide/|Sim racing room and set-up guide]]</li>
</ul>
<h2>More sections are planned</h2>
<p>The site is built so new sections can be added over time, such as VR and flight simulation.</p>'''),

# ---------------- GOLF HUB ----------------
dict(path="/golf/", title="Home golf simulators and practice set-ups (UK)", short="Home golf",
 description="Everything that goes into a home golf bay in the UK: launch monitors, nets and impact screens, hitting mats, enclosures, projectors and room sizes.",
 body='''<p class="lede">A home golf set-up can be as simple as a net and a mat in the garden, or a full indoor bay with a launch monitor, impact screen and projector. This section covers each part.</p>
<div class="cards two">
<a class="card tile" href="[[BP]]/golf/launch-monitors/"><h3>Launch monitors</h3><p>The device that measures each shot. Radar units sit behind you; camera units sit beside the ball.</p></a>
<a class="card tile" href="[[BP]]/golf/simulators/"><h3>Home simulator bays</h3><p>Enclosures, impact screens and projectors that turn a launch monitor into a simulator.</p></a>
<a class="card tile" href="[[BP]]/golf/nets-and-mats/"><h3>Nets and mats</h3><p>Practice nets for the garden or garage, and hitting mats.</p></a>
<a class="card tile" href="[[BP]]/golf/room-size-guide/"><h3>Room size guide</h3><p>Ceiling height, width and depth, using the makers' published figures.</p></a>
</div>
<h2>Guides</h2>
<ul>
<li>[[link:/golf/launch-monitor-vs-simulator/|Launch monitor vs simulator explained]]</li>
<li>[[link:/golf/launch-monitors-under-1000/|Launch monitors under £1,000]]</li>
<li>[[link:/golf/garage-golf-simulator/|Setting up a golf simulator in a garage]]</li>
<li>[[link:/golf/garmin-r50-vs-skytrak-st-max/|Garmin Approach R50 vs SkyTrak ST MAX]]</li>
<li>[[link:/golf/golf-nets-for-the-garden/|Golf nets for the garden]]</li>
</ul>'''),

# ---------------- LAUNCH MONITORS HUB ----------------
dict(path="/golf/launch-monitors/", title="Golf launch monitors on Amazon UK", short="Launch monitors", crumbs=GOLF, type="article",
 description="How home golf launch monitors differ, where each one sits, and the launch monitors listed on Amazon UK with prices checked 24 Nov 2026.",
 body='''<p class="lede">A launch monitor measures what happens when you hit the ball, such as ball speed and launch angle. Many also link to simulator software so you can play virtual courses.</p>
<h2>Behind the ball or beside it</h2>
<p>Where a launch monitor sits decides how much room it needs.</p>
<ul>
<li>Radar units such as the Garmin Approach R10 and Rapsodo MLM2PRO sit on the floor behind the golfer. Garmin's R10 manual says to place it 1.8 to 2.4 m (6 to 8 ft) behind the tee. Rapsodo says 6.5 to 8.5 ft behind the ball for the MLM2PRO.</li>
<li>Camera units such as the Garmin Approach R50, SkyTrak ST MAX and Square Golf Omni sit beside the ball. Garmin's R50 manual says about 0.5 m (1.5 ft) to the side of the tee, facing it.</li>
</ul>
<p>See the [[link:/golf/room-size-guide/|room size guide]] for each maker's figures.</p>
<h2>Launch monitors listed on Amazon UK</h2>
<div class="tbl"><table><thead><tr><th>Model</th><th>Price checked [[checked]]</th><th>Where it sits (maker)</th></tr></thead><tbody>
<tr><td>[[buy:shot-scope-lm1|Shot Scope LM1]]</td><td>[[price:shot-scope-lm1]]</td><td>Check the maker's set-up guide</td></tr>
<tr><td>[[buy:garmin-approach-r10|Garmin Approach R10]]</td><td>[[price:garmin-approach-r10]]</td><td>1.8 to 2.4 m behind the tee</td></tr>
<tr><td>[[buy:rapsodo-mlm2pro|Rapsodo MLM2PRO]]</td><td>[[price:rapsodo-mlm2pro]]</td><td>6.5 to 8.5 ft behind the ball</td></tr>
<tr><td>[[buy:square-golf-indoor|Square Golf indoor launch monitor]]</td><td>[[price:square-golf-indoor]]</td><td>Check the maker's set-up guide</td></tr>
<tr><td>[[buy:square-golf-omni|Square Golf Omni]]</td><td>[[price:square-golf-omni]]</td><td>Beside the golfer, about 14 to 20 in from the tee (retailer figure)</td></tr>
<tr><td>[[buy:skytrak-st-max|SkyTrak ST MAX]]</td><td>[[price:skytrak-st-max]]</td><td>Beside the ball</td></tr>
<tr><td>[[buy:garmin-approach-r50|Garmin Approach R50]]</td><td>[[price:garmin-approach-r50]]</td><td>About 0.5 m to the side of the tee</td></tr>
</tbody></table></div>
<p class="small">Prices are as checked on [[checked]] and change often. Check Amazon for the current price.</p>
[[p:garmin-approach-r10]][[p:rapsodo-mlm2pro]][[p:shot-scope-lm1]][[p:square-golf-indoor]][[p:square-golf-omni]][[p:skytrak-st-max]][[p:garmin-approach-r50]]
<h2>Subscriptions</h2>
<p>Some features need a paid subscription. For example, the Amazon listings for the Garmin R10 and R50 say virtual rounds need an active Garmin Golf membership or subscription. Check each maker's current terms before you buy.</p>
''' + SRC_GOLF),

# ---------------- SIMULATOR HUB ----------------
dict(path="/golf/simulators/", title="Home golf simulator bays: enclosures, screens and projectors", short="Simulator bays", crumbs=GOLF, type="article",
 description="What goes into a home golf simulator bay in the UK: launch monitor, impact screen or net, enclosure, hitting mat, projector and software.",
 body='''<p class="lede">A home simulator bay puts a picture of the shot in front of you. It needs a launch monitor plus a few other parts.</p>
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
dict(path="/golf/nets-and-mats/", title="Golf nets, practice cages and hitting mats (UK)", short="Nets and mats", crumbs=GOLF, type="article",
 description="Golf practice nets, cages and hitting mats listed on Amazon UK, with sizes from each listing and prices checked 24 Nov 2026.",
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
dict(path="/golf/room-size-guide/", title="How much room do you need for a golf simulator? (UK guide)", short="Room size guide", crumbs=GOLF, type="article",
 description="Ceiling height, width and depth for a home golf simulator, using Garmin, Rapsodo and SkyTrak published figures, converted to metres for UK rooms.",
 body='''<p class="lede">Three measurements decide whether a golf simulator fits: ceiling height, room width and room depth. Each launch monitor maker publishes its own figures, so start with the one you're considering.</p>
<div class="callout">The quickest check, which SkyTrak suggests: stand where you'd hit, take a slow practice swing with your driver, and see whether you clear the ceiling, walls and lights.</div>
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
dict(path="/golf/launch-monitor-vs-simulator/", title="Launch monitor vs golf simulator: what's the difference?", short="Launch monitor vs simulator", crumbs=GOLF, type="article",
 description="A launch monitor measures your shots; a golf simulator adds a screen, software and an enclosure so you can see the shot and play courses. Here's how they fit together.",
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
dict(path="/golf/launch-monitors-under-1000/", title="Golf launch monitors under £1,000 on Amazon UK", short="Under £1,000", crumbs=GOLF, type="article",
 description="Launch monitors under £1,000 listed on Amazon UK, compared by where they sit and how much room the maker says they need. Prices checked 24 Nov 2026.",
 body='''<p class="lede">These four launch monitors were listed on Amazon UK under £1,000 when we checked on [[checked]]. We've set out where each one sits and what the maker says about space, so you can check them against your room.</p>
<div class="tbl"><table><thead><tr><th>Model</th><th>Price checked</th><th>Placement</th><th>Indoor space (maker)</th></tr></thead><tbody>
<tr><td>Shot Scope LM1</td><td>[[price:shot-scope-lm1]]</td><td>See maker guide</td><td>Not checked</td></tr>
<tr><td>Garmin Approach R10</td><td>[[price:garmin-approach-r10]]</td><td>Behind the ball, 1.8 to 2.4 m</td><td>Ball at least 2.4 m from the net</td></tr>
<tr><td>Rapsodo MLM2PRO</td><td>[[price:rapsodo-mlm2pro]]</td><td>Behind the ball, 6.5 to 8.5 ft</td><td>A little more than 14 ft in total</td></tr>
<tr><td>Square Golf indoor</td><td>[[price:square-golf-indoor]]</td><td>See maker guide</td><td>Not checked</td></tr>
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
dict(path="/golf/garage-golf-simulator/", title="Setting up a golf simulator in a UK garage", short="Garage simulator", crumbs=GOLF, type="article",
 description="A step-by-step guide to fitting a home golf simulator into a UK garage: measuring, picking a launch monitor for the depth, screens, mats and projectors.",
 body='''<p class="lede">A garage can have more depth than a spare room, which helps with launch monitors that sit behind the golfer. Check the ceiling height carefully, including any garage door track or opener.</p>
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
dict(path="/golf/garmin-r50-vs-skytrak-st-max/", title="Garmin Approach R50 vs SkyTrak ST MAX", short="R50 vs ST MAX", crumbs=GOLF, type="article",
 description="Garmin Approach R50 and SkyTrak ST MAX compared side by side using Amazon UK listing details and each maker's set-up guidance. Prices checked 24 Nov 2026.",
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
dict(path="/golf/golf-nets-for-the-garden/", title="Golf nets for the garden: sizes and options on Amazon UK", short="Garden golf nets", crumbs=GOLF, type="article",
 description="Golf practice nets and cages for UK gardens, compared by the sizes given in each Amazon UK listing, with prices checked 24 Nov 2026.",
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
dict(path="/racing/", title="Sim racing at home: wheels, pedals, cockpits and stands (UK)", short="Sim racing",
 description="UK guides to a home sim racing set-up: wheel bases, pedals, cockpits and rigs, seats and monitor stands, with Amazon UK prices checked 24 Nov 2026.",
 body='''<p class="lede">A sim racing set-up needs a wheel and pedals, something solid to mount them on, and a screen in front of you. This section covers each part and how much room it takes.</p>
<div class="cards two">
<a class="card tile" href="[[BP]]/racing/room-and-setup-guide/"><h3>Room and set-up guide</h3><p>Floor space for desk, stand and cockpit set-ups, using makers' dimensions.</p></a>
<a class="card tile" href="[[BP]]/racing/direct-drive-wheels/"><h3>Wheels and pedals</h3><p>Direct drive and geared wheels on Amazon UK, plus pedal sets.</p></a>
<a class="card tile" href="[[BP]]/racing/cockpits-and-rigs/"><h3>Cockpits, seats and stands</h3><p>Foldable seats, full cockpits, wheel stands and monitor stands.</p></a>
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
dict(path="/racing/room-and-setup-guide/", title="Sim racing room and set-up guide: how much space you need", short="Room and set-up guide", crumbs=RACE, type="article",
 description="How much floor space a sim racing set-up takes, from a wheel stand to a full cockpit, using Playseat, Next Level Racing and Amazon UK listing dimensions.",
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
dict(path="/racing/direct-drive-wheels/", title="Direct drive and geared sim racing wheels on Amazon UK", short="Wheels and pedals", crumbs=RACE, type="article",
 description="Sim racing wheel bases and pedal sets on Amazon UK, from geared wheels to direct drive bases, with listing details and prices checked 24 Nov 2026.",
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
dict(path="/racing/cockpits-and-rigs/", title="Sim racing cockpits, rigs, seats and monitor stands on Amazon UK", short="Cockpits and rigs", crumbs=RACE, type="article",
 description="Sim racing cockpits, foldable seats, wheel stands, seats and monitor stands on Amazon UK, with makers' dimensions and prices checked 24 Nov 2026.",
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
dict(path="/about/", title="About Home Sim Hub", short="About",
 description="Who runs Home Sim Hub, how we research products, and how the site makes money.",
 body='''<p>Home Sim Hub is a UK website about setting up home simulators, starting with golf and sim racing.</p>
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
dict(path="/affiliate-disclosure/", title="Affiliate disclosure", short="Affiliate disclosure",
 description="Home Sim Hub is a participant in the Amazon Associates Programme for Amazon.co.uk. Here's how our affiliate links work.",
 body='''<p>Home Sim Hub is a participant in the Amazon Associates Programme for Amazon.co.uk, an affiliate advertising programme that lets sites earn advertising fees by linking to Amazon.co.uk.</p>
<p>As an Amazon Associate, Home Sim Hub earns from qualifying purchases.</p>
<ul>
<li>Links to Amazon on this site are affiliate links. If you buy after clicking one, we may earn a commission. The price you pay is the same.</li>
<li>Affiliate links are marked as sponsored in the page code.</li>
<li>Prices and availability were checked on the date shown on each page and may have changed. The price on Amazon at the time of purchase applies.</li>
<li>Commissions don't change what we include. We list products that are relevant to the guide and available on Amazon UK when checked.</li>
</ul>'''),

# ---------------- PRIVACY ----------------
dict(path="/privacy/", title="Privacy", short="Privacy",
 description="How Home Sim Hub handles privacy: no accounts, no analytics, no forms, and what happens when you click through to Amazon.",
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
dict(path="/contact/", title="Contact", short="Contact",
 description="How to contact Home Sim Hub.",
 body='''<p>A contact form is coming soon.</p>
<p>When it's ready, you'll be able to use it to tell us about an out-of-date price, a broken link or a product listing that has changed.</p>'''),

# ---------------- 404 ----------------
dict(path="/404.html", title="Page not found", short="Not found", disclosure=False,
 description="This page could not be found.",
 body='''<p>That page couldn't be found. Try the [[link:/|home page]], [[link:/golf/|home golf]] or [[link:/racing/|sim racing]].</p>'''),
]
