import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.screen import Screen
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFloatingActionButton
from kivy.lang import Builder

import requests
import os
import random



class main(FloatLayout):
	def __init__(self, **kwargs):
		super(main, self).__init__(**kwargs)
		self.cols = 1
		self.header = Label(text="requestsPy",font_size=100,pos_hint={"center_x":0.5,"center_y":0.9},color=(0.5,0.4,0.1,1))
		self.output = TextInput(hint_text="content response:",size_hint_x=None,size_hint_y=None,width=700,height=500,pos_hint={"center_x":0.5,"center_y":0.53})
		self.downloadbutton = Button(text="Download",size_hint_x=None,size_hint_y=None,width=150,height=60,pos_hint={"center_x":0.5,"center_y":0.3})
		self.downloadbutton.bind(on_press=self.downloadbtn)
		
				
		# response container
		self.responsecont = FloatLayout()
		self.responsecont.reslabel = Label(text="Res::",pos_hint={"center_x":0.2,"center_y":0.8})
		self.responsecont.resoutput = TextInput(hint_text="http response",size_hint_x=None,size_hint_y=None,width=300,height=50,pos_hint={"center_x":0.5,"center_y":0.8})
		self.responsecont.resbutton = Button(text="clear",size_hint_x=None,size_hint_y=None,width=100,height=50,pos_hint={"center_x":0.8,"center_y":0.8})
		self.responsecont.resbutton.bind(on_press=self.rescleanbtn)
		self.responsecont.urlinput = TextInput(multiline=False,text="http://0.0.0.0:8080/",size_hint_x=None,size_hint_y=None,width=400,height=50,pos_hint={"center_x":0.38,"center_y":0.74})
		self.responsecont.sendbutton = Button(text="send request",size_hint_x=None,size_hint_y=None,width=200,height=55,pos_hint={"center_x":0.83,"center_y":0.74})
		self.responsecont.sendbutton.bind(on_press=self.sendbtn)
		
		
		self.responsecont.add_widget(self.responsecont.reslabel)
		self.responsecont.add_widget(self.responsecont.resoutput)
		self.responsecont.add_widget(self.responsecont.resbutton)
		self.responsecont.add_widget(self.responsecont.urlinput)
		self.responsecont.add_widget(self.responsecont.sendbutton)
		# response container
		
		
		# add to main
		self.add_widget(self.header)
		self.add_widget(self.output)
		self.add_widget(self.downloadbutton)
		self.add_widget(self.responsecont)
	
	# buttons
	def rescleanbtn(self, instance):
		self.responsecont.resoutput.text= ""
		#self.responsecont.urlinput = ""
		self.output.text = ""
	
	def sendbtn(self, instance):
		if self.responsecont.urlinput.text != "":
			try:
				self.link = self.responsecont.urlinput.text
				self.r = requests.get(self.link)
				self.output.text = self.r.text
				self.responsecont.resoutput.text = str(self.r)
			except:
				self.output.text = "offline:: OR something wrong"
				pass	
		else:
			pass
			
	def downloadbtn(self, instance):
		pass
	
class myapp(App):
	def build(self):
		return main()
myapp().run()