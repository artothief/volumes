__author__ = 'artothief'

from gi.repository import Gtk


class AddTub:
    
    def __init__(self, tub, liststore, window):
        
        # Add tub Dialog box
        self.tub = tub
        self.builder = Gtk.Builder()
        self.builder.add_from_file('add_tub.glade')
        self.builder.connect_signals(self)
        self.add_tub = self.builder.get_object('add_tub_dialog')
        self.add_tub.set_transient_for(window)
        self.tub_name_entry = self.builder.get_object('tub_name_entry')
        self.tub_cap_entry = self.builder.get_object('tub_cap_entry')
        self.tub_ce_cap_entry = self.builder.get_object('tub_ce_cap_entry')
        self.ce_cap_label = self.builder.get_object('ce_cap_label')
        self.tub_label = self.builder.get_object('tub_label')
        self.tub_label.set_text('Add/Remove ' + self.tub)
        self.tub_tv = self.builder.get_object('tub_tv')
        self.liststore = liststore

        if 'OH' != self.tub != 'MP':

            self.tub_tv.set_model(self.liststore)
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

            self.tub_tv.set_model(self.liststore)
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
            self.tub_name_entry.set_text('')
            self.tub_cap_entry.set_text('')
            self.tub_ce_cap_entry.set_text('')
            self.liststore.append([pipe_name, pipe_cap, pipe_ce_cap])
        else:
            pipe_name = self.tub_name_entry.get_text()
            pipe_cap = self.tub_cap_entry.get_text()
            self.tub_name_entry.set_text('')
            self.tub_cap_entry.set_text('')
            self.liststore.append([pipe_name, pipe_cap])

    def on_rem_tub_btn_clicked(self, *args):
        self.liststore.remove(treeiter)

    def on_add_tub_dialog_delete_event(self, *args):
        self.add_tub.hide()

    # noinspection PyMethodMayBeStatic
    def on_tub_selection_changed(self, selection):
        global pipe_rem
        global treeiter
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            pipe_rem = model[treeiter][0]
        return pipe_rem