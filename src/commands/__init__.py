import platform
from environment import *

from macos_commands import macosCommands
from windows_commands import windowsCommands

print('Platform: %s' % (platform.system()))
PLATFORM = platform.system()

class Commands:
  def __init__(self):
    self.list = []
    # switch case if macos or windows
    if PLATFORM == PLATFORM_MAC:
      self.list = macosCommands()
    else:
      self.list = windowsCommands()