import logging
import demucs.separate

class SourceSeperation:
    def __init__(self, model, source_file):
        self.model = model
        self.source_file = source_file
        self.seperate()

    def seperate(self):
        try:
            #demucs.separate.main(["--mp3", "-n", "mdx_extra", "./music/FileName.mp3"])
            #demucs.separate.main(["--mp3", "-n", "htdemucs_6s", "./music/FileName.mp3"])
            demucs.separate.main(["--mp3", "-n", self.model, "./music/" + self.source_file])
            logging.info("Completed Seperation")
        except:
            logging.debug("Failure to use local mp3")