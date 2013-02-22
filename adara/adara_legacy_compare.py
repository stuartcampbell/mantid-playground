# Load ADARA File
Load(Filename='/home/scu/data/HYSA_13819.nxs.h5',OutputWorkspace='HYSA_13819')
FilterByTime(InputWorkspace='HYSA_13819',OutputWorkspace='HYSA_13819_filtered',AbsoluteStartTime='2013-02-11T22:56:25.256070666',AbsoluteStopTime='2013-02-11T23:25:55.855892666')

# Load Legacy File
Load(Filename='/SNS/HYS/IPTS-8839/0/14820/NeXus/HYS_14820_event.nxs',OutputWorkspace='HYS_14820')
FilterByTime(InputWorkspace='HYS_14820',OutputWorkspace='HYS_14820_filtered',AbsoluteStartTime='2013-02-11T22:56:25.256070666',AbsoluteStopTime='2013-02-11T23:25:55.855892666')

# Get Run Object
adara_run=mtd['HYSA_13819'].getRun()
legacy_run=mtd['HYS_14820'].getRun()

# Get Ei
adara_ei=adara_run['EnergyRequest'].getStatistics().mean
legacy_ei=legacy_run['EnergyRequest'].getStatistics().mean

# Work out some energy bins
emin = -(2.0*adara_ei)
emax = adara_ei*0.9
estep = 0.1
energy_bins = "%f,%f,%f" % (emin,estep,emax)

DgsReduction(SampleInputWorkspace='HYSA_13819',IncidentEnergyGuess=adara_ei,EnergyTransferRange=energy_bins,
		IncidentBeamNormalisation='ByCurrent',OutputWorkspace="adara")
#		OutputWorkspace="adara")
		

# Work out some energy bins
emin = -(2.0*legacy_ei)
emax = legacy_ei*0.9
estep = 0.1
energy_bins = "%f,%f,%f" % (emin,estep,emax)

DgsReduction(SampleInputWorkspace='HYS_14820',IncidentEnergyGuess=legacy_ei,EnergyTransferRange=energy_bins,
		IncidentBeamNormalisation='ByCurrent',OutputWorkspace="legacy")
#		OutputWorkspace="legacy")
