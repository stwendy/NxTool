# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:28:16 2018

@author: czhen
"""


import math

def Dbm_To_Power():
    dbm = float(input("Please input power in dBm(dBm):"))
    p = math.pow(10,dbm/10)
    print("The result is %f mW" % p)

def Power_To_Dbm():
    p = float(input("Please input power(mW):"))
    dbm = 10*math.log10(p/1)
    print("The result is %f dBm" % dbm)

def Free_Space_Loss():
    d = float(input("Please input distance(m):"))
    f = float(input("Please input frequency(MHz):"))
    loss = 20*math.log10(4*math.pi*d*f*1000000/299792458)
    print("The result is %f dB" % loss)

def RC_Parallel_Impedance():
    r = float(input("Please input parallel resistance(ohm):"))
    c = float(input("Please input parallel capacitance(pF):"))
    f = float(input("Please input frequency(MHz):"))
    jwc = complex(0,1)*math.pi*2*f*1e6*c/1e12
    complex_im = r*(1/jwc)/(r+1/jwc)
    print("The result is %r" % complex_im)

def Wavelengh():
    f = float(input("Please input frequency(MHz):"))
    wl = 299792458/(f*1e6)
    half_wl = wl/2
    q_wl = wl/4
    print("The result wavelenth is %f m" % wl)
    print("The result wavelength/2 is %f m" % half_wl)
    print("The result wavelength/4 is %f m" % q_wl)

def dB_to_Ratio():
    db = float(input("Please input db(dB):"))
    ratio = math.pow(10,db/10)
    print("The result is %f" % ratio)

def Ratio_to_dB():
    ratio = float(input("Please input ratio:"))
    db = 10*math.log10(ratio)
    print("The result is %f dB" % db)

def ToT():
    f = float(input("Please input frequency(MHz):"))
    Pr_dbm = float(input("Please input reader's transmit power(dBm):"))
    Pr = math.pow(10,Pr_dbm/10)/1000
    Gr_db = float(input("Please input reader's antenna gain(dB):"))
    Gr = math.pow(10,Gr_db/10)
    Gt_db = float(input("Please input tag's antenna gain(dB):"))
    Gt = math.pow(10,Gt_db/10)
    r = float(input("Please input distance between reader and tag(m):"))
    polar = float(input("Please input polarization coefficient(0 to 1) of reader's antenna and tag's:"))
    wl = 299792458/(f*1e6)
    tot_w = Pr*Gr/(4*math.pi*r*r)*wl*wl/(4*math.pi)*Gt*polar
    tot_dbm = 10*math.log10(tot_w*1000/1)
    print("The result is %f dBm" % tot_dbm)

def BS():
    f = float(input("Please input frequency(MHz):"))
    tot_db = float(input("Please input tag's ToT power(dBm):"))
    tot = math.pow(10,tot_db/10)/1000
    bs_ratio = float(input("Please input tag's BS coefficient(0 to 1):"))
    Gr_db = float(input("Please input reader's antenna gain(dB):"))
    Gr = math.pow(10,Gr_db/10)
    r = float(input("Please input distance between reader and tag(m):"))
    polar = float(input("Please input polarization coefficient(0 to 1) of reader's antenna and tag's:"))
    wl = 299792458/(f*1e6)
    bs_w = tot/(4*math.pi*r*r)*wl*wl/(4*math.pi)*Gr*polar*bs_ratio
    bs_dbm = 10*math.log10(bs_w*1000/1)
    print("The result is %f dBm" % bs_dbm)

def Forward_vs_Reverse():
    reader_sense = float(input("Please input reader's sensitivity(dBm):"))
    tag_sense = float(input("Please input tag's sensitivity(dBm):"))
    f = float(input("Please input frequency(MHz):"))
    wl = 299792458/(f*1e6)
    Pr_dbm = float(input("Please input reader's transmit power(dBm):"))
    # convert dbm to Watt
    Pr = math.pow(10,Pr_dbm/10)/1000
    Gr_db = float(input("Please input reader's antenna gain(dB):"))
    # convert db to ratio
    Gr = math.pow(10,Gr_db/10)
    Gt_db = float(input("Please input tag's antenna gain(dB):"))
    # convert db to ratio
    Gt = math.pow(10,Gt_db/10)
    r = float(input("Please input distance between reader and tag(m):"))
    polar = float(input("Please input polarization coefficient(0 to 1) of reader's antenna and tag's:"))
    bs_ratio = float(input("Please input tag's BS coefficient(0 to 1):"))
    # calc tot power
    tot_w = Pr*Gr/(4*math.pi*r*r)*wl*wl/(4*math.pi)*Gt*polar
    tot_dbm = 10*math.log10(tot_w*1000/1)
    print("The ToT power is %f dBm" % tot_dbm)
    # calc bs power
    bs_w = tot_w/(4*math.pi*r*r)*wl*wl/(4*math.pi)*Gr*polar*bs_ratio
    bs_dbm = 10*math.log10(bs_w*1000/1)
    print("The BS power is %f dBm" % bs_dbm)
    if tot_dbm <= tag_sense:
        print("Forward Limited!")
    elif bs_dbm <= reader_sense:
        print("Reverse Limited!")
    else:
        print("No Limit!")

def Gain_to_Range():
    f = float(input("Please input frequency(MHz):"))
    wl = 299792458/(f*1e6)
    Pr_dbm = float(input("Please input reader's transmit power(dBm):"))
    # convert dbm to Watt
    Pr = math.pow(10,Pr_dbm/10)/1000
    Gr_db = float(input("Please input reader's antenna gain(dB):"))
    # convert db to ratio
    Gr = math.pow(10,Gr_db/10)
    Gt_db = float(input("Please input tag's antenna gain(dB):"))
    # convert db to ratio
    Gt = math.pow(10,Gt_db/10)
    tag_sense = float(input("Please input tag's sensitivity(dBm):"))
    tag_s = math.pow(10,tag_sense/10)/1000
    polar = float(input("Please input polarization coefficient(0 to 1) of reader's antenna and tag's:"))
    # power transfer coefficient
    pt_coe = float(input("Please input tag's power transfer coefficient(<1):"))
    # calc range
    r = wl/(4*math.pi)*math.sqrt(Pr*Gr*Gt*polar*pt_coe/tag_s)
    print("The Range is %f m" % r)
    
def RL_to_VSWR():
    return_loss = float(input("Please input return loss(dB):"))
    reflect_coef_amp = pow(10,return_loss/-20)
    vswr = (1+reflect_coef_amp)/(1-reflect_coef_amp)
    print("The VSWR is %f" % vswr)
    print("The reflected power is %f" % pow(reflect_coef_amp,2)) 

def VSWR_to_RL():
    vswr = float(input("Please input VSWR:"))
    reflect_coef_amp = (vswr-1)/(vswr+1)
    return_loss = -20*math.log10(abs(reflect_coef_amp))
    print("The Return Loss is %f" % return_loss)
    print("The reflected power is %f" % pow(reflect_coef_amp,2)) 
    
def Read_Range_Forward():
    p_tx_dbm = float(input("Please input Reader's Transmit Power(EIRP,dBm):"))
    p_tag_dbm = float(input("Please input Tag's Sensitivity(dBm):"))
    freq = float(input("Please input Frequency(MHz):"))
    p_tx = math.pow(10,p_tx_dbm/10)
    p_tag = math.pow(10,p_tag_dbm/10)
    forward_range = math.sqrt(p_tx/p_tag)*299792458/(4*math.pi*freq*1e6)
    print("The Read Range is %f m" % forward_range)
    
def Read_Range_Reverse():
    p_bs_dbm = float(input("Please input Tag's backscratter Power(dBm):"))
    p_reader_dbm = float(input("Please input Reader's Sensitivity(dBm):"))
    freq = float(input("Please input Frequency(MHz):"))
    p_bs = math.pow(10,p_bs_dbm/10)
    p_reader = math.pow(10,p_reader_dbm/10)
    reverse_range = math.sqrt(p_bs/p_reader)*299792458/(4*math.pi*freq*1e6)
    print("The Read Range is %f m" % reverse_range)
    
def Coversion_Forward_Range_and_TxPower():
    p_tx_dbm = float(input("Please input Reader's Reference Transmit Power(dBm):"))
    forward_range = float(input("Please input Reference Forward Read Range(m):"))
    freq = float(input("Please input Frequency(MHz):"))
    p_target_dbm = float(input("Please input Reader's Target Transmit Power(dBm):"))
    p_tx = math.pow(10,p_tx_dbm/10)
    p_target = math.pow(10,p_target_dbm/10)
    p_tag = p_tx/math.pow((forward_range * (4*math.pi*freq*1e6)/299792458),2)
    p_tag_dbm = 10*math.log10(p_tag/1)
    print("The tag's Sensitivity  is %f" % p_tag_dbm)
    conv_forward_range = math.sqrt(p_target/p_tag)*299792458/(4*math.pi*freq*1e6)
    print("The Conversion Forward Read Range is %f m" % conv_forward_range)   

def Coversion_Reverse_Range_and_BsRSSI():
    p_rssi_dbm = float(input("Please input Reader's Reference Tag's RSSI(dBm):"))
    reverse_range = float(input("Please input Reference Reverse Read Range(m):"))
    freq = float(input("Please input Frequency(MHz):"))
    p_rx_limit_dbm = float(input("Please input Reader's Target Senstivity Limit(RSSI limit,dBm):"))
    free_space_loss = 20*math.log10(4*math.pi*reverse_range*freq*1000000/299792458)  
    p_bs = free_space_loss + p_rssi_dbm
    print("The tag's Backscratter power is %f dBm" % p_bs)    
    target_loss = p_bs - p_rx_limit_dbm
    target_range = 299792458/(4*math.pi*freq*1e6) * math.pow(10,(target_loss/20)) 
    print("The Conversion Reverse Read Range is %f m" % target_range) 

def Free_Space_Loss_To_Range():
    fpl = float(input("Please input Free Space Loss(dB):"))
    freq = float(input("Please input frequency(MHz):"))
    target_range = 299792458/(4*math.pi*freq*1e6) * math.pow(10,(fpl/20)) 
    print("The Range is %f m" % target_range)
    
switcher = {
    0: Dbm_To_Power,
    1: Power_To_Dbm,
    2: Free_Space_Loss,
    3: RC_Parallel_Impedance,
    4: Wavelengh,
    5: ToT,
    6: BS,
    7: dB_to_Ratio,
    8: Ratio_to_dB,
    9: Forward_vs_Reverse,
    10: Gain_to_Range,
    11: RL_to_VSWR,
    12: VSWR_to_RL,
    13: Read_Range_Forward,
    14: Read_Range_Reverse,
    15: Coversion_Forward_Range_and_TxPower,
    16: Coversion_Reverse_Range_and_BsRSSI,
    17: Free_Space_Loss_To_Range
}

while True:
    print("""
    =============Welcome===============
    0: dBm to Power
    1: Power to dBm
    2: Free Space Loss
    3: RC Parallel Impedance
    4: Wavelengh
    5: TOT(Turn‐on‐Threshold) power received by tag when reader -> tag
    6: BS(Back‐scatter radiation) power received by reader when tag -> reader
    7: dB to Ratio
    8: Ratio to dB
    9: Forward vs Reverse
    10：Gain to Range
    11: Return Loss to VSWR
    12: VSWR to Return Loss
    13: Read Range Forward
    14: Read Range Reverse
    15: Coversion Forward_Range and TxPower
    16: Coversion Reverse Range and BsRSSI
    17: Free Space Loss To Range
    99:Exit
    """)
    i = int(input("Please input the number:"))
    if i == 99:
        break
    else:
        func = switcher.get(i)
        func()


print("Goodbye...")