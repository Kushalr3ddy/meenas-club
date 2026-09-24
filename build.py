#!/usr/bin/env python3
"""Generates the static pages (folder-per-page). Run: python3 build.py"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
NAME = "Meenaa's Millionaire Club"
TAGLINE = "Connect · Grow · Build Wealth"
EMAIL_SEC = "secretarymmclub@gmail.com"
EMAIL_PRES = "presidentmmclub@gmail.com"
PHONE = "9449904569"
PHONE_INTL = "919449904569"

NAV = [("", "Home"), ("about", "About"), ("membership", "Membership"),
       ("branches", "Branches"), ("facilities", "Facilities"), ("contact", "Contact")]

CITIES = [
    ("Bengaluru", "Karnataka", "bengaluru", "Headquarters · First Stop · Inauguration City", 7),
    ("Chennai", "Tamil Nadu", "chennai", "South India cluster", 7),
    ("Hyderabad", "Telangana", "hyderabad", "South India cluster", 7),
    ("Mumbai", "Maharashtra", "mumbai", "West India cluster", 6),
    ("Ahmedabad", "Gujarat", "ahmedabad", "West India cluster", 6),
    ("Delhi", "New Delhi", "delhi", "North & East cluster", 6),
    ("Kolkata", "West Bengal", "kolkata", "North & East cluster", 6),
]

# (sl, name, amount, remarks, category)
TIERS = [
    (1, "Lifetime Membership", "₹1.00 Crore", "Full privileges as per Club Rules", "individual"),
    (2, "Resident Membership – Men", "₹50 Lakhs", "Subject to eligibility criteria", "individual"),
    (3, "Resident Membership – Lady", "₹30 Lakhs", "Subject to eligibility criteria", "individual"),
    (4, "Institutional Membership (Life Time Temporary)", "₹15 Lakhs", "Limited tenure; no voting rights", "institutional"),
    (5, "Institutional Membership (Permanent Member)", "₹30 Lakhs", "As per Club Rules", "institutional"),
    (6, "State Government – Officer Grade (LTTM)", "₹15 Lakhs", "Subject to service verification", "government"),
    (7, "Central Government – Officer Grade (LTTM)", "₹25 Lakhs", "Subject to service verification", "government"),
    (8, "Cabinet Ranking Officer (LTTM)", "₹40 Lakhs", "As approved by Governing Body", "government"),
    (9, "Defence Personnel – Army, Navy, Air Force & Administrative (LTTM)", "₹10 Lakhs", "Subject to valid credentials", "government"),
    (10, "Business Class Membership (LTTM)", "₹50 Lakhs", "As per Club Rules", "business"),
    (11, "Landlord – General Category", "₹25 Lakhs", "Subject to eligibility", "individual"),
    (12, "Guest Membership", "—", "Temporary access as per Club Rules", "special"),
    (13, "Premium Membership · All-India", "₹5.00 Crore", "Utilise all 19 branches of the Club across India", "premium"),
    (14, "Premium Membership · South", "₹3.00 Crore", "7 branches in Bengaluru, Hyderabad and Chennai only", "premium"),
    (15, "Premium Membership · West", "₹3.00 Crore", "6 branches in Mumbai and Ahmedabad only", "premium"),
    (16, "Premium Membership · North & East", "₹3.00 Crore", "6 branches in Delhi and Kolkata only", "premium"),
    (17, "Corporate Membership", "₹10.00 Crore", "Access and utilise all 19 branches across India", "business"),
    (18, "State Judiciary (LTTM)", "₹15 Lakhs", "Designated branches in Bengaluru only", "government"),
    (19, "National Judiciary (LTTM)", "₹40 Lakhs", "Access all 19 branches across India", "government"),
    (20, "MNC Corporate (LTTM)", "₹10.00 Crore", "Utilise all 19 branches across India", "business"),
    (21, "NRI (LTTM)", "₹3.00 Crore", "Access all 19 branches across India", "special"),
]

SIGNATURE = [
    ("Meenaa's Silver", "Entry to the Club"),
    ("Meenaa's Gold", "Everyday club privileges"),
    ("Meenaa's Pearl", "Family & lifestyle access"),
    ("Meenaa's Jasmine", "Wellness & leisure focus"),
    ("Meenaa's Gem", "Enhanced dining & events"),
    ("Meenaa's Regular", "Standard membership"),
    ("Meenaa's Premium", "Priority facilities"),
    ("Meenaa's Universal", "Multi-branch access"),
    ("Meenaa's Diamond", "Elite business & lifestyle"),
    ("Meenaa's Platinum", "Top-tier privileges"),
    ("Meenaa's VVIP", "Private & priority access"),
]

STARS = [
    ("Business", "Business lounge, board room, conference centre, co-working, investor meets, startup forum and CEO networking.", "💼"),
    ("Social", "Members lounge, social evenings, community programmes and relationship-building among peers.", "🤝"),
    ("Sports", "Gym, swimming, badminton, tennis, cricket practice, table tennis, billiards, snooker and chess.", "🏆"),
    ("Wellness", "Yoga, meditation, spa, sauna, steam, nutrition centre and wellness consultation.", "🧘"),
    ("Family", "Family lounge, kids zone, hobby and art rooms, birthday zone and summer camps.", "👨‍👩‍👧"),
    ("Entertainment", "Mini theatre, music lounge, karaoke, gaming, cultural stage and live events.", "🎭"),
    ("Hospitality", "Premium restaurant, café, banquet, private dining, guest suites, concierge and valet.", "🍽️"),
]

FACILITIES = [
    ("Reception & Services", ["Grand reception", "Membership desk", "Concierge", "Digital check-in", "Member help desk", "Visitor management", "Information centre"]),
    ("Business", ["Business lounge", "Board room", "Conference hall", "Executive meeting rooms", "Co-working space", "Private offices", "Business library", "Digital meeting room"]),
    ("Sports", ["Gym", "Swimming pool", "Badminton courts", "Tennis court", "Table tennis", "Billiards & snooker", "Chess room", "Cricket practice area"]),
    ("Wellness", ["Yoga studio", "Meditation hall", "Spa", "Sauna & steam", "Relaxation lounge", "Fitness assessment", "Nutrition centre", "Recovery zone"]),
    ("Family & Kids", ["Family lounge", "Kids play area", "Activity & hobby rooms", "Art room", "Reading room", "Birthday zone", "Kids learning zone", "Summer camp centre"]),
    ("Entertainment", ["Mini theatre", "Music lounge", "Karaoke room", "Gaming zone", "Cultural stage", "Art gallery", "Movie screening room", "Talent show area"]),
    ("Hospitality", ["Premium restaurant", "Café & coffee lounge", "Private dining", "Banquet hall", "Guest rooms & suites", "Valet parking", "Event catering"]),
    ("Outdoor & Sky", ["Rooftop garden", "Sky lounge", "Open-air dining", "Walking area", "Event lawn", "Children's outdoor zone", "Family picnic area"]),
    ("VIP Services", ["VIP lounge", "VVIP lounge", "Private meeting rooms", "Executive concierge", "Corporate event services", "Travel assistance", "Business referral network", "Helipad & air taxi (planned)"]),
]

EVENTS = [
    ("Jan", "New Year Members' Celebration"), ("Feb", "Business Networking"), ("Mar", "Sports Championship"),
    ("Apr", "Family Festival"), ("May", "Summer Kids Programme"), ("Jun", "Wellness Month"),
    ("Jul", "Entrepreneurs Summit"), ("Aug", "Cultural Programme"), ("Sep", "Business Meet"),
    ("Oct", "Family Carnival"), ("Nov", "Sports Festival"), ("Dec", "Annual Awards & Gala"),
]

TIER_FILTERS = [("all", "All"), ("individual", "Individual"), ("institutional", "Institutional"),
                ("government", "Government & Services"), ("business", "Business & Corporate"),
                ("premium", "Premium Multi-Branch"), ("special", "NRI & Guest")]


def e(s):
    return html.escape(s, quote=True)


def head(title, desc, r):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#070d1c">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{r}assets/img/poster-membership.jpg">
<link rel="icon" href="{r}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;0,700;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
</head>"""


