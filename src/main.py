import sys, argparse, logging
import os
import demucs.separate
from pytubefix import YouTube
from pytubefix.cli import on_progress
from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    logging.info("Beginning Seperation")
    logging.debug("Chosen Source: %s" % args.source)
    logging.debug("Chosen Model: %s" % args.model)

    source_title = args.source
    source_name = args.source

    if(args.source.startswith("https:") or args.source.startswith("http:")):
        try:
            logging.info("Hyperlink Detected")

            yt = YouTube(args.source, on_progress_callback=on_progress)

            source_title = yt.title
            source_name = yt.title + ".mp3"

            audio_steam = yt.streams.get_audio_only()
            audio_steam.download(mp3=True, output_path="./music")

            logging.info("YouTube Audio Downloaded")
        except Exception as e:
            logging.debug("Failure to download from YouTube: " + e)




    try:
        #demucs.separate.main(["--mp3", "-n", "mdx_extra", "./music/FileName.mp3"])
        #demucs.separate.main(["--mp3", "-n", "htdemucs_6s", "./music/FileName.mp3"])
        demucs.separate.main(["--mp3", "-n", args.model, "./music/" + source_name])
        logging.info("Completed Seperation")
    except:
        logging.debug("Failure to use local mp3")

    prediction_string = ["./separated/" + args.model + "/" + source_title + "/guitar.mp3"]
    predict_and_save(prediction_string,
                     "./output/",
                     save_midi=True,
                     sonify_midi=False,
                     save_model_outputs=False,
                     save_notes=False,
                     model_or_model_path=Model(ICASSP_2022_MODEL_PATH))
    
    os.rename("./output/guitar_basic_pitch.mid", "./output/guitar_" + source_title + ".mid")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='TabIt',
                                     description = 'Converts Audio into Guitar Tablature',
                                     epilog = "Epilogue to help (TODO: Update Later)")
    
    # Arguments (Source, Model, Verbose)
    parser.add_argument('source',
                        type=str,
                        help='requires mp3 file path or full link to YouTube')
    parser.add_argument("-m", "--model",
                        type=str,
                        default='htdemucs_6s',
                        help='list of available models in TODO')
    parser.add_argument("-v",
                        "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    
    # Read User Arguments
    try:
        args = parser.parse_args()

        # Setup logging
        if args.verbose:
            loglevel = logging.DEBUG
        else:
            loglevel = logging.INFO
    
        main(args, loglevel)

    except Exception as e:
        logging.debug("Main Exited with Error: " + e)
        pass
  