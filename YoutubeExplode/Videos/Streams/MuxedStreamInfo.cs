using System.Diagnostics.CodeAnalysis;
using YoutubeExplode.Common;

namespace YoutubeExplode.Videos.Streams;

/// <summary>
/// Metadata associated with a muxed (audio + video combined) media stream.
/// </summary>
public partial class MuxedStreamInfo : IAudioStreamInfo, IVideoStreamInfo
{
    /// <inheritdoc />
    public string Url { get; }

    /// <inheritdoc />
    public Container Container { get; }

    /// <inheritdoc />
    public FileSize Size { get; }

    /// <inheritdoc />
    public Bitrate Bitrate { get; }

    /// <inheritdoc />
    public string AudioCodec { get; }

    /// <inheritdoc />
    public string VideoCodec { get; }

    /// <inheritdoc />
    public VideoQuality VideoQuality { get; }

    /// <inheritdoc />
    public Resolution VideoResolution { get; }

    /// <summary>
    /// Initializes an instance of <see cref="MuxedStreamInfo" />.
    /// </summary>
    public MuxedStreamInfo(
        string url,
        Container container,
        FileSize size,
        Bitrate bitrate,
        string audioCodec,
        string videoCodec,
        VideoQuality videoQuality,
        Resolution resolution)
    {
        Url = url;
        Container = container;
        Size = size;
        Bitrate = bitrate;
        AudioCodec = audioCodec;
        VideoCodec = videoCodec;
        VideoQuality = videoQuality;
        VideoResolution = resolution;
    }

    /// <inheritdoc />
    [ExcludeFromCodeCoverage]
    public override string ToString() => $"Muxed ({VideoQuality} | {Container})";
}

public partial class MuxedStreamInfo : IAudioStreamInfo, IVideoStreamInfo
{
    public string Id {
        get {
            string[] components = {
                this.Container.Name,
                this.VideoCodec,
                this.VideoResolution.ToString(),
                this.AudioCodec,
                this.Bitrate.BitsPerSecond.ToString(),
                this.Size.Bytes.ToString()
            };
            return string.Join(".", components);
        }
    }

    public AudioOnlyStreamInfo? asAudioOnlyStreamInfo()
    {
        return null;
    }

    public VideoOnlyStreamInfo? asVideoOnlyStreamInfo()
    {
        return null;
    }

    public MuxedStreamInfo? asMuxedStreamInfo()
    {
        return this as MuxedStreamInfo;
    }
}
