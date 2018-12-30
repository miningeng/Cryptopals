# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:12:52 2018

@author: Nico
"""
import binascii
import base64

def hex2b64(x):
   decoded = binascii.unhexlify(x)
   return base64.b64encode(decoded).decode('ascii')

key = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

result = hex2b64(key)



