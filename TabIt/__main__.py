import sys, argparse, logging
from App import *

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    logging.info("Beginning Seperation")
    logging.debug("Chosen Source: %s" % args.source)
    logging.debug("Chosen Model: %s" % args.model)

    app = App(args.source, args.model)
    print(app.get_source())
    
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
  