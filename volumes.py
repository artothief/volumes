__author__ = 'martin'

from gi.repository import Gtk

pipelist = [1]
dclist = [1]
hwdplist = [1]

class Volumes:

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file('volumes.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('window1')
        self.window.show_all()

        self.seabed_entry = self.builder.get_object('seabed_entry')
        self.seabed = float(self.seabed_entry.get_text())
        print 'Seabed = ' + str(self.seabed)
        self.riser_cap_label = self.builder.get_object('riser_cap_label')
        self.riser_cap = float(self.riser_cap_label.get_text())
        print 'Riser cap = ' + str(self.riser_cap)
        self.bit_depth_entry = self.builder.get_object('bit_depth_entry')
        self.bit_depth = float(self.bit_depth_entry.get_text())
        self.csg_shoe_entry = self.builder.get_object('csg_shoe_entry')
        self.csg_shoe = float(self.csg_shoe_entry.get_text())

        #tubular info
        self.p_box = self.builder.get_object('p_box')
        self.p_store = self.builder.get_object('liststore3')
        self.p_entry = self.builder.get_object('p_length_entry')
        self.hwdp_entry = self.builder.get_object('hwdp_length_entry')
        self.hwdp_box = self.builder.get_object('hwdp_box')
        self.hwdp_store = self.builder.get_object('liststore5')
        self.dc_entry = self.builder.get_object('dc_length_entry')
        self.dc_box = self.builder.get_object('dc_box')
        self.dc_store = self.builder.get_object('liststore6')

        self.vol_label = self.builder.get_object('str_vol_label')
        self.stroke_label = self.builder.get_object('str_stroke_label')
        self.liner_box = self.builder.get_object('liner_box')
        self.linerstore = self.builder.get_object('liststore1')
        self.riser_vol_label = self.builder.get_object('riser_btms_up_label')
        self.riser_stroke_label = self.builder.get_object('riser_strokes_label')


    def pipe_vol(self):
        self.dp_length = float(self.p_entry.get_text())
        self.p_act = self.p_box.get_active()
        self.p_cap = self.p_store[self.p_act] [1]
        self.p_vol = self.dp_length * self.p_cap
        return self.p_vol

    def hwdp_vol(self):
        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_cap = self.hwdp_store[self.hwdp_act] [1]
        self.hwdp_volu = self.hwdp_length * self.hwdp_cap
        return self.hwdp_volu

    def dc_vol(self):
        self.dc_length = float(self.dc_entry.get_text())
        self.dc_act = self.dc_box.get_active()
        self.dc_cap = self.dc_store[self.dc_act] [1]
        self.dc_volu = self.dc_length * self.dc_cap
        return self.dc_volu

     #Pipe / Riser volume
    def dp_riser_vol(self):
        self.dp_length = float(self.p_entry.get_text())
        self.p_act = self.p_box.get_active()
        self.dp_ce_cap = self.p_store[self.p_act] [2]
        print 'DP CE cap = ' + str(self.dp_ce_cap)

        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_ce_cap = self.hwdp_store[self.hwdp_act] [2]
        print 'HWDP CE cap = ' + str(self.hwdp_ce_cap)

        self.dc_length = float(self.dc_entry.get_text())
        self.dc_act = self.dc_box.get_active()
        self.dc_ce_cap = self.dc_store[self.dc_act] [2]
        print 'DC CE cap = ' + str(self.dc_ce_cap)

        if self.dp_length >= self.seabed:
            self.riser_dp_vol = (self.riser_cap - self.dp_ce_cap) * self.seabed

        elif self.dp_length < self.seabed and self.dp_length > 0:
            self.riser_dp_vol = (self.riser_cap - self.dp_ce_cap) * self.dp_length

        else:
            self.riser_dp_vol = 0

        print 'Riser/DP vol = ' + str(self.riser_dp_vol)
        return self.riser_dp_vol

    # HWDP / Riser volume
    def hwdp_riser_vol(self):

        self.dp_length = float(self.p_entry.get_text())
        self.p_act = self.p_box.get_active()
        self.dp_ce_cap = self.p_store[self.p_act] [2]

        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_ce_cap = self.hwdp_store[self.hwdp_act] [2]

        self.dc_length = float(self.dc_entry.get_text())
        self.dc_act = self.dc_box.get_active()
        self.dc_ce_cap = self.dc_store[self.dc_act] [2]

        if self.dp_length >= self.seabed:
            self.riser_hwdp_vol = 0
            print 'Riser/HWDP vol = ' + str(self.riser_hwdp_vol)
            return self.riser_hwdp_vol

        elif self.dp_length < self.seabed and self.dp_length + self.hwdp_length > self.seabed:
            self.riser_hwdp_vol = (self.riser_cap - self.hwdp_ce_cap) * (self.seabed - self.dp_length)
            print 'Riser/HWDP vol = ' + str(self.riser_hwdp_vol)
            return self.riser_hwdp_vol
        else:
            self.riser_hwdp_vol = (self.riser_cap - self.hwdp_ce_cap) * self.hwdp_length
            print 'Riser/HWDP vol = ' + str(self.riser_hwdp_vol)
            return self.riser_hwdp_vol

    # DC / Riser volume
    def dc_riser_vol(self):

        self.dp_length = float(self.p_entry.get_text())
        self.p_act = self.p_box.get_active()
        self.dp_ce_cap = self.p_store[self.p_act] [2]

        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_ce_cap = self.hwdp_store[self.hwdp_act] [2]

        self.dc_length = float(self.dc_entry.get_text())
        self.dc_act = self.dc_box.get_active()
        self.dc_ce_cap = self.dc_store[self.dc_act] [2]

        if self.dp_length + self.hwdp_length + self.dc_length < self.seabed:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.bit_depth - (self.hwdp_length + self.dp_length))

        elif self.dp_length + self.hwdp_length < self.seabed and self.dp_length + self.hwdp_length + self.dc_length > self.seabed:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.seabed - (self.dp_length + self.hwdp_length))

        else:
            self.riser_dc_vol = 0

        print 'Riser/DC vol = ' + str(self.riser_dc_vol)
        return self.riser_dc_vol

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_calc_button_pressed(self, *args):
        self.string = Volumes.pipe_vol(self) + Volumes.hwdp_vol(self) + Volumes.dc_vol(self)
        self.vol_label.set_text(str(round(self.string, 2)) + ' Litres')
        self.liner_act = self.liner_box.get_active()
        self.liner_cap = self.linerstore[self.liner_act] [1]
        self.str_strokes = self.string / self.liner_cap
        self.stroke_label.set_text(str(int(self.str_strokes)) + ' Strokes')
        self.riser_volume = Volumes.dp_riser_vol(self) + Volumes.hwdp_riser_vol(self) + Volumes.dc_riser_vol(self)
        self.riser_vol_label.set_text(str(round(self.riser_volume)) + ' Litres' )
        self.riser_strokes = self.riser_volume / self.liner_cap
        self.riser_stroke_label.set_text(str(int(self.riser_strokes)) + ' Strokes')


main = Volumes()
Gtk.main()
