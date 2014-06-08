__author__ = 'artothief'

from gi.repository import Gtk
import sqlite3

#Connect to database
conn = sqlite3.connect('input.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS add_hwdp(Name text, Capacity text, CE_Capacity)')


# noinspection PyUnusedLocal,PyUnusedLocal
class Add_HWDP:

    def __init__(self):
        #Add HWDP Dialog
        self.builder = Gtk.Builder()
        self.builder.add_from_file('add_hwdp.glade')
        self.builder.connect_signals(self)
        self.add_hwdp = self.builder.get_object('add_hwdp_dialog')
        self.hwdp_name_entry = self.builder.get_object('hwdp_name_entry')
        self.hwdp_cap_entry = self.builder.get_object('hwdp_cap_entry')
        self.hwdp_ce_cap_entry = self.builder.get_object('hwdp_ce_cap_entry')
        self.hwdp_store = self.builder.get_object('hwdp_store')
        for row in c.execute('SELECT * FROM add_hwdp'):
            self.hwdp_store.append(row)
        self.hwdp_tv = self.builder.get_object('hwdp_tv')
        renderer = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
        column2 = Gtk.TreeViewColumn("Capacity", renderer, text=1)
        column3 = Gtk.TreeViewColumn("Closed End Capacity", renderer, text=2)
        self.hwdp_tv.append_column(column1)
        self.hwdp_tv.append_column(column2)
        self.hwdp_tv.append_column(column3)
        tree_selection = self.hwdp_tv.get_selection()
        tree_selection.connect("changed", self.on_hwdp_selection_changed)

    def on_add_hwdp_btn_clicked(self, *args):
        hwdp_name = self.hwdp_name_entry.get_text()
        hwdp_cap = self.hwdp_cap_entry.get_text()
        hwdp_ce_cap = self.hwdp_ce_cap_entry.get_text()
        c.execute('''INSERT INTO add_hwdp(Name, Capacity, CE_Capacity)
                          VALUES(?,?,?)''', (hwdp_name, hwdp_cap, hwdp_ce_cap))
        conn.commit()
        self.hwdp_store.append([hwdp_name, hwdp_cap, hwdp_ce_cap])
        self.hwdp_name_entry.set_text('')
        self.hwdp_cap_entry.set_text('')
        self.hwdp_ce_cap_entry.set_text('')
        self.add_hwdp.hide()

    def on_rem_hwdp_btn_clicked(self, *args):
        c.execute("DELETE FROM add_hwdp WHERE Name=?", (pipe_rem,))
        conn.commit()
        self.hwdp_store.remove(treeiter)
        self.add_hwdp.hide()

    # noinspection PyMethodMayBeStatic
    def on_hwdp_selection_changed(self, selection):
        global pipe_rem
        global treeiter
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            pipe_rem = model[treeiter][0]
        return pipe_rem

    def run(self):
        self.add_hwdp.show()