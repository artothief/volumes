__author__ = 'artothief'

from gi.repository import Gtk

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
        print 'Riser cap = ' + str(self.riser_cap)
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

    #Calculated pipe length
    def pipe_length(self):
        self.bit_depth = float(self.bit_depth_entry.get_text())
        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.dc_length = float(self.dc_entry.get_text())
        p_length = self.bit_depth - (self.hwdp_length + self.dc_length)
        return p_length

    #String volume calculations
    def pipe_vol(self):
        self.dp_length = Volumes.pipe_length(self)
        self.p_cap = self.p_store[self.p_act] [1]
        self.p_vol = self.dp_length * self.p_cap
        return self.p_vol

    def hwdp_vol(self):
        self.hwdp_length = float(self.hwdp_entry.get_text())
        self.hwdp_cap = self.hwdp_store[self.hwdp_act] [1]
        self.hwdp_volu = self.hwdp_length * self.hwdp_cap
        return self.hwdp_volu

    def dc_vol(self):
        self.dc_length = float(self.dc_entry.get_text())
        self.dc_cap = self.dc_store[self.dc_act] [1]
        self.dc_volu = self.dc_length * self.dc_cap
        return self.dc_volu

    #Pipe / Riser volume
    def dp_riser_vol(self):

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

        if self.dp_length >= self.seabed:
            self.riser_hwdp_vol = 0

        elif self.dp_length < self.seabed and self.dp_length + self.hwdp_length > self.seabed:
            self.riser_hwdp_vol = (self.riser_cap - self.hwdp_ce_cap) * (self.seabed - self.dp_length)

        else:
            self.riser_hwdp_vol = (self.riser_cap - self.hwdp_ce_cap) * self.hwdp_length

        print 'Riser/HWDP vol = ' + str(self.riser_hwdp_vol)
        return self.riser_hwdp_vol

    # DC / Riser volume
    def dc_riser_vol(self):

        if self.bit_depth <= self.seabed:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.bit_depth - (self.hwdp_length + self.dp_length))

        elif self.dp_length + self.hwdp_length < self.seabed and self.bit_depth > self.seabed:
            self.riser_dc_vol = (self.riser_cap - self.dc_ce_cap) * (self.seabed - (self.dp_length + self.hwdp_length))

        else:
            self.riser_dc_vol = 0

        print 'Riser/DC vol = ' + str(self.riser_dc_vol)
        return self.riser_dc_vol

    #Pipe / Csg volume
    def pipe_csg_vol(self):


        if self.dp_length >= self.csg_shoe:
            self.pipe_csg_vol = (self.csg_cap - self.dp_ce_cap) * (self.csg_shoe - self.seabed)
            
        elif self.dp_length > self.seabed and self.dp_length < self.csg_shoe:
            self.pipe_csg_vol = (self.csg_cap - self.dp_ce_cap) * (self.dp_length - self.seabed)
            
        else:
            self.pipe_csg_vol = 0

        print 'Csg/DP vol = ' + str(self.pipe_csg_vol)
        return self.pipe_csg_vol

    #HWDP / Csg volume
    def hwdp_csg_volu(self):
        
        if self.dp_length > self.seabed and self.dp_length + self.hwdp_length < self.csg_shoe:
            self.hwdp_csg_vol = (self.csg_cap - self.hwdp_ce_cap) * self.hwdp_length

        elif (self.dp_length < self.seabed and self.dp_length + self.hwdp_length > self.seabed and
    self.dp_length + self.hwdp_length < self.csg_shoe):
            self.hwdp_csg_vol = (self.csg_cap - self.hwdp_ce_cap) * ((self.dp_length + self.hwdp_length) - self.seabed)

        elif (self.dp_length > self.seabed and self.dp_length < self.csg_shoe and
    self.dp_length + self.hwdp_length > self.csg_shoe):
            self.hwdp_csg_vol = (self.csg_cap - self.hwdp_ce_cap) * (self.csg_shoe - self.dp_length)

        elif self.hwdp_length >= self.seabed and self.hwdp_length >= self.csg_shoe:
            self.hwdp_csg_vol = (self.csg_cap - self.hwdp_ce_cap) * self.hwdp_length

        else:
            self.hwdp_csg_vol = 0

        print 'Csg/HWDP vol = ' + str(self.hwdp_csg_vol)
        return self.hwdp_csg_vol
            
    #DC / Csg volume
    def dc_csg_vol(self):
         
        if self.dp_length + self.hwdp_length < self.seabed and self.bit_depth > self.seabed:
            self.dc_csg_vol = (self.csg_cap - self.dc_ce_cap) * (self.bit_depth - self.seabed)
        
        elif (self.dp_length + self.hwdp_length > self.seabed and self.dp_length + self.hwdp_length < self.csg_shoe and
    self.bit_depth <= self.csg_shoe):
            self.dc_csg_vol = (self.csg_cap - self.dc_ce_cap) * self.dc_length
            
        elif self.dp_length + self.hwdp_length < self.csg_shoe and self.bit_depth > self.csg_shoe:
            self.dc_csg_vol = (self.csg_cap - self.dc_ce_cap) * (self.csg_shoe - (self.dp_length + self.hwdp_length))
            
        else:
            self.dc_csg_vol = 0

        print 'Csg/DC vol = ' + str(self.dc_csg_vol)
        return self.dc_csg_vol

    def dp_oh_volume(self):
            
        #Pipe / OH
        if self.dp_length > self.csg_shoe:
            self.dp_oh_vol = (self.oh_cap - self.dp_ce_cap) * (self.dp_length - self.csg_shoe)
            
        else:
            self.dp_oh_vol = 0

        print 'Dp/OH = ' + str(self.dp_oh_vol)
        return self.dp_oh_vol


    def hwdp_oh_volume(self):
        #HWDP / OH
        if self.dp_length < self.csg_shoe and self.dp_length + self.hwdp_length > self.csg_shoe:
            self.hwdp_oh_vol = (self.oh_cap - self.hwdp_ce_cap) * ((self.dp_length + self.hwdp_length) - self.csg_shoe)
            
        elif self.dp_length > self.csg_shoe:
            self.hwdp_oh_vol = (self.oh_cap - self.hwdp_ce_cap) * self.hwdp_length
            
        else:
            self.hwdp_oh_vol = 0

        print 'HWDP/OH = ' + str(self.hwdp_oh_vol)
        return self.hwdp_oh_vol

    def dc_oh_volume(self):
        #DC / OH
        if self.dp_length + self.hwdp_length < self.csg_shoe and self.bit_depth > self.csg_shoe:
            self.dc_oh_vol = (self.oh_cap - self.dc_ce_cap) * (self.bit_depth - self.csg_shoe)
            
        elif self.dp_length + self.hwdp_length > self.csg_shoe and self.bit_depth > self.dp_length + self.hwdp_length:
            self.dc_oh_vol = (self.oh_cap - self.dc_ce_cap) * self.dc_length
            
        elif self.dc_length > self.csg_shoe:
            self.dc_oh_vol = (self.oh_cap - self.dc_ce_cap) * self.dc_length
             
        else:
            self.dc_oh_vol = 0
        
        print 'DC/OH = ' + str(self.dc_oh_vol)
        return self.dc_oh_vol

    def on_window1_delete_event(self, *args):
        Gtk.main_quit()

    def on_calc_button_pressed(self, *args):
        #get active comboboxes and liststores
        self.dc_act = self.dc_box.get_active()
        self.dc_ce_cap = self.dc_store[self.dc_act] [2]
        self.hwdp_act = self.hwdp_box.get_active()
        self.hwdp_ce_cap = self.hwdp_store[self.hwdp_act] [2]
        self.p_act = self.p_box.get_active()
        self.p_cap = self.p_store[self.p_act] [1]
        self.dp_ce_cap = self.p_store[self.p_act] [2]
        self.seabed = float(self.seabed_entry.get_text())
        print 'Seabed = ' + str(self.seabed)
        self.bit_depth = float(self.bit_depth_entry.get_text())
        self.csg_cap = float(self.csg_cap_entry.get_text())
        self.csg_shoe = float(self.csg_shoe_entry.get_text())
        self.oh_act = self.oh_box.get_active()
        self.oh_cap = self.oh_store[self.oh_act] [1]
        self.liner_act = self.liner_box.get_active()
        self.liner_cap = self.linerstore[self.liner_act] [1]
        #Calculate and set label text
        self.dp_length_label.set_text(str(Volumes.pipe_length(self)))
        self.string = Volumes.pipe_vol(self) + Volumes.hwdp_vol(self) + Volumes.dc_vol(self)
        self.vol_label.set_markup('<b>' + str(round(self.string, 2)) + ' Litres</b>')
        self.str_strokes = self.string / self.liner_cap
        self.stroke_label.set_markup('<b>' + str(int(self.str_strokes)) + ' Strokes</b>')
        self.riser_volume = Volumes.dp_riser_vol(self) + Volumes.hwdp_riser_vol(self) + Volumes.dc_riser_vol(self)
        self.riser_vol_label.set_text(str(round(self.riser_volume, 1)) + ' Litres' )
        self.riser_strokes = self.riser_volume / self.liner_cap
        self.riser_stroke_label.set_text(str(int(self.riser_strokes)) + ' Strokes')
        self.csg_vol = Volumes.pipe_csg_vol(self) + Volumes.hwdp_csg_volu(self) + Volumes.dc_csg_vol(self)
        self.shoe_btms_up_label.set_text(str(round(self.csg_vol, 1)) + ' Litres')
        self.csg_strokes = self.csg_vol / self.liner_cap
        self.shoe_strokes_label.set_text(str(int(self.csg_strokes)) + ' Strokes')
        self.oh_volume = Volumes.dp_oh_volume(self) + Volumes.hwdp_oh_volume(self) + Volumes.dc_oh_volume(self)
        self.oh_vol_label.set_text(str(round(self.oh_volume, 1)) + ' Litres' )
        self.oh_strokes = self.oh_volume / self.liner_cap
        self.oh_strokes_label.set_text(str(int(self.oh_strokes)) + ' Strokes')
        self.btms_up_vol = self.riser_volume + self.csg_vol + self.oh_volume
        self.btms_up_vol_label.set_markup('<b>' + str(round(self.btms_up_vol, 1)) + ' Litres</b>')
        self.btms_up_strokes = self.btms_up_vol / self.liner_cap
        self.btms_up_strokes_label.set_markup('<b>' + str(int(self.btms_up_strokes)) + ' Strokes</b>')
main = Volumes()
Gtk.main()
