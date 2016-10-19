from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def wrap(value, wrapper = '"'):
  return wrapper + value + wrapper

class FilterModule(object):
  def filters(self):
    return {
      'wrap': wrap
    }
