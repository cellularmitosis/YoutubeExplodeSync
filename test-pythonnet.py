#!/usr/bin/env python3

# See https://pythonnet.github.io/pythonnet/python.html
# See https://github.com/Tyrrrz/YoutubeExplode

# bash:
# nuget install AngleSharp
# ln -s AngleSharp.1.0.1/lib/net7.0/*.dll .

print("Booting")
import pythonnet
pythonnet.load("coreclr")
import clr
clr.AddReference("AngleSharp")
clr.AddReference("YoutubeExplode")
import YoutubeExplode
yt = YoutubeExplode.YoutubeClient()

v_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
v_id = YoutubeExplode.Videos.VideoId("dQw4w9WgXcQ")

print()
print("Testing Search.GetResults()")
pr = yt.Search.GetResults("imac g3")
print("  PagedSearchResults: %s results:" % len(pr.Results))
for sr in pr.Results:
    print("    ISearchResult: Title: %s" % sr.Title)
    print("      Url: %s" % sr.Url)
    vsr = sr.asVideoSearchResult()
    if vsr is not None:
        print("      VideoSearchResult: Id: %s, Title: %s, Author: %s, Duration: %s" % (vsr.Id, vsr.Title, vsr.Author, vsr.Duration))
        # for th in vsr.Thumbnails:
        #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
        #     print("          Url: %s" % th.Url) 
        th = vsr.Thumbnails[0]
        print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
        print("          Url: %s" % th.Url) 
    csr = sr.asChannelSearchResult()
    if csr is not None:
        print("      ChannelSearchResult: Id: %s" % csr.Id)
        # for th in csr.Thumbnails:
        #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
        #     print("          Url: %s" % th.Url) 
        th = csr.Thumbnails[0]
        print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
        print("          Url: %s" % th.Url) 
    psr = sr.asPlaylistSearchResult()
    if psr is not None:
        print("      PlaylistSearchResult: Id: %s" % psr.Id)
        print("      PlaylistSearchResult: Id: %s, Author: %s" % (vsr.Id, vsr.Author))
        # for th in psr.Thumbnails:
        #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
        #     print("          Url: %s" % th.Url) 
        th = psr.Thumbnails[0]
        print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
        print("          Url: %s" % th.Url) 
for vsr in pr.Videos():
    print("      VideoSearchResult: Id: %s, Title: %s, Author: %s, Duration: %s" % (vsr.Id, vsr.Title, vsr.Author, vsr.Duration))
    # for th in vsr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = vsr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 
for csr in pr.Channels():
    print("      ChannelSearchResult: Id: %s" % csr.Id)
    # for th in csr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = csr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 
for psr in pr.Playlists():
    print("      PlaylistSearchResult: Id: %s" % psr.Id)
    print("      PlaylistSearchResult: Id: %s, Author: %s" % (vsr.Id, vsr.Author))
    # for th in psr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = psr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 

print()
print("Testing Search.GetVideos()")
pr = yt.Search.GetVideos("imac g3")
print("  PagedSearchResults: %s results:" % len(pr.Results))
for vsr in pr.Videos():
    print("      VideoSearchResult: Id: %s, Title: %s, Author: %s, Duration: %s" % (vsr.Id, vsr.Title, vsr.Author, vsr.Duration))
    print("        Url: %s" % vsr.Url)
    # for th in vsr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = vsr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 

print()
print("Testing Search.GetVideos() (Page 2)")
pr2 = yt.Search.GetVideos("imac g3", pr.ContinuationToken)
print("  PagedSearchResults: %s results:" % len(pr2.Results))
for vsr in pr2.Videos():
    print("      VideoSearchResult: Id: %s, Title: %s, Author: %s, Duration: %s" % (vsr.Id, vsr.Title, vsr.Author, vsr.Duration))
    print("        Url: %s" % vsr.Url)
    # for th in vsr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = vsr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 

print()
print("Testing Search.GetChannels()")
pr = yt.Search.GetChannels("imac g3")
print("  PagedSearchResults: %s results:" % len(pr.Results))
for csr in pr.Channels():
    print("      ChannelSearchResult: Id: %s" % csr.Id)
    print("        Url: %s" % csr.Url)
    # for th in csr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = csr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 

