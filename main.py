#This is made for Kivy on Android

from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from dictionary import *

def newSearch(key, group):
    if not key:
        yield ""

    if group == "Saw":
        result = searchWord(key, False)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    n = 0
    if group != "Laeh":
        for i in result:
            for j in i[1]:
                yield j
    else:
        for i in result:
            if not i in value:
                yield i

def Create_NewSearch(instance):
        key = instance.text
        if python_version().startswith("2"):
            key = unicode(key)
        levenshtein = False
        result_yield = newSearch(key, "Saw")
        if levenshtein:
            import accurate_search
            result_yield = accurate_search.byLevenshtein(key, result_yield)
        result = ""
        n = 1
        for i in result_yield:
            result += "%d.%s\n" % (n, i)
            n += 1
        text_output._refresh_text(result)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation="vertical"
        self.cols=2
        self.add_widget(text_input)
        self.add_widget(text_output)
        
        

class TestApp(App):

    def build(self):
        return RootWidget()


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
            raise IOError, 'No appropriate fonts for Kivy UI'
    
    add_paths('/system/fonts', '/data/fonts')
    set_regular(DEFAULT_FONT,
        'DroidSansFallback.ttf',
    )
    
    
    #Begin
    text=""
    
    text_input=TextInput(multiline=False) #get input from this widget
    text_input.bind(on_text_validate=Create_NewSearch)
    
    text_output=TextInput(text="Ndi miz")
    
    TestApp().run()
