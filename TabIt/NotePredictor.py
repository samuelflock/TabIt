import os
from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH

class NotePredictor:
    def __init__(self, source_title = None):
        self.source_title = source_title

    def predict(self):
        prediction_string = ["./separated/" + self.model + "/" + self.source_title + "/guitar.mp3"]
        predict_and_save(prediction_string,
                        "./output/",
                        save_midi=True,
                        sonify_midi=False,
                        save_model_outputs=False,
                        save_notes=False,
                        model_or_model_path=Model(ICASSP_2022_MODEL_PATH))
        
        os.rename("./output/guitar_basic_pitch.mid", "./output/guitar_" + self.source_title + ".mid")


    """Creates a MIDI file from mp3 file using Basic-Pitch
    
    Args:
        source_file (str): path of source audio file, absolute or relative
        output_folder (str): path to output directory, absolute or relative
        output_name (str): file name for output file, do not include file extension
        
    """
    def predict_full_midi(self, source_file, output_folder, output_name):
        fragmented_file_string = os.path.basename(source_file[0]).replace('/', '.').split('.')
        saved_file = fragmented_file_string[len(fragmented_file_string) - 2] + "_basic_pitch.mid"

        if os.path.exists(output_folder + saved_file):
            os.rename(output_folder + saved_file, output_folder + "temp.mid")

        predict_and_save(source_file,
                        output_folder,
                        save_midi=True,
                        sonify_midi=False,
                        save_model_outputs=False,
                        save_notes=False,
                        model_or_model_path=Model(ICASSP_2022_MODEL_PATH))
        
        # Alters File name to Match the Song rather than the Instrument
        os.rename(output_folder + saved_file, output_folder + "guitar_" + output_name + ".mid")

        if os.path.exists(output_folder + "temp.mid"):
            os.rename(output_folder + "temp.mid", output_folder + saved_file)