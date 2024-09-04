block_cipher = None
a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas+=[(r'sound\close.wav', r'sound\close.wav', "DATA")]
a.datas+=[(r'sound\objection.wav', r'sound\objection.wav', "DATA")]
a.datas+=[(r'sound\open.wav', r'sound\open.wav', "DATA")]
a.datas+=[(r'sound\takethat.wav', r'sound\takethat.wav', "DATA")]
a.datas+=[(r'assets\aaifr.png', r'assets\aaifr.png', "DATA")]
a.datas+=[(r'assets\discord.png', r'assets\discord.png', "DATA")]
a.datas+=[(r'assets\icon.png', r'assets\icon.png', "DATA")]
a.datas+=[(r'assets\logo.png', r'assets\logo.png', "DATA")]
a.datas+=[(r'assets\msg.json', r'assets\msg.json', "DATA")]
a.datas+=[(r'assets\web.png', r'assets\web.png', "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Ace Attorney Investigations 2 Benjamin Hunter Prosecutors Path VF',
          debug=False,
          strip=False,
          upx=True,
          console=False,
		  clean = True,
          icon=r'icon.ico')
