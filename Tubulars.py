__author__ = 'artothief'

from gi.repository import Gtk
import sqlite3


class AddTub:
    
    def __init__(self, tub, db):
        
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS add_DP(Name text, Capacity text, CE_Capacity)')
        self.c.execute('CREATE TABLE IF NOT EXISTS add_HWDP(Name text, Capacity text, CE_Capacity)')
        self.c.execute('CREATE TABLE IF NOT EXISTS add_DC(Name text, Capacity text, CE_Capacity)')
        self.c.execute('CREATE TABLE IF NOT EXISTS add_MP(Name text, Capacity text)')
        self.c.execute('CREATE TABLE IF NOT EXISTS add_OH(Name text, Capacity text)')
        
        # Add tub Dialog box
        self.tub = tub
        self.builder = Gtk.Builder()
        self.builder.add_from_file('add_tub.glade')
        self.builder.connect_signals(self)
        self.add_tub = self.builder.get_object('add_tub_dialog')
        self.tub_name_entry = self.builder.get_object('tub_name_entry')
        self.tub_cap_entry = self.builder.get_object('tub_cap_entry')
        self.tub_ce_cap_entry = self.builder.get_object('tub_ce_cap_entry')
        self.ce_cap_label = self.builder.get_object('ce_cap_label')
        self.tub_label = self.builder.get_object('tub_label')
        self.tub_label.set_text('Add/Remove ' + self.tub)
        self.tub_store = Gtk.ListStore(str, str, str) if 'OH' != self.tub != 'MP' else Gtk.ListStore(str, str)
        self.tub_tv = self.builder.get_object('tub_tv')

        if 'OH' != self.tub != 'MP':
            for row in self.c.execute('SELECT * FROM add_' + self.tub):
                self.tub_store.append(row)

            self.tub_tv.set_model(self.tub_store)
            renderer = Gtk.CellRendererText()
            column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
            column2 = Gtk.TreeViewColumn("Capacity", renderer, text=1)
            column3 = Gtk.TreeViewColumn("Closed End Capacity", renderer, text=2)
            self.tub_tv.append_column(column1)
            self.tub_tv.append_column(column2)
            self.tub_tv.append_column(column3)
            tree_selection = self.tub_tv.get_selection()
            tree_selection.connect("changed", self.on_tub_selection_changed)

        else:
            self.tub_ce_cap_entry.hide()
            self.ce_cap_label.hide()

            for row in self.c.execute('SELECT * FROM add_' + self.tub):
                    self.tub_store.append(row)

            self.tub_tv.set_model(self.tub_store)
            renderer = Gtk.CellRendererText()
            column1 = Gtk.TreeViewColumn("Name", renderer, text=0)
            column2 = Gtk.TreeViewColumn("Capacity", renderer, text=1)
            self.tub_tv.append_column(column1)
            self.tub_tv.append_column(column2)
            tree_selection = self.tub_tv.get_selection()
            tree_selection.connect("changed", self.on_tub_selection_changed)

    def on_add_tub_btn_clicked(self, *args):

        if 'OH' != self.tub != 'MP':
            pipe_name = self.tub_name_entry.get_text()
            pipe_cap = self.tub_cap_entry.get_text()
            pipe_ce_cap = self.tub_ce_cap_entry.get_text()
            self.c.execute('''INSERT INTO add_''' + self.tub + '''(Name, Capacity, CE_Capacity)
                              VALUES(?,?,?)''', (pipe_name, pipe_cap, pipe_ce_cap))
            self.conn.commit()
            self.tub_name_entry.set_text('')
            self.tub_cap_entry.set_text('')
            self.tub_ce_cap_entry.set_text('')
            self.tub_store.append([pipe_name, pipe_cap, pipe_ce_cap])
        else:
            pipe_name = self.tub_name_entry.get_text()
            pipe_cap = self.tub_cap_entry.get_text()
            self.c.execute('''INSERT INTO add_''' + self.tub + '''(Name, Capacity)
                              VALUES(?,?)''', (pipe_name, pipe_cap))
            self.conn.commit()
            self.tub_name_entry.set_text('')
            self.tub_cap_entry.set_text('')
            self.tub_store.append([pipe_name, pipe_cap])

    def on_rem_tub_btn_clicked(self, *args):
        self.c.execute('DELETE FROM add_' + self.tub + ' WHERE Name=?', (pipe_rem,))
        self.conn.commit()
        self.tub_store.remove(treeiter)

    # noinspection PyMethodMayBeStatic
    def on_tub_selection_changed(self, selection):
        global pipe_rem
        global treeiter
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            pipe_rem = model[treeiter][0]
        return pipe_rem