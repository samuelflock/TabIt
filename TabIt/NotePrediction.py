import os
from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH

class NotePrediction:
    def __init__(self, demucs_model, source_title):
        self.model = demucs_model
        self.source_title = source_title
        self.predict()

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