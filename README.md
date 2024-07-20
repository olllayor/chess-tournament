
# Chess Tournament Management System

Welcome to the Chess Tournament Management System! This project is designed to manage chess tournaments, including player registration, tournament management, match scheduling, and leaderboard generation.

## Features

- **User Authentication:** Secure user registration and login.
- **Player Management:** Add and manage players with their ratings.
- **Tournament Management:** Create tournaments with unique names and assign players to them.
- **Match Management:** Automatically generate pairings for each round based on the Swiss-system tournament rules and update match results.
- **Leaderboard:** Generate and display leaderboards showing player ranks, points, and other statistics.
- **API Documentation:** Comprehensive API documentation using Swagger.

### Prerequisites

- Python 3.6+
- Django 3.2+
- Virtual Environment (optional but recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/olllayor/chess-tournament.git
   cd chess-tournament

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt

4. **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser

6. **Run the development server:**
    ```bash
    python manage.py runserver

7. **Access the application:**
    Open your browser and go to http://127.0.0.1:8000/admin to access the admin interface.

## API Endpoints
The project uses Django Rest Framework to provide API endpoints for managing players, tournaments, and matches. The API documentation is available at http://127.0.0.1:8000/swagger/.


### Testing
    ```bash
    python manage.py test


# Contact
Message Olloyor on [gmail@ollayor.uz](mailto:gmail@ollayor.uz), [Telegram](https://t.me/olllayor)