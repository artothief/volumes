__author__ = 'artothief'

from gi.repository import Gtk
from decimal import Decimal
import os
import glob
import sqlite3

sqlite3.register_adapter(Decimal, lambda x: str(x))
sqlite3.register_converter('decimal', Decimal)


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
        self.title = ''

        if not os.path.exists('databases'):
            os.makedirs('databases')
        try:
            self.database = max(glob.iglob('databases/*.db'), key=os.path.getmtime)

        except ValueError as a:
            self.database = 'databases/MyDatabase.db'
            print(a, 'No databases in folder')

        self.hwdp = Tubulars.AddTub('HWDP', self.database)
        self.dp = Tubulars.AddTub('DP', self.database)
        self.dc = Tubulars.AddTub('DC', self.database)
        self.mp_liner = Tubulars.AddTub('MP', self.database)
        self.open_hole = Tubulars.AddTub('OH', self.database)

        # Load image and hide liner related stuff for unchecked box
        self.image = builder.get_object('image1')
        self.image.set_from_file('rig_riser.png')

        # Buttons
        self.filechooser_button = builder.get_object('filechooser_button')
        self.autosave = builder.get_object('autosave')

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

        # Combo Boxes
        self.dp_box = builder.get_object('dp_box')
        self.dp2_box = builder.get_object('dp2_box')
        self.hwdp_box = builder.get_object('hwdp_box')
        self.dc_box = builder.get_object('dc_box')
        self.oh_box = builder.get_object('oh_box')
        self.mp_liner_box = builder.get_object('liner_box')

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

        # List of labels for database purposes
        self.label_list = [self.oh_vol_label,
                           self.oh_strokes_label,
                           self.btms_up_vol_label,
                           self.btms_up_strokes_label,
                           self.dp_length_label,
                           self.vol_label,
                           self.stroke_label,
                           self.riser_vol_label,
                           self.riser_stroke_label,
                           self.shoe_strokes_label,
                           self.shoe_btms_up_label,
                           self.liner_vol_label,
                           self.liner_stk_label,
                           self.csg_liner_vol_label,
                           self.csg_liner_stk_label]

        # List of combo boxes for database purposes
        self.combo_list = [self.oh_box,
                           self.dp_box,
                           self.dp2_box,
                           self.hwdp_box,
                           self.dc_box,
                           self.mp_liner_box]

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
                        self.csg_liner_stk_cb,
                        self.autosave]

        self.populate(self.load_db(self.database))
        self.window.show_all()
        self.window.resize(1, 1)

    def load_db(self, database):

            self.dp = Tubulars.AddTub('DP', database)
            self.hwdp = Tubulars.AddTub('HWDP', database)
            self.dc = Tubulars.AddTub('DC', database)
            self.mp_liner = Tubulars.AddTub('MP', database)
            self.open_hole = Tubulars.AddTub('OH', database)
            conn = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            c = conn.cursor()

            c.execute('CREATE TABLE IF NOT EXISTS checkbuttons(id INTEGER PRIMARY KEY, cb BOOLEAN)')
            c.execute('CREATE TABLE IF NOT EXISTS combos(id INTEGER PRIMARY KEY, com INTEGER)')
            c.execute('CREATE TABLE IF NOT EXISTS  entries(id INTEGER PRIMARY KEY, ent TEXT)')

            try:
                c.execute('SELECT ent FROM entries')
                x = [record[0] for record in c.fetchall()]
                print(x)
            except Exception as e:
                x = []
                print(e, 'Ok, if first time using app! Entries retrieve table from db')

            try:
                c.execute('SELECT com FROM combos')
                y = [record[0] for record in c.fetchall()]
                print(y)
            except Exception as e:
                y = []
                print(e, 'Ok, if first time using app! Combos retrieve table from db')

            try:
                c.execute('SELECT cb FROM checkbuttons')
                z = [record[0] for record in c.fetchall()]
                print(z)
            except Exception as e:
                z = []
                print(e, 'Ok, if first time using app! Checkboxes retrieve table from db')
            return x, y, z

    def save_db(self, database):
            conn = sqlite3.connect(database)
            c = conn.cursor()

            for d in self.cb_list:
                c.execute('UPDATE OR IGNORE checkbuttons SET cb = ? WHERE id = ?', (d.get_active(), self.cb_list.index(d)))
                c.execute('INSERT OR  IGNORE INTO checkbuttons(id, cb)  VALUES (?, ?)', (self.cb_list.index(d), d.get_active()))

            for d in self.combo_list:
                c.execute('UPDATE OR IGNORE combos SET com = ? WHERE id = ?', (d.get_active(), self.combo_list.index(d)))
                c.execute('INSERT OR  IGNORE INTO combos(id, com)  VALUES (?, ?)', (self.combo_list.index(d), d.get_active()))

            for d in self.entry_list:
                c.execute('UPDATE OR IGNORE entries SET ent = ? WHERE id = ?', (d.get_text(), self.entry_list.index(d)))
                c.execute('INSERT OR  IGNORE INTO entries(id, ent)  VALUES (?, ?)', (self.entry_list.index(d), d.get_text()))
            conn.commit()
            return

    def populate(self, database):
        liststore_list = [self.open_hole.tub_store,
                          self.dp.tub_store,
                          self.dp.tub_store,
                          self.hwdp.tub_store,
                          self.dc.tub_store,
                          self.mp_liner.tub_store]
        store_set = zip(self.combo_list, liststore_list)
        for cl in store_set:
            cl[0].set_model(cl[1])

        for index, cb in enumerate(self.cb_list):
            z = database[2]
            try:
                if z[index] == 1:
                    cb.set_active(True)
                else:
                    cb.set_active(False)

            except Exception as r:
                print(r, 'Ok, if first time using app! Checkboxes set active')

        for index, entry in enumerate(self.entry_list):
            x = database[0]
            if len(x) - 1 < index:
                entry.set_text('0.00')

            elif x and x[index] != '0.00':
                entry.set_text(x[index])
            else:
                pass

        for index, combo in enumerate(self.combo_list):
            y = database[1]
            try:
                combo.set_active(y[index])
            except Exception as er:
                print(er, 'Ok, if first time using app! Combo set active')

        for label in self.label_list:
            label.set_text(' ')

        self.title = str(self.database).split('/')[-1][:-3]
        self.window.set_title(self.title)

    # All button handlers
    def on_string_vol_cb_toggled(self, button):
        if button.get_active():
            self.bold1.show()
            self.vol_label.show()
        else:
            self.bold1.hide()
            self.vol_label.hide()
        self.window.resize(1, 1)

    def on_string_stk_cb_toggled(self, button):
        if button.get_active():
            self.bold2.show()
            self.stroke_label.show()
        else:
            self.bold2.hide()
            self.stroke_label.hide()
        self.window.resize(1, 1)

    def on_riser_vol_cb_toggled(self, button):
        if button.get_active():
            self.label11.show()
            self.riser_vol_label.show()
        else:
            self.label11.hide()
            self.riser_vol_label.hide()
        self.window.resize(1, 1)

    def on_riser_stk_cb_toggled(self, button):
        if button.get_active():
            self.label20.show()
            self.riser_stroke_label.show()
        else:
            self.label20.hide()
            self.riser_stroke_label.hide()
        self.window.resize(1, 1)

    def on_csg_vol_cb_toggled(self, button):
        if button.get_active():
            self.label21.show()
            self.shoe_btms_up_label.show()
        else:
            self.label21.hide()
            self.shoe_btms_up_label.hide()
        self.window.resize(1, 1)

    def on_csg_stk_cb_toggled(self, button):
        if button.get_active():
            self.label22.show()
            self.shoe_strokes_label.show()
        else:
            self.label22.hide()
            self.shoe_strokes_label.hide()
        self.window.resize(1, 1)

    def on_liner_vol_cb_toggled(self, button):
        if button.get_active():
            self.label17.show()
            self.liner_vol_label.show()
        else:
            self.label17.hide()
            self.liner_vol_label.hide()
        self.window.resize(1, 1)

    def on_liner_stk_cb_toggled(self, button):
        if button.get_active():
            self.label23.show()
            self.liner_stk_label.show()
        else:
            self.label23.hide()
            self.liner_stk_label.hide()
        self.window.resize(1, 1)

    def on_csg_liner_vol_cb_toggled(self, button):
        if button.get_active():
            self.label24.show()
            self.csg_liner_vol_label.show()
        else:
            self.label24.hide()
            self.csg_liner_vol_label.hide()
        self.window.resize(1, 1)

    def on_csg_liner_stk_cb_toggled(self, button):
        if button.get_active():
            self.label25.show()
            self.csg_liner_stk_label.show()
        else:
            self.label25.hide()
            self.csg_liner_stk_label.hide()
        self.window.resize(1, 1)

    def on_oh_vol_cb_toggled(self, button):
        if button.get_active():
            self.label18.show()
            self.oh_vol_label.show()
        else:
            self.label18.hide()
            self.oh_vol_label.hide()
        self.window.resize(1, 1)

    def on_oh_stk_cb_toggled(self, button):
        if button.get_active():
            self.label19.show()
            self.oh_strokes_label.show()
        else:
            self.label19.hide()
            self.oh_strokes_label.hide()
        self.window.resize(1, 1)

    def on_btms_vol_cb_toggled(self, button):
        if button.get_active():
            self.bold3.show()
            self.btms_up_vol_label.show()
        else:
            self.bold3.hide()
            self.btms_up_vol_label.hide()
        self.window.resize(1, 1)

    def on_btms_stk_cb_toggled(self, button):
        if button.get_active():
            self.bold4.show()
            self.btms_up_strokes_label.show()
        else:
            self.bold4.hide()
            self.btms_up_strokes_label.hide()
        self.window.resize(1, 1)

    def on_add_pipe_activate(self, *args):
        self.dp.add_tub.run()
        self.dp.add_tub.hide()

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
        self.filechooser_dialog.set_current_folder('databases/')
        self.filechooser_button.set_label('Open')
        self.filechooser_dialog.set_action(0)
        self.filechooser_dialog.run()
        self.filechooser_dialog.hide()

    def on_save_activate(self, *args):
        self.save_db(self.database)
        print('save')

    def on_save_as_activate(self, *args):
        self.filechooser_dialog.set_current_folder('databases/')
        self.filechooser_button.set_label('Save As')
        self.filechooser_dialog.set_action(1)
        self.filechooser_dialog.set_current_name(self.title + '.db')
        self.filechooser_dialog.run()
        self.filechooser_dialog.hide()

    def on_filechooser_button_clicked(self, *args):
        x = str(self.filechooser_dialog.get_action())
        if 'SAVE' in x:
            self.database = self.filechooser_dialog.get_filename()
            self.save_db(self.database)
            print('save')
        elif 'OPEN' in x:
            self.database = self.filechooser_dialog.get_filename()
            self.populate(self.load_db(self.database))
            print('open')
        else:
            print('Fail')

        self.filechooser_dialog.hide()

    def on_ok_button_clicked(self, *args):
        self.error_dialog.hide()

    def on_values_activate(self, *args):
        self.values.run()
        self.values.hide()

    def on_value_close_button_clicked(self, *args):
        self.values.hide()

    def on_window1_delete_event(self, *args):
        if self.autosave.get_active():
            self.save_db(self.database)
            print('Close with Save')
        else:
            conn = sqlite3.connect(self.database)
            c = conn.cursor()
            c.execute("UPDATE OR IGNORE checkbuttons SET cb = ? WHERE id = ?", (self.autosave.get_active(), 16))
            conn.commit()
            c.close()
            print('Close Without Save ')
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
        liner = self.liner_chbutton.get_active()
        if liner:
            csg_shoe = pbr
        bit_depth = num(self.bit_depth_entry.get_text())
        dc_length = num(self.dc_entry.get_text())
        dc_act = self.dc_box.get_active()
        dc_ce_cap = num(self.dc.tub_store[dc_act][2]) if dc_act >= 0 else Decimal('0.00')
        dc_cap = num(self.dc.tub_store[dc_act][1]) if dc_act >= 0 else Decimal('0.00')
        dc_vol = dc_length * dc_cap
        hwdp_length = num(self.hwdp_entry.get_text())
        hwdp_act = self.hwdp_box.get_active()
        hwdp_cap = num(self.hwdp.tub_store[hwdp_act][1]) if hwdp_act >= 0 else Decimal('0.00')
        hwdp_ce_cap = num(self.hwdp.tub_store[hwdp_act][2]) if hwdp_act >= 0 else Decimal('0.00')
        hwdp_vol = hwdp_length * hwdp_cap

        # Check tapered checkbutton, set dp2 values accordingly
        if self.tap_chbutton.get_active() and self.dp2_box.get_active() >= 0:
            dp2_length = num(self.dp2_entry.get_text())
            dp2_act = self.dp2_box.get_active()
            dp2_cap = num(self.dp.tub_store[dp2_act][1]) if dp2_act >= 0 else Decimal('0.00')
            dp2_ce_cap = num(self.dp.tub_store[dp2_act][2]) if dp2_act >= 0 else Decimal('0.00')
        else:
            dp2_length = num('0.00')
            dp2_cap = num('0.00')
            dp2_ce_cap = num('0.00')

        dp2_vol = dp2_length * dp2_cap

        dp_length = Decimal(bit_depth - (dp2_length + hwdp_length + dc_length))
        dp_act = self.dp_box.get_active()
        dp_cap = num(self.dp.tub_store[dp_act][1]) if dp_act >= 0 else Decimal('0.00')
        dp_ce_cap = num(self.dp.tub_store[dp_act][2]) if dp_act >= 0 else Decimal('0.00')
        dp_vol = dp_length * dp_cap
        oh_act = self.oh_box.get_active()
        oh_cap = num(self.open_hole.tub_store[oh_act][1]) if oh_act >= 0 else Decimal('0.00')
        mp_liner_act = self.mp_liner_box.get_active()
        mp_liner_cap = num(self.mp_liner.tub_store[mp_liner_act][1]) if mp_liner_act >= 0 else Decimal('0.00')

        if dp_length < 0:
            self.error_dialog.set_markup('<b>Drillstring length calculation error, check your numbers!</b>')
            self.error_dialog.show()
            raise AssertionError('eee')

        # Drillstring length and volumes calculations
        print('DP vol: ' + str(dp_vol))
        print('DP2 vol: ' + str(dp2_vol))
        print('HWDP vol: ' + str(hwdp_vol))
        print('DC vol: ' + str(dc_vol) + '\n------------------------------')

        self.dp_length_label.set_text(str(dp_length))
        above_hwdp = dp_length + dp2_length
        above_dc = above_hwdp + hwdp_length
        string = dp_vol + dp2_vol + hwdp_vol + dc_vol
        self.vol_label.set_markup('<b>' + str(round(string, 1)) + ' Litres</b>')
        try:
            str_strokes = string / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            str_strokes = Decimal('0.00')

        self.stroke_label.set_markup('<b>' + str(int(str_strokes)) + ' Strokes</b>')

        # Riser volume calculation
        riser_volume = dp_riser(seabed, riser_cap, dp_length, dp_ce_cap) +\
                       tub_riser(seabed, riser_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                       tub_riser(seabed, riser_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_riser(seabed, riser_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if riser_cap > 0 > riser_volume:
            self.error_dialog.set_markup('Tubular is bigger than Riser or Riser Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Riser or Riser Capacity not entered!')

        self.riser_vol_label.set_text(str(round(riser_volume, 1)) + ' Litres')
        try:
            riser_strokes = riser_volume / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            riser_strokes = Decimal('0.00')

        self.riser_stroke_label.set_text(str(int(riser_strokes)) + ' Strokes')

        # Casing volume calculation
        csg_vol = dp_csg(seabed, csg_shoe if not liner else
                         pbr, csg_cap, dp_length, dp_ce_cap) +\
                  tub_csg(seabed, csg_shoe if not liner else
                          pbr, csg_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                  tub_csg(seabed, csg_shoe if not liner else
                           pbr, csg_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                  tub_csg(seabed, csg_shoe if not liner else
                         pbr, csg_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if csg_vol < 0 < csg_cap and bit_depth > seabed:
            self.error_dialog.set_markup('Tubular is bigger than Casing or Casing Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Casing or Casing Capacity not entered!')

        self.shoe_btms_up_label.set_text(str(round(csg_vol, 1)) + ' Litres')
        try:
            csg_strokes = csg_vol / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            csg_strokes = Decimal('0.00')

        self.shoe_strokes_label.set_text(str(int(csg_strokes)) + ' Strokes')

        # Liner volume calculation
        liner_vol = Decimal('0.00') if not liner else \
                       dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap) +\
                       tub_liner(pbr, liner_shoe, liner_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                       tub_liner(pbr, liner_shoe, liner_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if liner_vol <= 0 and liner and bit_depth > pbr:
            self.error_dialog.set_markup('Tubular is bigger than Liner or Liner Capacity not entered!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than Liner or Liner Capacity not entered!')

        self.liner_vol_label.set_text(str(round(liner_vol, 1)) + ' Litres')
        try:
            liner_strokes = liner_vol / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            liner_strokes = Decimal('0.00')

        self.liner_stk_label.set_text(str(int(liner_strokes)) + ' Strokes')

        csg_liner_vol = csg_vol + liner_vol
        self.csg_liner_vol_label.set_text(str(int(csg_liner_vol)) + ' Litres')

        csg_liner_stk = csg_strokes + liner_strokes
        self.csg_liner_stk_label.set_text(str(int(csg_liner_stk)) + ' Strokes')

        # Open hole volume calculation
        oh_volume = dp_oh(seabed, csg_shoe if not liner else liner_shoe,
                          oh_cap, dp_length, dp_ce_cap) +\
                    tub_oh(seabed, csg_shoe if not liner else liner_shoe,
                           oh_cap, dp_length, dp2_length, dp2_ce_cap, 'DP2') +\
                    tub_oh(seabed, csg_shoe if not liner else liner_shoe,
                            oh_cap, above_hwdp, hwdp_length, hwdp_ce_cap, 'HWDP') +\
                    tub_oh(seabed, csg_shoe if not liner else liner_shoe,
                          oh_cap, above_dc, dc_length, dc_ce_cap, 'DC')

        if oh_volume < 0 and bit_depth > csg_shoe:
            self.error_dialog.set_markup('Tubular is bigger than Open Hole or Open Hole not chosen!')
            self.error_dialog.show()
            raise AssertionError('Tubular is bigger than open hole')

        self.oh_vol_label.set_text(str(round(oh_volume, 1)) + ' Litres')
        try:
            oh_strokes = oh_volume / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            oh_strokes = Decimal('0.00')

        self.oh_strokes_label.set_text(str(int(oh_strokes)) + ' Strokes')

        # Bottoms up calculation
        btms_up_vol = riser_volume + csg_vol + liner_vol + oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(btms_up_vol, 1)) + ' Litres</b>')
        try:
            btms_up_strokes = btms_up_vol / mp_liner_cap
        except (InvalidOperation, DivisionByZero):
            btms_up_strokes = Decimal('0.00')
        self.btms_up_strokes_label.set_markup('<b>' + str(int(btms_up_strokes)) + ' Strokes</b>')


main = Volumes()
main.window.resize(1, 1)
Gtk.main()