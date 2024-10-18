import logging
import demucs.separate


demucs_models = ["htdemucs",
                 "htdemucs_ft",
                 "htdemucs_6s",
                 "hdemucs_mmi",
                 "mdx",
                 "mdx_extra",
                 "mdx_q",
                 "SIG"]

class SourceSeparator:

    """Initializer for Source Seperation.

    Args:
        model (str): name of demucs model, defaults to "htdemucs_6s"

    """
    def __init__(self, model = None):
        if model == None:
            model = "htdemucs_6s"
        self.set_model(model)
        pass


    """Sets the Demucs model to a new model
    
    Args:
        model (str): name of demucs model
        
    """
    def set_model(self, model):
        if model in demucs_models:
            self.model = model
        else:
            raise ValueError("The model chosen does not exist")
        pass


    """Separates an mp3 file into different tracks defined by its model
    
    Args:
        source_path (str): path of source audio file, absolute or relative
        
    """
    def separate(self, source_file):
        try:
            demucs.separate.main(["--mp3", "-n", self.model, source_file])
            logging.info("Completed Seperation")
        except:
            logging.debug("Failure to use local mp3")
        pass