# Meenaa's Millionaire Club — website

Static, no-dependency site (HTML/CSS/JS). Clean URLs via folder-per-page, ready for GitHub Pages or any static host.

- Pages: Home · About · Membership (21-category fee table with filters) · Branches · Facilities · Contact
- Enquiry form opens the visitor's email app addressed to the Secretary (nothing is stored)

## Edit content
Content lives in `build.py` (tiers, cities, facilities, contacts). After editing:

```bash
python3 build.py
python3 -m http.server 8080   # http://localhost:8080
```

`index.html` files are generated — edit `build.py`, not the HTML.
