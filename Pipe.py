__author__ = 'artothief'

from gi.repository import Gtk
import sqlite3

#Connect to database
conn = sqlite3.connect('input.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS add_dp(Name text, Capacity text, CE_Capacity)')


# noinspection PyUnusedLocal,PyUnusedLocal
class AddDP:
    
    def __init__(self):
        #Add DP Dialog box
        self.builder = Gtk.Builder()
        self.builder.add_from_file('add_dp.glade')
        self.builder.connect_signals(self)
        self.add_dp = self.builder.get_object('add_dp_dialog')
        self.dp_name_entry = self.builder.get_object('dp_name_entry')
        self.dp_cap_entry = self.builder.get_object('dp_cap_entry')
        self.dp_ce_cap_entry = self.builder.get_object('dp_ce_cap_entry')
        self.dp_store = self.builder.get_object('dp_store')

        for row in c.execute('SELECT * FROM add_dp'):
            self.dp_store.append(row)
        self.dp_tv = self.builder.get_object('dp_tv')
        renderer = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
        column2 = Gtk.TreeViewColumn("Capacity", renderer, text=1)
        column3 = Gtk.TreeViewColumn("Closed End Capacity", renderer, text=2)
        self.dp_tv.append_column(column1)
        self.dp_tv.append_column(column2)
        self.dp_tv.append_column(column3)
        tree_selection = self.dp_tv.get_selection()
        tree_selection.connect("changed", self.on_dp_selection_changed)

    def on_add_dp_btn_clicked(self, *args):
        pipe_name = self.dp_name_entry.get_text()
        pipe_cap = self.dp_cap_entry.get_text()
        pipe_ce_cap = self.dp_ce_cap_entry.get_text()
        c.execute('''INSERT INTO add_dp(Name, Capacity, CE_Capacity)
                          VALUES(?,?,?)''', (pipe_name, pipe_cap, pipe_ce_cap))
        conn.commit()
        self.dp_name_entry.set_text('')
        self.dp_cap_entry.set_text('')
        self.dp_ce_cap_entry.set_text('')
        self.dp_store.append([pipe_name, pipe_cap, pipe_ce_cap])
        self.add_dp.hide()

    def on_rem_dp_btn_clicked(self, *args):
        c.execute("DELETE FROM add_dp WHERE Name=?", (pipe_rem,))
        conn.commit()
        self.dp_store.remove(treeiter)
        self.add_dp.hide()

    # noinspection PyMethodMayBeStatic
    def on_dp_selection_changed(self, selection):
        global pipe_rem
        global treeiter
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            pipe_rem = model[treeiter][0]
        return pipe_rem
