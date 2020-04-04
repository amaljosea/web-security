#!/usr/bin/python
import sys
import jwt
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description='JWT',epilog='JWT')
parser.add_argument("--file",help="Provide file input",dest='filename',required=True)
parser.add_argument("--token",help="Provide token",dest='token',required=True)
parser.add_argument("--algorithm",help="Provide algorithm",dest='algorithm',required=True)
args = parser.parse_args() #print(args.accumulate(args.integers))

filename = args.filename
encoded=args.token
algorithm=args.algorithm

with open(filename) as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithms=[algorithm])
            print colored('Success! Token decoded with ....[' + secret.rstrip() + ']','green')
            break
        except jwt.InvalidTokenError:
            print colored('Invalid Token .... [' + secret.rstrip() + ']','red')
        except jwt.ExpiredSignatureError:
            print colored('Token Expired ....[' + secret.rstrip() + ']','red')
