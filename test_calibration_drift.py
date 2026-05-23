def test_device_calibration():
    # Simulates a minor environment configuration drift (SEV 3)
    calibration_drift = 4.8
    max_tolerance = 5.0
    assert calibration_drift <= max_tolerance, (
        f"ConfigurationError: Calibration offset drift ({calibration_drift}%) "
        f"exceeded maximum tolerance ({max_tolerance}%). Run env recalibration."
    )

if __name__ == "__main__":
    test_device_calibration()