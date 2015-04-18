__author__ = 'artothief'

from gi.repository import Gtk
from decimal import *
import sqlite3

sqlite3.register_adapter(Decimal, lambda x: str(x))
sqlite3.register_converter('decimal', Decimal)

conn = sqlite3.connect("input.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
c = conn.cursor()

from Annulus import *
import Tubulars


def num(entry, choice):
    if choice == 1:
        de_com = entry.replace(',', '.')
        number = Decimal('0.00') if not entry else Decimal(de_com)
        c.execute('INSERT INTO entries(ent) VALUES (?)', (number,))
        conn.commit()
        return number

    elif choice == 2:
        de_com = entry.replace(',', '.')
        number = Decimal('0.00') if not entry else Decimal(de_com)
        return number

    elif choice == 3:
        if entry >= 0:
            number = entry
            c.execute('INSERT INTO combos(com) VALUES (?)', (number,))
        else:
            number = 0
            c.execute('INSERT INTO combos(com) VALUES (?)', (number,))
        conn.commit()
        return number


class Volumes:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('volumes.glade')
        builder.connect_signals(self)
        self.window = builder.get_object('window1')
        self.error_dialog = builder.get_object('error_dialog')
        self.error_label = builder.get_object('error_text')
        self.hwdp = Tubulars.AddTub('HWDP')
        self.dp = Tubulars.AddTub('DP')
        self.dp2 = Tubulars.AddTub('DP2')
        self.dc = Tubulars.AddTub('DC')
        self.mp_liner = Tubulars.AddTub('MP')
        self.open_hole = Tubulars.AddTub('OH')
        try:
            c.execute('SELECT ent FROM entries')
            x = [record[0] for record in c.fetchall()]
            print x
        except Exception as e:
            x = []
            print e, 'Ok, if first time using app'

        try:
            c.execute('SELECT com FROM combos')
            y = [record[0] for record in c.fetchall()]
            print y
        except Exception as e:
            y = []
            print e, 'Ok, if first time using app'

        def st(entry, dig):
            if len(x) - 1 < dig:
                entry.set_text('0.00')

            elif x and x[dig] != '0.00':
                entry.set_text(x[dig])
            else:
                pass

        def sd(combo, dig):
            try:
                combo.set_active(y[dig])
            except Exception as er:
                print er, 'Ok, if first time using app '

        # making important labels bold
        bold1 = builder.get_object('bold1')
        bold1.set_markup('<b>String Volume :</b>')
        bold2 = builder.get_object('bold2')
        bold2.set_markup('<b>String Strokes :</b>')
        bold3 = builder.get_object('bold3')
        bold3.set_markup('<b>Btms Up Volume :</b>')
        bold4 = builder.get_object('bold4')
        bold4.set_markup('<b>Btms Up Strokes :</b>')

        # bit depth, casing, riser and open hole info
        self.seabed_entry = builder.get_object('seabed_entry')
        st(self.seabed_entry, 0)
        self.riser_cap_entry = builder.get_object('riser_cap_entry')
        st(self.riser_cap_entry, 1)
        self.bit_depth_label = builder.get_object('bit_depth_label')
        self.bit_depth_entry = builder.get_object('bit_depth_entry')
        st(self.bit_depth_entry, 7)
        self.liner_chbutton = builder.get_object('liner_chbutton')
        self.tap_chbutton = builder.get_object('tap_chbutton')
        self.csg_shoe_label = builder.get_object('csg_shoe_label')
        self.csg_shoe_entry = builder.get_object('csg_shoe_entry')
        st(self.csg_shoe_entry, 6)
        self.csg_cap_entry = builder.get_object('csg_cap_entry')
        st(self.csg_cap_entry, 5)
        self.liner_shoe_label = builder.get_object('liner_shoe_label')
        self.liner_shoe_entry = builder.get_object('liner_shoe_entry')
        st(self.liner_shoe_entry, 3)
        self.liner_cap_entry = builder.get_object('liner_cap_entry')
        st(self.liner_cap_entry, 2)
        self.liner_cap_label = builder.get_object('liner_cap_label')
        self.pbr_label = builder.get_object('pbr_label')
        self.pbr_entry = builder.get_object('pbr_entry')
        st(self.pbr_entry, 4)
        self.oh_store = self.open_hole.tub_store
        self.oh_box = builder.get_object('oh_box')
        self.oh_box.set_model(self.oh_store)
        sd(self.oh_box, 4)
        self.oh_vol_label = builder.get_object('oh_vol_label')
        self.oh_strokes_label = builder.get_object('oh_stroke_label')
        self.btms_up_vol_label = builder.get_object('btms_up_vol_label')
        self.btms_up_strokes_label = builder.get_object('btms_up_strokes_label')

        # tubular info
        self.dp_store = self.dp.tub_store
        self.dp_box = builder.get_object('dp_box')
        self.dp_box.set_model(self.dp_store)
        sd(self.dp_box, 3)
        self.dp2_entry = builder.get_object('dp2_entry')
        st(self.dp2_entry, 10)
        self.dp2_entry_label = builder.get_object('dp2_entry_label')
        self.dp2_store = self.dp2.tub_store
        self.dp2_box = builder.get_object('dp2_box')
        self.dp2_box.set_model(self.dp2_store)
        sd(self.dp2_box, 2)
        self.dp2_box_label = builder.get_object('dp2_box_label')
        self.hwdp_entry = builder.get_object('hwdp_length_entry')
        st(self.hwdp_entry, 9)
        self.hwdp_store = self.hwdp.tub_store
        self.hwdp_box = builder.get_object('hwdp_box')
        self.hwdp_box.set_model(self.hwdp_store)
        sd(self.hwdp_box, 1)
        self.dc_entry = builder.get_object('dc_length_entry')
        st(self.dc_entry, 8)
        self.dc_store = self.dc.tub_store
        self.dc_box = builder.get_object('dc_box')
        self.dc_box.set_model(self.dc_store)
        sd(self.dc_box, 0)
        self.dp_length_label = builder.get_object('dp_length_label')
        self.vol_label = builder.get_object('str_vol_label')
        self.stroke_label = builder.get_object('str_stroke_label')
        self.mp_linerstore = self.mp_liner.tub_store
        self.mp_liner_box = builder.get_object('liner_box')
        self.mp_liner_box.set_model(self.mp_linerstore)
        sd(self.mp_liner_box, 5)
        self.riser_vol_label = builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = builder.get_object('riser_strokes_label')
        self.shoe_strokes_label = builder.get_object('shoe_strokes_label')
        self.shoe_btms_up_label = builder.get_object('shoe_btms_up_label')

        self.window.show_all()

        # Load image and hide liner related stuff for unchecked box
        self.image = builder.get_object('image1')
        self.image.set_from_file('rig_riser.png')
        self.pbr_label.hide()
        self.pbr_entry.hide()
        self.liner_shoe_label.hide()
        self.liner_shoe_entry.hide()
        self.liner_cap_entry.hide()
        self.liner_cap_label.hide()
        self.dp2_box.hide()
        self.dp2_box_label.hide()
        self.dp2_entry.hide()
        self.dp2_entry_label.hide()

    def on_add_pipe_activate(self, *args):
        self.dp.add_tub.run()
        self.dp.add_tub.hide()

    def on_add_pipe2_activate(self, *args):
        self.dp2.add_tub.run()
        self.dp2.add_tub.hide()

    def on_add_hwdp_activate(self, *args):
        self.hwdp.add_tub.run()
        self.hwdp.add_tub.hide()

    def on_add_dc_activate(self, *args):
        self.dc.add_tub.run()
        self.dc.add_tub.hide()

    def on_add_mp_liner_activate(self, *args):
        self.mp_liner.add_tub.run()
        self.mp_liner.add_tub.hide()

    def on_add_open_hole_activate(self, *args):
        self.open_hole.add_tub.run()
        self.open_hole.add_tub.hide()

    def on_ok_button_clicked(self, *args):
        self.error_dialog.hide()

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

    def on_tap_chbutton_toggled(self, button):
        if button.get_active():
            self.dp2_box.show()
            self.dp2_box_label.show()
            self.dp2_entry.show()
            self.dp2_entry_label.show()
        else:
            self.dp2_box.hide()
            self.dp2_box_label.hide()
            self.dp2_entry.hide()
            self.dp2_entry_label.hide()
            self.window.resize(1, 1)

    def on_calc_button_clicked(self, *args):
        c.execute('DROP TABLE IF EXISTS entries')
        c.execute('DROP TABLE IF EXISTS combos')
        c.execute('CREATE TABLE IF NOT EXISTS  entries(ent TEXT)')
        c.execute('CREATE TABLE IF NOT EXISTS combos(com INTEGER)')

        # get active comboboxes and liststores, entry's first to meet dependencies
        seabed = num(self.seabed_entry.get_text(), 1)
        riser_cap = num(self.riser_cap_entry.get_text(), 1)
        liner_cap = num(self.liner_cap_entry.get_text(), 1)
        liner_shoe = num(self.liner_shoe_entry.get_text(), 1)
        pbr = num(self.pbr_entry.get_text(), 1)
        csg_cap = num(self.csg_cap_entry.get_text(), 1)
        csg_shoe = num(self.csg_shoe_entry.get_text(), 1)
        if self.liner_chbutton.get_active():
            csg_shoe = pbr
        bit_depth = num(self.bit_depth_entry.get_text(), 1)
        dc_length = num(self.dc_entry.get_text(), 1)
        dc_act = num(self.dc_box.get_active(), 3)
        dc_ce_cap = num(self.dc_store[dc_act][2], 2) if self.dc_store[dc_act][2] else num('0.00', 2)
        dc_cap = num(self.dc_store[dc_act][1], 2) if self.dc_store[dc_act][1] else num('0.00', 2)
        dc_vol = dc_length * dc_cap
        hwdp_length = num(self.hwdp_entry.get_text(), 1)
        hwdp_act = num(self.hwdp_box.get_active(), 3)
        hwdp_cap = num(self.hwdp_store[hwdp_act][1], 2) if self.hwdp_store[hwdp_act][1] else num('0.00', 2)
        hwdp_ce_cap = num(self.hwdp_store[hwdp_act][2], 2) if self.hwdp_store[hwdp_act][2] else num('0.00', 2)
        hwdp_vol = hwdp_length * hwdp_cap

        # Check tapered checkbutton, set dp2 values accordingly
        if self.tap_chbutton.get_active() and self.dp2_box.get_active() >= 0:
            dp2_length = num(self.dp2_entry.get_text(), 1)
            dp2_act = num(self.dp2_box.get_active(), 3)
            dp2_cap = num(self.dp2_store[dp2_act][1], 2) if self.dp2_store[dp2_act][1] else num('0.00', 2)
            dp2_ce_cap = num(self.dp2_store[dp2_act][2], 2) if self.dp2_store[dp2_act][2] else num('0.00', 2)
        else:
            dp2_length = num('0.00', 1)
            dp2_act = num('0.00', 3)
            dp2_cap = num('0.00', 2)
            dp2_ce_cap = num('0.00', 2)

        dp2_vol = dp2_length * dp2_cap

        dp_length = Decimal(bit_depth - (dp2_length + hwdp_length + dc_length))
        dp_act = num(self.dp_box.get_active(), 3)
        dp_cap = num(self.dp_store[dp_act][1], 2)
        dp_ce_cap = num(self.dp_store[dp_act][2], 2)
        dp_vol = dp_length * dp_cap
        oh_act = num(self.oh_box.get_active(), 3)
        oh_cap = num(self.oh_store[oh_act][1], 2)
        mp_liner_act = num(self.mp_liner_box.get_active(), 3)
        mp_liner_cap = num(self.mp_linerstore[mp_liner_act][1], 2)

        if dp_length < 0:
            self.error_dialog.set_markup('<b>Drillstring length calculation error, check your numbers!</b>')
            self.error_dialog.show()
            raise AssertionError('eee')

        # Drillstring length and volumes calculations
        print 'DP vol: ' + str(dp_vol)
        print 'DP2 vol: ' + str(dp2_vol)
        print 'HWDP vol: ' + str(hwdp_vol)
        print 'DC vol: ' + str(dc_vol) + '\n------------------------------'

        self.dp_length_label.set_text(str(dp_length))
        above_hwdp = dp_length + dp2_length
        above_dc = above_hwdp + hwdp_length
        string = dp_vol + dp2_vol + hwdp_vol + dc_vol
        self.vol_label.set_markup('<b>' + str(round(string, 1)) + ' Litres</b>')
        str_strokes = string / mp_liner_cap
        self.stroke_label.set_markup('<b>' + str(int(str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        riser_volume = dp_riser(seabed, riser_cap, dp_length, dp_ce_cap) +\
                       tub_riser(seabed, riser_cap, dp_length,  dp2_length,  dp2_ce_cap, 'DP2') +\
                       tub_riser(seabed, riser_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_riser(seabed, riser_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if riser_volume <= 0 > bit_depth:
            self.error_dialog.set_markup('Tubular is bigger than riser')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than riser')

        self.riser_vol_label.set_text(str(round(riser_volume, 1)) + ' Litres')
        riser_strokes = riser_volume / mp_liner_cap
        self.riser_stroke_label.set_text(str(int(riser_strokes)) + ' Strokes')

        # Casing volume calculation
        csg_vol = dp_csg(seabed, csg_shoe if not self.liner_chbutton.get_active() else
                         pbr, csg_cap, dp_length, dp_ce_cap) +\
                  tub_csg(seabed, csg_shoe if not self.liner_chbutton.get_active() else
                          pbr, csg_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                  tub_csg(seabed, csg_shoe if not self.liner_chbutton.get_active() else
                           pbr, csg_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                  tub_csg(seabed, csg_shoe if not self.liner_chbutton.get_active() else
                         pbr, csg_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if csg_vol <= 0 and bit_depth > seabed:
            self.error_dialog.set_markup('Tubular is bigger than casing')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than casing')

        self.shoe_btms_up_label.set_text(str(round(csg_vol, 1)) + ' Litres')
        csg_strokes = csg_vol / mp_liner_cap
        self.shoe_strokes_label.set_text(str(int(csg_strokes)) + ' Strokes')

        # Liner volume calculation
        liner_volume = Decimal('0.00') if not self.liner_chbutton.get_active() else \
                       dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap) +\
                       tub_liner(pbr, liner_shoe, liner_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if liner_volume <= 0 and self.liner_chbutton.get_active() and bit_depth > pbr:
            self.error_dialog.set_markup('Tubular is bigger than liner')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than liner')

        # Open hole volume calculation
        oh_volume = dp_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe,
                          oh_cap, dp_length, dp_ce_cap) +\
                    tub_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe,
                           oh_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                    tub_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe,
                            oh_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                    tub_oh(csg_shoe if not self.liner_chbutton.get_active() else liner_shoe,
                          oh_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if oh_volume < 0 and bit_depth > csg_shoe:
            self.error_dialog.set_markup('Tubular is bigger than open hole')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than open hole')

        self.oh_vol_label.set_text(str(round(oh_volume, 1)) + ' Litres')
        oh_strokes = oh_volume / mp_liner_cap
        self.oh_strokes_label.set_text(str(int(oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        btms_up_vol = riser_volume + csg_vol + liner_volume + oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(btms_up_vol, 1)) + ' Litres</b>')
        btms_up_strokes = btms_up_vol / mp_liner_cap
        self.btms_up_strokes_label.set_markup('<b>' + str(int(btms_up_strokes)) + ' Strokes</b>')



main = Volumes()
main.window.resize(1, 1)
Gtk.main()