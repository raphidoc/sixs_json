import os
import logging
import subprocess
import json

class SixS:

    def __init__(self):
        # Find the sixsV2.1 executable
        package_dir = os.path.dirname(__file__)
        rel_path = os.path.join('..', '6sV2.1', 'sixsV2.1')
        abs_path = os.path.abspath(os.path.join(package_dir, rel_path))

        # TODO: add test of 6S installation ?

        self.sixs_path = abs_path
        logging.debug(f"Running 6S from: {self.sixs_path}")

        # TODO: use arbitrary arguments (*args) or keyword arguments (**kwargs)
        #  to pass the parameters in the methods.
        #  And perform conditional formatting depending on the arguments

        self.igeom = None
        self.idatm = None
        self.iaer = None
        self.xps = None
        self.xpp = None
        self.iwave = None
        self.inhomo = None
        self.idirec = None
        self.igroun = None
        self.irapp = None

        # Store the parameters in class attributes for outside access
        self.param = None

    def geometry(self, sun_zen, sun_azi, view_zen, view_azi, month, day):
        """
        igeom               geometrical conditions
        --------------------------------------

        you choose your own conditions; igeom=0
        0     enter
        solar zenith angle   (in degrees )
        solar azimuth angle        "
        satellite zenith angle     "
        satellite azimuth angle    "
        month
        day of the month

        :param sun_zen:
        :param sun_azi:
        :param view_zen:
        :param view_azi:
        :param month:
        :param day:
        :return:
        """

        self.igeom = ("\n0 # IGEOM\n"
                      + f"{sun_zen} {sun_azi} {view_zen} {view_azi} {month} {day} \n")

    def gas(self):
        """
        idatm      atmospheric model
        --------------------

        you select one of the following standard atmosphere: idatm=0 to 6
        0    no gaseous absorption
        1    tropical
        2    midlatitude summer
        3    midlatitude winter
        4    subarctic summer (from lowtran)
        5    subarctic winter
        6    us standard 62

        or you define your own atmospheric model idatm=7 or 8

        7    user profile  (radiosonde data on 34 levels)
        enter altitude       (  in km )
        pressure       (  in mb )
        temperature    (  in k  )
        h2o density    (in  g/m3)
        o3  density    (in  g/m3)

        for example, altitudes are  from  0 to 25km step of 1km from 25 to 50km step of 5km
        and two values at 70km and 100km, so you have 34*5 values to input.

        8    enter water vapor and ozone contents
        uw  (in  g/cm2 )
        uo3 (in  cm-atm)
        profil is taken from us62
        :return:
        """
        self.idatm = "2 # IDATM midlatitude summer\n"

    def aerosol(self, aot_550):
        """
        iaer       aerosol model(type) and profile
        --------------
        iaer = -1  The user-defined profile. You have to input the
        number of layers first, then the height (km),
        optical thickness (at 550 nm), and type of aerosol
        (see below) for each layer, starting from the
        ground. The present version of the program works
        only with the same type of aerosol for each layer.

        Example for iaer = -1:
        4
        2.0 0.200 1
        10.0 0.025 1
        8.0 0.003 1
        80.0 0.000 1

        The maximum total height of all layers cannot exceed 300 km.

        If you do not input iaer = -1, the program will use the default
        exponential profile. In this case, you need to select one of
        the following standard aerosol models:

        iaer = 0  no aerosols
        1  continental
        2  maritime according to d'Almeida's models
        3  urban (see the manual)
        5  background desert )
        6  biomass burning from AERONET measurements
        7  stratospheric according to Russel's model

        or you define your own model using basic components: iaer=4
        4 enter the volumetric percentage of each component
        c(1) = volumetric % of dust-like
        c(2) = volumetric % of water-soluble
        c(3) = volumetric % of oceanic
        c(4) = volumetric % of soot
        between 0 to 1

        or you define your own model using a size distribution function:
        8  Multimodal Log-Normal distribution (up to 4 modes)
        9  Modified Gamma  distribution
        10  Junge Power-Law distribution

        or you define a model using sun-photometer measurements:
        11  Sun Photometer  distribution (50 values max)
        you have to enter:  r and dV/d(logr)
        where r is the radius (in micron), V is the volume,
        and dV/d(logr) is in (cm3/cm2/micron)
        then you have to enter: nr and ni for each wavelength
        where nr and ni are respectively the real and the
        imaginary parts of the refractive index

        or you can use the results computed and saved previously
        12  Reading of data previously saved into FILE
        you have to enter the identification name FILE in the next line of inputs.


        iaerp and FILE  aerosol model(type)-Printing of results
        ---------------------------------------

        For iaer=8,9,10,and 11:
        results from the MIE subroutine may be saved into the file
        FILE.mie (Extinction and scattering coefficients, single
        scattering albedo, asymmetry parameter, phase function at
        predefined wavelengths) and then can be re-used with the
        option iaer=12 where FILE is an identification name youhave to enter.

        So, if you select iaer=8,9,10, or 11, you will have to enter
        iaerp after the inputs requested by options 8,9,10, or 11:

        iaerp=0    results will not be saved
        iaerp=1    results will be saved into the file FILE.mie next line enter FILE

        Example for iaer and iaerp
        8                      Multimodal Log-Normal distribution selected
        0.001 20 3             Rmin, Rmax, 3 components
        0.471 2.512 0.17       Rmean, Sigma, % density - 1st component
        1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.528
        1.52 1.462 1.4 1.368 1.276 1.22 1.2      nr for 20 wavelengths
        0.008 0.008 0.008 0.008 0.008 0.008 0.008 0.008 0.008 0.008 0.008
        0.008 0.008 0.008 0.008 0.008 0.008 0.008 0.0085 0.011     ni
        0.0285 2.239 0.61      Rmean, Sigma, % density - 2nd component
        1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.528
        1.52 1.51 1.42 1.42 1.42 1.42 1.452      nr for 20 wavelengths
        0.005 0.005 0.005 0.005 0.005 0.005 0.0053 0.006 0.006 0.0067 0.007
        0.007 0.0088 0.0109 0.0189  0.0218 0.0195 0.0675 0.046 0.004   ni
        0.0118 2.0 0.22        Rmean, Sigma, % density - 3rd component
        1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75 1.75
        1.75 1.77 1.791 1.796 1.808 1.815 1.9    nr for 20 wavelengths
        0.465 0.46 0.4588 0.4557 0.453 0.4512 0.447 0.44 0.436 0.435 0.433
        0.4306 0.43 0.433 0.4496 0.4629 0.472 0.488 0.5 0.57      ni
        1                      Results will be saved into FILE.mie
        Urban_Indust           Identification of the output file (FILE)
                    -> results will be saved into Urban_Indust.mie


        aerosol model concentration (only for the default exponential profile)
        -------------------------
        v             if you have an estimate of the meteorological parameter: the visibility v,
        enter directly the value of v in km (the aerosol optical depth will
        be computed from a standard aerosol profile)

        v=0, taer55   if you have an estimate of aerosol optical depth
        enter v=0 for the visibility and enter the aerosol optical depth at 550

        v=-1          warning:  if iaer=0, enter v=-1

        :param aot_550:
        :return:
        """

        self.iaer = ("2 # IAER maritime\n"
                     + f"0 # visibility\n"
                     + f"{aot_550} # aot(550)\n")

    def target_altitude(self):
        """
        xps is the parameter to express the  altitude of target
        xps >=0.  the pressure is given in mb
        xps <0. means you know the altitude of the target expressed in km and you put that value as xps

        NOTE : 6Sversion 1 states "xps >=0. means the target is at the sea level"

        """
        self.xps = f"{1013} # XPS pressure at target\n"

    def sensor_altitude(self):
        """
        xpp is the parameter to express the sensor altitude

        xpp= -1000  means that the sensor is a board a satellite
        xpp=     0  means that the sensor is at the ground level

        for aircraft simulations
        -100< xpp <0  means you know the altitude of the sensor expressed
        in kilometers units
        this altitude is relative to the target altitude
        for aircraft simulations only, you have to give
        puw,po3   (water vapor content,ozone content between the
        aircraft and the surface)
        taerp     (the aerosol optical thickness at 550nm between the
        aircraft and the surface)
        if these data are not available, enter negative values for all
        of them, puw,po3 will then be interpolated from the us62 standard
        profile according to the values at ground level. Taerp will be
        computed according to a 2km exponential profile for aerosol.
        """
        self.xpp = f"{0} # XPP sensor altitude\n"

    def wavelength(self, wl):
        """
        iwave input of the spectral conditions

        you choose to define your own spectral conditions: iwave=-1,0 or 1
        (three user s conditions )

        -2  enter wlinf, wlsup, the filter function will be equal to 1
        over the whole band (as iwave=0) but step by step output will be printed

        -1  enter wl (monochr. cond,  gaseous absorption is included)

        0  enter wlinf, wlsup. the filter function will be equal to over the whole band.

        1  enter wlinf, wlsup and user's filter function s(lambda) ( by step of 0.0025 micrometer).
        """

        self.iwave = ("-1 # IWAVE monochromatic\n"
                      + f"{wl * 1e-3} # wavelength\n")

    def to_be_implemented(self):
        self.inhomo = "0 # INHOMO\n"

        self.idirec = "0 # IDIREC\n"

        self.igroun = ("0 # IGROUN 0 = rho\n"
                       + "0 # surface reflectance\n")

        self.irapp = "-1 # IRAPP no atmospheric correction\n"

    def run(self):
        self.param = (self.igeom
                      + self.idatm
                      + self.iaer
                      + self.xps
                      + self.xpp
                      + self.iwave
                      + self.inhomo
                      + self.idirec
                      + self.igroun
                      + self.irapp)

        command = f'echo "{self.param}" | {self.sixs_path}'

        process = subprocess.run(command, shell=True, capture_output=True)

        breakpoint()

        logging.debug(f"Subprocess exited with status {process.returncode}")

        dict_res = json.loads(process.stdout)

        return dict_res

