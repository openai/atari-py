#ifndef __ALE_C_WRAPPER_H__
#define __ALE_C_WRAPPER_H__

#include <ale_interface.hpp>

#ifdef _WIN32
#  define SYMBOL_EXPORT __declspec(dllexport)
#endif
#ifndef SYMBOL_EXPORT
#  define SYMBOL_EXPORT
#endif

extern "C" {
  // Declares int rgb_palette[256]
  #include "atari_ntsc_rgb_palette.h"
  SYMBOL_EXPORT ALEInterface *ALE_new() {return new ALEInterface();}
  SYMBOL_EXPORT void ALE_del(ALEInterface *ale){delete ale;}
  SYMBOL_EXPORT const char *getString(ALEInterface *ale, const char *key){return ale->getString(key).c_str();}
  SYMBOL_EXPORT int getInt(ALEInterface *ale,const char *key) {return ale->getInt(key);}
  SYMBOL_EXPORT bool getBool(ALEInterface *ale,const char *key){return ale->getBool(key);}
  SYMBOL_EXPORT float getFloat(ALEInterface *ale,const char *key){return ale->getFloat(key);}
  SYMBOL_EXPORT void setString(ALEInterface *ale,const char *key,const char *value){ale->setString(key,value);}
  SYMBOL_EXPORT void setInt(ALEInterface *ale,const char *key,int value){ale->setInt(key,value);}
  SYMBOL_EXPORT void setBool(ALEInterface *ale,const char *key,bool value){ale->setBool(key,value);}
  SYMBOL_EXPORT void setFloat(ALEInterface *ale,const char *key,float value){ale->setFloat(key,value);}
  SYMBOL_EXPORT void loadROM(ALEInterface *ale,const char *rom_file){ale->loadROM(rom_file);}
  SYMBOL_EXPORT int act(ALEInterface *ale,int action){return ale->act((Action)action);}
  SYMBOL_EXPORT bool game_over(ALEInterface *ale){return ale->game_over();}
  SYMBOL_EXPORT void reset_game(ALEInterface *ale){ale->reset_game();}
  SYMBOL_EXPORT void getLegalActionSet(ALEInterface *ale,int *actions){
    ActionVect action_vect = ale->getLegalActionSet();
    for(unsigned int i = 0;i < ale->getLegalActionSet().size();i++){
      actions[i] = action_vect[i];
    }
  }
  SYMBOL_EXPORT int getLegalActionSize(ALEInterface *ale){return ale->getLegalActionSet().size();}
  SYMBOL_EXPORT void getMinimalActionSet(ALEInterface *ale,int *actions){
    ActionVect action_vect = ale->getMinimalActionSet();
    for(unsigned int i = 0;i < ale->getMinimalActionSet().size();i++){
      actions[i] = action_vect[i];
    }
  }
  SYMBOL_EXPORT int getMinimalActionSize(ALEInterface *ale){return ale->getMinimalActionSet().size();}
  SYMBOL_EXPORT int getFrameNumber(ALEInterface *ale){return ale->getFrameNumber();}
  SYMBOL_EXPORT int lives(ALEInterface *ale){return ale->lives();}
  SYMBOL_EXPORT int getEpisodeFrameNumber(ALEInterface *ale){return ale->getEpisodeFrameNumber();}
  SYMBOL_EXPORT void getScreen(ALEInterface *ale,unsigned char *screen_data){
    int w = ale->getScreen().width();
    int h = ale->getScreen().height();
    pixel_t *ale_screen_data = (pixel_t *)ale->getScreen().getArray();
    memcpy(screen_data,ale_screen_data,w*h*sizeof(pixel_t));
  }
  SYMBOL_EXPORT void getRAM(ALEInterface *ale,unsigned char *ram){
    unsigned char *ale_ram = ale->getRAM().array();
    int size = ale->getRAM().size();
    memcpy(ram,ale_ram,size*sizeof(unsigned char));
  }
  SYMBOL_EXPORT int getRAMSize(ALEInterface *ale){return ale->getRAM().size();}
  SYMBOL_EXPORT int getScreenWidth(ALEInterface *ale){return ale->getScreen().width();}
  SYMBOL_EXPORT int getScreenHeight(ALEInterface *ale){return ale->getScreen().height();}

  SYMBOL_EXPORT void getScreenRGB(ALEInterface *ale, int *output_buffer){
    size_t w = ale->getScreen().width();
    size_t h = ale->getScreen().height();
    size_t screen_size = w*h;
    pixel_t *ale_screen_data = ale->getScreen().getArray();

    for(int i = 0;i < w*h;i++){
        output_buffer[i] = rgb_palette[ale_screen_data[i]];
    }

  }

  SYMBOL_EXPORT void getScreenGrayscale(ALEInterface *ale, unsigned char *output_buffer){
    size_t w = ale->getScreen().width();
    size_t h = ale->getScreen().height();
    size_t screen_size = w*h;
    pixel_t *ale_screen_data = ale->getScreen().getArray();

    ale->theOSystem->colourPalette().applyPaletteGrayscale(output_buffer, ale_screen_data, screen_size);
  }

  SYMBOL_EXPORT void saveState(ALEInterface *ale){ale->saveState();}
  SYMBOL_EXPORT void loadState(ALEInterface *ale){ale->loadState();}
  SYMBOL_EXPORT void saveScreenPNG(ALEInterface *ale,const char *filename){ale->saveScreenPNG(filename);}

  SYMBOL_EXPORT ALEState* cloneState(ALEInterface *ale) {
    return new ALEState(ale->cloneState());
  }

  SYMBOL_EXPORT void ALEState_del(ALEState* state) {
    delete state;
  }

  SYMBOL_EXPORT void restoreState(ALEInterface *ale, ALEState* state) {
    ale->restoreState(*state);
  }

  SYMBOL_EXPORT int ALEState_getFrameNumber(ALEState* state) {
    return state->getFrameNumber();
  }

  SYMBOL_EXPORT int ALEState_getEpisodeFrameNumber(ALEState* state) {
    return state->getEpisodeFrameNumber();
  }

  SYMBOL_EXPORT bool ALEState_equals(ALEState* a, ALEState *b) {
    return a->equals(*b);
  }

}

#endif
