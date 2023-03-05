dll:
	dotnet build /p:EnableWindowsTargeting=true
	ln -sf YoutubeExplode/bin/Debug/net5.0/YoutubeExplode.dll .
.PHONY: dll

build-deps:
	wget https://packages.microsoft.com/config/ubuntu/22.10/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb
	sudo dpkg -i /tmp/packages-microsoft-prod.deb
	rm -f /tmp/packages-microsoft-prod.deb
	sudo apt-get update && sudo apt-get install dotnet-sdk-6.0 dotnet-sdk-7.0
	echo if you encounter "A fatal error occurred. The folder [/usr/share/dotnet/host/fxr] does not exist"
	echo then see https://stackoverflow.com/a/73899341
.PHONY: build-deps