def header(r, active):
    cur = ' class="active" aria-current="page"'
    links = "".join(
        f'<a href="{r}{p + "/" if p else ""}"{cur if p == active else ""}>{lbl}</a>'
        for p, lbl in NAV)
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="{r}" aria-label="{e(NAME)} home">
      <img src="{r}assets/img/logo.png" alt="" width="46" height="36">
      <span><b>Meenaa's</b><small>Millionaire Club</small></span>
    </a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><i></i><i></i><i></i></button>
    <nav id="nav" class="nav">{links}<a class="btn btn-sm" href="{r}contact/#enquire">Join the Club</a></nav>
  </div>
</header>
<main id="main">"""


def footer(r):
    cities = "".join(f'<li><a href="{r}branches/#{c[2]}">{c[0]}</a></li>' for c in CITIES)
    pages = "".join(f'<li><a href="{r}{p + "/" if p else ""}">{l}</a></li>' for p, l in NAV)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <div class="foot-brand"><img src="{r}assets/img/logo.png" alt="" width="64" height="51"><div><b>Meenaa's</b><small>Millionaire Club<sup>®</sup></small></div></div>
      <p class="muted">More than a club — a complete lifestyle destination. Business, social, sports, wellness, family, entertainment and hospitality under one roof, in seven great cities.</p>
    </div>
    <div><h4>Explore</h4><ul>{pages}</ul></div>
    <div><h4>Branches</h4><ul>{cities}</ul></div>
    <div><h4>Contact</h4>
      <ul class="contact-list">
        <li><span>Secretary</span><a href="mailto:{EMAIL_SEC}">{EMAIL_SEC}</a></li>
        <li><span>President</span><a href="mailto:{EMAIL_PRES}">{EMAIL_PRES}</a></li>
        <li><span>Mobile</span><a href="tel:+{PHONE_INTL}">{PHONE}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap fine">
    <p>Membership contributions are for access to club facilities and services and are not an investment product; no returns are promised. Fees, eligibility and branch access are indicative and subject to the Club's rules and Governing Body approval.</p>
    <p>© <span id="yr">2026</span> {e(NAME)}<sup>®</sup>. All rights reserved.</p>
  </div>
</footer>
<script src="{r}assets/js/main.js"></script>
</body>
</html>
"""


