# -*- coding: utf-8 -*-
import argparse
import utils
import regClean as rc
import Lights

"""Main module."""
def main():
    ###############################################################################
    ###############################################################################

    #------------- Accepting command line arguments here--------------------

    parser = argparse.ArgumentParser() # parser to parse the command line aruments

    # Adding the list of accepted arguments to the parser

    parser.add_argument(
        "--input", "-i", help="Parameter required to provide input to the program", action="store_true") # Store true --> set it true only when this argument is provided
    
    parser.add_argument("filename", help="Complete path for the file") # Filepath

    args = parser.parse_args() # Parse the arguments

    # Get the file path provided

    filePath = args.filename

    # ------------- Arguments Parsing completed---------------------

    ###############################################################################
    ###############################################################################

    # ------------- Reading the File and performing functions--------------------

    # Read the file only if input argument is provided
    if args.input:
        L,ins = utils.parseFile(filePath)

        ## Creating the lights grid
        _lights = Lights.Lights(L)

        ## Getting the methods to be performed to test on the light grid
        for i in ins:
            method, l1, l2, l3, l4 = rc.regexClean(i)

            ## Get the instructios within the bounds of the Grid
            if l1 < 0:
                l1 = 0
            if l3 < 0:
                l3 = 0
            if l2 > L:
                l2 = L-1
            if l4 > L:
                l4 = L-1
        
        return 0

if __name__ == "__main__":
    main()

