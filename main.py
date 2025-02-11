import os
from flask import Flask, redirect,session, url_for, request
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = "258ba1badd9247c9b88999500e883d59"
client_secret = "d45f2362c5bd42718060bd8a58038f32"
redirect_uri = 'http://localhost:5000/callback'
scope= 'playlist-read-private' 
cache_handler = FlaskSessionCacheHandler(session)

sp_oauth = SpotifyOAuth(client_id, 
                        client_secret, redirect_uri, 
                        scope=scope, cache_handler=cache_handler,
                        show_dialog=True)

sp = Spotify(auth_manager=sp_oauth)

@app.route('/')
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_playlist'))


    
@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlist'))

@app.route('/get_playlist')
def get_playlist():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    playlists = sp.current_user_playlists()
    playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
    playlists_html = '<br>'.join([f'{name}:{url}' for name , url in playlists_info])


    return playlists_html

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

    

    

if __name__ == '__main__':
    app.run(debug=True)