def page(path, title, desc, active, body):
    r = "" if path == "" else "../"
    out = head(title, desc, r) + header(r, active) + body.replace("{R}", r) + footer(r)
    d = os.path.join(ROOT, path) if path else ROOT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


def page_hero(kicker, title, sub):
    return f"""<section class="page-hero"><div class="wrap">
  <p class="kicker">{kicker}</p><h1>{title}</h1><p class="lead">{sub}</p>
  <div class="rule"><span>✦</span></div></div></section>"""


def tier_row(t):
    sl, name, amt, rem, cat = t
    return (f'<tr data-cat="{cat}"><td class="sl">{sl:02d}</td><td class="nm">{e(name)}</td>'
            f'<td class="amt">{e(amt)}</td><td class="rm">{e(rem)}</td></tr>')


def stars_grid():
    return "".join(
        f'<article class="star reveal"><div class="star-n">{i}</div>'
        f'<h3>{n}</h3><p>{d}</p></article>' for i, (n, d, ico) in enumerate(STARS, 1))


def city_cards(link=True):
    out = ""
    for n, st, slug, role, br in CITIES:
        out += (f'<a class="city reveal" href="{{R}}branches/#{slug}"><img src="{{R}}assets/img/city-{slug}.jpg" alt="{n}" loading="lazy">'
                f'<div><h3>{n}</h3><span>{st}</span></div></a>')
    return out


