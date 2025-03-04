﻿using System.Net.Http;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using YoutubeExplode.Bridge;
using YoutubeExplode.Exceptions;

namespace YoutubeExplode.Videos.Streams;

internal partial class StreamController : VideoController
{
    public StreamController(HttpClient http) : base(http)
    {
    }

    public async ValueTask<PlayerSource> GetPlayerSourceAsync(
        CancellationToken cancellationToken = default)
    {
        var iframe = await Http.GetStringAsync("https://www.youtube.com/iframe_api", cancellationToken);

        var version = Regex.Match(iframe, @"player\\?/([0-9a-fA-F]{8})\\?/").Groups[1].Value;
        if (string.IsNullOrWhiteSpace(version))
            throw new YoutubeExplodeException("Could not extract player version.");

        return PlayerSource.Parse(
            await Http.GetStringAsync(
                $"https://www.youtube.com/s/player/{version}/player_ias.vflset/en_US/base.js",
                cancellationToken
            )
        );
    }

    public async ValueTask<DashManifest> GetDashManifestAsync(
        string url,
        CancellationToken cancellationToken = default) =>
        DashManifest.Parse(
            await Http.GetStringAsync(url, cancellationToken)
        );
}

internal partial class StreamController : VideoController
{
    public PlayerSource GetPlayerSource(
        CancellationToken cancellationToken = default)
    {
        var iframe = Http.GetStringAsync("https://www.youtube.com/iframe_api", cancellationToken).Result;

        var version = Regex.Match(iframe, @"player\\?/([0-9a-fA-F]{8})\\?/").Groups[1].Value;
        if (string.IsNullOrWhiteSpace(version))
            throw new YoutubeExplodeException("Could not extract player version.");

        return PlayerSource.Parse(
            Http.GetStringAsync(
                $"https://www.youtube.com/s/player/{version}/player_ias.vflset/en_US/base.js",
                cancellationToken
            ).Result
        );
    }

    public DashManifest GetDashManifest(
        string url,
        CancellationToken cancellationToken = default
    ) {
        return DashManifest.Parse(
            Http.GetStringAsync(url, cancellationToken).Result
        );
    }
}