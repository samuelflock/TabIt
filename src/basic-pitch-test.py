from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH

file_name = "Song"
predict_and_save(["separated/htdemucs_6s/" + file_name + ".mp3"],
                     "./output/",
                     save_midi=True,
                     sonify_midi=False,
                     save_model_outputs=False,
                     save_notes=False,
                     model_or_model_path=Model(ICASSP_2022_MODEL_PATH))