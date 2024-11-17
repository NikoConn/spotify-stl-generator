import requests

# Función para obtener el enlace del SVG del código de Spotify
def get_spotify_url(url):
    separation = url.split("/")
    spotify_types = ["track", "playlist", "album", "artist"]
    type_ = ""
    position = -1
    
    for i, aux in enumerate(separation):
        if aux in spotify_types:
            type_ = aux
            position = i
            break

    if type_ == "" or position == -1:
        return None

    code = separation[position + 1].split("?")[0]
    svg_link = f"https://www.spotifycodes.com/downloadCode.php?uri=svg/000000/white/640/spotify:{type_}:{code}"

    return svg_link

# Función para descargar el SVG de Spotify
def download_spotify_svg(url):
    svg_link = get_spotify_url(url)
    if not svg_link:
        return None

    response = requests.get(svg_link)
    if response.status_code == 200:
        return response.content
    else:
        return None