print()
print("Testing Search.GetPlaylists()")
pr = yt.Search.GetPlaylists("imac g3")
print("  PagedSearchResults: %s results:" % len(pr.Results))
for psr in pr.Playlists():
    print("      PlaylistSearchResult: Id: %s, Author: %s" % (vsr.Id, vsr.Author))
    print("        Url: %s" % psr.Url)
    # for th in psr.Thumbnails:
    #     print("        Thumbnail: Resolution: %s" % th.Resolution) 
    #     print("          Url: %s" % th.Url) 
    th = psr.Thumbnails[0]
    print("        Thumbnail[0]: Resolution: %s" % th.Resolution)
    print("          Url: %s" % th.Url) 

print()
print("Testing Videos.Get()")
v = yt.Videos.Get(v_id)
print("  Video.Url:", v.Url)
print("  Video.Title:", v.Title)
print("  Video.Description.splitlines()[0]:", v.Description.splitlines()[0])
print("  Video.Author:", v.Author)
print("  Video.UploadDate:", v.UploadDate)
print("  Video.Duration:", v.Duration)
print("  Video.Thumbnails:", v.Thumbnails)
# for th in v.Thumbnails:
#     print("    Thumbnail: Resolution: %s" % th.Resolution)
#     print("      Url: %s" % th.Url)
th = v.Thumbnails[0]
print("    Thumbnail[0]: Resolution: %s" % th.Resolution)
print("      Url: %s" % th.Url) 
print("  Video.Keywords:", v.Keywords)
print("    Video.Keyword[0]:", v.Keywords[0])
print("  Video.Engagement.ViewCount:", v.Engagement.ViewCount)
print("  Video.Engagement.LikeCount:", v.Engagement.LikeCount)
print("  Video.Engagement.DislikeCount:", v.Engagement.DislikeCount)

print()
print("Testing Videos.Streams.GetManifest()")
m = yt.Videos.Streams.GetManifest(v_id)
print("  Testing StreamManifest.GetAudioOnlyStreams()")
for s in m.GetAudioOnlyStreams():
    print("    Container: %s, AudioCodec: %s, Bitrate: %s, Size: %s" % (s.Container, s.AudioCodec, s.Bitrate, s.Size))
#    print("      Url: %s" % s.Url)
print("  Testing StreamManifest.GetVideoOnlyStreams()")
for s in m.GetVideoOnlyStreams():
    print("    Container: %s, VideoCodec: %s, Bitrate: %s, Size: %s, VideoQuality: %s, VideoResolution: %s" % (s.Container, s.VideoCodec, s.Bitrate, s.Size, s.VideoQuality, s.VideoResolution))
#    print("      Url: %s" % s.Url)
print("  Testing StreamManifest.GetMuxedStreams()")
for s in m.GetMuxedStreams():
    print("    Container: %s, VideoCodec: %s, Bitrate: %s, Size: %s, VideoQuality: %s, VideoResolution: %s, AudioCodec: %s" % (s.Container, s.VideoCodec, s.Bitrate, s.Size, s.VideoQuality, s.VideoResolution, s.AudioCodec))
#    print("      Url: %s" % s.Url)

print()
print("Testing Videos.Streams.Get()")
s = list(m.GetAudioOnlyStreams())[1]
#ss = yt.Videos.Streams.Get(s)
#print("  Stream: %s" % ss)

print("Testing Videos.Streams.Download()")
yt.Videos.Streams.Download(s, "/tmp/stream")

print()
print("Testing Videos.ClosedCaptions.GetManifest()")
m = yt.Videos.ClosedCaptions.GetManifest(v_id)
for ccti in m.Tracks:
    print("  ClosedCaptionTrackInfo: Language: %s" % ccti.Language)
    #print("    Url: %s" % ccti.Url)
ccti = list(m.Tracks)[0]
cct = yt.Videos.ClosedCaptions.Get(ccti)
print("  ClosedCaptionTrack: Captions: %s" % cct.Captions)
cc = list(cct.Captions)[2]
print("  ClosedCaption[1]: Text: %s, Offset: %s, Duration: %s" % (cc.Text.rstrip(), cc.Offset, cc.Duration))

print()
print("Testing Videos.ClosedCaptions.Download()")
yt.Videos.ClosedCaptions.Download(ccti, "/tmp/cc.srt")
