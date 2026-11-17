[app]
title = MyApp
package.name = myapp
package.domain = org.rootya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_dirs = bin,.buildozer,.git,__pycache__
version = 0.1
# Библиотеки, которые нужны твоему коду (через запятую), например: python3,kivy,requests,pillow
requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
p4a.branch = v2024.01.21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
bin_dir = ./bin
