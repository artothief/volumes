__author__ = 'artothief'

from decimal import *


#Pipe / Riser volume
def dp_riser(seabed, riser_cap, dp_length, dp_ce_cap):

    if dp_length >= seabed:
        riser_dp_vol = (riser_cap - dp_ce_cap) * seabed
        print seabed

    elif dp_length < seabed and dp_length > 0:
        riser_dp_vol = (riser_cap - dp_ce_cap) * dp_length
        print dp_length

    else:
        riser_dp_vol = Decimal('0.00')

    print 'DP/Riser = ' + str(riser_dp_vol)
    return riser_dp_vol


def dp2_riser(seabed, riser_cap, dp_length, dp2_length, dp2_ce_cap):

    if dp_length >= seabed:
        riser_dp2_vol = Decimal('0.00')

    elif dp_length < seabed and dp_length +  dp2_length > seabed:
        riser_dp2_vol = (riser_cap - dp2_ce_cap) * (seabed - dp_length)
        print seabed - dp_length
    else:
        riser_dp2_vol = (riser_cap - dp2_ce_cap) * dp2_length
        if dp2_length != Decimal('0.00'):
            print dp2_length
        else:
            pass

    print 'Pipe #2/Riser = ' + str(riser_dp2_vol)
    return riser_dp2_vol


# HWDP / Riser volume
def hwdp_riser(seabed, riser_cap, pipe_length, hwdp_length, hwdp_ce_cap):

    if pipe_length >= seabed:
        riser_hwdp_vol = Decimal('0.00')

    elif pipe_length < seabed and pipe_length + hwdp_length > seabed:
        riser_hwdp_vol = (riser_cap - hwdp_ce_cap) * (seabed - pipe_length)
        print seabed - pipe_length
    else:
        riser_hwdp_vol = (riser_cap - hwdp_ce_cap) * hwdp_length
        if hwdp_length != Decimal('0.00'):
            print hwdp_length
        else:
            pass

    print 'HWDP/Riser = ' + str(riser_hwdp_vol)
    return riser_hwdp_vol


# DC / Riser volume
def dc_riser(seabed, riser_cap, pipe_length, hwdp_length, dc_length, dc_ce_cap, bit_depth):

    if bit_depth <= seabed and dc_length > 0:
        riser_dc_vol = (riser_cap - dc_ce_cap) * (bit_depth - (hwdp_length + pipe_length))
        print bit_depth - (hwdp_length + pipe_length)

    elif pipe_length + hwdp_length < seabed and bit_depth > seabed:
        riser_dc_vol = (riser_cap - dc_ce_cap) * (seabed - (pipe_length + hwdp_length))
        print seabed - (pipe_length + hwdp_length)

    else:
        riser_dc_vol = Decimal('0.00')

    print 'DC/Riser = ' + str(riser_dc_vol)
    return riser_dc_vol