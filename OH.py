__author__ = 'artothief'



def dp_oh(csg_shoe, oh_cap, dp_length, dp_ce_cap):
        
    #Pipe / OH
    if dp_length > csg_shoe:
        dp_oh_vol = (oh_cap - dp_ce_cap) * (dp_length - csg_shoe)
        
    else:
        dp_oh_vol = 0

    print 'Dp/OH = ' + str(dp_oh_vol)
    return dp_oh_vol


def hwdp_oh(csg_shoe, oh_cap, dp_length, hwdp_length, hwdp_ce_cap):
    #HWDP / OH
    if dp_length < csg_shoe and dp_length + hwdp_length > csg_shoe:
        hwdp_oh_vol = (oh_cap - hwdp_ce_cap) * ((dp_length + hwdp_length) - csg_shoe)
        
    elif dp_length > csg_shoe:
        hwdp_oh_vol = (oh_cap - hwdp_ce_cap) * hwdp_length
        
    else:
        hwdp_oh_vol = 0

    print 'HWDP/OH = ' + str(hwdp_oh_vol)
    return hwdp_oh_vol

def dc_oh(csg_shoe, oh_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth):
    #DC / OH
    if dp_length + hwdp_length < csg_shoe and bit_depth > csg_shoe:
        dc_oh_vol = (oh_cap - dc_ce_cap) * (bit_depth - csg_shoe)
        
    elif dp_length + hwdp_length > csg_shoe and bit_depth > dp_length + hwdp_length:
        dc_oh_vol = (oh_cap - dc_ce_cap) * dc_length
        
    elif dc_length > csg_shoe:
        dc_oh_vol = (oh_cap - dc_ce_cap) * dc_length
         
    else:
        dc_oh_vol = 0
    
    print 'DC/OH = ' + str(dc_oh_vol)
    return dc_oh_vol