# # TODO: if sun_azimuth is set then view_azimuth should be the north azimuth and not the relative azimuth
# #  if we have the viewing azimuth relative to the sun then we can set sun_azimuth = 0
# #  and just pass the relative azimuth
#
# # Path to the 6s executable modified with json output
# # see (https://github.com/raphidoc/6S_json)
# path_6s = "/home/raphael/PycharmProjects/6S_json/6sV2.1/sixsV2.1"
#
# # Input parameters according to the Py6S code above
# commands = []
# for wl in wvl:
#     command = (
#             'echo "\n0 # IGEOM\n'
#             + f"{sun_zenith[ind_anc]} {sun_azimuth[ind_anc]} 180 {rel_az[ind_anc]} {datetime[ind_anc].month} {datetime[ind_anc].day} # sun_zenith sun_azimuth view_zenith view_azimuth month day\n"
#             + "2 # IDATM midlatitude summer\n"
#             + "2 # IAER maritime\n"
#             + f"0 # visibility\n"
#             + f"{aod[ind_anc]} # aot(555)\n"
#             + f"{1013} # XPS pressure at target\n"
#             + f"{0} # XPP sensor altitude\n"
#             + "-1 # IWAVE monochromatic\n"
#             + f"{wl * 1e-3} # wavelength\n"
#             + "0 # INHOMO\n"
#             + "0 # IDIREC\n"
#             + "0 # IGROUN 0 = rho\n"
#             + "0 # surface reflectance\n"
#             + '-1 # IRAPP no atmospheric correction\n"' + f"| {path_6s}"
#     )
#     commands.append(command)
#
# # Create placeholder to contain the values
# percent_direct_solar_irradiance = [0] * len(commands)
# percent_diffuse_solar_irradiance = [0] * len(commands)
# direct_solar_irradiance = [0] * len(commands)
# diffuse_solar_irradiance = [0] * len(commands)
# environmental_irradiance = [0] * len(commands)
#
# # Determine the number of workers to use
# num_workers = os.cpu_count()
# logging.info(f"Running on {num_workers} threads")
# iterations_per_worker = len(commands) // num_workers
# logging.info(f"{iterations_per_worker} iteration per threads")
#
#
# # Create the function for 6s that will be run by each worker
# def run_model_and_accumulate(
#         start,
#         end,
#         commands,
#         percent_direct_solar_irradiance,
#         percent_diffuse_solar_irradiance,
#         direct_solar_irradiance,
#         diffuse_solar_irradiance,
#         environmental_irradiance
#
# ):
#     for i in range(start, end):
#         command = commands[i]
#         process = subprocess.run(command, shell=True, capture_output=True)
#
#         # print(f"Subprocess exited with status {process.returncode}")
#
#         temp = json.loads(process.stdout)
#
#         # if math.isnan(float(temp["atmospheric_reflectance_at_sensor"])):
#         #     print("atmospheric_path_radiance is NaN ...")
#
#         percent_direct_solar_irradiance[i] = float(
#             temp["percent_of_direct_solar_irradiance_at_target"]
#         )
#         percent_diffuse_solar_irradiance[i] = float(
#             temp["percent_of_diffuse_atmospheric_irradiance_at_target"]
#         )
#         direct_solar_irradiance[i] = float(
#             temp["direct_solar_irradiance_at_target_[W m-2 um-1]"]
#         )
#         diffuse_solar_irradiance[i] = float(
#             temp["diffuse_atmospheric_irradiance_at_target_[W m-2 um-1]"]
#         )
#         environmental_irradiance[i] = float(
#             temp["environement_irradiance_at_target_[W m-2 um-1]"]
#         )
#
#     return
#
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
#     futures = []
#     for i in range(num_workers):
#         # Calculate the start and end indices for this worker
#         start = i * iterations_per_worker
#         end = (
#             start + iterations_per_worker
#             if i != num_workers - 1
#             else len(commands)
#         )
#
#         # Start the worker
#         futures.append(
#             executor.submit(
#                 run_model_and_accumulate,
#                 start,
#                 end,
#                 commands,
#                 percent_direct_solar_irradiance,
#                 percent_diffuse_solar_irradiance,
#                 direct_solar_irradiance,
#                 diffuse_solar_irradiance,
#                 environmental_irradiance
#             )
#         )
#
# # Wait for all workers to finish
# concurrent.futures.wait(futures)
#
# direct[n, :] = np.array(percent_direct_solar_irradiance)
# diffuse[n, :] = np.array(percent_diffuse_solar_irradiance)
# irr_direct[n, :] = np.array(direct_solar_irradiance)
# irr_diffuse[n, :] = np.array(diffuse_solar_irradiance)
# irr_env[n, :] = np.array(environmental_irradiance)
# solar_zenith[n] = sun_zenith[ind_anc]
#
# end_time = time.perf_counter()
# logging.info(f"6s took {end_time - start_time} seconds")
#
# breakpoint()
