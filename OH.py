__author__ = 'artothief'

from decimal import *


def dp_oh(csg_shoe, oh_cap, dp_length, dp_ce_cap):
        
    #Pipe / OH
    if dp_length > csg_shoe:
        dp_oh_vol = (oh_cap - dp_ce_cap) * (dp_length - csg_shoe)
        print dp_length - csg_shoe
    else:
        dp_oh_vol = Decimal('0.00')

    print 'Dp/OH = ' + str(dp_oh_vol)
    return dp_oh_vol


def dp2_oh(csg_shoe, oh_cap, dp_length, dp2_length, dp2_ce_cap):
    #dp2 / OH
    if dp_length < csg_shoe and dp_length + dp2_length >= csg_shoe:
        dp2_oh_vol = (oh_cap - dp2_ce_cap) * ((dp_length + dp2_length) - csg_shoe)
        print (dp_length + dp2_length) - csg_shoe

    elif dp_length > csg_shoe:
        dp2_oh_vol = (oh_cap - dp2_ce_cap) * dp2_length
        if dp2_length != Decimal('0.00'):
            print dp2_length
        else:
            pass
    else:
        dp2_oh_vol = Decimal('0.00')

    print 'Pipe #2/OH = ' + str(dp2_oh_vol)
    return dp2_oh_vol


def hwdp_oh(csg_shoe, oh_cap, above_hwdp, hwdp_length, hwdp_ce_cap):
    #HWDP / OH
    if above_hwdp < csg_shoe and above_hwdp + hwdp_length >= csg_shoe:
        hwdp_oh_vol = (oh_cap - hwdp_ce_cap) * ((above_hwdp + hwdp_length) - csg_shoe)
        print (above_hwdp + hwdp_length) - csg_shoe
        
    elif above_hwdp > csg_shoe:
        hwdp_oh_vol = (oh_cap - hwdp_ce_cap) * hwdp_length
        if hwdp_length != Decimal('0.00'):
            print hwdp_length
        else:
            pass
    else:
        hwdp_oh_vol = Decimal('0.00')

    print 'HWDP/OH = ' + str(hwdp_oh_vol)
    return hwdp_oh_vol


def dc_oh(csg_shoe, oh_cap, above_dc, dc_length, dc_ce_cap, bit_depth):
    #DC / OH
    if above_dc<= csg_shoe and  above_dc+ dc_length > csg_shoe:
        dc_oh_vol = (oh_cap - dc_ce_cap) * (bit_depth - csg_shoe)
        print bit_depth - csg_shoe
        
    elif above_dc> csg_shoe and bit_depth > above_dc:
        dc_oh_vol = (oh_cap - dc_ce_cap) * dc_length
        print dc_length
        
    elif dc_length > csg_shoe:
        dc_oh_vol = (oh_cap - dc_ce_cap) * dc_length
        print dc_length
         
    else:
        dc_oh_vol = Decimal('0.00')
    
    print 'DC/OH = ' + str(dc_oh_vol)
    return dc_oh_vol
