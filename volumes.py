__author__ = 'artothief'

from gi.repository import Gtk

from Riser import *
from Casing import *
from OH import *

class Volumes:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('volumes.glade')
        builder.connect_signals(self)
        window = builder.get_object('window1')
        window.show_all()

        #making important labels bold
        bold1 = builder.get_object('bold1')
        bold1.set_markup('<b>String Volume :</b>')
        bold2 = builder.get_object('bold2')
        bold2.set_markup('<b>String Strokes :</b>')
        bold3 = builder.get_object('bold3')
        bold3.set_markup('<b>Btms Up Volume :</b>')
        bold4 = builder.get_object('bold4')
        bold4.set_markup('<b>Btms Up Strokes :</b>')

        #bit depth, casing, riser and open hole info
        self.seabed_entry = builder.get_object('seabed_entry')
        riser_cap_label = builder.get_object('riser_cap_label')
        self.riser_cap = float(riser_cap_label.get_text())
        self.bit_depth_entry = builder.get_object('bit_depth_entry')
        self.csg_shoe_entry = builder.get_object('csg_shoe_entry')
        self.csg_cap_entry = builder.get_object('csg_cap_entry')
        self.oh_box = builder.get_object('oh_box')
        self.oh_store = builder.get_object('liststore2')
        self.oh_vol_label = builder.get_object('oh_vol_label')
        self.oh_strokes_label = builder.get_object('oh_stroke_label')
        self.btms_up_vol_label = builder.get_object('btms_up_vol_label')
        self.btms_up_strokes_label = builder.get_object('btms_up_strokes_label')

        #tubular info
        self.p_box = builder.get_object('p_box')
        self.p_store = builder.get_object('liststore3')
        self.hwdp_entry = builder.get_object('hwdp_length_entry')
        self.hwdp_box = builder.get_object('hwdp_box')
        self.hwdp_store = builder.get_object('liststore5')
        self.dc_entry = builder.get_object('dc_length_entry')
        self.dc_box = builder.get_object('dc_box')
        self.dc_store = builder.get_object('liststore6')
        self.dp_length_label = builder.get_object('dp_length_label')
        self.vol_label = builder.get_object('str_vol_label')
        self.stroke_label = builder.get_object('str_stroke_label')
        self.liner_box = builder.get_object('liner_box')
        self.linerstore = builder.get_object('liststore1')
        self.riser_vol_label = builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = builder.get_object('riser_strokes_label')
        self.shoe_strokes_label = builder.get_object('shoe_strokes_label')
        self.shoe_btms_up_label = builder.get_object('shoe_btms_up_label')

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_calc_button_clicked(self, *args):
        #get active comboboxes and liststores, entry's first to meet dependencies
        seabed = float(self.seabed_entry.get_text())
        csg_cap = float(self.csg_cap_entry.get_text())
        csg_shoe = float(self.csg_shoe_entry.get_text())
        bit_depth = float(self.bit_depth_entry.get_text())
        dc_length = float(self.dc_entry.get_text())
        dc_act = self.dc_box.get_active()
        dc_ce_cap = self.dc_store[dc_act] [2]
        dc_cap = self.dc_store[dc_act] [1]
        dc_vol = dc_length * dc_cap
        hwdp_length = float(self.hwdp_entry.get_text())
        hwdp_act = self.hwdp_box.get_active()
        hwdp_cap = self.hwdp_store[hwdp_act] [1]
        hwdp_ce_cap = self.hwdp_store[hwdp_act] [2]
        hwdp_vol = hwdp_length * hwdp_cap
        dp_length = bit_depth - (hwdp_length + dc_length)
        p_act = self.p_box.get_active()
        p_cap = self.p_store[p_act] [1]
        dp_ce_cap = self.p_store[p_act] [2]
        dp_vol = dp_length * p_cap
        oh_act = self.oh_box.get_active()
        oh_cap = self.oh_store[oh_act] [1]
        liner_act = self.liner_box.get_active()
        liner_cap = self.linerstore[liner_act] [1]

        # Drillstring length and volumes calculations
        self.dp_length_label.set_text(str(dp_length))
        string = dp_vol + hwdp_vol + dc_vol
        self.vol_label.set_markup('<b>' + str(round(string, 2)) + ' Litres</b>')
        str_strokes = string / liner_cap
        self.stroke_label.set_markup('<b>' + str(int(str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        riser_volume = dp_riser(seabed, self.riser_cap, dp_length, dp_ce_cap) +\
                            hwdp_riser(seabed, self.riser_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                            dc_riser(seabed, self.riser_cap, dp_length, hwdp_length, dc_ce_cap, bit_depth)
        self.riser_vol_label.set_text(str(round(riser_volume, 1)) + ' Litres' )
        riser_strokes = riser_volume / liner_cap
        self.riser_stroke_label.set_text(str(int(riser_strokes)) + ' Strokes')

        # Casing volume calculation
        csg_vol = dp_csg(seabed, csg_shoe, csg_cap, dp_length, dp_ce_cap) +\
                       hwdp_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                       dc_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth)
        self.shoe_btms_up_label.set_text(str(round(csg_vol, 1)) + ' Litres')
        csg_strokes = csg_vol / liner_cap
        self.shoe_strokes_label.set_text(str(int(csg_strokes)) + ' Strokes')

        # Open hole volume calculation
        oh_volume = dp_oh(csg_shoe, oh_cap, dp_length, dp_ce_cap) +\
                         hwdp_oh(csg_shoe, oh_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                         dc_oh(csg_shoe, oh_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth)
        self.oh_vol_label.set_text(str(round(oh_volume, 1)) + ' Litres' )
        oh_strokes = oh_volume / liner_cap
        self.oh_strokes_label.set_text(str(int(oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        btms_up_vol = riser_volume + csg_vol + oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(btms_up_vol, 1)) + ' Litres</b>')
        btms_up_strokes = btms_up_vol / liner_cap
        self.btms_up_strokes_label.set_markup('<b>' + str(int(btms_up_strokes)) + ' Strokes</b>')
        print '------------------------------'

main = Volumes()
Gtk.main()
