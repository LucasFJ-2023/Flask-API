# Flask-API

## Introduktion
Dette projekt er et RESTful API til at administrere studerende. API'et tillader oprettelse, læsning, opdatering og 
sletning af studerende og integration med GitHub for at hente repositories.


## Installation
1. Klon repositoryet:
   ```bash
  git clone <[<repository-url>](https://github.com/LucasFJ-2023/Flask-API.git)>
  
2. Naviger til projektmappen
   cd "Flask-api aflevering"

3. Installer nødvendige biblioteker:
   - pip install Flask
   - pip install Flask-CORS
   - pip install requests


## Det gør følgende
GET/students --> Henter en lister over alle studerende
POST/students --> Opretter en ny studerene (Send JSON-data)
PUT/students/<id> --> Ændrer en studerendes GitHub-username
DELETE/students/<id> --> Slet en studerende via id
GET/students/repos --> Henter den studerendes GitHub-repositories
