# win_can_tool.spec
# Ensures PyInstaller bundles the entire win_can_tool package + assets

block_cipher = None

a = Analysis(
    ['can_gui_launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('win_can_tool/**/*.py', 'win_can_tool'),
        ('assets/*', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='win_can_tool',
    icon='win_can_tool.ico',
    debug=False,
    strip=False,
    upx=True,
    console=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='win_can_tool'
)
