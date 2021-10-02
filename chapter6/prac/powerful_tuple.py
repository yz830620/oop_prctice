song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("Beautiiiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
    ("November Rain", "Guns N' Roses")
]

if __name__ == "__main__":
    artists = set()

    for song, artist in song_library:
        artists.add(artist)

    print(artists)
    print("Opeth" in artists)
    artist_list = list(artists)
    artist_list.sort()
    print(artist_list)

    my_artists = {'Vixy and Tony', "Guns N' Roses", 'Sarah Brightman', 'Opeth'}
    auburns_artist = {"Guns N' Roses", 'Nickelback', 'Savage Garden'}
    print('union: ', my_artists.union(auburns_artist))
    print("intersection: ", my_artists.intersection(auburns_artist))
    print("symmetric difference: ", my_artists.symmetric_difference(auburns_artist))

    bands = {"Guns N' Roses", 'Opeth'}
    print('my_artists is to bands')
    print("issuperset: ", my_artists.issuperset(bands))
    print("issubset: ", my_artists.issubset(bands))
    print('difference: ', my_artists.difference(bands))
    print('*'*20)
    print('bands is to my_artists')
    print("issuperset: ", bands.issuperset(my_artists))
    print("issubset: ", bands.issubset(my_artists))
    print('difference: ', bands.difference(my_artists))

    # set only check if hash match, nomatter how big the set is, only need one computation
    # compare with list, you have to compare it one by one, which cost time


