__author__ = 'artothief'

from decimal import *


#Pipe/Liner volume
def dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap):

    if dp_length >= liner_shoe and dp_length > 0:
        dp_liner_vol = (liner_cap - dp_ce_cap) * (liner_shoe - pbr)
        print liner_shoe - pbr

    elif dp_length > pbr and dp_length <= liner_shoe:
        dp_liner_vol = (liner_cap - dp_ce_cap) * (dp_length - pbr)
        print dp_length - pbr

    else:
        dp_liner_vol = Decimal('0.00')

    print 'DP/Liner = ' + str(dp_liner_vol)
    return dp_liner_vol


# Pipe #2/Liner volume
def dp2_liner(pbr, liner_shoe, liner_cap, dp_length, dp2_length, dp2_ce_cap):

    if dp_length >= pbr and dp_length + dp2_length <= liner_shoe:
        dp2_liner_vol = (liner_cap - dp2_ce_cap) * dp2_length
        print dp2_length

    elif (dp_length < pbr and dp_length + dp2_length > pbr and
          dp_length + dp2_length < liner_shoe):
        dp2_liner_vol = (liner_cap - dp2_ce_cap) * ((dp_length + dp2_length) - pbr)
        print dp_length + dp2_length - pbr

    elif (dp_length > pbr and dp_length < liner_shoe and
          dp_length + dp2_length > liner_shoe):
        dp2_liner_vol = (liner_cap - dp2_ce_cap) * (liner_shoe - dp_length)
        print liner_shoe - dp_length

    elif dp2_length >= pbr and dp2_length >= liner_shoe and dp2_length > 0:
        dp2_liner_vol = (liner_cap - dp2_ce_cap) * dp2_length
        print dp2_length

    else:
        dp2_liner_vol = Decimal('0.00')

    print 'Pipe #2/Liner = ' + str(dp2_liner_vol)
    return dp2_liner_vol


#HWDP /Liner volume
def hwdp_liner(pbr, liner_shoe, liner_cap, pipe_length, hwdp_length, hwdp_ce_cap):

    if pipe_length >= pbr and pipe_length + hwdp_length <= liner_shoe:
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * hwdp_length
        print hwdp_length

    elif (pipe_length < pbr and pipe_length + hwdp_length > pbr and
          pipe_length + hwdp_length < liner_shoe):
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * ((pipe_length + hwdp_length) - pbr)
        print pipe_length + hwdp_length

    elif (pipe_length > pbr and pipe_length < liner_shoe and
          pipe_length + hwdp_length > liner_shoe):
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * (liner_shoe - pipe_length)
        print liner_shoe - pipe_length

    elif hwdp_length >= pbr and hwdp_length >= liner_shoe and hwdp_length > 0:
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * hwdp_length
        print hwdp_length

    else:
        hwdp_liner_vol = Decimal('0.00')

    print 'HWDP/Liner = ' + str(hwdp_liner_vol)
    return hwdp_liner_vol


#DC /Liner volume
def dc_liner(pbr, liner_shoe, liner_cap, pipe_length, hwdp_length, dc_length, dc_ce_cap, bit_depth):

    if pipe_length + hwdp_length < pbr and bit_depth > pbr:
        dc_liner_vol = (liner_cap - dc_ce_cap) * (bit_depth - pbr)
        print bit_depth - pbr

    elif (pipe_length + hwdp_length > pbr and pipe_length + hwdp_length < liner_shoe and
         bit_depth <= liner_shoe):
        dc_liner_vol = (liner_cap - dc_ce_cap) * dc_length
        print dc_length

    elif pipe_length + hwdp_length < liner_shoe and bit_depth > liner_shoe:
        dc_liner_vol = (liner_cap - dc_ce_cap) * (liner_shoe - (pipe_length + hwdp_length))
        print liner_shoe - (pipe_length + hwdp_length)

    else:
        dc_liner_vol = Decimal('0.00')

    print 'DC/Liner = ' + str(dc_liner_vol)
    return dc_liner_vol