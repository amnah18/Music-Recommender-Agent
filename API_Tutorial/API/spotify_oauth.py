import requests
import json
import urllib.parse
import base64
from datetime import datetime

class SpotifyOAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_url = 'https://accounts.spotify.com/api/token'

    def get_client_credentials(self):
        """Encodes the client ID and client secret."""
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode()).decode()
        return client_creds_b64

    def get_access_token(self, code):
        """Exchanges the authorization code for an access token."""
        auth_header = self.get_client_credentials()
        headers = {
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        response = requests.post(self.token_url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error obtaining access token:", response.status_code, response.text)
            return None

def get_playlists(access_token):
    """Fetches the user's playlists from Spotify."""
    playlists_url = "https://api.spotify.com/v1/me/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(playlists_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching playlists:", response.status_code, response.text)
        return None

def main():
    # Replace with your actual credentials
    client_id = "547e2f8694f14a1b99874756bc48383e"
    client_secret = "84995754a59344858ed714376bd84da0"
    redirect_uri = "http://localhost:8888/callback"  # Must match your registered redirect URI

    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri)

    # Build the authorization URL
    scope = "user-read-private user-read-email playlist-read-private"
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope,
        "show_dialog": "true"
    }
    auth_url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
    
    print("Please follow these steps:")
    print("1. Open the following URL in your browser:")
    print(auth_url)
    print("2. Log in to Spotify and authorize the application.")
    print("3. Once redirected, copy the 'code' parameter from the URL.")
    code = input("Paste the authorization code here: ").strip()
    
    token_info = sp_oauth.get_access_token(code)
    if not token_info:
        print("Failed to obtain access token. Exiting.")
        return

    access_token = token_info['access_token']
    print("Access token obtained successfully.")

    # Fetch playlists
    playlists_data = get_playlists(access_token)
    if playlists_data:
        with open("playlists.json", "w", encoding="utf-8") as f:
            json.dump(playlists_data, f, indent=4)
        print("Playlists data saved to playlists.json")
    else:
        print("Failed to fetch playlists data.")

if __name__ == "__main__":
    main()
