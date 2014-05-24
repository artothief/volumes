__author__ = 'artothief'

from gi.repository import Gtk

from Riser import *
from Casing import *
from OH import *

class Volumes:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('volumes.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('window1')
        self.window.show_all()

        #making important labels bold
        self.bold1 = self.builder.get_object('bold1')
        self.bold1.set_markup('<b>String Volume :</b>')
        self.bold2 = self.builder.get_object('bold2')
        self.bold2.set_markup('<b>String Strokes :</b>')
        self.bold3 = self.builder.get_object('bold3')
        self.bold3.set_markup('<b>Btms Up Volume :</b>')
        self.bold4 = self.builder.get_object('bold4')
        self.bold4.set_markup('<b>Btms Up Strokes :</b>')

        #bit depth, casing, riser and open hole info
        self.seabed_entry = self.builder.get_object('seabed_entry')
        self.riser_cap_label = self.builder.get_object('riser_cap_label')
        self.riser_cap = float(self.riser_cap_label.get_text())
        self.bit_depth_entry = self.builder.get_object('bit_depth_entry')
        self.csg_shoe_entry = self.builder.get_object('csg_shoe_entry')
        self.csg_cap_entry = self.builder.get_object('csg_cap_entry')
        self.oh_box = self.builder.get_object('oh_box')
        self.oh_store = self.builder.get_object('liststore2')
        self.oh_vol_label = self.builder.get_object('oh_vol_label')
        self.oh_strokes_label = self.builder.get_object('oh_stroke_label')
        self.btms_up_vol_label = self.builder.get_object('btms_up_vol_label')
        self.btms_up_strokes_label = self.builder.get_object('btms_up_strokes_label')

        #tubular info
        self.p_box = self.builder.get_object('p_box')
        self.p_store = self.builder.get_object('liststore3')
        self.hwdp_entry = self.builder.get_object('hwdp_length_entry')
        self.hwdp_box = self.builder.get_object('hwdp_box')
        self.hwdp_store = self.builder.get_object('liststore5')
        self.dc_entry = self.builder.get_object('dc_length_entry')
        self.dc_box = self.builder.get_object('dc_box')
        self.dc_store = self.builder.get_object('liststore6')
        self.dp_length_label = self.builder.get_object('dp_length_label')
        self.vol_label = self.builder.get_object('str_vol_label')
        self.stroke_label = self.builder.get_object('str_stroke_label')
        self.liner_box = self.builder.get_object('liner_box')
        self.linerstore = self.builder.get_object('liststore1')
        self.riser_vol_label = self.builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = self.builder.get_object('riser_strokes_label')
        self.shoe_strokes_label = self.builder.get_object('shoe_strokes_label')
        self.shoe_btms_up_label = self.builder.get_object('shoe_btms_up_label')

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_calc_button_clicked(self, *args):
        #get active comboboxes and liststores, entry's first to meet dependencies
        self.seabed = float(self.seabed_entry.get_text())
        self.csg_cap = float(self.csg_cap_entry.get_text())
        self.csg_shoe = float(self.csg_shoe_entry.get_text())
        self.bit_depth = float(self.bit_depth_entry.get_text())
        self.dc_length = float(self.dc_entry.get_text())
        self.dc_act = self.dc_box.get_active()
        self.dc_ce_cap = self.dc_store[self.dc_act] [2]
        self.dc_cap = self.dc_store[self.dc_act] [1]
        self.dc_vol = self.dc_length * self.dc_cap
        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_cap = self.hwdp_store[self.hwdp_act] [1]
        self.hwdp_ce_cap = self.hwdp_store[self.hwdp_act] [2]
        self.hwdp_vol = self.hwdp_length * self.hwdp_cap
        self.dp_length = self.bit_depth - (self.hwdp_length + self.dc_length)
        self.p_act = self.p_box.get_active()
        self.p_cap = self.p_store[self.p_act] [1]
        self.dp_ce_cap = self.p_store[self.p_act] [2]
        self.dp_vol = self.dp_length * self.p_cap
        self.oh_act = self.oh_box.get_active()
        self.oh_cap = self.oh_store[self.oh_act] [1]
        self.liner_act = self.liner_box.get_active()
        self.liner_cap = self.linerstore[self.liner_act] [1]

        # Drillstring length and volumes calculations
        self.dp_length_label.set_text(str(self.dp_length))
        self.string = self.dp_vol + self.hwdp_vol + self.dc_vol
        self.vol_label.set_markup('<b>' + str(round(self.string, 2)) + ' Litres</b>')
        self.str_strokes = self.string / self.liner_cap
        self.stroke_label.set_markup('<b>' + str(int(self.str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        self.riser_volume = dp_riser(self.seabed, self.riser_cap, self.dp_length, self.dp_ce_cap) +\
                            hwdp_riser(self.seabed, self.riser_cap, self.dp_length, self.hwdp_length, self.hwdp_ce_cap) +\
                            dc_riser(self.seabed, self.riser_cap, self.dp_length, self.hwdp_length, self.dc_ce_cap, self.bit_depth)
        self.riser_vol_label.set_text(str(round(self.riser_volume, 1)) + ' Litres' )
        self.riser_strokes = self.riser_volume / self.liner_cap
        self.riser_stroke_label.set_text(str(int(self.riser_strokes)) + ' Strokes')

        # Casing volume calculation
        self.csg_vol = dp_csg(self.seabed, self.csg_shoe, self.csg_cap, self.dp_length, self.dp_ce_cap) +\
                       hwdp_csg(self.seabed, self.csg_shoe, self.csg_cap, self.dp_length, self.hwdp_length, self.hwdp_ce_cap) +\
                       dc_csg(self.seabed, self.csg_shoe, self.csg_cap, self.dp_length, self.hwdp_length, self.dc_length, self.dc_ce_cap, self.bit_depth)
        self.shoe_btms_up_label.set_text(str(round(self.csg_vol, 1)) + ' Litres')
        self.csg_strokes = self.csg_vol / self.liner_cap
        self.shoe_strokes_label.set_text(str(int(self.csg_strokes)) + ' Strokes')

        # Open hole volume calculation
        self.oh_volume = dp_oh(self.csg_shoe, self.oh_cap, self.dp_length, self.dp_ce_cap) +\
                         hwdp_oh(self.csg_shoe, self.oh_cap, self.dp_length, self.hwdp_length, self.hwdp_ce_cap) +\
                         dc_oh(self.csg_shoe, self.oh_cap, self.dp_length, self.hwdp_length, self.dc_length, self.dc_ce_cap, self.bit_depth)
        self.oh_vol_label.set_text(str(round(self.oh_volume, 1)) + ' Litres' )
        self.oh_strokes = self.oh_volume / self.liner_cap
        self.oh_strokes_label.set_text(str(int(self.oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        self.btms_up_vol = self.riser_volume + self.csg_vol + self.oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(self.btms_up_vol, 1)) + ' Litres</b>')
        self.btms_up_strokes = self.btms_up_vol / self.liner_cap
        self.btms_up_strokes_label.set_markup('<b>' + str(int(self.btms_up_strokes)) + ' Strokes</b>')

main = Volumes()
Gtk.main()
