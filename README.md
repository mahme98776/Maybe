# Egyptian Baccalaureate 2027 Study Hub

A fully interactive educational website built for students preparing for the Egyptian Baccalaureate 2027. It uses a structured local API and a detailed curriculum dataset that reflects the released materials currently available for teaching and revision.

## Features
- HTML, CSS, JavaScript, PHP, and Python integration
- Interactive subject filters and topic search
- API-backed curriculum data using PHP
- Study-planning logic for weekly revision schedules
- Educational explanations and subject-specific objectives
- Responsive design for desktop and mobile screens

## Project structure
- `index.html` — main frontend page
- `assets/styles.css` — application styling
- `assets/app.js` — interactivity and fetch logic
- `api/materials.php` — PHP API endpoint returning curriculum data
- `data/egyptian_bacc_2027.json` — main educational dataset
- `python/build_data.py` — Python script to generate or refresh the JSON data

## Run locally
1. Generate the dataset:
   ```bash
   python3 python/build_data.py
   ```
2. Start a PHP server from the project root:
   ```bash
   php -S localhost:8000
   ```
3. Open in your browser:
   ```text
   http://localhost:8000
   ```

## Notes
The application is designed as a detailed educational dashboard and can be extended with official API data or institutional curriculum sources as they are released.





















