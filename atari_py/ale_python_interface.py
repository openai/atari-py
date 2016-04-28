# ale_python_interface.py
# Author: Ben Goodrich
# This directly implements a python version of the arcade learning
# environment interface.

from ctypes import *
import numpy as np
from numpy.ctypeslib import as_ctypes
import os
import six

ale_lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__),
                                        'ale_interface/build/libale_c.so'))

ale_lib.ALE_new.argtypes = None
ale_lib.ALE_new.restype = c_void_p
ale_lib.ALE_del.argtypes = [c_void_p]
ale_lib.ALE_del.restype = None
ale_lib.getString.argtypes = [c_void_p, c_char_p]
ale_lib.getString.restype = c_char_p
ale_lib.getInt.argtypes = [c_void_p, c_char_p]
ale_lib.getInt.restype = c_int
ale_lib.getBool.argtypes = [c_void_p, c_char_p]
ale_lib.getBool.restype = c_bool
ale_lib.getFloat.argtypes = [c_void_p, c_char_p]
ale_lib.getFloat.restype = c_float
ale_lib.setString.argtypes = [c_void_p, c_char_p, c_int]
ale_lib.setString.restype = None
ale_lib.setInt.argtypes = [c_void_p, c_char_p, c_int]
ale_lib.setInt.restype = None
ale_lib.setBool.argtypes = [c_void_p, c_char_p, c_bool]
ale_lib.setBool.restype = None
ale_lib.setFloat.argtypes = [c_void_p, c_char_p, c_float]
ale_lib.setFloat.restype = None
ale_lib.loadROM.argtypes = [c_void_p, c_char_p]
ale_lib.loadROM.restype = None
ale_lib.act.argtypes = [c_void_p, c_int]
ale_lib.act.restype = c_int
ale_lib.game_over.argtypes = [c_void_p]
ale_lib.game_over.restype = c_bool
ale_lib.reset_game.argtypes = [c_void_p]
ale_lib.reset_game.restype = None
ale_lib.getLegalActionSet.argtypes = [c_void_p, c_void_p]
ale_lib.getLegalActionSet.restype = None
ale_lib.getLegalActionSize.argtypes = [c_void_p]
ale_lib.getLegalActionSize.restype = c_int
ale_lib.getMinimalActionSet.argtypes = [c_void_p, c_void_p]
ale_lib.getMinimalActionSet.restype = None
ale_lib.getMinimalActionSize.argtypes = [c_void_p]
ale_lib.getMinimalActionSize.restype = c_int
ale_lib.getFrameNumber.argtypes = [c_void_p]
ale_lib.getFrameNumber.restype = c_int
ale_lib.lives.argtypes = [c_void_p]
ale_lib.lives.restype = c_int
ale_lib.getEpisodeFrameNumber.argtypes = [c_void_p]
ale_lib.getEpisodeFrameNumber.restype = c_int
ale_lib.getScreen.argtypes = [c_void_p, c_void_p]
ale_lib.getScreen.restype = None
ale_lib.getRAM.argtypes = [c_void_p, c_void_p]
ale_lib.getRAM.restype = None
ale_lib.getRAMSize.argtypes = [c_void_p]
ale_lib.getRAMSize.restype = c_int
ale_lib.getScreenWidth.argtypes = [c_void_p]
ale_lib.getScreenWidth.restype = c_int
ale_lib.getScreenHeight.argtypes = [c_void_p]
ale_lib.getScreenHeight.restype = c_int
ale_lib.getScreenRGB.argtypes = [c_void_p, c_void_p]
ale_lib.getScreenRGB.restype = None
ale_lib.getScreenGrayscale.argtypes = [c_void_p, c_void_p]
ale_lib.getScreenGrayscale.restype = None
ale_lib.saveState.argtypes = [c_void_p]
ale_lib.saveState.restype = None
ale_lib.loadState.argtypes = [c_void_p]
ale_lib.loadState.restype = None
ale_lib.saveScreenPNG.argtypes = [c_void_p, c_char_p]
ale_lib.saveScreenPNG.restype = None
ale_lib.cloneState.argtypes = [c_void_p]
ale_lib.cloneState.restype = c_void_p
ale_lib.restoreState.argtypes = [c_void_p, c_void_p]
ale_lib.restoreState.restype = None

ale_lib.ALEState_del.argtypes = [c_void_p]
ale_lib.ALEState_del.restype = None
ale_lib.ALEState_getFrameNumber.argtypes = [c_void_p]
ale_lib.ALEState_getFrameNumber.restype = c_int
ale_lib.ALEState_getEpisodeFrameNumber.argtypes = [c_void_p]
ale_lib.ALEState_getEpisodeFrameNumber.restype = c_int
ale_lib.ALEState_equals.argtypes = [c_void_p, c_void_p]
ale_lib.ALEState_equals.restype = c_bool


class ALEState(object):
    def __init__(self, obj, ale):
        self.obj = obj
        self.ale = ale

    def __del__(self):
        ale_lib.ALEState_del(self.obj)

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
                and ale_lib.ALEState_equals(self.obj, other.obj)

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def frame_number(self):
        return ale_lib.ALEState_getFrameNumber(self.obj)

    @property
    def episode_frame_number(self):
        return ale_lib.ALEState_getEpisodeFrameNumber(self.obj)

