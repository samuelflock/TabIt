from pytubefix import YouTube
from pytubefix.cli import on_progress
import logging

class AudioDownloader:
    """Initializer for the Audio Downloader"""
    def __init__(self, source = None):
        self.source = source
        self.source_title = None
        self.source_file = None


    """Updates the Source"""
    def set_source(self, source):
        self.source = source


    """Youtube Downlaod using PyTubeFix
        Downloads in the format of mp3 and save it to local machine

    Args:
        save_path (str): absolute/relative path to save mp3 file
    
    Returns:
        mp3 absolute path

    """
    def download_from_yt(self, save_path):
        if(self.source.startswith("https:") or self.source.startswith("http:")):
            try:
                logging.info("Hyperlink Detected")

                yt = YouTube(self.source, on_progress_callback=on_progress)

                audio_steam = yt.streams.get_audio_only()
                audio_steam.download(mp3=True, output_path=save_path)

                logging.info("YouTube Audio Downloaded")

                return yt.title
            except Exception as e:
                logging.debug("Failure to download from YouTube: " + e)
        else:
            logging.info("Only Hyperlink is supported")
            raise ValueError("Only Hyperlinks are supported right now")
    


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