# rpm_device is the name of the ported device
%define rpm_device shieldtablet
# rpm_vendor is used in the rpm space
%define rpm_vendor nvidia

# Manufacturer and device name to be shown in UI
%define vendor_pretty Nvidia
%define device_pretty Shield Tablet

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 0
%define have_led 0

%include droid-hal-version/droid-hal-version.inc
