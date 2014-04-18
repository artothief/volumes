__author__ = 'martin'

from gi.repository import Gtk

class Handlers():

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_entry2_activate(self, widget):
        print 'entry activated'

builder = Gtk.Builder()
builder.add_from_file('volumes.glade')
builder.connect_signals(Handlers())
window= builder.get_object('window1')
window.show_all()

Gtk.main()
