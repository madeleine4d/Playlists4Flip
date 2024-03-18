import os

playlistnames = os.listdir("playlists")

for p in playlistnames:
    contence = os.listdir("playlists\\" + p)
    songnames = []
    for file in contence:
        if file[-4:] == '.mp3':
            songnames.append(file)
        
    with open('m3us\\' + p + '.m3u', 'w', encoding="utf-8") as playlist:
        playlist.write('#EXTM3U\n')
        for song in songnames:
            playlist.write('Playlists/' + p + '/' + song + '\n')
        print('Made \'' + p + '\'')
