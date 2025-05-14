from argparse import ArgumentParser

"""
usage : upload [ - h ] [ - v | -q ] [ - H ADDR ] [ - p PORT ] [ - s FILEPATH ] [ - n FILENAME ] [ - r protocol ]
<command description>
optional arguments :
-h , -- help show this help message and exit
-v , -- verbose increase output verbosity
-q , -- quiet decrease output verbosity
-H , -- host server IP address
-p , -- port server port
-s , -- src source file path
-n , -- name file name
-r , -- protocol error recovery protocol

"""

parser = ArgumentParser(
    description="Upload a file to a server using a specified protocol."
)
parser.add_argument(
    "-v, --verbose", action="store_true", help="increase output verbosity"
)
parser.add_argument(
    "-q, --quiet", action="store_true", help="decrease output verbosity"
)
parser.add_argument("-H, --host", action="store_true", help="server IP address")
parser.add_argument("-p, --port", action="store_true", help="server port")
parser.add_argument("-s, --storage", action="store_true", help="storage dir path")
parser.add_argument("-n, --name", action="store_true", help="file name")
parser.add_argument(
    "-r, --protocol", action="store_true", help="error recovery protocol"
)