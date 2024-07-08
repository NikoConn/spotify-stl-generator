import argparse

from utils import codes, scene

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera llavero de spotify multicolor dada una url")

    # Añadir argumentos posicionales
    parser.add_argument("spotify_url", type=str, help="La URL de Spotify.")
    parser.add_argument("output_path", type=str, help="La ruta de salida para el archivo .zip")

    args = parser.parse_args()

    spotify_url = args.spotify_url
    output_path = args.output_path

    svg_content = codes.download_spotify_svg(spotify_url)
    scene.generate_stl(svg_content, output_path)