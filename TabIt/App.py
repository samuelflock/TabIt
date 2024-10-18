from AudioDownloader import *
from SourceSeparator import *
from NotePredictor import *

save_folder = "./music/"
output_folder = "./output/"

class App:
    """Initializer for the Application"""
    def __init__(self):
        self.audioDL = AudioDownloader()
        self.sourceSep = SourceSeparator()
        self.notePred = NotePredictor()
    
    def download_audio(self, source):
        self.audioDL.set_source(source)
        return self.audioDL.download_from_yt(save_folder)

    def separate_source(self, source_file):
        self.sourceSep.separate(source_file)
        pass

    def predict_instrument(self, title):
        source_file = ["./separated/" + self.sourceSep.model + "/" + title + "/guitar.mp3"] # TODO: Fix Instrument (Currently only works with one demucs model)
        self.notePred.predict_full_midi(source_file, output_folder, title)
        pass

    def run(self, source = None, model = None):
        try:
            title = self.download_audio(source)

            file_to_be_separated = save_folder + title + ".mp3"
            self.separate_source(file_to_be_separated)

            self.predict_instrument(title)
        except Exception as e:
            logging.debug("There was an error: " + e)