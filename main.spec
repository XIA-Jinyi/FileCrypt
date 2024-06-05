# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('./frontend/dist/*', './frontend/dist'),
        ('./frontend/dist/js/*', './frontend/dist/js'),
        ('./frontend/dist/css/*', './frontend/dist/css'),
        ('./frontend/dist/img/*', './frontend/dist/img'),
        ('./frontend/dist/fonts/*', './frontend/dist/fonts'),
        ('./driver/*', './driver'),
        ('./backup', '.')
    ],
    hiddenimports=[],
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FileCrypt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon='frontend/dist/favicon.png'
)
