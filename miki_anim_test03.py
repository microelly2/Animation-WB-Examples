# -*- coding: utf-8 -*-
#-------------------------------------------------
#-- miki - my kivy like creation tools
#--
#-- microelly 2016
#--
#-- GNU Lesser General Public License (LGPL)
#-------------------------------------------------

import FreeCAD, FreeCADGui
import Animation
import geodat.miki as miki
reload(miki)


s='''
#: import Animation
#: import Part
#: App.newDocument("Unbenannt")

Part.Box: &box

Animation.Manager:
	Label: 'Mr. Pytt'
	start: 5
	intervall: 10
	Animation.Rotator:
		duration:30

#: App.activeDocument().ActiveObject.obj2 = App.activeDocument().getObject('test')

#: App.activeDocument().recompute()
#: FreeCADGui.SendMsgToActiveView("ViewFit")
#: App.ActiveDocument.getObject('My_Manager').Proxy.run()

'''

m=miki.Miki()
m.run(s)
