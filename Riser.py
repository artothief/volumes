__author__ = 'artothief'

#Pipe / Riser volume
def dp_riser(seabed, riser_cap, dp_length, dp_ce_cap):

    if dp_length >= seabed:
        riser_dp_vol = (riser_cap - dp_ce_cap) * seabed

    elif dp_length < seabed and dp_length > 0:
        riser_dp_vol = (riser_cap - dp_ce_cap) * dp_length

    else:
        riser_dp_vol = 0

    return riser_dp_vol

# HWDP / Riser volume
def hwdp_riser(seabed, riser_cap, dp_length, hwdp_length, hwdp_ce_cap):

    if dp_length >= seabed:
        riser_hwdp_vol = 0

    elif dp_length < seabed and dp_length + hwdp_length > seabed:
        riser_hwdp_vol = (riser_cap - hwdp_ce_cap) * (seabed - dp_length)

    else:
        riser_hwdp_vol = (riser_cap - hwdp_ce_cap) * hwdp_length

    return riser_hwdp_vol

# DC / Riser volume
def dc_riser(seabed, riser_cap, dp_length, hwdp_length, dc_ce_cap, bit_depth):

    if bit_depth <= seabed:
        riser_dc_vol = (riser_cap - dc_ce_cap) * (bit_depth - (hwdp_length + dp_length))

    elif dp_length + hwdp_length < seabed and bit_depth > seabed:
        riser_dc_vol = (riser_cap - dc_ce_cap) * (seabed - (dp_length + hwdp_length))

    else:
        riser_dc_vol = 0

    return riser_dc_vol