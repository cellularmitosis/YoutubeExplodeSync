dll:
	dotnet build /p:EnableWindowsTargeting=true
	ln -sf YoutubeExplode/bin/Debug/net5.0/YoutubeExplode.dll .
.PHONY: dll
