from argparse import ArgumentParser
from pprint import pprint

from atlant.api import AuthClient, ConfigClient, APIException


def parse_args():
    parser = ArgumentParser(
        description="Get setting value using F-Secure Atlant's configuration API."
    )
    parser.add_argument("authorization_address", help="Authorization server address.")
    parser.add_argument("management_address", help="Management server address.")
    parser.add_argument("client_id", help="OAuth2 client ID")
    parser.add_argument("client_secret", help="OAuth2 client secret")
    parser.add_argument("setting", nargs="+")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        authenticator = AuthClient(
            args.authorization_address, args.client_id, args.client_secret
        )
        configurator = ConfigClient(args.management_address, authenticator)
        pprint(configurator.get(args.setting))
    except APIException as err:
        print("{}: {}".format(err, err.long_description))
        exit(1)
