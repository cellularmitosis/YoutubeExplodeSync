YoutubeExplode.dll:
	dotnet build /p:EnableWindowsTargeting=true
	ln -sf YoutubeExplode/bin/Debug/net5.0/YoutubeExplode.dll .
.PHONY: YoutubeExplode.dll

ubuntu-deps:
	wget https://packages.microsoft.com/config/ubuntu/22.10/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb
	sudo dpkg -i /tmp/packages-microsoft-prod.deb
	rm -f /tmp/packages-microsoft-prod.deb
	sudo apt-get update && sudo apt-get install dotnet-sdk-6.0 dotnet-sdk-7.0 nuget
	echo if you encounter "A fatal error occurred. The folder [/usr/share/dotnet/host/fxr] does not exist"
	echo then see https://stackoverflow.com/a/73899341
	dotnet --list-sdks
	sudo apt-get install python3-pip
	sudo pip3 install -U pythonnet
.PHONY: ubuntu-deps

tmp/AngleSharp.dll:
	mkdir -p tmp
	cd tmp && nuget install AngleSharp
	cd tmp && ln -s AngleSharp.1.0.1/lib/net7.0/*.dll .

test-pythonnet: YoutubeExplode.dll tmp/AngleSharp.dll
	mkdir -p tmp
	cd tmp && ln -sf ../YoutubeExplode.dll .
	cd tmp && cp ../test-pythonnet.py .
	cd tmp && ./test-pythonnet.py
.PHONY: test-pythonnet
