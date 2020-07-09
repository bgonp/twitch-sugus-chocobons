#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------------------
# Import Libraries
#---------------------------------------
import sys
import os
import json
import codecs
import clr

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "Sugus VS Chocobons"
Website = "http://bgon.es"
Description = "Contador de usuarios que prefieren Sugus o Chocobons"
Creator = "BGON"
Version = "1.0"

#---------------------------------------
# Settings Class
#---------------------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

class Settings(object):
	def __init__(self, settingsfile=None):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
				self.__dict__ = json.load(f, encoding="utf-8")
		except:
			self.cooldown_user = 10
			self.api_url = ""
			self.api_user = ""
			self.api_key = ""
		return

	def Reload(self, jsondata):
		self.__dict__ = json.loads(jsondata, encoding="utf-8")
		return

#---------------------------------------
# [Required] Intialize Data
#---------------------------------------
def Init():
	global Settings
	Settings = Settings(SettingsFile)
	return

#---------------------------------------
# [Required] Process messages
#---------------------------------------
def Execute(data):

	if data.IsChatMessage() and data.IsFromTwitch() and not Parent.IsOnUserCooldown(ScriptName, "", data.User):

		pref = data.GetParam(0).lower()
		if '!sugus':
			pref = 'sugus'
		elif pref == '!chocobons':
			pref = 'chocobons'
		else:
			return

		raw_data = ParseRawData( data.RawData )
		if RequestPreference(raw_data['user-id'], data.UserName, pref):
			Parent.AddUserCooldown(ScriptName, "", data.User, Settings.cooldown_user)

	return

#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
	return

#---------------------------------------
# Save the key in server
#---------------------------------------
def RequestPreference(twitch_id, twitch_nombre, prefiere):
	target_url = "{}?user={}&key={}&twitch_id={}&twitch_nombre={}&prefiere={}".format(Settings.api_url, Settings.api_user, Settings.api_key, twitch_id, twitch_nombre, prefiere)
	response = json.loads(Parent.GetRequest(target_url,{}))
	return response["status"] == 200

#---------------------------------------
# Parse raw data to dictionary
#---------------------------------------
def ParseRawData( rawData ):
	parsed = {}
	for singleData in rawData.split(";"):
		singleDataSplitted = singleData.split("=")
		parsed[singleDataSplitted[0]] = singleDataSplitted[1]
	return parsed