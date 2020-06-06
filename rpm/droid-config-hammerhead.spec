# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device evk_8mm
%define vendor fsl
%define vendor_pretty Freescale
%define device_pretty IMX8M Mini
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
