from sixs_json import SixS


def test_run():

    s = SixS()
    s.geometry(30, 260, 180,30, 1, 1)
    s.gas()
    s.aerosol(0.04)
    s.target_altitude()
    s.sensor_altitude()
    s.wavelength(445)
    s.to_be_implemented()

    dict_res = s.run()

    assert isinstance(dict_res, dict)
    assert dict_res['6s_version'] == 2.1