# ---------------- HOME ----------------
home = f"""
<section class="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-in">
    <img class="hero-logo" src="{{R}}assets/img/logo.png" alt="{e(NAME)} crest" width="320" height="254">
    <p class="ribbon">Now Membership Open</p>
    <h1>Meenaa's <span>Millionaire Club<sup>®</sup></span></h1>
    <p class="tag">Connect &nbsp;|&nbsp; Grow &nbsp;|&nbsp; Build Wealth</p>
    <p class="lead">A global-class members' club bringing together entrepreneurs, professionals, families and leaders — across 7 cities and 19 places in India.</p>
    <div class="cta">
      <a class="btn" href="{{R}}membership/">View Memberships</a>
      <a class="btn btn-ghost" href="{{R}}contact/#enquire">Enquire Now</a>
    </div>
  </div>
</section>

<section class="stats"><div class="wrap stat-grid">
  <div><b data-count="7">7</b><span>★ Cities</span></div>
  <div><b data-count="19">19</b><span>Places</span></div>
  <div><b>Fortune 50000+</b><span>Business network</span></div>
  <div><b data-count="21">21</b><span>Membership categories</span></div>
</div></section>

<section class="sec inaug"><div class="wrap split">
  <div class="reveal">
    <p class="kicker">A New Chapter Begins</p>
    <h2>First Stop: <em>Bengaluru</em></h2>
    <p>The Club's journey begins in Bengaluru with the inauguration ceremony, then travels on to Chennai, Hyderabad, Mumbai, Ahmedabad, Delhi and Kolkata — a connected network of 19 places where a single membership can open doors across the country.</p>
    <ul class="ticks">
      <li>Inauguration ceremony in Bengaluru, Karnataka</li>
      <li>Founding members recognised with a special membership card</li>
      <li>Multi-city access on Premium, Corporate and NRI memberships</li>
    </ul>
    <a class="btn" href="{{R}}branches/">Explore the Network</a>
  </div>
  <figure class="reveal map-fig"><img src="{{R}}assets/img/india-map.jpg" alt="Map of India showing Bengaluru, Chennai, Hyderabad, Mumbai, Ahmedabad, Delhi and Kolkata" loading="lazy"></figure>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">The Seven-Star Experience</p><h2>Seven Stars. One Exclusive Experience.</h2>
  <p>Every branch is built around seven pillars so members can work, train, dine, unwind and celebrate — all under one roof.</p></div>
  <div class="star-grid">{stars_grid()}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Membership</p><h2>A Place for Every Member</h2>
  <p>From resident and lifetime memberships to premium multi-branch and corporate access — 21 categories in all.</p></div>
  <div class="hl-grid">
    <article class="hl reveal"><span class="hl-k">Lifetime</span><b>₹1 Crore</b><p>Full privileges as per Club Rules.</p></article>
    <article class="hl reveal"><span class="hl-k">Resident</span><b>₹30L – ₹50L</b><p>Resident membership for ladies and men.</p></article>
    <article class="hl hl-feat reveal"><span class="hl-k">Premium · All-India</span><b>₹5 Crore</b><p>Utilise all 19 branches across India.</p></article>
    <article class="hl reveal"><span class="hl-k">Corporate</span><b>₹10 Crore</b><p>Company-wide access to all 19 branches.</p></article>
  </div>
  <p class="center"><a class="btn" href="{{R}}membership/">See the full fee structure</a></p>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Signature Tiers</p><h2>The Meenaa's Collection</h2>
  <p>Eleven signature names to recognise every level of membership.</p></div>
  <div class="sig-grid reveal">{"".join(f'<div class="sig"><b>{n}</b><span>{d}</span></div>' for n, d in SIGNATURE)}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Signature Privileges</p><h2>Beyond the Ordinary</h2></div>
  <div class="priv-grid">
    <article class="priv reveal"><h3>Helipad &amp; Air Taxi</h3><p>Planned helipad and air-taxi connectivity between club cities, with inter-club travel limits by membership tier.</p></article>
    <article class="priv reveal"><h3>Business Magnets Meet-ups</h3><p>Regular gatherings that bring Fortune-scale business leaders, investors and founders together.</p></article>
    <article class="priv reveal"><h3>Club Network</h3><p>Members can be welcomed at partner branches across cities, with future international club partnerships.</p></article>
    <article class="priv reveal"><h3>Digital Club</h3><p>Membership card, bookings, event registration, guest entry and payments in one app.</p></article>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Our Cities</p><h2>Seven Cities. Nineteen Places.</h2></div>
  <div class="city-grid">{city_cards()}</div>
</div></section>

<section class="cta-band"><div class="wrap reveal">
  <h2>Join Meenaa's Millionaire Club</h2>
  <p>Membership is now open. Speak to our Secretary or President to find the right category for you.</p>
  <div class="cta"><a class="btn" href="{{R}}contact/#enquire">Enquire Now</a><a class="btn btn-ghost" href="tel:+{PHONE_INTL}">Call {PHONE}</a></div>
</div></section>
"""
page("", f"{NAME} — Connect · Grow · Build Wealth",
     "Meenaa's Millionaire Club — a global-class members' club across 7 cities and 19 places in India. Membership now open.", "", home)

