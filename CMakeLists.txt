###############################################################################
#
# CMake build scripts for 6SV
#
# Created 10/07/2014 by Pete Bunting (petebunting@mac.com)
# Modified 2024-05-27 by Raphael Mabit (raphael.mabit@gmail.com)
#   - Support 6sV2.1
###############################################################################

###############################################################################
# Set Project name and version
project (SIXSV)

# The version number.
set (SIXS_VERSION "2.1")

# CMake settings
cmake_minimum_required(VERSION 2.6.0)

enable_language (Fortran)

IF(NOT CMAKE_BUILD_TYPE)
  #SET(CMAKE_BUILD_TYPE "DEBUG")
  SET(CMAKE_BUILD_TYPE "RELEASE")
  #SET(CMAKE_BUILD_TYPE "RELWITHDEBINFO")
  #SET(CMAKE_BUILD_TYPE "MINSIZEREL")
ENDIF()

set(CMAKE_COLOR_MAKEFILE ON)

# Allow advanced users to generate Makefiles printing detailed commands
mark_as_advanced(CMAKE_VERBOSE_MAKEFILE)

# Path to additional CMake modules
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ./cmake/modules/)

# Set up compiler flags
# FFLAGS depend on the compiler
get_filename_component (Fortran_COMPILER_NAME ${CMAKE_Fortran_COMPILER} NAME)

if (Fortran_COMPILER_NAME MATCHES "gfortran.*")
  # gfortran
  set (CMAKE_Fortran_FLAGS_RELEASE "-ffpe-summary='none' -funroll-all-loops -std=legacy -ffixed-line-length-none -fno-f2c -O3")
  set (CMAKE_Fortran_FLAGS_DEBUG   "-ffpe-summary='none' -fno-f2c -O0 -g -std=legacy -ffixed-line-length-none")
elseif (Fortran_COMPILER_NAME MATCHES "ifort.*")
  # ifort (untested)
  set (CMAKE_Fortran_FLAGS_RELEASE "-f77rtl -O3 -fPIC -static-intel ")
  set (CMAKE_Fortran_FLAGS_DEBUG   "-f77rtl -O0 -g -fPIC -static-intel ")
elseif (Fortran_COMPILER_NAME MATCHES "g77")
  # g77
  set (CMAKE_Fortran_FLAGS_RELEASE "-funroll-all-loops -fno-f2c -O3 -m32")
  set (CMAKE_Fortran_FLAGS_DEBUG   "-fno-f2c -O0 -g -m32")
else (Fortran_COMPILER_NAME MATCHES "gfortran.*")
  message ("CMAKE_Fortran_COMPILER full path: " ${CMAKE_Fortran_COMPILER})
  message ("Fortran compiler: " ${Fortran_COMPILER_NAME})
  message ("No optimized Fortran compiler flags are known, we just try -O2...")
  set (CMAKE_Fortran_FLAGS_RELEASE "-O2")
  set (CMAKE_Fortran_FLAGS_DEBUG   "-O0 -g")
endif (Fortran_COMPILER_NAME MATCHES "gfortran.*")


