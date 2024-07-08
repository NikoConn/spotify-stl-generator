# Spotify Code Generator README

## Description

This program generates STL objects that can be used to 3D print Spotify codes in multiple colors. Using Docker to manage dependencies, the program allows you to easily generate codes from a Spotify URL.

## Requirements

- Docker

## Installation

To install the program, ensure you have Docker installed and running on your system. Then, clone the repository and build the Docker image using the following command:

```sh
docker build -t spotify-code-generator .
```

## Usage

Once the Docker image is built, you can generate an STL file with the Spotify code using the `spotify-code-generator.sh` script. The script takes two arguments:

1. The Spotify track URL.
2. The name of the ZIP file that will contain the generated STL files.

Example usage:

```sh
./spotify-code-generator.sh <url-spotify> <output-zip>
```

This command will generate a file `<output-zip>` containing the STL files corresponding to the provided Spotify code.