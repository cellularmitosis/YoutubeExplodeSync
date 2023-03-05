using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using YoutubeExplode.Bridge;
using YoutubeExplode.Utils;
using YoutubeExplode.Utils.Extensions;

namespace YoutubeExplode.Videos.ClosedCaptions;

internal partial class ClosedCaptionController : VideoController
{
    public ClosedCaptionController(HttpClient http) : base(http)
    {
    }

    public async ValueTask<ClosedCaptionTrackResponse> GetClosedCaptionTrackResponseAsync(
        string url,
        CancellationToken cancellationToken = default)
    {
        // Enforce known format
        var urlWithFormat = url
            .Pipe(s => UriEx.SetQueryParameter(s, "format", "3"))
            .Pipe(s => UriEx.SetQueryParameter(s, "fmt", "3"));

        return ClosedCaptionTrackResponse.Parse(
            await Http.GetStringAsync(urlWithFormat, cancellationToken)
        );
    }
}

internal partial class ClosedCaptionController : VideoController
{
    public ClosedCaptionTrackResponse GetClosedCaptionTrackResponse(
        string url,
        CancellationToken cancellationToken = default)
    {
        // Enforce known format
        var urlWithFormat = url
            .Pipe(s => UriEx.SetQueryParameter(s, "format", "3"))
            .Pipe(s => UriEx.SetQueryParameter(s, "fmt", "3"));

        return ClosedCaptionTrackResponse.Parse(
            Http.GetStringAsync(urlWithFormat, cancellationToken).Result
        );
    }
}