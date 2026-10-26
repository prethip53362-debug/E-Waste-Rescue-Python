[app]
title = E-Waste Rescue
package.name = ewasterescue
package.domain = org.ewasterescue
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Android build defaults
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
