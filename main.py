#This is made for Kivy on Android

from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.stacklayout import StackLayout
from kivy.uix.slider import Slider

import info

from new_search import newSearch


def Create_NewSearch(instance):
        slider.value = 100
        key = instance.text
        if key == "":
            text_output._refresh_text("Raiz saw youq gwnz neix ma ra.")
            return False
        if python_version().startswith("2"):
            key = key.decode("utf-8")
        levenshtein = checkbox.active
        result_yield = newSearch(key, "Saw", levenshtein)
        
        text_output.setGenerator(result_yield)
        text_output.setText()


def on_slider_changed(instance, event):
    value_ratio = 1 - instance.value_normalized
    if value_ratio == 1:
        try:
            text_output.addText()
            slider.value_ratio = 1
        except AttributeError:
            pass
    else:
        text_output.cursor = (0, int(value_ratio * text_output.text_count))

class RootWidget(StackLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(text_input)
        self.add_widget(checkbox)
        self.add_widget(text_output)
        self.add_widget(slider)


class TextBrowser(TextInput):#There can only be 1 TextBrowser
    def __browser_init__(self):
        self.text_count = 0
        self.result = ""
    
    def setGenerator(self,generator):
        self.__browser_init__()
        self.text_generator = generator
    
    def setText(self):#set the current text of the browser
        self.list_result = []
        for i in self.text_generator:
            self.list_result.append((self.text_count, i))
        self.addText()
        
    def addText(self):#put some text from buffer to the widget
        count = 0
        for i in self.list_result[self.text_count + count :]:
            self.result += "%d.%s\n" % i
            self.text_count += 1
            count += 1
            if count == 100:
                break
        self._refresh_text(self.result)
        


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
    
    text_input=TextInput(width=100, size_hint=(0.8,0.07), multiline=False) #get input from this widget
    text_input.bind(on_text_validate=Create_NewSearch)
    
    checkbox=CheckBox(width=2, size_hint=(0.2, 0.07))
    checkbox.active=True #Enable Levenshtein Distance
    
    text_output=TextBrowser(text="Sawroeg-%s youq Android~\n" % info.version ,size_hint=(0.87,0.93))
    text_output.__browser_init__()
    
    slider = Slider(min=0, max=100, value=100, size_hint=(0.12,0.9),orientation="vertical")
    slider.bind(on_touch_move=on_slider_changed)
    
    try:
        from kivy.properties import BooleanProperty
        text_output.readonly = BooleanProperty(True)
    except ImportError:
        text_output.readonly = True
    
    Sawroeg().run()
