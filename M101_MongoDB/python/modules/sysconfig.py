import sysconfig

print sysconfig.get_python_version()
print sysconfig.get_platform()
print sysconfig.get_path_names()
pn = sysconfig.get_path_names()
for i in pn:
	print sysconfig.get_path(i)
	
print sysconfig.get_paths()
print sysconfig.get_config_h_filename()
print sysconfig.get_scheme_names()
print sysconfig.is_python_build()
#~ fp = sysconfig.get_config_h_filename()
#~ print sysconfig.parse_config_h(fp, vars=None)