from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from _TranslatorDB_local  import *

class Translation(Screen):
        sp=ObjectProperty()
        eng=ObjectProperty()
        def limpiar(self):
                self.translation=""

        def translator(self):
                spa=self.sp.text
                engl=self.eng.text
                print(spa)
                print(engl)
                                

class TranslatorApp(App):
	def build (self):
                return Translation()

if __name__ == '__main__':
	TranslatorApp().run()
