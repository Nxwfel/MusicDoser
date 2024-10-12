# MusicDoser

MusicDoser is a web-based platform that delivers personalized music recommendations and playlists. The platform is powered by a Flask-based API, offering a range of features for users to explore music based on their preferences, moods, and genres.

## Features

- **Personalized Music Recommendations**: Tailored suggestions based on user preferences.
- **Playlists**: Automatically generated playlists.
- **Music Search**: Search for songs, artists, or albums.
- **Mood-Based Playlists**: Curated playlists to match your current mood.
- **API Access**: Expose endpoints to integrate music features into other applications.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3 
- **Deployment**: Gunicorn, Render, or any preferred cloud platform.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/musicdoser.git
   cd musicdoser
    ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt  

4. Run the Flask application:
   ```bash
   flask run
   ```