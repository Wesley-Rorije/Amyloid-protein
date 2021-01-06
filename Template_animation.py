#!/usr/bin/env python3

"""
Template for the final movie design
"""

__author__ = 'J.A. Busker W.A. Rorije'

from pypovray import pypovray, models, SETTINGS, pdb
from vapory import *
from shapes import static_objects
import numpy as np

CAMERA = LIGHT = BETA4 = INTER = JULIA = NFRAMES = None

# calculating the number of frames to percentage of the video
NFRAMES = eval(pypovray.SETTINGS.NumberFrames)
first_sec = int(NFRAMES * 0.2)
end_second_sec = int(NFRAMES * 0.6)
last_sec = int(NFRAMES * 0.8)
standard_frames = first_sec / 2


def molecules():
    """ fuction for only reading pdb file amyloid once instead of every frame"""
    global beta4

    beta4 = pdb.PDBMolecule('{}/pdb/beta4.pdb'.format(SETTINGS.AppLocation), center=False, offset=[0, 5, 35])


def frame(step):
    """Creates molecules and other shapes and move them around"""
    CAMERA, LIGHT, INTER, sect = static_objects()

    # makings list to store the objects
    TEXT = []
    BETA4 = []
    NEURO = []
    JULIA = []

    # Ion radius of neurons
    radius = 0.8

    # Natrium calc
    na_y_start = 20
    na_y_end = 6
    na_y_dis = na_y_end - na_y_start
    na_dis_frame = na_y_dis / standard_frames

    # Calcium calc
    ca_x_start = -10
    ca_y_start = 10
    ca_x_end = -1
    ca_y_end = 3.5
    ca_x_dis = ca_x_end - ca_x_start
    ca_y_dis = ca_y_end - ca_y_start
    ca_x_dis_frame = ca_x_dis / standard_frames
    ca_y_dis_frame = ca_y_dis / standard_frames

    # Channel calcium calculation
    ccal_y_start = 5
    ccal_y_start1 = 3.8
    ccal_y_end = 6.5
    ccal_y_end1 = 2.3
    ccal_dis = ccal_y_end - ccal_y_start
    ccal_dis1 = ccal_y_end1 - ccal_y_start1
    ccal_dis_frame = ccal_dis / standard_frames
    ccal_dis_frame1 = ccal_dis1 / standard_frames

    # Potassium distance calculation
    ka_x_start = -1
    ka_x_end = -7
    ka_y_start = -9
    ka_y_end = -4
    ka_x_dis = ka_x_end - ka_x_start
    ka_y_dis = ka_y_end - ka_y_start
    ka_x_dis_frame = ka_x_dis / standard_frames
    ka_y_dis_frame = ka_y_dis / standard_frames

    # Neurons distance calculation
    neu_x_start = 1
    neu_x_end = 5
    neu_y_start = 1
    neu_y_end = -3
    neu_y_dis_frame = (neu_y_end - neu_y_start) / standard_frames
    neu_x_dis_frame = (neu_x_end - neu_x_start) / standard_frames

    # Neurotransmitter the green membrane around neurons distance calculation
    tra_x_start = 0.75
    tra_x_end = 4.75
    tra_y_start = 0.75
    tra_y_end = -2.75
    tra_x_dis_frame = (tra_x_end - tra_x_start) / standard_frames
    tra_y_dis_frame = (tra_y_end - tra_y_start) / standard_frames

    # Second bottom natrium ion distance calculation
    n2_x_start = 8
    n2_x_end = 1
    n2_y_start = -2
    n2_y_end = -10
    n2_x_dis = n2_x_end - n2_x_start
    n2_y_dis = n2_y_end - n2_y_start

    # Natrium channel distance calculation
    cna_y_start = -7
    cna_y_start1 = -8.2
    cna_y_end = -5.5
    cna_y_end1 = -9.7
    cna_dis = cna_y_end - cna_y_start
    cna_dis1 = cna_y_end1 - cna_y_start1
    cna_dis_frame = cna_dis / standard_frames
    cna_dis_frame1 = cna_dis1 / standard_frames

    # Potassium channel distance calculation
    cka_y_start = -7
    cka_y_start1 = -8.2
    cka_y_end = -5.5
    cka_y_end1 = -9.7
    cka_dis = cka_y_end - cka_y_start
    cka_dis1 = cka_y_end1 - cka_y_start1
    cka_dis_frame = cka_dis / standard_frames
    cka_dis_frame1 = cka_dis1 / standard_frames

    # Neurotransmitters  travelling to Potassium channel distance calculation
    neuro_natrium_x_dis = -3 - tra_x_end - 1.25
    neuro_natrium_y_dis = cka_y_start - tra_y_end + 0.5
    neuro_natrium_x_dis1 = -3.5 - tra_x_end - 1.25
    neuro_natrium_y_dis1 = (cka_y_start1 + 1.25) - tra_y_end

    neuro_nat_x_dis_frame = neuro_natrium_x_dis / standard_frames
    neuro_nat_y_dis_frame = neuro_natrium_y_dis / standard_frames
    neuro_nat_x_dis_frame1 = neuro_natrium_x_dis1 / standard_frames
    neuro_nat_y_dis_frame1 = neuro_natrium_y_dis1 / standard_frames

    # Neurotransmitters travelling to sodium channel distance calculation
    neuro_natrium_x_dis2 = 3 - tra_x_end + 0.5
    neuro_natrium_y_dis2 = cna_y_start - tra_y_end + 0.5
    neuro_natrium_x_dis3 = 3.5 - tra_x_end + 0.5
    neuro_natrium_y_dis3 = cna_y_start1 - tra_y_end + 1.25

    neuro_nat_x_dis_frame2 = neuro_natrium_x_dis2 / standard_frames
    neuro_nat_y_dis_frame2 = neuro_natrium_y_dis2 / standard_frames
    neuro_nat_x_dis_frame3 = neuro_natrium_x_dis3 / standard_frames
    neuro_nat_y_dis_frame3 = neuro_natrium_y_dis3 / standard_frames

    # creation of cylinders for membrame
    cyl3 = Cylinder([neu_x_start, neu_y_start, -2], [neu_x_start, neu_y_start, 0], 1.5, Pigment('color', 'Green'))
    cyl4 = Cylinder([neu_x_start, neu_y_start, -10], [neu_x_start, neu_y_start, 10], 1, Pigment('color', 'Green'))

    # start of the first section
    if step < first_sec:

        # Sodium channel
        channelna = Cylinder([3, cna_y_start, -2], [5, cna_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelna2 = Cylinder([3.5, cna_y_start1, -2], [5.5, cna_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        # Potassium channel
        channelka = Cylinder([-3, cka_y_start, -2], [-5, cka_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelka2 = Cylinder([-3.5, cka_y_start1, -2], [-5.5, cka_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        # travelling neurons
        neuro = Sphere([tra_x_start, tra_y_start + 0.5, -2], 0.2, Pigment('color', 'Pink'))
        neuro1 = Sphere([tra_x_start, tra_y_start, -2], 0.2, Pigment('color', 'Pink'))
        neuro2 = Sphere([tra_x_start + 0.5, tra_y_start + 0.5, -2], 0.2, Pigment('color', 'Pink'))
        neuro3 = Sphere([tra_x_start + 0.5, tra_y_start, -2], 0.2, Pigment('color', 'Pink'))
        NEURO = [neuro, neuro1, neuro2, neuro3]

        # second natrium ion
        second_natrium = Sphere([n2_x_start, n2_y_start, -2], radius, Pigment('color', 'Red'))

        # with Difference we shape out a round hole to look like a membrane
        DIFF = [Difference(cyl3, cyl4), Difference(sect, cyl4)]

        kalium = Sphere([ka_x_start, ka_y_start, -2], radius, Pigment('color', 'Magenta'))

        # splitting the first 20 percent in 2 parts
        if step < standard_frames:
            na_y_coord = na_y_start + step * na_dis_frame

            natrium = Sphere([0, na_y_coord, -2], radius, Pigment('color', 'Red'))

            calcium = Sphere([ca_x_start, ca_y_start, -2], radius, Pigment('color', 'White'))

            channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                                   Pigment('color', 'Blue'))

        # second 10 percent of 20
        else:
            natrium = Sphere([0, na_y_end, -2], radius, Pigment('color', 'Red'))

            ca_x_coord = ca_x_start + (step - standard_frames) * ca_x_dis_frame
            ca_y_coord = ca_y_start + (step - standard_frames) * ca_y_dis_frame
            calcium = Sphere([ca_x_coord, ca_y_coord, -2], radius, Pigment('color', 'White'))

            cal_y_coord = ccal_y_start + (step - standard_frames) * ccal_dis_frame
            cal_y_coord1 = ccal_y_start1 + (step - standard_frames) * ccal_dis_frame1

            channelcal = cyl1 = Cylinder([-3, cal_y_coord, -2], [-5, cal_y_coord + 2.5, -2], 0.5,
                                         Pigment('color', 'Blue'))
            channelcal2 = cyl1 = Cylinder([-3.5, cal_y_coord1, -2], [-5.5, cal_y_coord1 + 2.5, -2], 0.5,
                                          Pigment('color', 'Blue'))
    # second section
    if step > (first_sec - 1) and step < end_second_sec:
        calcium = Sphere([ca_x_end, ca_y_end, -2], radius, Pigment('color', 'White'))
        natrium = Sphere([0, na_y_end, -2], radius, Pigment('color', 'Red'))

        # first 10 %
        if step > first_sec - 1 and step < (first_sec + standard_frames):
            # natrium channel
            channelna = Cylinder([3, cna_y_start, -2], [5, cna_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelna2 = Cylinder([3.5, cna_y_start1, -2], [5.5, cna_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

            # kalium channel
            channelka = Cylinder([-3, cka_y_start, -2], [-5, cka_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelka2 = Cylinder([-3.5, cka_y_start1, -2], [-5.5, cka_y_start1 + 2.5, -2], 0.5,
                                  Pigment('color', 'Blue'))

            ccal_dis_frame = ccal_dis / standard_frames
            ccal_dis_frame1 = ccal_dis1 / standard_frames

            second_natrium = Sphere([n2_x_start, n2_y_start, -2], radius, Pigment('color', 'Red'))

            kalium = Sphere([ka_x_start, ka_y_start, -2], radius, Pigment('color', 'Magenta'))

            cal_y_coord = ccal_y_end + (step - first_sec) * (ccal_dis_frame * -1)
            cal_y_coord1 = ccal_y_end1 + (step - first_sec) * (ccal_dis_frame1 * -1)

            channelcal = Cylinder([-3, cal_y_coord, -2], [-5, cal_y_coord + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelcal2 = Cylinder([-3.5, cal_y_coord1, -2], [-5.5, cal_y_coord1 + 2.5, -2], 0.5,
                                   Pigment('color', 'Blue'))

            neu_y_coord = neu_y_start + (step - first_sec) * neu_y_dis_frame
            neu_x_coord = neu_x_start + (step - first_sec) * neu_x_dis_frame

            # z-as veranderd
            cyl3 = Cylinder([neu_x_coord, neu_y_coord, -2], [neu_x_coord, neu_y_coord, 0], 1.5,
                            Pigment('color', 'Green'))
            cyl4 = Cylinder([neu_x_coord, neu_y_coord, -10], [neu_x_coord, neu_y_coord, 10], 1,
                            Pigment('color', 'Green'))

            DIFF = [Difference(cyl3, cyl4), Difference(sect, cyl4)]

            tra_y_coord = tra_y_start + (step - first_sec) * tra_y_dis_frame
            tra_x_coord = tra_x_start + (step - first_sec) * tra_x_dis_frame

            neuro = Sphere([tra_x_coord, tra_y_coord + 0.5, -2], 0.2, Pigment('color', 'Pink'))
            neuro1 = Sphere([tra_x_coord, tra_y_coord, -2], 0.2, Pigment('color', 'Pink'))
            neuro2 = Sphere([tra_x_coord + 0.5, tra_y_coord + 0.5, -2], 0.2, Pigment('color', 'Pink'))
            neuro3 = Sphere([tra_x_coord + 0.5, tra_y_coord, -2], 0.2, Pigment('color', 'Pink'))

            NEURO = [neuro, neuro1, neuro2, neuro3]
        # second 10 percent
        if step > (first_sec + standard_frames - 1) and step < (first_sec + (standard_frames * 2)):
            channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                                   Pigment('color', 'Blue'))
            # CHANNELS = [channel, channel1]

            channelna = Cylinder([3, cna_y_start, -2], [5, cna_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelna2 = Cylinder([3.5, cna_y_start1, -2], [5.5, cna_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

            channelka = Cylinder([-3, cka_y_start, -2], [-5, cka_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelka2 = Cylinder([-3.5, cka_y_start1, -2], [-5.5, cka_y_start1 + 2.5, -2], 0.5,
                                  Pigment('color', 'Blue'))

            # secoind natrium ion
            second_natrium = Sphere([n2_x_start, n2_y_start, -2], radius, Pigment('color', 'Red'))

            # kalium
            kalium = Sphere([ka_x_start, ka_y_start, -2], radius, Pigment('color', 'Magenta'))

            # 2 neurotransmitters die naar het kalium kanaal gaan
            neuro_nat_x_coord = tra_x_end + (step - (first_sec + standard_frames)) * neuro_nat_x_dis_frame
            neuro_nat_y_coord = tra_y_end + 0.5 + (step - (first_sec + standard_frames)) * neuro_nat_y_dis_frame
            neuro_nat_x_coord1 = tra_x_end + (step - (first_sec + standard_frames)) * neuro_nat_x_dis_frame1
            neuro_nat_y_coord1 = tra_y_end + (step - (first_sec + standard_frames)) * neuro_nat_y_dis_frame1

            neuro = Sphere([neuro_nat_x_coord, neuro_nat_y_coord + 0.5, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro1 = Sphere([neuro_nat_x_coord1, neuro_nat_y_coord1, -2.5], 0.2, Pigment('color', 'Pink'))

            # 2 neurotransmitters die naar het natrium kanaal gaan
            neuro_nat_x_coord2 = tra_x_end + 0.5 + (step - (first_sec + standard_frames)) * neuro_nat_x_dis_frame2
            neuro_nat_y_coord2 = tra_y_end + 0.5 + (step - (first_sec + standard_frames)) * neuro_nat_y_dis_frame2
            neuro_nat_x_coord3 = tra_x_end + 0.5 + (step - (first_sec + standard_frames)) * neuro_nat_x_dis_frame3
            neuro_nat_y_coord3 = tra_y_end + (step - (first_sec + standard_frames)) * neuro_nat_y_dis_frame3

            # z-as veranderd
            neuro2 = Sphere([neuro_nat_x_coord2, neuro_nat_y_coord2, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro3 = Sphere([neuro_nat_x_coord3, neuro_nat_y_coord3, -2.5], 0.2, Pigment('color', 'Pink'))

            NEURO = [neuro, neuro1, neuro2, neuro3]
            DIFF = [sect]
        # third 10 %
        if step > ((first_sec + standard_frames * 2) - 1) and step < (first_sec + (standard_frames * 3)):
            channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                                   Pigment('color', 'Blue'))

            ka_x_coord = ka_x_start + (step - ((first_sec + standard_frames * 2))) * ka_x_dis_frame
            ka_y_coord = ka_y_start + (step - ((first_sec + standard_frames * 2))) * ka_y_dis_frame

            kalium = Sphere([ka_x_coord, ka_y_coord, -2], radius, Pigment('color', 'Magenta'))
            # KALIUM = [kalium]

            n2_x_dis_frame = n2_x_dis / standard_frames
            n2_y_dis_frame = n2_y_dis / standard_frames

            n2_x_coord = n2_x_start + (step - ((first_sec + standard_frames * 2))) * n2_x_dis_frame
            n2_y_coord = n2_y_start + (step - ((first_sec + standard_frames * 2))) * n2_y_dis_frame

            # Second natrium ion
            second_natrium = Sphere([n2_x_coord, n2_y_coord, -2], radius, Pigment('color', 'Red'))

            # Natrium channel
            cna_y_coord = cna_y_start + (step - ((first_sec + standard_frames * 2))) * cna_dis_frame
            cna_y_coord1 = cna_y_start1 + (step - ((first_sec + standard_frames * 2))) * cna_dis_frame1

            channelna = Cylinder([3, cna_y_coord, -2], [5, cna_y_coord + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelna2 = Cylinder([3.5, cna_y_coord1, -2], [5.5, cna_y_coord1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

            # Kalium channel
            cka_sec_y_coord = cka_y_start + (step - ((first_sec + standard_frames * 2))) * cka_dis_frame
            cka_sec_y_coord1 = cka_y_start1 + (step - ((first_sec + standard_frames * 2))) * cka_dis_frame1

            channelka = Cylinder([-3, cka_sec_y_coord, -2], [-5, cka_sec_y_coord + 2.5, -2], 0.5,
                                 Pigment('color', 'Blue'))
            channelka2 = Cylinder([-3.5, cka_sec_y_coord1, -2], [-5.5, cka_sec_y_coord1 + 2.5, -2], 0.5,
                                  Pigment('color', 'Blue'))

            # Neurotransmitters op het kalium kanaal
            neuro = Sphere([-4, cka_sec_y_coord + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro1 = Sphere([-4.5, cka_sec_y_coord1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))

            # Neurotransmitters op natrium kanaal
            neuro2 = Sphere([4, cna_y_coord + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro3 = Sphere([4.5, cna_y_coord1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))

            NEURO = [neuro, neuro1, neuro2, neuro3]
            DIFF = [sect]
        # last 10 percent
        if step > (first_sec + (standard_frames * 3) - 1):
            # ionen
            calcium = Sphere([ca_x_end, ca_y_end, -2], radius, Pigment('color', 'White'))
            natrium = Sphere([0, na_y_end, -2], radius, Pigment('color', 'Red'))
            second_natrium = Sphere([n2_x_end, n2_y_end, -2], radius, Pigment('color', 'Red'))

            kalium = Sphere([ka_x_end, ka_y_end, -2], radius, Pigment('color', 'Magenta'))

            # Calcium kanalen
            channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                                   Pigment('color', 'Blue'))

            # kalium kanalen
            cka_sec_y_coord = cka_y_end + (step - ((first_sec + standard_frames * 3))) * cka_dis_frame * -1
            cka_sec_y_coord1 = cka_y_end1 + (step - ((first_sec + standard_frames * 3))) * cka_dis_frame

            channelka = Cylinder([-3, cka_sec_y_coord, -2], [-5, cka_sec_y_coord + 2.5, -2], 0.5,
                                 Pigment('color', 'Blue'))
            channelka2 = Cylinder([-3.5, cka_sec_y_coord1, -2], [-5.5, cka_sec_y_coord1 + 2.5, -2], 0.5,
                                  Pigment('color', 'Blue'))

            # natrium kanalen
            cna_y_coord = cna_y_end + (step - ((first_sec + standard_frames * 3))) * cna_dis_frame * -1
            cna_y_coord1 = cna_y_end1 + (step - ((first_sec + standard_frames * 3))) * cna_dis_frame1 * -1

            channelna = Cylinder([3, cna_y_coord, -2], [5, cna_y_coord + 2.5, -2], 0.5, Pigment('color', 'Blue'))
            channelna2 = Cylinder([3.5, cna_y_coord1, -2], [5.5, cna_y_coord1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

            # neurotransmitters
            neuro = Sphere([-4, cka_sec_y_coord + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro1 = Sphere([-4.5, cka_sec_y_coord1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro2 = Sphere([4, cna_y_coord + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
            neuro3 = Sphere([4.5, cna_y_coord1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))

            NEURO = [neuro, neuro1, neuro2, neuro3]
            DIFF = [sect]
    # third section of simulation
    if step > (end_second_sec - 1) and step < (end_second_sec + standard_frames):
        # Ionen
        calcium = Sphere([ca_x_end, ca_y_end, -2], radius, Pigment('color', 'White'))
        natrium = Sphere([0, na_y_end, -2], radius, Pigment('color', 'Red'))
        second_natrium = Sphere([n2_x_end, n2_y_end, -2], radius, Pigment('color', 'Red'))
        kalium = Sphere([ka_x_end, ka_y_end, -2], radius, Pigment('color', 'Magenta'))

        # Kanalen
        channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                               Pigment('color', 'Blue'))

        channelna = Cylinder([3, cna_y_start, -2], [5, cna_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelna2 = Cylinder([3.5, cna_y_start1, -2], [5.5, cna_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        channelka = Cylinder([-3, cka_y_start, -2], [-5, cka_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelka2 = Cylinder([-3.5, cka_y_start1, -2], [-5.5, cka_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        # Neurotransmitters
        neuro = Sphere([-4, cka_y_start + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro1 = Sphere([-4.5, cka_y_start1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro2 = Sphere([4, cna_y_start + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro3 = Sphere([4.5, cna_y_start1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))

        NEURO = [neuro, neuro1, neuro2, neuro3]
        DIFF = [sect]
    # last section also known as section 4
    if step > (end_second_sec + standard_frames - 1) and step < last_sec:
        # Ionen en kanalen
        calcium = natrium = second_natrium = kalium = channelcal \
            = channelcal2 = channelna = channelna2 = channelka = channelka2 = ''

        # Neurotransmitters
        neuro = Sphere([-4, cka_y_start + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro1 = Sphere([-4.5, cka_y_start1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro2 = Sphere([4, cna_y_start + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))
        neuro3 = Sphere([4.5, cna_y_start1 + 1.25, -2.5], 0.2, Pigment('color', 'Pink'))

        NEURO = []
        DIFF = []
        INTER = []

        TEXT = [Text('ttf', '"timrom.ttf"', '"Het amyloide eiwit!"', 1, 0, 'translate', [-4, -2, -15],
                     Pigment('color', 'Red'))]

        BETA4 = beta4.povray_molecule

    # after showing amyloid protein we return all objects to original places with julia fractors in the center
    if step > (last_sec - 1):
        TEXT = [Text('ttf', '"timrom.ttf"', '"amyloide eiwit"', 0.25, 0, 'translate', [-3.2, -1.8, -15],
                     Pigment('color', 'White'))]
        BETA4 = []

        # Ionen
        calcium = Sphere([ca_x_start, ca_y_start, -2], radius, Pigment('color', 'White'))
        natrium = Sphere([0, na_y_start, -2], radius, Pigment('color', 'Red'))
        second_natrium = Sphere([n2_x_start, n2_y_start, -2], radius, Pigment('color', 'Red'))
        kalium = Sphere([ka_x_start, ka_y_start, -2], radius, Pigment('color', 'Magenta'))

        # channels
        channelcal = Cylinder([-3, ccal_y_start, -2], [-5, ccal_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelcal2 = Cylinder([-3.5, ccal_y_start1, -2], [-5.5, ccal_y_start1 + 2.5, -2], 0.5,
                               Pigment('color', 'Blue'))

        channelna = Cylinder([3, cna_y_start, -2], [5, cna_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelna2 = Cylinder([3.5, cna_y_start1, -2], [5.5, cna_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        channelka = Cylinder([-3, cka_y_start, -2], [-5, cka_y_start + 2.5, -2], 0.5, Pigment('color', 'Blue'))
        channelka2 = Cylinder([-3.5, cka_y_start1, -2], [-5.5, cka_y_start1 + 2.5, -2], 0.5, Pigment('color', 'Blue'))

        # Neurotransmitters
        neuro = Sphere([tra_x_start, tra_y_start + 0.5, -2], 0.2, Pigment('color', 'Pink'))
        neuro1 = Sphere([tra_x_start, tra_y_start, -2], 0.2, Pigment('color', 'Pink'))
        neuro2 = Sphere([tra_x_start + 0.5, tra_y_start + 0.5, -2], 0.2, Pigment('color', 'Pink'))
        neuro3 = Sphere([tra_x_start + 0.5, tra_y_start, -2], 0.2, Pigment('color', 'Pink'))
        NEURO = [neuro, neuro1, neuro2, neuro3]

        # calculated shaped out hole
        DIFF = [Difference(cyl3, cyl4), Difference(sect, cyl4)]

        number_julia = 8
        JULIA = []
        # append 8 julia fractors for simulation object
        for i in range(1, number_julia + 1):
            if i % 2 == 0:
                y = -3.3
            else:
                y = -2.7
            JULIA.append(
                JuliaFractal([0.083, 0.0, -0.83, -0.025], 'max_iteration', 8, 'precision', 20, Pigment('color', 'Red'),
                             'scale', 0.8,
                             'translate', [-7 + (i * 1.5), y, 0]))

    return Scene(CAMERA,
                 objects=[natrium, second_natrium, calcium, kalium, channelcal, channelcal2, channelna, channelna2,
                          channelka, channelka2]
                         + LIGHT + TEXT + BETA4 + DIFF + NEURO + INTER + JULIA, included=['colors.inc'])


if __name__ == '__main__':
    molecules()
    pypovray.render_scene_to_mp4(frame)
