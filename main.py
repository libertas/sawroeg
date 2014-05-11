#This is made for Kivy on Android

from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.stacklayout import StackLayout

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
        if key == "":
            text_output._refresh_text("Raiz saw youq gwnz neix ma ra.")
            return False
        if python_version().startswith("2"):
            key = unicode(key)
        levenshtein = checkbox.active
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

class RootWidget(StackLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols=3
        self.add_widget(text_input)
        self.add_widget(checkbox)
        self.add_widget(text_output)
        

class Sawroeg(App):

    def build(self):
        return RootWidget()
    
    def on_pause(self):
        return True
    
    def on_resume(self):
        pass


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
    try:
        add_paths('/system/fonts', '/data/fonts')
        set_regular(DEFAULT_FONT,
            'DroidSansFallback.ttf',
        )
    except IOError:
        pass
    
    #Begin
    text=""
    
    text_input=TextInput(width=100, size_hint=(0.8,0), multiline=False) #get input from this widget
    text_input.bind(on_text_validate=Create_NewSearch)
    
    checkbox=CheckBox(width=2, size_hint=(0.2, 0))
    checkbox.active=True #Enable Levenshtein Distance
    
    text_output=TextInput(text="Sawroeg youq Android~\n")
    try:
        from kivy.properties import BooleanProperty
        text_output.readonly = BooleanProperty(True)
    except ImportError:
        text_output.readonly = True
    
    Sawroeg().run()
