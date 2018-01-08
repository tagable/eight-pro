import os, platform, sys

class myOS:
  "It holds the system info"
  def __init__(self):
    self.name = sys.platform

  def get_os_info(self):
    return self.name;