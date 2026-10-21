# Egyptian Baccalaureate 2027 Study Hub

A complete self-contained educational platform for Egyptian Baccalaureate 2027 students. It includes a full curriculum structure for the main study streams, detailed explanations, exam preparation tools, monthly and comprehensive quizzes, local/offline access, and a simple dashboard.

## Features
- Full curriculum map for science, literary, and commercial streams
- Detailed subject explanations and learning objectives
- Interactive monthly and comprehensive tests
- Content references aligned with widely used study materials and exam prep sources
- Offline-first browser access with local caching
- Lightweight local PHP API and static front-end design

## Project structure
- `index.html` — app shell and main interface
- `assets/styles.css` — responsive styling
- `assets/app.js` — data loading, filtering, quiz logic, and dashboard logic
- `api/materials.php` — local JSON API for curriculum and tests
- `data/egyptian_bacc_2027.json` — generated curriculum dataset
- `python/build_data.py` — script that generates the dataset
- `service-worker.js` — offline cache support

## Run locally
1. Generate the dataset:
   ```bash
   python3 python/build_data.py
   ```
2. Start a PHP server from the project root:
   ```bash
   php -S localhost:8000
   ```
3. Open the app in your browser:
   ```text
   http://localhost:8000
   ```

## Notes
This version is designed to work as a self-contained local study platform with content available even without network access after the first load.
