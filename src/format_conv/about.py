# -*- coding: utf-8 -*-

import gtk
import os
from gettext import gettext as _

Authors = ["Christian Schaller <uraeus@gnome.org>",
           "Łukasz Jernaś <deejay1@srem.org>",
           "Nicolò Chieffo <nicolo.chieffo@gmail.com>",
           "Steven Walter <stevenrwalter@gmail.com>",
           "Michal Schmidt <mschmidt@redhat.com>",
           "Stephane Maniaci <stephane.maniaci@gmail.com>",
           "Jordi Mas <jmas@softcatala.org>",
           "Stuart Langridge <sil@kryogenix.org>",
           "Tom Parker <palfrey@tevp.neta>",
           "Arun Raghavan <arunsr@gnome.org>",
           "Laszlo Pandy <laszlok2@gmail.com>",
           "Claude Paroz <claude@2xlibre.net>"
           ]

Artists = ["Emily and Liam <liam@fightingcrane.com>"]
LGPL = """
Transmageddon
Copyright (C) 2009 Transmageddon Authors
 
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

class AboutDialog:
   def __init__(self):
       x = gtk.AboutDialog()
       x.set_version("0.20")
       x.set_name("Transmageddon")
       x.set_authors(Authors)
       x.set_translator_credits("translator-credits")
       x.set_artists(Artists)
       x.set_logo_icon_name("transmageddon")
       x.set_license(LGPL)   
       x.connect("response", lambda d, r: d.destroy())
       x.show()

   def close(self,widget):
        sys.exit(0)
