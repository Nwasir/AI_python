#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search("^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])


# chmod +x rearrange_test.py 