# BUILD EXE
add_executable(
sixs
./6sV2.1/main.f
./6sV2.1/AATSR.f
./6sV2.1/ABSTRA.f
./6sV2.1/AEROPROF.f
./6sV2.1/AEROSO.f
./6sV2.1/AKTOOL.f
./6sV2.1/ALI.f
./6sV2.1/ASTER.f
./6sV2.1/ATMREF.f
./6sV2.1/AVHRR.f
./6sV2.1/BBM.f
./6sV2.1/BDM.f
./6sV2.1/BRDFGRID.f
./6sV2.1/CAVIS.f # This is new in 6SV 2.1
./6sV2.1/CHAND.f
./6sV2.1/CLEARW.f
./6sV2.1/CSALBR.f
./6sV2.1/DICA1.f
./6sV2.1/DICA2.f
./6sV2.1/DICA3.f
./6sV2.1/DISCOM.f
./6sV2.1/DISCRE.f
./6sV2.1/DUST.f
./6sV2.1/ENVIRO.f
./6sV2.1/EQUIVWL.f
./6sV2.1/ETM.f
./6sV2.1/GAUSS.f
./6sV2.1/GLI.f
./6sV2.1/GOES.f
./6sV2.1/HAPKALBE.f
./6sV2.1/DMC.f
./6sV2.1/HAPKBRDF.f
./6sV2.1/HRV.f
./6sV2.1/HYPBLUE.f
./6sV2.1/IAPIALBE.f
./6sV2.1/IAPIBRDF.f
./6sV2.1/IAPITOOLS.f
./6sV2.1/INTERP.f
./6sV2.1/ISO.f
./6sV2.1/KERNEL.f
./6sV2.1/KERNELPOL.f
./6sV2.1/LAKEW.f
./6sV2.1/LDCM.f
./6sV2.1/MAS.f
./6sV2.1/MERIS.f
./6sV2.1/METEO.f
./6sV2.1/METH1.f
./6sV2.1/METH2.f
./6sV2.1/METH3.f
./6sV2.1/METH4.f
./6sV2.1/METH5.f
./6sV2.1/METH6.f
./6sV2.1/MIDSUM.f
./6sV2.1/MIDWIN.f
./6sV2.1/MIE.f
./6sV2.1/MINNALBE.f
./6sV2.1/MINNBRDF.f
./6sV2.1/MOCA1.f
./6sV2.1/MOCA2.f
./6sV2.1/MOCA3.f
./6sV2.1/MOCA4.f
./6sV2.1/MOCA5.f
./6sV2.1/MOCA6.f
./6sV2.1/MODIS.f
./6sV2.1/MODIS1km.f
./6sV2.1/MODISALBE.f
./6sV2.1/MODISBRDF.f
./6sV2.1/MODISBRDFFOS.f
./6sV2.1/MSS.f
./6sV2.1/NIOX1.f
./6sV2.1/NIOX2.f
./6sV2.1/NIOX3.f
./6sV2.1/NIOX4.f
./6sV2.1/NIOX5.f
./6sV2.1/NIOX6.f
./6sV2.1/OCEA.f
./6sV2.1/OCEAALBE.f
./6sV2.1/OCEABRDF.f
./6sV2.1/OCEABRDFFAST.f
./6sV2.1/OCEATOOLS.f
./6sV2.1/ODA550.f
./6sV2.1/ODRAYL.f
./6sV2.1/OS.f
./6sV2.1/OSPOL.f
./6sV2.1/OSSURF.f
./6sV2.1/OXYG3.f
./6sV2.1/OXYG4.f
./6sV2.1/OXYG5.f
./6sV2.1/OXYG6.f
./6sV2.1/OZON1.f
./6sV2.1/PLANPOL.f
./6sV2.1/POLDER.f
./6sV2.1/POLGLIT.f
./6sV2.1/POLNAD.f
./6sV2.1/POSGE.f
./6sV2.1/POSGW.f
./6sV2.1/POSLAN.f
./6sV2.1/POSMTO.f
./6sV2.1/POSNOA.f
./6sV2.1/POSSOL.f
./6sV2.1/POSSPO.f
./6sV2.1/PRESPLANE.f
./6sV2.1/PRESSURE.f
./6sV2.1/PRINT_ERROR.f
./6sV2.1/RAHMALBE.f
./6sV2.1/RAHMBRDF.f
./6sV2.1/RAHMBRDFFOS.f
./6sV2.1/ROUJALBE.f
./6sV2.1/ROUJBRDF.f
./6sV2.1/ROSSLIMAIGNANBRDF.f
./6sV2.1/ROSSLIMAIGNANALBE.f
./6sV2.1/ROSSLIMAIGNANBRDFFOS.f
./6sV2.1/SAND.f
./6sV2.1/SCATRA.f
./6sV2.1/SEAWIFS.f
./6sV2.1/SOLIRR.f
./6sV2.1/SOOT.f
./6sV2.1/SPECINTERP.f
./6sV2.1/SPLIE2.f
./6sV2.1/SPLIN2.f
./6sV2.1/SPLINE.f
./6sV2.1/SPLINT.f
./6sV2.1/STM.f
./6sV2.1/SUBSUM.f
./6sV2.1/SUBWIN.f
./6sV2.1/TM.f
./6sV2.1/TROPIC.f
./6sV2.1/TRUNCA.f
./6sV2.1/US62.f
./6sV2.1/VARSOL.f
./6sV2.1/VEGETA.f
./6sV2.1/VERSALBE.f
./6sV2.1/VERSBRDF.f
./6sV2.1/VERSTOOLS.f
./6sV2.1/VGT.f
./6sV2.1/VIIRS.f
./6sV2.1/WALTALBE.f
./6sV2.1/WALTBRDF.f
./6sV2.1/WATE.f
./6sV2.1/WAVA1.f
./6sV2.1/WAVA2.f
./6sV2.1/WAVA3.f
./6sV2.1/WAVA4.f
./6sV2.1/WAVA5.f
./6sV2.1/WAVA6.f
)

# INSTALL
install (TARGETS sixs DESTINATION bin PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
