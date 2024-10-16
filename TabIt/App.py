from AudioDownloader import *
from SourceSeperation import *
from NotePrediction import *

class App:
    """Initializer for the Application"""
    def __init__(self, audio_source, demucs_model = None):
        self.source = audio_source
        self.ad = AudioDownloader(self.source)
        # Default Model is "htdemucs_6s", unless overwritten
        if demucs_model == None:
            self.model = "htdemucs_6s"
        else:
            self.model = demucs_model

    def get_source_link(self):
        return self.ad.source
    
    def get_demucs_model(self):
        return self.model