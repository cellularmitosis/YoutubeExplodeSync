using System.Diagnostics.CodeAnalysis;

namespace YoutubeExplode.Videos.Streams;

/// <summary>
/// Metadata associated with an audio-only YouTube media stream.
/// </summary>
public partial class AudioOnlyStreamInfo : IAudioStreamInfo
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

    /// <summary>
    /// Initializes an instance of <see cref="AudioOnlyStreamInfo" />.
    /// </summary>
    public AudioOnlyStreamInfo(
        string url,
        Container container,
        FileSize size,
        Bitrate bitrate,
        string audioCodec)
    {
        Url = url;
        Container = container;
        Size = size;
        Bitrate = bitrate;
        AudioCodec = audioCodec;
    }

    /// <inheritdoc />
    [ExcludeFromCodeCoverage]
    public override string ToString() => $"Audio-only ({Container})";
}

public partial class AudioOnlyStreamInfo : IAudioStreamInfo
{
    public string Id {
        get {
            string[] components = {
                this.Container.Name,
                this.AudioCodec,
                this.Bitrate.BitsPerSecond.ToString(),
                this.Size.Bytes.ToString()
            };
            return string.Join(".", components);
        }
    }

    public AudioOnlyStreamInfo? asAudioOnlyStreamInfo()
    {
        return this as AudioOnlyStreamInfo;
    }

    public VideoOnlyStreamInfo? asVideoOnlyStreamInfo()
    {
        return null;
    }

    public MuxedStreamInfo? asMuxedStreamInfo()
    {
        return null;
    }
}
