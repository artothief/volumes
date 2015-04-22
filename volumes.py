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


def num(value):
        de_com = value.replace(',', '.')
        if ',' in value:
            number = Decimal(de_com)

        elif value == '':
            number = Decimal('0.00')

        else:
            number = value
        return Decimal(number)


class Volumes:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('volumes.glade')
        builder.connect_signals(self)
        self.window = builder.get_object('window1')
        self.error_dialog = builder.get_object('error_dialog')
        self.filechooser_dialog = builder.get_object('filechooserdialog')
        self.error_label = builder.get_object('error_text')
        self.values = builder.get_object('value_dialog')
        self.hwdp = Tubulars.AddTub('HWDP')
        self.dp = Tubulars.AddTub('DP')
        self.dp2 = Tubulars.AddTub('DP2')
        self.dc = Tubulars.AddTub('DC')
        self.mp_liner = Tubulars.AddTub('MP')
        self.open_hole = Tubulars.AddTub('OH')

        # Load image and hide liner related stuff for unchecked box
        self.image = builder.get_object('image1')
        self.image.set_from_file('rig_riser.png')

        def get_db():
            try:
                c.execute('SELECT ent FROM entries')
                x = [record[0] for record in c.fetchall()]
                print x
            except Exception as e:
                x = []
                print e, 'Ok, if first time using app! Entries retrieve table from db'

            try:
                c.execute('SELECT com FROM combos')
                y = [record[0] for record in c.fetchall()]
                print y
            except Exception as e:
                y = []
                print e, 'Ok, if first time using app! Combos retrieve table from db'

            try:
                c.execute('SELECT cb FROM checkbuttons')
                z = [record[0] for record in c.fetchall()]
                print z
            except Exception as e:
                z = []
                print e, 'Ok, if first time using app! Checkboxes retrieve table from db'
            return x, y, z

        self.load = get_db()

        def sc(cbtn, dig):
            z = self.load[2]
            try:
                if z[dig] == 1:
                    cbtn.set_active(True)
                else:
                    cbtn.set_active(False)

            except Exception as r:
                print r, 'Ok, if first time using app! Checkboxes set active'

        def st(ety, dig):
            x = self.load[0]
            if len(x) - 1 < dig:
                ety.set_text('0.00')

            elif x and x[dig] != '0.00':
                ety.set_text(x[dig])
            else:
                pass

        def sd(cmb, dig):
            y = self.load[1]
            try:
                cmb.set_active(y[dig])
            except Exception as er:
                print er, 'Ok, if first time using app! Combo set active'

        # Buttons
        self.filechooser_button = builder.get_object('filechooser_button')

        # making important labels bold
        self.bold1 = builder.get_object('bold1')
        self.bold1.set_markup('<b>String Volume :</b>')
        self.bold2 = builder.get_object('bold2')
        self.bold2.set_markup('<b>String Strokes :</b>')
        self.bold3 = builder.get_object('bold3')
        self.bold3.set_markup('<b>Btms Up Volume :</b>')
        self.bold4 = builder.get_object('bold4')
        self.bold4.set_markup('<b>Btms Up Strokes :</b>')

        # Labels (need better naming)
        self.bit_depth_label = builder.get_object('bit_depth_label')
        self.csg_shoe_label = builder.get_object('csg_shoe_label')
        self.liner_shoe_label = builder.get_object('liner_shoe_label')
        self.liner_cap_label = builder.get_object('liner_cap_label')
        self.pbr_label = builder.get_object('pbr_label')
        self.oh_vol_label = builder.get_object('oh_vol_label')
        self.oh_strokes_label = builder.get_object('oh_stroke_label')
        self.btms_up_vol_label = builder.get_object('btms_up_vol_label')
        self.btms_up_strokes_label = builder.get_object('btms_up_strokes_label')
        self.dp2_entry_label = builder.get_object('dp2_entry_label')
        self.dp2_box_label = builder.get_object('dp2_box_label')
        self.dp_length_label = builder.get_object('dp_length_label')
        self.vol_label = builder.get_object('str_vol_label')
        self.stroke_label = builder.get_object('str_stroke_label')
        self.riser_vol_label = builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = builder.get_object('riser_strokes_label')
        self.shoe_strokes_label = builder.get_object('shoe_strokes_label')
        self.shoe_btms_up_label = builder.get_object('shoe_btms_up_label')
        self.liner_vol_label = builder.get_object('liner_vol_label')
        self.liner_stk_label = builder.get_object('liner_stk_label')
        self.csg_liner_vol_label = builder.get_object('csg_liner_vol_label')
        self.csg_liner_stk_label = builder.get_object('csg_liner_stk_label')
        self.label11 = builder.get_object('label11')
        self.label17 = builder.get_object('label17')
        self.label18 = builder.get_object('label18')
        self.label19 = builder.get_object('label19')
        self.label20 = builder.get_object('label20')
        self.label21 = builder.get_object('label21')
        self.label22 = builder.get_object('label22')
        self.label23 = builder.get_object('label23')
        self.label24 = builder.get_object('label24')
        self.label25 = builder.get_object('label25')

        # Entries
        self.seabed_entry = builder.get_object('seabed_entry')
        self.riser_cap_entry = builder.get_object('riser_cap_entry')
        self.csg_shoe_entry = builder.get_object('csg_shoe_entry')
        self.csg_cap_entry = builder.get_object('csg_cap_entry')
        self.pbr_entry = builder.get_object('pbr_entry')
        self.liner_shoe_entry = builder.get_object('liner_shoe_entry')
        self.liner_cap_entry = builder.get_object('liner_cap_entry')
        self.bit_depth_entry = builder.get_object('bit_depth_entry')
        self.dp2_entry = builder.get_object('dp2_entry')
        self.hwdp_entry = builder.get_object('hwdp_length_entry')
        self.dc_entry = builder.get_object('dc_length_entry')

        # Combo Boxes and Liststores
        self.dp_store = self.dp.tub_store
        self.dp_box = builder.get_object('dp_box')
        self.dp_box.set_model(self.dp_store)
        self.dp2_store = self.dp2.tub_store
        self.dp2_box = builder.get_object('dp2_box')
        self.dp2_box.set_model(self.dp2_store)
        self.hwdp_store = self.hwdp.tub_store
        self.hwdp_box = builder.get_object('hwdp_box')
        self.hwdp_box.set_model(self.hwdp_store)
        self.dc_store = self.dc.tub_store
        self.dc_box = builder.get_object('dc_box')
        self.dc_box.set_model(self.dc_store)
        self.oh_store = self.open_hole.tub_store
        self.oh_box = builder.get_object('oh_box')
        self.oh_box.set_model(self.oh_store)
        self.mp_linerstore = self.mp_liner.tub_store
        self.mp_liner_box = builder.get_object('liner_box')
        self.mp_liner_box.set_model(self.mp_linerstore)

        # Checkbuttons
        self.string_vol_cb = builder.get_object('string_vol_cb')
        self.string_stk_cb = builder.get_object('string_stk_cb')
        self.riser_vol_cb = builder.get_object('riser_vol_cb')
        self.riser_stk_cb = builder.get_object('riser_stk_cb')
        self.csg_vol_cb = builder.get_object('csg_vol_cb')
        self.csg_stk_cb = builder.get_object('csg_stk_cb')
        self.liner_vol_cb = builder.get_object('liner_vol_cb')
        self.liner_stk_cb = builder.get_object('liner_stk_cb')
        self.oh_vol_cb = builder.get_object('oh_vol_cb')
        self.oh_stk_cb = builder.get_object('oh_stk_cb')
        self.btms_vol_cb = builder.get_object('btms_vol_cb')
        self.btms_stk_cb = builder.get_object('btms_stk_cb')
        self.liner_chbutton = builder.get_object('liner_chbutton')
        self.tap_chbutton = builder.get_object('tap_chbutton')
        self.csg_liner_vol_cb = builder.get_object('csg_liner_vol_cb')
        self.csg_liner_stk_cb = builder.get_object('csg_liner_stk_cb')

        self.combo_list = [self.oh_box,
                           self.dp_box,
                           self.dp2_box,
                           self.hwdp_box,
                           self.dc_box,
                           self.mp_liner_box]

        for index, combo in enumerate(self.combo_list):
            sd(combo, index)

        # List of entries for database purposes
        self.entry_list = [self.seabed_entry,
                           self.riser_cap_entry,
                           self.bit_depth_entry,
                           self.csg_shoe_entry,
                           self.csg_cap_entry,
                           self.liner_shoe_entry,
                           self.liner_cap_entry,
                           self.pbr_entry,
                           self.dp2_entry,
                           self.hwdp_entry,
                           self.dc_entry]

        for index, entry in enumerate(self.entry_list):
            st(entry, index)

        # List of checkboxes for database purposes
        self.cb_list = [self.string_vol_cb,
                        self.string_stk_cb,
                        self.riser_vol_cb,
                        self.riser_stk_cb,
                        self.csg_vol_cb,
                        self.csg_stk_cb,
                        self.liner_vol_cb,
                        self.liner_stk_cb,
                        self.oh_vol_cb,
                        self.oh_stk_cb,
                        self.btms_vol_cb,
                        self.btms_stk_cb,
                        self.liner_chbutton,
                        self.tap_chbutton,
                        self.csg_liner_vol_cb,
                        self.csg_liner_stk_cb]

        for index, cb in enumerate(self.cb_list):
            sc(cb, index)

        self.window.show_all()
        self.window.resize(1, 1)

    # All button handlers
    def on_string_vol_cb_toggled(self, button):
        if button.get_active():
            self.bold1.show()
            self.vol_label.show()
        else:
            self.bold1.hide()
            self.vol_label.hide()

    def on_string_stk_cb_toggled(self, button):
        if button.get_active():
            self.bold2.show()
            self.stroke_label.show()
        else:
            self.bold2.hide()
            self.stroke_label.hide()

    def on_riser_vol_cb_toggled(self, button):
        if button.get_active():
            self.label11.show()
            self.riser_vol_label.show()
        else:
            self.label11.hide()
            self.riser_vol_label.hide()

    def on_riser_stk_cb_toggled(self, button):
        if button.get_active():
            self.label20.show()
            self.riser_stroke_label.show()
        else:
            self.label20.hide()
            self.riser_stroke_label.hide()

    def on_csg_vol_cb_toggled(self, button):
        if button.get_active():
            self.label21.show()
            self.shoe_btms_up_label.show()
        else:
            self.label21.hide()
            self.shoe_btms_up_label.hide()

    def on_csg_stk_cb_toggled(self, button):
        if button.get_active():
            self.label22.show()
            self.shoe_strokes_label.show()
        else:
            self.label22.hide()
            self.shoe_strokes_label.hide()

    def on_liner_vol_cb_toggled(self, button):
        if button.get_active():
            self.label17.show()
            self.liner_vol_label.show()
        else:
            self.label17.hide()
            self.liner_vol_label.hide()

    def on_liner_stk_cb_toggled(self, button):
        if button.get_active():
            self.label23.show()
            self.liner_stk_label.show()
        else:
            self.label23.hide()
            self.liner_stk_label.hide()

    def on_csg_liner_vol_cb_toggled(self, button):
        if button.get_active():
            self.label24.show()
            self.csg_liner_vol_label.show()
        else:
            self.label24.hide()
            self.csg_liner_vol_label.hide()

    def on_csg_liner_stk_cb_toggled(self, button):
        if button.get_active():
            self.label25.show()
            self.csg_liner_stk_label.show()
        else:
            self.label25.hide()
            self.csg_liner_stk_label.hide()

    def on_oh_vol_cb_toggled(self, button):
        if button.get_active():
            self.label18.show()
            self.oh_vol_label.show()
        else:
            self.label18.hide()
            self.oh_vol_label.hide()

    def on_oh_stk_cb_toggled(self, button):
        if button.get_active():
            self.label19.show()
            self.oh_strokes_label.show()
        else:
            self.label19.hide()
            self.oh_strokes_label.hide()

    def on_btms_vol_cb_toggled(self, button):
        if button.get_active():
            self.bold3.show()
            self.btms_up_vol_label.show()
        else:
            self.bold3.hide()
            self.btms_up_vol_label.hide()

    def on_btms_stk_cb_toggled(self, button):
        if button.get_active():
            self.bold4.show()
            self.btms_up_strokes_label.show()
        else:
            self.bold4.hide()
            self.btms_up_strokes_label.hide()

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

    def on_open_database_activate(self, *args):
        self.filechooser_button.set_label('Open')
        self.filechooser_dialog.set_action(0)
        self.filechooser_dialog.run()
        self.filechooser_dialog.hide()

    def on_export_database_activate(self, *args):
        self.filechooser_button.set_label('Export As')
        self.filechooser_dialog.set_action(1)
        self.filechooser_dialog.set_current_name('YourDatabase.db')
        self.filechooser_dialog.run()
        self.filechooser_dialog.hide()

    def on_filechooser_button_clicked(self, *args):
        x = str(self.filechooser_dialog.get_action())
        if 'SAVE' in x:
            print 'Save'
        elif 'OPEN' in x:
            print 'open'
        else:
            print 'Fail'

        self.filechooser_dialog.hide()

    def on_ok_button_clicked(self, *args):
        self.error_dialog.hide()

    def on_values_activate(self, *args):
        self.values.run()
        self.values.hide()

    def on_value_close_button_clicked(self, *args):
        self.values.hide()

    def on_window1_delete_event(self, *args):
        c.execute('DROP TABLE IF EXISTS checkbuttons')
        c.execute('CREATE TABLE IF NOT EXISTS checkbuttons(cb BOOLEAN)')

        for d in self.cb_list:
            c.execute('INSERT INTO checkbuttons(cb) VALUES (?)', (d.get_active(),))

        c.execute('DROP TABLE IF EXISTS combos')
        c.execute('CREATE TABLE IF NOT EXISTS combos(com INTEGER)')

        for a in self.combo_list:
            c.execute('INSERT INTO combos(com) VALUES (?)', (a.get_active(),))

        c.execute('DROP TABLE IF EXISTS entries')
        c.execute('CREATE TABLE IF NOT EXISTS  entries(ent TEXT)')

        for e in self.entry_list:
            c.execute('INSERT INTO entries(ent) VALUES (?)', (e.get_text(),))
        conn.commit()

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

        # get active comboboxes and liststores, entry's first to meet dependencies
        seabed = num(self.seabed_entry.get_text())
        riser_cap = num(self.riser_cap_entry.get_text())
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
        dc_ce_cap = num(self.dc_store[dc_act][2]) if dc_act else num('0.00')
        dc_cap = num(self.dc_store[dc_act][1]) if dc_act else num('0.00')
        dc_vol = dc_length * dc_cap
        hwdp_length = num(self.hwdp_entry.get_text())
        hwdp_act = self.hwdp_box.get_active()
        hwdp_cap = num(self.hwdp_store[hwdp_act][1]) if hwdp_act else num('0.00')
        hwdp_ce_cap = num(self.hwdp_store[hwdp_act][2]) if hwdp_act else num('0.00')
        hwdp_vol = hwdp_length * hwdp_cap

        # Check tapered checkbutton, set dp2 values accordingly
        if self.tap_chbutton.get_active() and self.dp2_box.get_active() >= 0:
            dp2_length = num(self.dp2_entry.get_text())
            dp2_act = self.dp2_box.get_active()
            dp2_cap = num(self.dp2_store[dp2_act][1]) if dp2_act else num('0.00')
            dp2_ce_cap = num(self.dp2_store[dp2_act][2]) if dp2_act else num('0.00')
        else:
            dp2_length = num('0.00')
            dp2_cap = num('0.00')
            dp2_ce_cap = num('0.00')

        dp2_vol = dp2_length * dp2_cap

        dp_length = Decimal(bit_depth - (dp2_length + hwdp_length + dc_length))
        dp_act = self.dp_box.get_active()
        dp_cap = num(self.dp_store[dp_act][1]) if dp_act else num('0.00')
        dp_ce_cap = num(self.dp_store[dp_act][2]) if dp_act else num('0.00')
        dp_vol = dp_length * dp_cap
        oh_act = self.oh_box.get_active()
        oh_cap = num(self.oh_store[oh_act][1]) if oh_act >= 0 else Decimal('0.00')
        mp_liner_act = self.mp_liner_box.get_active()
        mp_liner_cap = num(self.mp_linerstore[mp_liner_act][1]) if mp_liner_act else num('0.00')

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
        try:
            str_strokes = string / mp_liner_cap
        except InvalidOperation:
            str_strokes = Decimal('0.00')

        self.stroke_label.set_markup('<b>' + str(int(str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        riser_volume = dp_riser(seabed, riser_cap, dp_length, dp_ce_cap) +\
                       tub_riser(seabed, riser_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                       tub_riser(seabed, riser_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_riser(seabed, riser_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if riser_volume <= 0 > bit_depth:
            self.error_dialog.set_markup('Tubular is bigger than Riser or Riser Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Riser or Riser Capacity not entered!')

        self.riser_vol_label.set_text(str(round(riser_volume, 1)) + ' Litres')
        try:
            riser_strokes = riser_volume / mp_liner_cap
        except InvalidOperation:
            riser_strokes = Decimal('0.00')

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
            self.error_dialog.set_markup('Tubular is bigger than Casing or Casing Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Casing or Casing Capacity not entered!')

        self.shoe_btms_up_label.set_text(str(round(csg_vol, 1)) + ' Litres')
        try:
            csg_strokes = csg_vol / mp_liner_cap
        except InvalidOperation:
            csg_strokes = Decimal('0.00')

        self.shoe_strokes_label.set_text(str(int(csg_strokes)) + ' Strokes')

        # Liner volume calculation
        liner_vol = Decimal('0.00') if not self.liner_chbutton.get_active() else \
                       dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap) +\
                       tub_liner(pbr, liner_shoe, liner_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if liner_vol <= 0 and self.liner_chbutton.get_active() and bit_depth > pbr:
            self.error_dialog.set_markup('Tubular is bigger than Liner or Liner Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Liner or Liner Capacity not entered!')

        self.liner_vol_label.set_text(str(round(liner_vol, 1)) + ' Litres')
        try:
            liner_strokes = liner_vol / mp_liner_cap
        except InvalidOperation:
            liner_strokes = Decimal('0.00')

        self.liner_stk_label.set_text(str(int(liner_strokes)) + ' Strokes')

        csg_liner_vol = csg_vol + liner_vol
        self.csg_liner_vol_label.set_text(str(int(csg_liner_vol)) + ' Litres')

        csg_liner_stk = csg_strokes + liner_strokes
        self.csg_liner_stk_label.set_text(str(int(csg_liner_stk)) + ' Strokes')

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
            self.error_dialog.set_markup('Tubular is bigger than Open Hole or Open Hole not chosen!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than open hole')

        self.oh_vol_label.set_text(str(round(oh_volume, 1)) + ' Litres')
        try:
            oh_strokes = oh_volume / mp_liner_cap
        except InvalidOperation:
            oh_strokes = Decimal('0.00')

        self.oh_strokes_label.set_text(str(int(oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        btms_up_vol = riser_volume + csg_vol + liner_vol + oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(btms_up_vol, 1)) + ' Litres</b>')
        try:
            btms_up_strokes = btms_up_vol / mp_liner_cap
        except InvalidOperation:
            btms_up_strokes = Decimal('0.00')
        self.btms_up_strokes_label.set_markup('<b>' + str(int(btms_up_strokes)) + ' Strokes</b>')


main = Volumes()
main.window.resize(1, 1)
Gtk.main()