# E-Waste Rescue — Python/Kivy port

This is a starter Python port based on the Java `MainActivity.java` shared in chat.

## Included
- Home dashboard and navigation
- Six e-waste categories
- Recycling guide
- Impact dashboard (clearly labelled illustrative demo figures)
- Recycler verification page with official CPCB portal link
- Pickup form with 10-digit phone validation and local JSON storage

## Important notes
- This is a Python/Kivy rewrite of the UI and app logic, not a line-by-line Java conversion.
- Existing Java drawables are not included automatically. Add your existing `ewaste_logo.png` and `splash_screen.png` to `assets/` if you have them. This starter currently uses an emoji mark and does not yet display those image assets.
- Pickup requests are saved locally on the device and are not transmitted to a recycler.
- Recycler names/addresses from the original Java source were not presented as verified live information; the app directs users to verify official listings.
- Test the app before using it in a hackathon demo.

## Run on a computer
Install Python 3 and Kivy in a compatible desktop environment, then run:
`python main.py`

## Build Android APK
Buildozer is best supported on Linux (or WSL2 on Windows). Android APK builds are not reliably produced directly on an Android phone.
1. Install Buildozer and its system dependencies on Linux.
2. In this folder run `buildozer android debug`.
3. The APK should appear under `bin/` if the build succeeds.

This package is source code, not a prebuilt APK.