# ---------------- ABOUT ----------------
about = page_hero("About the Club", "More Than a Club — <em>A Complete Lifestyle Destination</em>",
                  "A premium integrated membership club where people connect, families enjoy, businesses grow and communities come together.") + f"""
<section class="sec"><div class="wrap split">
  <div class="reveal"><p class="kicker">Who We Are</p><h2>A Premium Integrated Club</h2>
    <p>Meenaa's Millionaire Club brings Business Networking, Sports, Fitness, Wellness, Family Recreation, Entertainment, Dining and Hospitality onto a single platform.</p>
    <p>Our aim is to give members an outstanding lifestyle experience while creating the right setting for entrepreneurs, professionals, investors, families and community members to meet and interact.</p>
  </div>
  <div class="reveal vm">
    <div class="vm-card"><h3>Vision</h3><p>“To build a premium destination where people connect, families enjoy, businesses grow and communities come together.”</p></div>
    <div class="vm-card"><h3>Mission</h3><ul class="ticks"><li>Premium lifestyle facilities</li><li>Healthy living</li><li>Sports development</li><li>Family recreation</li><li>Business and professional networking</li><li>Cultural engagement</li><li>Quality hospitality</li><li>Community interaction</li></ul></div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Our Objectives</p><h2>What We Are Building</h2></div>
  <ol class="obj reveal">
    <li>Establish a premium membership club across India's leading cities.</li>
    <li>Provide a professional platform for business networking.</li>
    <li>Promote sports and fitness.</li>
    <li>Offer family recreation facilities.</li>
    <li>Develop wellness programmes.</li>
    <li>Host cultural and entertainment programmes.</li>
    <li>Grow corporate memberships and partnerships.</li>
    <li>Build a digital membership ecosystem.</li>
  </ol>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Core Values</p><h2>Trust · Excellence · Respect</h2></div>
  <div class="val-row reveal">{"".join(f'<span>{v}</span>' for v in ["Trust","Excellence","Respect","Wellness","Family","Networking","Experience"])}</div>
</div></section>

<section class="sec alt"><div class="wrap split">
  <div class="reveal"><p class="kicker">Business Networking</p><h2>The Business Forum</h2>
    <p>A forum for entrepreneurs, investors, CEOs, corporate executives, professionals, startups, consultants, technology leaders, manufacturers and service providers.</p>
    <ul class="ticks"><li>Business Breakfast</li><li>CEO Networking</li><li>Investor Meet</li><li>Startup Showcase</li><li>Professional Knowledge Series</li><li>Corporate Networking Evening</li></ul>
  </div>
  <div class="reveal"><p class="kicker">Service Standard</p><h2>Welcome · Respect · Respond · Resolve · Improve</h2>
    <p>Professional reception, quick response, complaint resolution, digital support and a feedback system for every member.</p>
    <p>Safety comes first: 24×7 security, CCTV, access control, fire safety, first-aid and emergency response, lifeguards and periodic equipment inspection.</p>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Roadmap</p><h2>From First Stop to a National Network</h2></div>
  <div class="road reveal">
    <div><b>Year 1</b><p>Launch &amp; founding members · infrastructure and brand building</p></div>
    <div><b>Year 2</b><p>Events, business networking, sports and family programmes</p></div>
    <div><b>Year 3</b><p>Premium positioning, VIP programmes, corporate partnerships</p></div>
    <div><b>Year 4</b><p>Inter-city network and member benefits</p></div>
    <div><b>Year 5</b><p>Additional locations and strategic partnerships</p></div>
  </div>
</div></section>
"""
page("about", f"About — {NAME}", "Vision, mission, objectives and values of Meenaa's Millionaire Club.", "about", about)

