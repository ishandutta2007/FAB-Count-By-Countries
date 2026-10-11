# Contributing to FAB-Count-By-Countries

Thank you for your interest in contributing to **FAB-Count-By-Countries**! This document provides guidelines and instructions for developers and contributors looking to maintain, update, or improve the dataset and project tooling.

---

## 📂 Project Structure

```
FAB-Count-By-Countries/
├── assets/
│   └── banner.svg         # Animated SVG banner for README
├── data/
│   └── fabs_2026.json     # Year-wise JSON dataset (e.g., fabs_2026.json, fabs_2027.json)
├── scripts/
│   └── update_readme.py   # Python automation script to render latest data into README.md
├── README.md              # Main project page containing rendered statistics & insights
└── CONTRIBUTING.md        # Contribution guidelines for developers
```

---

## 🛠️ How to Update Fab Data for New Years or Edits

The dataset is stored in JSON format inside the `data/` folder, labeled by year (`fabs_YYYY.json`). Follow these steps to submit updates:

### 1. Adding a New Year's Dataset (e.g., 2027)

1. Create a new file in `data/` named `fabs_2027.json` (copy `data/fabs_2026.json` as a base template).
2. Update the entries with verified data from reliable industry sources (e.g., TrendForce, SEMI, ASML quarterly reports, company press releases).
3. Ensure each entry follows the schema below:

```json
[
  {
    "country": "Japan",
    "operating_fabs_count": 96,
    "asml_lithography_status": "DUV Only (EUV incoming)",
    "major_domestic_fabs_specialties": "Sony, Kioxia, Renesas, Rapidus (2nm EUV line)."
  }
]
```

### 2. Updating the README Table

Run the automated Python script from the repository root:

```bash
python scripts/update_readme.py
```

The script automatically detects the latest `fabs_YYYY.json` file, formats the entries into GitHub-flavored Markdown, and updates `README.md`.

---

## 🚀 Development Workflow

1. **Fork the Repository**: Create your own fork on GitHub.
2. **Clone & Branch**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/FAB-Count-By-Countries.git
   cd FAB-Count-By-Countries
   git checkout -b feature/update-2027-data
   ```
3. **Make Changes**: Edit or add JSON data under `data/`, then run `python scripts/update_readme.py`.
4. **Commit & Push**:
   ```bash
   git add data/ scripts/ README.md
   git commit -m "feat: update fab dataset for 2027"
   git push origin feature/update-2027-data
   ```
5. **Open a Pull Request**: Submit a PR to `main` with references/sources for any new or updated fab counts.

---

## 📜 Data Citation & Verification Guidelines

When updating counts or lithography status, please cite reliable sources in your Pull Request description:
- Official company press releases (TSMC, Intel, Samsung, GlobalFoundries, SMIC, etc.)
- Industry organization reports (SEMI, SIA)
- Regulatory filings & news from accredited semiconductor outlets (EE Times, Tom's Hardware, Reuters, Nikkei Asia).

Thank you for keeping this semiconductor dataset accurate and up to date! 🚀
