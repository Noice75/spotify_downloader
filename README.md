# Spotify Downloader

A simple Python application that allows you to download audio tracks from Spotify using their track links. This project utilizes the `requests` library to handle HTTP requests and fetch track information and download links.

## Features

- Fetches audio track information from Spotify.
- Downloads audio tracks in MP3 format.
- Handles various Spotify track URLs.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Noice75/spotify_downloader.git
   cd spotify_downloader
   ```

2. **Install Required Packages**:
   Make sure you have `requests` installed. You can install it using pip:
   ```bash
   pip install requests
   ```

## Usage

1. **Run the Script**:
   You can use the script by providing a Spotify track link. For example:
   ```python
   python main.py
   ```

2. **Track ID Extraction**:
   The script automatically extracts the track ID from the provided Spotify link. It checks if the link is valid and contains a track ID.

3. **Downloading the Track**:
   The track will be downloaded as `{songTitle} {Artist}.mp3` in the current directory.

## Example

```python
Enter track url = https://open.spotify.com/track/7B3z0ySL9Rr0XvZEAjWZzM  # Example URL
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
