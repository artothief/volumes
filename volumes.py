__author__ = 'artothief'

from gi.repository import Gtk
from decimal import *
import sqlite3

sqlite3.register_adapter(Decimal, lambda x: str(x))
sqlite3.register_converter('decimal', Decimal)

conn = sqlite3.connect("input.db",
    detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()

from Riser import *
from Casing import *
from Liner import *
from OH import *
import Hwdp
import Pipe
import DC


def num(entry):
    de_com = entry.replace(',', '.')
    number = Decimal(0.00) if not entry else Decimal(de_com)
    c.execute('INSERT INTO entries(ent) VALUES (?)', (number,))
    conn.commit()
    return number


class Volumes:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('volumes.glade')
        builder.connect_signals(self)
        window = builder.get_object('window1')

        self.hwdp = Hwdp.Add_HWDP()
        self.dp = Pipe.Add_DP()
        self.dc = DC.Add_DC()

        try:
            c.execute('SELECT ent FROM entries')
            x = [record[0] for record in c.fetchall()]
            print x
        except Exception as e:
            x = []
            print e


        def st(entry, dig):
            if x and x[dig] != '0':
                entry.set_text(x[dig])
            else:
                pass

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
        st(self.seabed_entry, 0)
        self.bit_depth_label = builder.get_object('bit_depth_label')
        self.bit_depth_entry = builder.get_object('bit_depth_entry')
        st(self.bit_depth_entry, 6)
        self.liner_chbutton = builder.get_object('liner_chbutton')
        self.csg_shoe_label = builder.get_object('csg_shoe_label')
        self.csg_shoe_entry = builder.get_object('csg_shoe_entry')
        st(self.csg_shoe_entry, 5)
        self.csg_cap_entry = builder.get_object('csg_cap_entry')
        st(self.csg_cap_entry, 4)
        self.liner_shoe_label = builder.get_object('liner_shoe_label')
        self.liner_shoe_entry = builder.get_object('liner_shoe_entry')
        st(self.liner_shoe_entry, 2)
        self.liner_cap_entry = builder.get_object('liner_cap_entry')
        st(self.liner_cap_entry, 1)
        self.liner_cap_label = builder.get_object('liner_cap_label')
        self.pbr_label = builder.get_object('pbr_label')
        self.pbr_entry = builder.get_object('pbr_entry')
        st(self.pbr_entry, 3)
        self.oh_box = builder.get_object('oh_box')
        self.oh_store = builder.get_object('liststore2')
        self.oh_vol_label = builder.get_object('oh_vol_label')
        self.oh_strokes_label = builder.get_object('oh_stroke_label')
        self.btms_up_vol_label = builder.get_object('btms_up_vol_label')
        self.btms_up_strokes_label = builder.get_object('btms_up_strokes_label')

        #tubular info
        self.dp_store = self.dp.dp_store
        self.dp_box = builder.get_object('dp_box')
        self.dp_box.set_model(self.dp_store)
        self.dp_box.set_active(0)
        self.hwdp_entry = builder.get_object('hwdp_length_entry')
        st(self.hwdp_entry, 8)
        self.hwdp_store = self.hwdp.hwdp_store
        self.hwdp_box = builder.get_object('hwdp_box')
        self.hwdp_box.set_model(self.hwdp_store)
        self.hwdp_box.set_active(0)
        self.dc_entry = builder.get_object('dc_length_entry')
        st(self.dc_entry, 7)
        self.dc_store = self.dc.dc_store
        self.dc_box = builder.get_object('dc_box')
        self.dc_box.set_model(self.dc_store)
        self.dc_box.set_active(0)
        self.dp_length_label = builder.get_object('dp_length_label')
        self.vol_label = builder.get_object('str_vol_label')
        self.stroke_label = builder.get_object('str_stroke_label')
        self.mp_liner_box = builder.get_object('liner_box')
        self.mp_linerstore = builder.get_object('liststore1')
        self.riser_vol_label = builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = builder.get_object('riser_strokes_label')
        self.shoe_strokes_label = builder.get_object('shoe_strokes_label')
        self.shoe_btms_up_label = builder.get_object('shoe_btms_up_label')

        window.show_all()

        #Load image and hide liner related stuff for unchecked box
        self.image = builder.get_object('image1')
        self.image.set_from_file('rig_riser.png')
        self.pbr_label.hide()
        self.pbr_entry.hide()
        self.liner_shoe_label.hide()
        self.liner_shoe_entry.hide()
        self.liner_cap_entry.hide()
        self.liner_cap_label.hide()

        window.resize(1, 1)

    def on_add_pipe_activate(self, *args):
        self.dp.add_dp.run()
        self.dp.add_dp.hide()

    def on_add_hwdp_activate(self, *args):
        self.hwdp.add_hwdp.run()
        self.hwdp.add_hwdp.hide()

    def on_add_dc_activate(self, *args):
        self.dc.add_dc.run()
        self.dc.add_dc.hide()

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_liner_chbutton_toggled(self, button):
        if button.get_active():
            self.csg_shoe_label.hide()
            self.csg_shoe_entry.hide()
            self.bit_depth_label.set_margin_top(43)
            self.pbr_label.show()
            self.pbr_entry.show()
            self.liner_shoe_label.show()
            self.liner_shoe_entry.show()
            self.liner_cap_entry.show()
            self.liner_cap_label.show()
            self.image.set_from_file('rig_liner.png')
        else:
            self.image.set_from_file('rig_riser.png')
            self.csg_shoe_label.show()
            self.csg_shoe_entry.show()
            self.bit_depth_label.set_margin_top(115)
            self.pbr_label.hide()
            self.pbr_entry.hide()
            self.liner_shoe_label.hide()
            self.liner_shoe_entry.hide()
            self.liner_cap_entry.hide()
            self.liner_cap_label.hide()

    def on_calc_button_clicked(self, *args):
        c.execute('DROP TABLE IF EXISTS entries')
        c.execute('CREATE TABLE  entries(ent TEXT)')
        #get active comboboxes and liststores, entry's first to meet dependencies
        seabed = num(self.seabed_entry.get_text())
        riser_cap = Decimal('187.77')
        liner_cap = num(self.liner_cap_entry.get_text())
        liner_shoe = num(self.liner_shoe_entry.get_text())
        pbr = num(self.pbr_entry.get_text())
        csg_cap = num(self.csg_cap_entry.get_text())
        csg_shoe = num(self.csg_shoe_entry.get_text())
        if self.liner_chbutton.get_active():
            csg_shoe = pbr
        bit_depth = num(self.bit_depth_entry.get_text())
        dc_length = num(self.dc_entry.get_text())
        dc_act = self.dc_box.get_active()
        dc_ce_cap = Decimal(self.dc_store[dc_act][2])
        dc_cap = Decimal(self.dc_store[dc_act][1])
        dc_vol = dc_length * dc_cap
        hwdp_length = num(self.hwdp_entry.get_text())
        hwdp_act = self.hwdp_box.get_active()
        hwdp_cap = Decimal(self.hwdp_store[hwdp_act][1])
        hwdp_ce_cap = Decimal(self.hwdp_store[hwdp_act][2])
        hwdp_vol = hwdp_length * hwdp_cap
        dp_length = Decimal(bit_depth - (hwdp_length + dc_length))
        dp_act = self.dp_box.get_active()
        dp_cap = Decimal(self.dp_store[dp_act][1])
        dp_ce_cap = Decimal(self.dp_store[dp_act][2])
        dp_vol = dp_length * dp_cap
        oh_act = self.oh_box.get_active()
        oh_cap = Decimal(self.oh_store[oh_act][1])
        mp_liner_act = self.mp_liner_box.get_active()
        mp_liner_cap = Decimal(self.mp_linerstore[mp_liner_act][1])

        # Drillstring length and volumes calculations
        self.dp_length_label.set_text(str(dp_length))
        string = dp_vol + hwdp_vol + dc_vol
        self.vol_label.set_markup('<b>' + str(round(string, 1)) + ' Litres</b>')
        str_strokes = string / mp_liner_cap
        self.stroke_label.set_markup('<b>' + str(int(str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        riser_volume = dp_riser(seabed, riser_cap, dp_length, dp_ce_cap) +\
                            hwdp_riser(seabed, riser_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                            dc_riser(seabed, riser_cap, dp_length, hwdp_length, dc_ce_cap, bit_depth)
        self.riser_vol_label.set_text(str(round(riser_volume, 1)) + ' Litres')
        riser_strokes = riser_volume / mp_liner_cap
        self.riser_stroke_label.set_text(str(int(riser_strokes)) + ' Strokes')

        # Casing volume calculation
        csg_vol = dp_csg(seabed, csg_shoe, csg_cap, dp_length, dp_ce_cap) +\
                  hwdp_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                  dc_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth)
        self.shoe_btms_up_label.set_text(str(round(csg_vol, 1)) + ' Litres')
        csg_strokes = csg_vol / mp_liner_cap
        self.shoe_strokes_label.set_text(str(int(csg_strokes)) + ' Strokes')

        # Liner volume calculation
        liner_volume = Decimal('0.00') if not self.liner_chbutton.get_active() else \
                       dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap) +\
                       hwdp_liner(pbr, liner_shoe, liner_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                       dc_liner(pbr, liner_shoe, liner_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth)

        # Open hole volume calculation
        oh_volume = dp_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe, oh_cap, dp_length, dp_ce_cap) +\
                    hwdp_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe, oh_cap, dp_length, hwdp_length, hwdp_ce_cap) +\
                    dc_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe, oh_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth)
        self.oh_vol_label.set_text(str(round(oh_volume, 1)) + ' Litres' )
        oh_strokes = oh_volume / mp_liner_cap
        self.oh_strokes_label.set_text(str(int(oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        btms_up_vol = riser_volume + csg_vol + liner_volume + oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(btms_up_vol, 1)) + ' Litres</b>')
        btms_up_strokes = btms_up_vol / mp_liner_cap
        self.btms_up_strokes_label.set_markup('<b>' + str(int(btms_up_strokes)) + ' Strokes</b>')
        print '------------------------------'

main = Volumes()
Gtk.main()