from lyricsgenius import Genius

# My token - Rangsiman - from Genius website
token=""

genius = Genius(token)
genius.verbose = False
genius.remove_section_headers = True
# genius.response_format = 'plain'
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
song = genius.search_song("To You", artist.name)
song = artist.song("To You")
print(song.lyrics.replace('\n'," "))
