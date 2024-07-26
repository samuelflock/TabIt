



# import modules used here -- sys is a very standard one
import sys, argparse, logging
import demucs.separate
import pytube

# Gather our code in a main() function
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    logging.info("Beginning Seperation")
    logging.debug("Chosen Source: %s" % args.source)
    logging.debug("Chosen Model: %s" % args.model)
  
    #demucs.separate.main(["--mp3", "-n", "mdx_extra", "./music/FileName.mp3"])
    #demucs.separate.main(["--mp3", "-n", "htdemucs_6s", "./music/FileName.mp3"])
    demucs.separate.main(["--mp3", "-n", args.model, args.source])

    logging.info("Completed Seperation")

    # separator = demucs.Separator()

    # origin, separated = separator.separate_audio_file("~/Downloads/FileName.mp3")

    # for file, sources in separated:
    #     for stem, source in sources.items():
    #         demucs.api.save_audio(source, f"{stem}_{file}", samplerate=separator.samplerate)
    
    
 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
                                    prog='TabIt',
                                    description = 'Converts Audio into Guitar Tablature',
                                    epilog = "Epilogue to help (TODO: Update Later)")
    
    # Arguments (Source, Model, Verbose)
    parser.add_argument('source',
                        type=str,
                        help='requires mp3 file path')
    parser.add_argument("-m", "--model",
                        type=str,
                        default='htdemucs_6s',
                        help='list of available models in TODO')
    parser.add_argument(
                      "-v",
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

    except:
        pass
  