class ALEInterface(object):
    def __init__(self):
        self.obj = ale_lib.ALE_new()

    def getString(self, key):
        return ale_lib.getString(self.obj, key)
    def getInt(self, key):
        return ale_lib.getInt(self.obj, key)
    def getBool(self, key):
        return ale_lib.getBool(self.obj, key)
    def getFloat(self, key):
        return ale_lib.getFloat(self.obj, key)

    def setString(self, key, value):
      ale_lib.setString(self.obj, key, value)
    def setInt(self, key, value):
      ale_lib.setInt(self.obj, key, value)
    def setBool(self, key, value):
      ale_lib.setBool(self.obj, key, value)
    def setFloat(self, key, value):
      ale_lib.setFloat(self.obj, key, value)

    def loadROM(self, rom_file):
        ale_lib.loadROM(self.obj, six.b(rom_file))

    def act(self, action):
        return ale_lib.act(self.obj, int(action))

    def game_over(self):
        return ale_lib.game_over(self.obj)

    def reset_game(self):
        ale_lib.reset_game(self.obj)

    def getLegalActionSet(self):
        act_size = ale_lib.getLegalActionSize(self.obj)
        act = np.zeros((act_size), dtype=np.intc)
        ale_lib.getLegalActionSet(self.obj, as_ctypes(act))
        return act

    def getMinimalActionSet(self):
        act_size = ale_lib.getMinimalActionSize(self.obj)
        act = np.zeros((act_size), dtype=np.intc)
        ale_lib.getMinimalActionSet(self.obj, as_ctypes(act))
        return act

    def getFrameNumber(self):
        return ale_lib.getFrameNumber(self.obj)

    def lives(self):
        return ale_lib.lives(self.obj)

    def getEpisodeFrameNumber(self):
        return ale_lib.getEpisodeFrameNumber(self.obj)

    def getScreenDims(self):
        """returns a tuple that contains (screen_width, screen_height)
        """
        width = ale_lib.getScreenWidth(self.obj)
        height = ale_lib.getScreenHeight(self.obj)
        return (width, height)


    def getScreen(self, screen_data=None):
        """This function fills screen_data with the RAW Pixel data
        screen_data MUST be a numpy array of uint8/int8. This could be initialized like so:
        screen_data = np.empty(w*h, dtype=np.uint8)
        Notice,  it must be width*height in size also
        If it is None,  then this function will initialize it
        Note: This is the raw pixel values from the atari,  before any RGB palette transformation takes place
        """
        if(screen_data is None):
            width = ale_lib.getScreenWidth(self.obj)
            height = ale_lib.getScreenHeight(self.obj)
            screen_data = np.zeros(width*height, dtype=np.uint8)
        ale_lib.getScreen(self.obj, as_ctypes(screen_data))
        return screen_data

    def getScreenRGB(self, screen_data=None):
        """This function fills screen_data with the data in RGB format
        screen_data MUST be a numpy array of uint8. This can be initialized like so:
        screen_data = np.empty((height,width,3), dtype=np.uint8)
        If it is None,  then this function will initialize it.
        """
        if(screen_data is None):
            width = ale_lib.getScreenWidth(self.obj)
            height = ale_lib.getScreenHeight(self.obj)
            screen_data = np.empty((height, width,3), dtype=np.uint8)
        ale_lib.getScreenRGB(self.obj, as_ctypes(screen_data[:]))
        return screen_data

    def getScreenGrayscale(self, screen_data=None):
        """This function fills screen_data with the data in grayscale
        screen_data MUST be a numpy array of uint8. This can be initialized like so:
        screen_data = np.empty((height,width,1), dtype=np.uint8)
        If it is None,  then this function will initialize it.
        """
        if(screen_data is None):
            width = ale_lib.getScreenWidth(self.obj)
            height = ale_lib.getScreenHeight(self.obj)
            screen_data = np.empty((height, width,1), dtype=np.uint8)
        ale_lib.getScreenGrayscale(self.obj, as_ctypes(screen_data[:]))
        return screen_data

    def getRAMSize(self):
        return ale_lib.getRAMSize(self.obj)

    def getRAM(self, ram=None):
        """This function grabs the atari RAM.
        ram MUST be a numpy array of uint8/int8. This can be initialized like so:
        ram = np.array(ram_size, dtype=uint8)
        Notice: It must be ram_size where ram_size can be retrieved via the getRAMSize function.
        If it is None,  then this function will initialize it.
        """
        if(ram is None):
            ram_size = ale_lib.getRAMSize(self.obj)
            ram = np.zeros(ram_size, dtype=np.uint8)
        ale_lib.getRAM(self.obj, as_ctypes(ram))
        return ram

    def saveScreenPNG(self, filename):
        return ale_lib.saveScreenPNG(self.obj, filename)

    def saveState(self):
        return ale_lib.saveState(self.obj)

    def loadState(self):
        return ale_lib.loadState(self.obj)

    def cloneState(self):
        return ALEState(ale_lib.cloneState(self.obj), self)

    def restoreState(self, state):
        if state.ale is not self:
            raise ValueError('Can only restore state on the ale instance it yielded from')
        return ale_lib.restoreState(self.obj, state.obj)

    def __del__(self):
        ale_lib.ALE_del(self.obj)
