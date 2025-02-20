# 🎵 Music Recommender Agent

This project is a personalized music recommendation system built using **Spotify's API** and **machine learning techniques**. The system fetches song, artist, and playlist data, processes it using **collaborative filtering** and **content-based approaches**, and enhances recommendations with an **AI agent**.

---

## 📂 Project Structure

```
Music-Recommender-Agent/
├── .cache                # Cache files for Spotify API
├── Get_playlist.ipynb    # Jupyter notebook for fetching playlists
├── main.py               # Flask API for playlist retrieval and management
├── playlists.json        # JSON file containing playlist data
├── requirements.txt      # Dependencies required to run the project
├── tracks.json           # JSON file containing track details
```

---

## 🚀 Features

- 🎧 Fetches **playlists, tracks, and artist details** from Spotify.
- 🔍 Uses **collaborative filtering** and **content-based filtering** for recommendations.
- 🤖 AI-enhanced recommendation system.
- 🛠️ **Flask API** for handling Spotify playlist retrieval.
- 📊 Jupyter notebook for easy exploration and testing.

---

## 🔧 Installation

1. **Clone the repository**  
    ```sh
    git clone https://github.com/amnah18/Music-Recommender-Agent.git
    cd Music-Recommender-Agent
    ```

2. **Create a virtual environment** (Optional but recommended)
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Spotify API**
    - Create a Spotify Developer Account.
    - Get your Client ID and Client Secret.
    - Add them to your environment variables or a config file.

---

## 🏃 Usage

1. **Run the Flask API:**
    ```sh
    python main.py
    ```
    This will start the backend server for handling requests.

2. **Fetch Playlists from Jupyter Notebook:**
    - Open `Get_playlist.ipynb` in Jupyter Notebook and execute the cells to fetch playlist data.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request. 🚀

---

## 📬 Contact

For any questions or collaborations, reach out via GitHub.