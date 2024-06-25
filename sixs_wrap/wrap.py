import os
import logging


class SixS:

    def __init__(self):
        # Find the sixsV2.1 executable
        package_dir = os.path.dirname(__file__)
        rel_path = os.path.join('..', '6sV2.1', 'sixsV2.1')
        abs_path = os.path.abspath(os.path.join(package_dir, rel_path))

        # TODO: add test of 6S installation ?

        self.sixs_path = abs_path
        logging.debug(f"Running 6S from: {self.sixs_path}")

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



    def geometry(self, sun_zen, sun_azi, view_zen, view_azi, month, day):
        self.igeom = ("\n0 # IGEOM\n"
                      + f"{sun_zen} {sun_azi} {view_zen} {view_azi} {month} {day} \n")

    def gas(self):
        self.idatm = "2 # IDATM midlatitude summer\n"

    def aerosol(self, aot_550):
        self.iaer = ("2 # IAER maritime\n"
                     + f"0 # visibility\n"
                     + f"{aot_550} # aot(550)\n")

    def target_altitude(self):
        """
        xps is the parameter to express the  altitude of target
        xps >=0.  the pressure is given in mb
        xps <0. means you know the altitude of the target expressed in km and you put that value as xps
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
        self.inhomo ="0 # INHOMO\n"

        self.idirec = "0 # IDIREC\n"

        self.igroun = ("0 # IGROUN 0 = rho\n"
                       + "0 # surface reflectance\n")

        self.irapp = "-1 # IRAPP no atmospheric correction\n"

    def run(self):
        param = (self.igeom
                 + self.idatm
                 + self.iaer
                 + self.xps
                 + self.xpp
                 + self.iwave
                 + self.inhomo
                 + self.idirec
                 + self.igroun
                 + self.irapp)

        pass

    pass
