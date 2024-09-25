# Flask-API

## Introduktion
Dette projekt er et RESTful API til at administrere studerende. API'et tillader oprettelse, læsning, opdatering og 
sletning af studerende og integration med GitHub for at hente repositories.


## Installation
1. Klon repositoryet:
   ```bash
   git clone https://github.com/LucasFJ-2023/Flask-API.git
  
2. Naviger til projektmappen:
   ```bash
   cd "Flask-api aflevering"

4. Installer nødvendige biblioteker:
   ```bash
   - pip install Flask Flask-CORS requests


## Det gør følgende
- GET/students --> Henter en lister over alle studerende
- POST/students --> Opretter en ny studerene (Send JSON-data)
- PUT/students/<id> --> Ændrer en studerendes GitHub-username
- DELETE/students/<id> --> Slet en studerende via id
- GET/students/repos --> Henter den studerendes GitHub-repositories
