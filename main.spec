# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['python\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('c/generate_diagonal_sudoku.exe', 'c'), ('c/sudoku_solver.exe', 'c'), ('c/cnf_to_grid.exe', 'c'), ('c/solver.exe', 'c'), ('c/cnf_parser.exe', 'c'), ('c/better_solver.exe', 'c'), ('python/Ui_start.py', 'python'), ('python/Ui_rules.py', 'python'), ('python/Ui_mode.py', 'python'), ('python/Ui_upload.py', 'python'), ('python/Ui_difficulty.py', 'python'), ('python/Ui_game.py', 'python')],
    hiddenimports=[],
    hookspath=[],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Qiu\\Downloads\\favicon.ico'],
)
