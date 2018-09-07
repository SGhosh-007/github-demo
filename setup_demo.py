from cx_Freeze import setup , Executable
setup(name = 'Demo Program',
		version = '0.1',
		author = 'Sushobhan Ghosh',
		description = 'A small demo program',
		executables = [Executable(r"C:\Users\USER\Desktop\Demo\test.py",
						shortcutName = "Demo",
						shortcutDir = "DesktopFolder")]
	)