using System;
using System.Collections.Generic;
using System.Linq;
using YoutubeExplode.Utils;

namespace YoutubeExplode.Videos.Streams;

/// <summary>
/// Metadata associated with a media stream of a YouTube video.
/// </summary>
public partial interface IStreamInfo
{
    /// <summary>
    /// Stream URL.
    /// </summary>
    string Url { get; }

    /// <summary>
    /// Stream container.
    /// </summary>
    Container Container { get; }

    /// <summary>
    /// Stream size.
    /// </summary>
    FileSize Size { get; }

    /// <summary>
    /// Stream bitrate.
    /// </summary>
    Bitrate Bitrate { get; }
}

/// <summary>
/// Extensions for <see cref="IStreamInfo" />.
/// </summary>
public static class StreamInfoExtensions
{
    internal static bool IsThrottled(this IStreamInfo streamInfo) => !string.Equals(
        UriEx.TryGetQueryParameterValue(streamInfo.Url, "ratebypass"),
        "yes",
        StringComparison.OrdinalIgnoreCase
    );

    /// <summary>
    /// Gets the stream with the highest bitrate.
    /// Returns null if the sequence is empty.
    /// </summary>
    public static IStreamInfo? TryGetWithHighestBitrate(this IEnumerable<IStreamInfo> streamInfos) =>
        streamInfos.OrderByDescending(s => s.Bitrate).FirstOrDefault();

    /// <summary>
    /// Gets the stream with the highest bitrate.
    /// </summary>
    public static IStreamInfo GetWithHighestBitrate(this IEnumerable<IStreamInfo> streamInfos) =>
        streamInfos.TryGetWithHighestBitrate() ??
        throw new InvalidOperationException("Input stream collection is empty.");
}

public partial interface IStreamInfo
{
    string Id { get; }
    AudioOnlyStreamInfo? asAudioOnlyStreamInfo();
    VideoOnlyStreamInfo? asVideoOnlyStreamInfo();
    MuxedStreamInfo? asMuxedStreamInfo();
}
