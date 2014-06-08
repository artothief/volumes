__author__ = 'artothief'

from decimal import *


#Pipe / Csg volume
def dp_csg(seabed, csg_shoe, csg_cap, dp_length, dp_ce_cap):

    if dp_length >= csg_shoe and dp_length > 0:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (csg_shoe - seabed)

    elif dp_length > seabed and dp_length < csg_shoe:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (dp_length - seabed)

    else:
        pipe_csg_vol = Decimal('0.00')

    print 'DP/Csg = ' + str(pipe_csg_vol)
    return pipe_csg_vol


#HWDP / Csg volume
def hwdp_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, hwdp_ce_cap):

    if dp_length >= seabed and dp_length + hwdp_length <= csg_shoe and hwdp_length > 0:
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * hwdp_length

    elif (dp_length < seabed and dp_length + hwdp_length > seabed and
dp_length + hwdp_length < csg_shoe):
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * ((dp_length + hwdp_length) - seabed)

    elif (dp_length > seabed and dp_length < csg_shoe and
dp_length + hwdp_length > csg_shoe):
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * (csg_shoe - dp_length)

    elif hwdp_length >= seabed and hwdp_length >= csg_shoe and hwdp_length > 0:
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * hwdp_length

    else:
        hwdp_csg_vol = Decimal('0.00')

    print 'HWDP/Csg = ' + str(hwdp_csg_vol)
    return hwdp_csg_vol


#DC / Csg volume
def dc_csg(seabed, csg_shoe, csg_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth):

    if dp_length + hwdp_length < seabed and bit_depth > seabed:
        dc_csg_vol = (csg_cap - dc_ce_cap) * (bit_depth - seabed)

    elif (dp_length + hwdp_length > seabed and dp_length + hwdp_length < csg_shoe and
bit_depth <= csg_shoe):
        dc_csg_vol = (csg_cap - dc_ce_cap) * dc_length

    elif dp_length + hwdp_length < csg_shoe and bit_depth > csg_shoe:
        dc_csg_vol = (csg_cap - dc_ce_cap) * (csg_shoe - (dp_length + hwdp_length))

    else:
        dc_csg_vol = Decimal('0.00')

    print 'DC/Csg = ' + str(dc_csg_vol)
    return dc_csg_vol