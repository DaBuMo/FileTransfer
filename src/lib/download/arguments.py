from argparse import ArgumentParser

'''
python download -h
usage : download [ - h ] [ - v | -q ] [ - H ADDR ] [ - p PORT ] [ - d FILEPATH ] [ - n FILENAME ] [ - r protocol ]
< command description >
optional arguments :
-h , -- help show this help message and exit
-v , -- verbose increase output verbosity
-q , -- quiet decrease output verbosity
-H , -- host server IP address
-p , -- port server port
-d , -- dst destination file path
-n , -- name file name
-r , -- protocol error recovery protocol
'''

parser = ArgumentParser(
    description="Start a Download Client to receive files using a specified protocol."
)