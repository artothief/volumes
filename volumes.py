__author__ = 'martin'

from gi.repository import Gtk

pipelist = []
dclist = []
hwdplist = []

class Volumes:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('volumes.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('window1')
        self.window.show_all()

    def pipe_vol(self):
        self.p_entry = self.builder.get_object('p_length_entry')
        self.p_length = float(self.p_entry.get_text())
        pipelist.append(self.p_length)
        self.p_box = self.builder.get_object('p_box')
        self.p_cap = self.p_box.get_active()
        self.p_store = self.builder.get_object('liststore3')
        self.p_val = self.p_store[self.p_cap] [1]
        self.p_vol = self.p_length * self.p_val
        return self.p_vol

    def hwdp_vol(self):
        self.hwdp_entry = self.builder.get_object('hwdp_length_entry')
        self.hwdp_length = float(self.hwdp_entry.get_text())
        hwdplist.append(self.hwdp_length)
        self.hwdp_box = self.builder.get_object('hwdp_box')
        self.hwdp_cap = self.hwdp_box.get_active()
        self.hwdp_store = self.builder.get_object('liststore5')
        self.hwdp_val = self.hwdp_store[self.hwdp_cap] [1]
        self.hwdp_volu = self.hwdp_length * self.hwdp_val
        return self.hwdp_volu

    def dc_vol(self):
        self.dc_entry = self.builder.get_object('dc_length_entry')
        self.dc_length = float(self.dc_entry.get_text())
        dclist.append(self.dc_length)
        self.dc_box = self.builder.get_object('dc_box')
        self.dc_cap = self.dc_box.get_active()
        self.dc_store = self.builder.get_object('liststore6')
        self.dc_val = self.dc_store[self.dc_cap] [1]
        self.dc_volu = self.dc_length * self.dc_val
        return self.dc_volu

    def riser_vol(self):

        self.seabed_entry = self.builder.get_object('seabed_entry')
        self.seabed = float(self.seabed_entry.get_text())
        self.riser_cap_label = self.builder.get_object('riser_cap_label')
        self.riser_cap = float(self.riser_cap_label.get_text())
        self.bit_depth_entry = self.builder.get_object('bit_depth_entry')
        self.bit_depth = float(self.bit_depth_entry.get_text())
        self.csg_shoe_entry = self.builder.get_object('csg_shoe_entry')
        self.csg_shoe = float(self.csg_shoe_entry.get_text())
        #tubular lengths
        self.dp_length = pipelist[0]
        self.hw_length = hwdplist[0]
        self.dc_length = dclist[0]

        #tubular closed end capacities
        self.dp_box = self.builder.get_object('p_box')
        self.dp_act = self.dp_box.get_active()
        self.ce_store = self.builder.get_object('liststore3')
        self.dp_ce_cap = self.p_store[self.dp_act] [2]

        self.hw_box = self.builder.get_object('hwdp_box')
        self.hw_act = self.hw_box.get_active()
        self.hw_store = self.builder.get_object('liststore5')
        self.hwdp_ce_cap = self.hw_store[self.hw_act] [2]

        self.dc_box = self.builder.get_object('dc_box')
        self.dc_act = self.dc_box.get_active()
        self.dc_store = self.builder.get_object('liststore6')
        self.dc_ce_cap = self.dc_store[self.dc_cap] [2]

        #Pipe / Riser volume
        if self.dp_length > self.seabed == True:
            self.riser_dp_vol = self.riser_cap - self.dp_ce_cap * self.seabed
        
        elif self.dp_length < self.seabed and self.dp_length > 0 == True:
            self.riser_dp_vol = (self.riser_cap - self.dp_ce_cap) * self.dp_length
            
        else:
            self.riser_dp_vol = 0
        
        # HWDP / Riser volume     
        if self.dp_length > self.seabed == True:
            self.riser_hwdp_vol = 0
            
        elif self.dp_length < self.seabed and self.dp_length + self.hw_length > self.seabed:
            self.riser_hwdp_vol = (self.riser_cap - self.hwdp_ce_cap) * (self.seabed - self.dp_length)
            
        else:
            self.riser_hwdp_vol = (self.riser_cap - self.hw_length) * self.hw_length
            
        # DC / Riser volume
        if self.dp_length + self.hw_length + self.dc_length < self.seabed == True:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.bit_depth - (self.hw_length + self.dp_length))
            
        elif self.dp_length + self.hw_length < self.seabed == True and self.dp_length + self.hw_length + self.dc_length > self.seabed == True:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.seabed - (self.dp_length + self.hw_length))
            
        else:
            self.riser_dc_vol = 0
            
        self.riser_volume = self.riser_dp_vol + self.riser_hwdp_vol + self.riser_dc_vol
        print self.riser_volume
        return self.riser_volume

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
        self.str_strokes = self.string / self.liner_cap
        self.stroke_label.set_text(str(int(self.str_strokes)) + ' Strokes')
        self.riser_vol_label = self.builder.get_object('riser_btms_up_label')
        self.riser_vol_label.set_text(str(round(Volumes.riser_vol(self))) + ' Litres' )



main = Volumes()
Gtk.main()
