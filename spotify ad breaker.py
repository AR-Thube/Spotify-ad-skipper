import requests
import os
import subprocess
import time


path = "C:\\Users\\Atharva\\AppData\\Roaming\\Spotify\\Spotify.exe"
SPOTIFY_ACCESS_TOKEN = "BQCmrbS0YpaYN1oYD0VbqOO2ItnUOWPbadHghTbYAsFBlsB_Y6doXCgBIBW2TrX58OxfsRjxJN5l-MwnYrzDEhDQRb2AM6_yuinBeqidNYJr-xtqNtpjpg6hjMHVSPDS4DfGQi331VfTgJEjThgxLeFcDR5Z4tlFH62KnYOgqDL8ZwD3gemsZJRZrLiYGXSJopQZg-KuJcVQeEt7CQi5cMwTHKhTJqa3EZkurUUZiNpJxjHhjV-F6YxbLUpZLjAwQZMEEKYLkmoaXpVvQj_WTF40z2io1drIVi8GR3_UxBaL"


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
	response = requests.get(
		SPOTIFY_GET_CURRENT_TRACK_URL,
		headers ={
			"Authorization"  : f'Bearer {access_token}'
		}
		)

	resp_json = response.json()
	play_type = resp_json['currently_playing_type']

	if play_type == 'ad':
		IS_AD = True
	else:
		IS_AD = False


	return IS_AD
	

def close_spotify():
	os.system(f'taskkill /F /IM Spotify.exe')

def reopen_spotify():
	subprocess.Popen(path)


def main():
	IS_AD = current_track = get_current_track(
			SPOTIFY_ACCESS_TOKEN
			)

	if IS_AD:
		print("Found an ad, restarting Spotify")
		close_spotify()
		reopen_spotify()
		time.sleep(0.1)

if __name__ == '__main__':

	while True:

		try:
			main()
		except:
			print("No song is playing currently.") 