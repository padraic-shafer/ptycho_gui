import os
import numpy as np


def get_working_directory():
    config_path = os.path.expanduser("~") + "/.ptycho_gui_config"
    working_dir = ''
    try:
        with open(config_path, "r") as config:
            while True:
                line = config.readline()
                if line == '':
                    raise Exception("working_directory not found, abort!")
                line = line.split()
                if line[0] == "working_directory":
                    working_dir = line[2] 
                    break
    except FileNotFoundError:
        working_dir = os.path.expanduser("~") # default to user's home
    return working_dir


class Param(object):
    """
    ptychography reconstruction parameters
    """
    def __init__(self):
        # from recon_ptycho.py
        # organized by grouping in GUI

        ### [Data] ###
        self.scan_num = '34784'       # scan number
        self.working_directory = get_working_directory()
        self.detectorkind = 'merlin1' # ['merlin1', 'merlin2', 'timepix1', 'timepix2']
        self.frame_num = 0            # frame number to check

        ### [Experimental parameters] ###
        self.xray_energy_kev = 0. # =1.2398/lambda_nm
        self.z_m = 0.             # detector_distance
        self.nx = 0               # x_arr_size
        self.dr_x = 0.            # x_step_size
        self.x_range = 0.
        self.ny = 0               # y_arr_size
        self.dr_y = 0.            # y_step_size
        self.y_range = 0.
        self.scan_type = 'mesh'   # ['mesh', 'spiral', 'fly']
        self.nz = 0               # number of scan points

        ### [Reconstruction parameters] ###
        self.n_iterations = 50       # number of iterations
        self.alg_flag = 'DM'         # ['DM', 'ER', 'ML_G', 'ML_P']
        self.alg2_flag = 'DM'        # ['DM', 'ER', 'ML_G', 'ML_P']
        self.alg_percentage = .8
        self.sign = 't1'             # saving file name

        self.init_prb_flag = True   # True: random guess; False: load an array
        self.prb_filename = ''
        self.prb_dir = ''
        self.prb_path = None         # path to existing probe array (.npy)

        self.init_obj_flag = True # True: random guess; False: load an array
        self.obj_filename = ''
        self.obj_dir = ''
        self.obj_path = None         # path to existing object array (.npy)

        self.mode_flag = False       # do multi-mode reconstruction
        self.prb_mode_num = 5
        self.obj_mode_num = 1

        self.multislice_flag = False
        self.slice_num = 2
        self.slice_spacing_m = 5.e-6

        self.amp_max = 1.    # up/low limit of allowed object amplitude range
        self.amp_min = 0.5   #
        self.pha_max = 0.01  # up/low limit of allowed object phase range
        self.pha_min = -1.0  #

        self.gpu_flag = True      # whether to use GPU
        self.gpus = [1, 2, 3]     # should be a list of gpu numbers, ex: [0, 2, 3]
        self.mpi_file_path = ''   # full path to a valid MPI machine file

        ### [adv param group] ###
        self.ccd_pixel_um = 55.      # detector pixel size (um)
        self.distance = 0.           # multislice distance
        self.angle_correction_flag = True
        self.x_direction = -1.
        self.y_direction = -1.
        self.angle = 15.

        self.start_update_probe = 0 # iteration number to start updating probe
        self.start_update_object = 0
        self.ml_mode = 'Poisson'     # mode for ML
        self.dm_version = 1
        self.cal_scan_pattern_flag = False

        self.nth = 5                 # number of points in the first ring
        self.start_ave = 0.8
        self.processes = 0

        # param for Bragg mode
        self.bragg_flag = False
        self.bragg_theta = 69.41
        self.bragg_gamma = 33.4
        self.bragg_delta = 15.458

        # partial coherence parameter
        self.pc_flag = False
        self.pc_sigma = 2.    # initial guess of kernel sigma
        self.pc_alg = 'lucy'  # deconvolution algorithm, lucy or wiener
        self.pc_kernel_n = 32

        # position correction parameter
        self.position_correction_flag = False
        self.position_correction_start = 50
        self.position_correction_step = 10

        # reconstruction feedback parameters
        self.alpha = 1.e-8
        self.beta = 0.9

        # GUI related 
        self.gui = True
        self.display_interval = 5 # plot every 5 steps
        self.preview_flag = True  # turn on live preview

        self.init_obj_dpc_flag = False
        self.prb_center_flag = True
        self.mask_prb_flag = False
        self.weak_obj_flag = False
        self.mesh_flag = 1
        self.ms_pie_flag = False
        self.sf_flag = False

        # mode calculation parameter
        self.save_tmp_pic_flag = False
        #self.p_flag = False          # True to load an exsiting probe

    def set_prb_path(self, dir, filename):
        self.prb_dir = dir
        self.prb_filename = filename
        self.prb_path = os.path.join(self.prb_dir, self.prb_filename)

    def set_obj_path(self, dir, filename):
        self.obj_dir = dir
        self.obj_filename = filename
        self.obj_path = os.path.join(self.obj_dir, self.obj_filename)

    def set_working_directory(self, path):
        self.working_directory = path

    def get_alg_flg_index(self):
        return ['DM', 'ER', 'ML_G', 'ML_P'].index(self.alg_flag)

    def get_ml_model_index(self):
        return ['Poisson'].index(self.ml_mode)

    def get_alg2_flg_index(self):
        return ['DM', 'ER', 'ML_G', 'ML_P'].index(self.alg2_flag)

    def get_pc_alg_index(self):
        return ['lucy', 'wiener'].index(self.pc_alg)

    def get_detector_kind_index(self):
        return ['merlin1', 'merlin2', 'timepix1', 'timepix2'].index(self.detectorkind)

    def get_scan_type_index(self):
        return ['mesh', 'spiral', 'fly'].index(self.scan_type)

    def get_slice_spacing_m(self):
        return np.round(self.slice_spacing_m / 1e-6)