# ---------------- MEMBERSHIP ----------------
filters = "".join(f'<button class="chip{" on" if k == "all" else ""}" data-f="{k}">{l}</button>' for k, l in TIER_FILTERS)
rows = "".join(tier_row(t) for t in TIERS)
membership = page_hero("Membership", "Membership Categories &amp; <em>Contribution Structure</em>",
                       "Twenty-one categories designed for individuals, institutions, professionals, corporates and NRIs.") + f"""
<section class="sec"><div class="wrap">
  <div class="chips" role="group" aria-label="Filter membership categories">{filters}</div>
  <div class="tbl-wrap reveal">
    <table class="fees" id="fees">
      <thead><tr><th>Sl</th><th>Type of Membership</th><th>Amount</th><th>Remarks</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <p class="note"><b>LTTM</b> = Life Time Temporary Membership. Amounts are contributions in Indian Rupees; eligibility, tenure, voting rights and branch access are as per Club Rules and Governing Body approval. Contact the Secretary to confirm current terms.</p>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Premium Multi-Branch</p><h2>Choose Your Circuit</h2>
  <p>Premium members can hold access to all 19 places, or a regional circuit of branches.</p></div>
  <div class="circuits">
    <article class="circ reveal"><span class="hl-k">₹5 Crore</span><h3>All-India</h3><b>19 branches</b><p>Every Meenaa's branch across India.</p></article>
    <article class="circ reveal"><span class="hl-k">₹3 Crore</span><h3>South</h3><b>7 branches</b><p>Bengaluru · Hyderabad · Chennai</p></article>
    <article class="circ reveal"><span class="hl-k">₹3 Crore</span><h3>West</h3><b>6 branches</b><p>Mumbai · Ahmedabad</p></article>
    <article class="circ reveal"><span class="hl-k">₹3 Crore</span><h3>North &amp; East</h3><b>6 branches</b><p>Delhi · Kolkata</p></article>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Signature Tiers</p><h2>The Meenaa's Collection</h2>
  <p>Recognition names for every level of membership. Fee structures for each signature tier are shared on request.</p></div>
  <div class="sig-grid reveal">{"".join(f'<div class="sig"><b>{n}</b><span>{d}</span></div>' for n, d in SIGNATURE)}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Founding Members</p><h2>Founding Meenaa's Members</h2></div>
  <ul class="ticks cols reveal"><li>Founding member recognition</li><li>Special membership card</li><li>Invitations to exclusive events</li><li>Member networking privileges</li><li>Launch-year benefits</li></ul>
</div></section>

<section class="cta-band"><div class="wrap reveal">
  <h2>Find the right membership</h2><p>Talk to the Secretary about eligibility, tenure and branch access.</p>
  <div class="cta"><a class="btn" href="{{R}}contact/#enquire">Enquire Now</a></div>
</div></section>
"""
page("membership", f"Membership & Fees — {NAME}", "Membership categories and contribution structure for Meenaa's Millionaire Club — lifetime, resident, premium, corporate, NRI and more.", "membership", membership)

