#This is made for Kivy on Android

from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
import info
from new_search import newSearch


def Create_NewSearch(instance):
        key = instance.text
        if key == "":
            text_output._refresh_text("Raiz saw youq gwnz neix ma ra.")
            return False
        if python_version().startswith("2"):
            key = key.decode("utf-8")
        levenshtein = True
        result_yield = newSearch(key, "Saw", levenshtein)
        
        text_output.setGenerator(result_yield)

class RootWidget(StackLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(text_input)
        self.add_widget(text_output)


class TextBrowser(TextInput):#There can only be 1 TextBrowser
    def __browser_init__(self):
        self.text_count = 0
        self.result = ""
    
    def setGenerator(self,generator):
        self.__browser_init__()
        self.text_generator = generator
        self.getText()
    
    def getText(self):#set the current text of the browser
        self.list_result = []
        for n,i in enumerate(self.text_generator):
            self.list_result.append((n + 1, i))
        self.addText()
        
    def addText(self):#put some text from buffer to the widget
        count = 0
        for i in self.list_result[self.text_count:]:
            self.result += "%d.%s\n" % i
            self.text_count += 1
            count += 1
            if count == 50:
                break
        self._refresh_text(self.result)
        


class Sawroeg(App):
    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard = hook_keyboard)
    
    def build(self):
        return RootWidget()
    
    def on_pause(self):
        return True
    
    def on_resume(self):
        pass


def hook_keyboard(self, window, key, *largs):
    if key == 4 or key == 82:
        if text_input.text == "":
            exit()
        else:
            text_input._refresh_text("")
    return True 


if __name__ == '__main__':
    
    #Solve the problem of fonts
    from kivy.resources import resource_add_path
    from kivy.core.text import LabelBase, DEFAULT_FONT
    def add_paths(*paths):
        for p in reversed(paths):
            resource_add_path(p)

    def set_regular(family, *filenames):
        for f in filenames:
            try:
                LabelBase.register(family, f)
                break
            except IOError:
                continue
        else:
            raise IOError('No appropriate fonts for Kivy UI')
    try:
        add_paths('/system/fonts', '/data/fonts')
        set_regular(DEFAULT_FONT,
            'DroidSansFallback.ttf',
        )
    except IOError:
        pass
    
    #Begin
    textlines=1
    
    text_input=TextInput(width=100, size_hint=(1, 0.07), multiline=False) #get input from this widget
    text_input.bind(on_text_validate=Create_NewSearch)
    
    text_output=TextBrowser(text="Sawroeg-%s youq Android~\n" % info.version ,size_hint=(1, 0.93))
    text_output.__browser_init__()
    
    try:
        from kivy.properties import BooleanProperty
        text_output.readonly = BooleanProperty(True)
    except ImportError:
        text_output.readonly = True
    
    Sawroeg().run()
