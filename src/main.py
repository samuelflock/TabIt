import demucs.separate
import demucs
import demucs.utils

#demucs.separate.main(["--mp3", "-n", "mdx_extra", "./music/FileName.mp3"])
demucs.separate.main(["--mp3", "-n", "htdemucs_6s", "./music/FileName.mp3"])

# separator = demucs.Separator()

# origin, separated = separator.separate_audio_file("~/Downloads/FileName.mp3")

# for file, sources in separated:
#     for stem, source in sources.items():
#         demucs.api.save_audio(source, f"{stem}_{file}", samplerate=separator.samplerate)