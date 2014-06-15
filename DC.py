__author__ = 'artothief'


from gi.repository import Gtk
import sqlite3

#Connect to database
conn = sqlite3.connect('input.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS add_dc(Name text, Capacity text, CE_Capacity)')


# noinspection PyUnusedLocal
class AddDC:
    
    def __init__(self):
        #Add dc Dialog box
        self.builder = Gtk.Builder()
        self.builder.add_from_file('add_dc.glade')
        self.builder.connect_signals(self)
        self.add_dc = self.builder.get_object('add_dc_dialog')
        self.dc_name_entry = self.builder.get_object('dc_name_entry')
        self.dc_cap_entry = self.builder.get_object('dc_cap_entry')
        self.dc_ce_cap_entry = self.builder.get_object('dc_ce_cap_entry')
        self.dc_store = self.builder.get_object('dc_store')
        for row in c.execute('SELECT * FROM add_dc'):
            self.dc_store.append(row)
        self.dc_tv = self.builder.get_object('dc_tv')
        renderer = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
        column2 = Gtk.TreeViewColumn("Capacity", renderer, text=1)
        column3 = Gtk.TreeViewColumn("Closed End Capacity", renderer, text=2)
        self.dc_tv.append_column(column1)
        self.dc_tv.append_column(column2)
        self.dc_tv.append_column(column3)
        tree_selection = self.dc_tv.get_selection()
        tree_selection.connect("changed", self.on_dc_selection_changed)

    def on_add_dc_btn_clicked(self, *args):
        pipe_name = self.dc_name_entry.get_text()
        pipe_cap = self.dc_cap_entry.get_text()
        pipe_ce_cap = self.dc_ce_cap_entry.get_text()
        c.execute('''INSERT INTO add_dc(Name, Capacity, CE_Capacity)
                          VALUES(?,?,?)''', (pipe_name, pipe_cap, pipe_ce_cap))
        conn.commit()
        self.dc_name_entry.set_text('')
        self.dc_cap_entry.set_text('')
        self.dc_ce_cap_entry.set_text('')
        self.dc_store.append([pipe_name, pipe_cap, pipe_ce_cap])
        self.add_dc.hide()

    def on_rem_dc_btn_clicked(self, *args):
        c.execute("DELETE FROM add_dc WHERE Name=?", (pipe_rem,))
        conn.commit()
        self.dc_store.remove(treeiter)
        self.add_dc.hide()

    # noinspection PyMethodMayBeStatic
    def on_dc_selection_changed(self, selection):
        global pipe_rem
        global treeiter
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            pipe_rem = model[treeiter][0]
        return pipe_rem

    def run(self):
        self.add_dc.show()