# ---------------- BRANCHES ----------------
blocks = ""
for n, st, slug, role, br in CITIES:
    blocks += (f'<article class="branch reveal" id="{slug}"><img src="{{R}}assets/img/city-{slug}.jpg" alt="{n}" loading="lazy">'
               f'<div><h3>{n} <small>{st}</small></h3><p class="role">{role}</p>'
               f'<p>Part of the Club\'s {"South India" if br == 7 else ("West India" if slug in ("mumbai","ahmedabad") else "North & East India")} circuit.</p></div></article>')
branches = page_hero("Branches", "Seven Cities. <em>Nineteen Places.</em>",
                     "Bengaluru leads the way as the first stop, with the network spreading across India.") + f"""
<section class="sec"><div class="wrap split">
  <figure class="reveal map-fig"><img src="{{R}}assets/img/india-map.jpg" alt="Map of India with Club cities" loading="lazy"></figure>
  <div class="reveal"><p class="kicker">First Stop</p><h2>Bengaluru — <em>Inauguration City</em></h2>
    <p>The Club begins at Bengaluru, Karnataka. From here, the network extends to Chennai, Hyderabad, Mumbai, Ahmedabad, Delhi and Kolkata.</p>
    <table class="mini"><thead><tr><th>Circuit</th><th>Cities</th><th>Branches</th></tr></thead><tbody>
      <tr><td>South</td><td>Bengaluru, Hyderabad, Chennai</td><td>7</td></tr>
      <tr><td>West</td><td>Mumbai, Ahmedabad</td><td>6</td></tr>
      <tr><td>North &amp; East</td><td>Delhi, Kolkata</td><td>6</td></tr>
      <tr class="tot"><td colspan="2">All-India</td><td>19</td></tr></tbody></table>
  </div>
</div></section>
<section class="sec alt"><div class="wrap"><div class="branch-list">{blocks}</div></div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Connected Network</p><h2>Move Between Cities with Ease</h2></div>
  <div class="priv-grid">
    <article class="priv reveal"><h3>Helipad &amp; Air Taxi</h3><p>Planned helipad and air-taxi facilities linking club cities, with inter-club limits set by membership tier.</p></article>
    <article class="priv reveal"><h3>Guest Suites</h3><p>Premium rooms and suites at branches for members and their guests.</p></article>
    <article class="priv reveal"><h3>Travel Assistance</h3><p>Concierge support for travel and stays across the network.</p></article>
    <article class="priv reveal"><h3>International Partners</h3><p>Future club partnerships, business exchange and member travel benefits.</p></article>
  </div>
</div></section>
"""
page("branches", f"Branches — {NAME}", "Meenaa's Millionaire Club branches across Bengaluru, Chennai, Hyderabad, Mumbai, Ahmedabad, Delhi and Kolkata.", "branches", branches)

# ---------------- FACILITIES ----------------
fac = "".join(
    f'<article class="fac reveal"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></article>' for t, items in FACILITIES)
