import argparse

from spotifystl import codes, scene

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a multicolor Spotify keychain given a URL")

    parser.add_argument("spotify_url", type=str, help="The Spotify URL.")
    parser.add_argument("output_path", type=str, help="The output path for the .zip file.")

    args = parser.parse_args()

    spotify_url = args.spotify_url
    output_path = args.output_path

    svg_content = codes.download_spotify_svg(spotify_url)
    scene.generate_stl(svg_content, output_path)