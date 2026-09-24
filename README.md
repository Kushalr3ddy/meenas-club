# Meenaa's Millionaire Club — website

Static site — plain HTML, CSS and JS. No build step, no dependencies. Clean URLs via folder-per-page, served by GitHub Pages.

- Pages: Home · About · Membership (21-category fee table with filters) · Branches · Facilities · Contact
- The enquiry form opens the visitor's email app addressed to the Secretary (nothing is stored)

## Run locally

```bash
python3 -m http.server 8080
```

Then open http://localhost:8080

## Edit

Each page is a folder with an `index.html` (`about/`, `membership/`, `branches/`, `facilities/`, `contact/`). The header and footer are repeated in each file, so change them in all pages. Styles: `assets/css/style.css`. Scripts: `assets/js/main.js`.
