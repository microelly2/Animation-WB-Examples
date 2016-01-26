# -*- coding: utf-8 -*-
#-------------------------------------------------
#-- miki - my kivy like creation tools
#--
#-- microelly 2016
#--
#-- GNU Lesser General Public License (LGPL)
#-------------------------------------------------

import Animation
import geodat.miki as miki

s='''
#: import Animation
#: App.newDocument("Unbenannt")

Animation.Manager:
	Label: 'Mr. Pytt'
	start: 5
	intervall: 10

#: App.ActiveDocument.ActiveObject.Proxy.run()

'''

m=miki.Miki()
m.run(s)
