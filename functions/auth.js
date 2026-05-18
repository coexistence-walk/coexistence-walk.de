export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  // CORS-Header für alle Antworten definieren
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*", // Ermöglicht dem CMS den Zugriff
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };

  // Vorabanfragen (Preflight) vom Browser abfangen
  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  // Schritt 1: Das CMS schickt den Nutzer zu /auth (bzw. /functions/auth)
  if (url.pathname.endsWith("/auth")) {
    const redirectUrl = `https://github.com/login/oauth/authorize?client_id=${env.GITHUB_CLIENT_ID}&scope=repo,user`;
    return Response.redirect(redirectUrl, 302);
  }

  // Schritt 2: GitHub schickt den Nutzer nach dem Login zurück
  if (url.pathname.endsWith("/callback")) {
    const code = url.searchParams.get("code");
    if (!code) return new Response("Missing code", { status: 400, headers: corsHeaders });

    const response = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Cloudflare-Pages-Function"
      },
      body: JSON.stringify({
        client_id: env.GITHUB_CLIENT_ID,
        client_secret: env.GITHUB_CLIENT_SECRET,
        code: code
      })
    });

    const data = await response.json();
    const token = data.access_token;

    if (!token) return new Response("Fehler beim Abrufen des Tokens von GitHub", { status: 500, headers: corsHeaders });

    const html = `
      <!DOCTYPE html>
      <html>
      <body>
        <script>
          const message = {
            token: '${token}',
            provider: 'github'
          };
          window.opener.postMessage(
            'authorization:github:success:' + JSON.stringify(message),
            '*'
          );
          window.close();
        </script>
      </body>
      </html>
    `;

    return new Response(html, {
      headers: { ...corsHeaders, "Content-Type": "text/html" }
    });
  }

  return new Response("Nicht gefunden", { status: 404, headers: corsHeaders });
}
