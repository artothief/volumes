__author__ = 'artothief'

#Pipe / Csg volume
def dp_liner(pbr, liner_shoe, liner_cap, dp_length, dp_ce_cap):

    if dp_length >= liner_shoe:
        pipe_liner_vol = (liner_cap - dp_ce_cap) * (liner_shoe - pbr)

    elif dp_length > pbr and dp_length < liner_shoe:
        pipe_liner_vol = (liner_cap - dp_ce_cap) * (dp_length - pbr)

    else:
        pipe_liner_vol = 0

    print 'DP/Liner = ' + str(pipe_liner_vol)
    return pipe_liner_vol

#HWDP / Csg volume
def hwdp_liner(pbr, liner_shoe, liner_cap, dp_length, hwdp_length, hwdp_ce_cap):

    if dp_length >= pbr and dp_length + hwdp_length <= liner_shoe:
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * hwdp_length

    elif (dp_length < pbr and dp_length + hwdp_length > pbr and
dp_length + hwdp_length < liner_shoe):
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * ((dp_length + hwdp_length) - pbr)

    elif (dp_length > pbr and dp_length < liner_shoe and
dp_length + hwdp_length > liner_shoe):
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * (liner_shoe - dp_length)

    elif hwdp_length >= pbr and hwdp_length >= liner_shoe:
        hwdp_liner_vol = (liner_cap - hwdp_ce_cap) * hwdp_length

    else:
        hwdp_liner_vol = 0

    print 'HWDP/Liner = ' + str(hwdp_liner_vol)
    return hwdp_liner_vol

#DC / Csg volume
def dc_liner(pbr, liner_shoe, liner_cap, dp_length, hwdp_length, dc_length, dc_ce_cap, bit_depth):

    if dp_length + hwdp_length < pbr and bit_depth > pbr:
        dc_liner_vol = (liner_cap - dc_ce_cap) * (bit_depth - pbr)

    elif (dp_length + hwdp_length > pbr and dp_length + hwdp_length < liner_shoe and
bit_depth <= liner_shoe):
        dc_liner_vol = (liner_cap - dc_ce_cap) * dc_length

    elif dp_length + hwdp_length < liner_shoe and bit_depth > liner_shoe:
        dc_liner_vol = (liner_cap - dc_ce_cap) * (liner_shoe - (dp_length + hwdp_length))

    else:
        dc_liner_vol = 0

    print 'DC/Liner = ' + str(dc_liner_vol)
    return dc_liner_vol