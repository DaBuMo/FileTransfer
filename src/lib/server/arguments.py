"""
python start - server -h
usage : start - server [ - h ] [ - v | -q ] [ - H ADDR ] [ - p PORT ] [ - s DIRPATH ] [ - r protocol ]
< command description >
optional arguments :
-h , -- help show this help message and exit
-v , -- verbose increase output verbosity
-q , -- quiet decrease output verbosity
-H , -- host service IP address
-p , -- port service port
-s , -- storage storage dir path
-r , -- protocol error recovery protocol
"""

from argparse import ArgumentParser

from lib.constants import LOCALHOST, DEFAULT_PORT

parser = ArgumentParser(
    description="Start a server to receive files using a specified protocol."
)
parser.add_argument(
    "-v", "--verbose", action="store_true", help="increase output verbosity"
)
parser.add_argument(
    "-q", "--quiet", action="store_true", help="decrease output verbosity"
)
parser.add_argument(
    "-H", "--host", type=str, default=LOCALHOST, help="service IP address"
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=DEFAULT_PORT,
    help="service port",
)
parser.add_argument("-s, --storage", type=str, help="storage dir path")
parser.add_argument("-r, --protocol", type=str, help="error recovery protocol")