ev = "".join(f'<div class="ev"><b>{m}</b><span>{n}</span></div>' for m, n in EVENTS)
facilities = page_hero("Facilities & Experiences", "Everything Under <em>One Roof</em>",
                       "Over 100 planned facilities across seven pillars — designed for members and their families.") + f"""
<section class="sec"><div class="wrap">
  <div class="star-grid">{stars_grid()}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Planned Facilities</p><h2>Club Facilities at a Glance</h2>
  <p>Facility mix varies by branch and is finalised per location.</p></div>
  <div class="fac-grid">{fac}</div>
</div></section>
<section class="sec"><div class="wrap split">
  <div class="reveal"><p class="kicker">Dining &amp; Hospitality</p><h2>Restaurant, Café &amp; Banquet</h2>
    <ul class="ticks"><li>Multi-cuisine, vegetarian and non-vegetarian menus</li><li>Healthy food menu and family dining</li><li>Café for coffee, snacks and business meetings</li><li>Banquet for weddings, corporate events, birthdays and conferences</li></ul></div>
  <div class="reveal"><p class="kicker">Digital Club</p><h2>The Meenaa's Club App</h2>
    <ul class="ticks"><li>Digital membership card</li><li>Facility, sports and restaurant booking</li><li>Event registration and guest entry</li><li>Payments, notifications and member directory</li></ul></div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Year-round</p><h2>Club Events Calendar</h2></div>
  <div class="ev-grid reveal">{ev}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="kicker">Programmes</p><h2>Sports · Family · Wellness · Culture</h2></div>
  <div class="prog-grid">
    <article class="fac reveal"><h3>Sports</h3><p>Daily gym, swimming, badminton and yoga; monthly tournaments and fitness challenges; the annual Meenaa's Sports Championship — cricket, badminton, tennis, table tennis, chess, snooker and billiards.</p></article>
    <article class="fac reveal"><h3>Family</h3><p>Family Day, kids' activities, art and music programmes; annual Family Carnival, Children's Talent Festival, Summer Camp and Family Sports Championship.</p></article>
    <article class="fac reveal"><h3>Wellness</h3><p>Yoga, meditation, fitness classes, workshops, nutrition awareness, senior wellness programmes and fitness assessment.</p></article>
    <article class="fac reveal"><h3>Entertainment</h3><p>Music night, movie night, karaoke, cultural evenings and members' nights; annual Cultural Festival, Talent Awards and Members' Celebration.</p></article>
  </div>
</div></section>
"""
page("facilities", f"Facilities & Experiences — {NAME}", "Business lounges, sports, wellness, family, entertainment and hospitality facilities at Meenaa's Millionaire Club.", "facilities", facilities)

# ---------------- CONTACT ----------------
opts = "".join(f"<option>{e(t[1])}</option>" for t in TIERS)
contact = page_hero("Contact", "Let's <em>Connect</em>", "Membership is now open. Reach the Secretary or the President directly.") + f"""
<section class="sec"><div class="wrap split">
  <div class="reveal">
    <div class="ccard"><span>Contact Secretary</span><a href="mailto:{EMAIL_SEC}">{EMAIL_SEC}</a></div>
    <div class="ccard"><span>Contact President</span><a href="mailto:{EMAIL_PRES}">{EMAIL_PRES}</a></div>
    <div class="ccard"><span>Mobile</span><a href="tel:+{PHONE_INTL}">{PHONE}</a></div>
    <a class="btn wa" href="https://wa.me/{PHONE_INTL}" rel="noopener" target="_blank">Chat on WhatsApp</a>
    <p class="muted small">First stop: Bengaluru, Karnataka — inauguration ceremony. Branch addresses will be shared as each location opens.</p>
  </div>
  <form class="form reveal" id="enquire" novalidate>
    <h2>Membership Enquiry</h2>
    <label>Full name<input name="name" required autocomplete="name"></label>
    <label>Email<input name="email" type="email" required autocomplete="email"></label>
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>City<select name="city">{"".join(f"<option>{c[0]}</option>" for c in CITIES)}<option>Other</option></select></label>
    <label>Membership of interest<select name="tier"><option>Not sure yet</option>{opts}</select></label>
    <label>Message<textarea name="msg" rows="4"></textarea></label>
    <button class="btn" type="submit">Send Enquiry</button>
    <p class="muted small">This opens your email app addressed to the Club Secretary. Nothing is stored on this website.</p>
  </form>
</div></section>
"""
page("contact", f"Contact — {NAME}", "Contact the Secretary or President of Meenaa's Millionaire Club for membership enquiries.", "contact", contact)

# 404
with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
    f.write(head("Page not found — " + NAME, "Page not found", "/") .replace('href="/assets', 'href="/assets')
            + header("/", "") + '<section class="page-hero"><div class="wrap"><p class="kicker">404</p><h1>Page not found</h1><p class="lead">The page you were looking for does not exist.</p><p><a class="btn" href="/">Back to home</a></p></div></section>' + footer("/"))
print("built")
