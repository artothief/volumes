__author__ = 'martin'

from gi.repository import Gtk

class Volumes:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('volumes_3.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('window1')
        self.window.show_all()

    def pipe_vol(self):
        self.entry = self.builder.get_object('p_length_entry')
        self.length = float(self.entry.get_text())
        self.box = self.builder.get_object('p_box')
        self.ce = self.box.get_active()
        self.store = self.builder.get_object('liststore3')
        self.val = self.store[self.ce] [1]
        self.result1 = self.length * self.val
        return self.result1

    def hwdp_vol(self):
        self.hwdp_entry = self.builder.get_object('hwdp_length_entry')
        self.hwdp_box = self.builder.get_object('hwdp_box')
        self.ce = self.hwdp_box.get_active()
        self.store = self.builder.get_object('liststore5')
        self.val = self.store[self.ce] [1]
        self.result2 = float(self.hwdp_entry.get_text()) * self.val
        return self.result2

    def dc_vol(self):
        self.dc_entry = self.builder.get_object('dc_length_entry')
        self.dc_box = self.builder.get_object('dc_box')
        self.ce = self.dc_box.get_active()
        self.store = self.builder.get_object('liststore6')
        self.val = self.store[self.ce] [1]
        self.result3 = float(self.dc_entry.get_text()) * self.val
        return self.result3

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_calc_button_pressed(self, *args):
        self.vol_label = self.builder.get_object('str_vol_label')
        self.string = Volumes.pipe_vol(self) + Volumes.hwdp_vol(self) + Volumes.dc_vol(self)
        self.vol_label.set_text(str(round(self.string, 2)) + ' Litres')
        self.stroke_label = self.builder.get_object('str_stroke_label')
        self.liner_box = self.builder.get_object('liner_box')
        self.liner_act = self.liner_box.get_active()
        self.store = self.builder.get_object('liststore1')
        self.liner_cap = self.store[self.liner_act] [1]
        self.strokes = self.string / self.liner_cap
        self.stroke_label.set_text(str(int(self.strokes)) + ' Strokes')




main = Volumes()
Gtk.main()
