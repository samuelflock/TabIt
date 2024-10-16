from pytubefix import YouTube
from pytubefix.cli import on_progress
import logging

class AudioDownloader:
    """Initializer for the Audio Downloader"""
    def __init__(self, source):
        self.source = source
        self.source_title = None
        self.source_file = None
        try:
            self.download_from_yt()
        except Exception as e:
            logging.debug("An Error occurred while downloading from Youtube: " + e)

    def download_from_yt(self):
        if(self.source.startswith("https:") or self.source.startswith("http:")):
            try:
                logging.info("Hyperlink Detected")

                yt = YouTube(self.source, on_progress_callback=on_progress)

                self.source_title = yt.title
                self.source_name = yt.title + ".mp3"

                audio_steam = yt.streams.get_audio_only()
                audio_steam.download(mp3=True, output_path="./music")

                logging.info("YouTube Audio Downloaded")
            except Exception as e:
                logging.debug("Failure to download from YouTube: " + e)
    


# from pytubefix import YouTube
# from pytubefix.cli import on_progress

#     source_title = args.source
#     source_name = args.source

#     if(args.source.startswith("https:") or args.source.startswith("http:")):
#         try:
#             logging.info("Hyperlink Detected")

#             yt = YouTube(args.source, on_progress_callback=on_progress)

#             source_title = yt.title
#             source_name = yt.title + ".mp3"

#             audio_steam = yt.streams.get_audio_only()
#             audio_steam.download(mp3=True, output_path="./music")

#             logging.info("YouTube Audio Downloaded")
#         except Exception as e:
#             logging.debug("Failure to download from YouTube: " + e)