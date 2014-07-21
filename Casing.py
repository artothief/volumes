__author__ = 'artothief'

from decimal import *


#Pipe / Csg volume
def dp_csg(seabed, csg_shoe, csg_cap, dp_length, dp_ce_cap):

    if dp_length >= csg_shoe and dp_length > 0:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (csg_shoe - seabed)
        print csg_shoe - seabed

    elif seabed > dp_length < csg_shoe:
        pipe_csg_vol = (csg_cap - dp_ce_cap) * (dp_length - seabed)
        print dp_length - seabed

    else:
        pipe_csg_vol = Decimal('0.00')

    print 'DP/Csg = ' + str(pipe_csg_vol)
    return pipe_csg_vol


#Pipe #2 / Csg volume
def dp2_csg(seabed, csg_shoe, csg_cap, above_dp, dp2_length, dp2_ce_cap):

    if above_dp >= seabed and above_dp + dp2_length <= csg_shoe and dp2_length > 0:
        dp2_csg_vol = (csg_cap - dp2_ce_cap) * dp2_length
        print dp2_length

    elif (above_dp < seabed and above_dp + dp2_length > seabed and
above_dp + dp2_length < csg_shoe):
        dp2_csg_vol = (csg_cap - dp2_ce_cap) * ((above_dp + dp2_length) - seabed)
        print (above_dp + dp2_length) - seabed

    elif (above_dp > seabed and above_dp < csg_shoe and
above_dp + dp2_length > csg_shoe):
        dp2_csg_vol = (csg_cap - dp2_ce_cap) * (csg_shoe - above_dp)
        print csg_shoe - above_dp

    elif above_dp <= seabed and above_dp + dp2_length >= csg_shoe:
        dp2_csg_vol = (csg_cap - dp2_ce_cap) * (csg_shoe - seabed)
        print csg_shoe - seabed

    else:
        dp2_csg_vol = Decimal('0.00')

    print 'Pipe #2/Csg = ' + str(dp2_csg_vol)
    return dp2_csg_vol


#HWDP / Csg volume
def hwdp_csg(seabed, csg_shoe, csg_cap, above_hwdp, hwdp_length, hwdp_ce_cap):

    if above_hwdp >= seabed and above_hwdp + hwdp_length <= csg_shoe and hwdp_length > 0:
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * hwdp_length
        print hwdp_length

    elif (above_hwdp < seabed and above_hwdp + hwdp_length > seabed and
          above_hwdp + hwdp_length < csg_shoe):
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * ((above_hwdp + hwdp_length) - seabed)
        print (above_hwdp + hwdp_length) - seabed

    elif (above_hwdp > seabed and above_hwdp < csg_shoe and
          above_hwdp + hwdp_length > csg_shoe):
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * (csg_shoe - above_hwdp)
        print csg_shoe - above_hwdp

    elif hwdp_length >= seabed and hwdp_length >= csg_shoe and hwdp_length > 0:
        hwdp_csg_vol = (csg_cap - hwdp_ce_cap) * hwdp_length
        print hwdp_length

    else:
        hwdp_csg_vol = Decimal('0.00')

    print 'HWDP/Csg = ' + str(hwdp_csg_vol)
    return hwdp_csg_vol


#DC / Csg volume
def dc_csg(seabed, csg_shoe, csg_cap, above_dc, dc_length, dc_ce_cap, bit_depth):

    if above_dc <= seabed and bit_depth > seabed and bit_depth <= csg_shoe and dc_length > 0:
        dc_csg_vol = (csg_cap - dc_ce_cap) * (bit_depth - csg_shoe)
        print bit_depth - csg_shoe

    elif (above_dc > seabed and above_dc < csg_shoe and
        bit_depth >= csg_shoe):
        dc_csg_vol = (csg_cap - dc_ce_cap) * dc_length
        print dc_length

    elif above_dc < csg_shoe and bit_depth > csg_shoe:
        dc_csg_vol = (csg_cap - dc_ce_cap) * (csg_shoe - (above_dc))
        print csg_shoe - (above_dc)

    else:
        dc_csg_vol = Decimal('0.00')

    print 'DC/Csg = ' + str(dc_csg_vol)
    return dc_csg_vol