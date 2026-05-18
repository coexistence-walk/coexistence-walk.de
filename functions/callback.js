export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };

  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  const code = url.searchParams.get("code");
  if (!code) {
    return new Response("Fehler: Kein Code von GitHub erhalten.", { status: 400, headers: corsHeaders });
  }

  try {
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
    const error = data.error;

    if (!token) {
      const html = `<!DOCTYPE html><html><body>
        <h2>Login fehlgeschlagen</h2>
        <p>GitHub Fehler: ${error || 'Kein Token erhalten'}</p>
        <p>Details: ${JSON.stringify(data)}</p>
      </body></html>`;
      return new Response(html, { headers: { ...corsHeaders, "Content-Type": "text/html" } });
    }

    // Erfolg: Handshake mit dem CMS durchführen, dann Token senden
    const html = `<!DOCTYPE html>
<html>
<body>
  <p>Login erfolgreich, weiterleitung...</p>
  <script>
    (function() {
      function receiveMessage(e) {
        console.log("receiveMessage", e);
        window.opener.postMessage(
          'authorization:github:success:' + JSON.stringify({
            token: ${JSON.stringify(token)},
            provider: 'github'
          }),
          e.origin
        );
      }
      window.addEventListener("message", receiveMessage, false);
      // Handshake starten: CMS mitteilen dass die Autorisierung läuft
      window.opener.postMessage("authorizing:github", "*");
    })();
  </script>
</body>
</html>`;

    return new Response(html, {
      headers: { ...corsHeaders, "Content-Type": "text/html" }
    });

  } catch (err) {
    const html = `<!DOCTYPE html><html><body>
      <h2>Serverfehler</h2>
      <p>${err.message}</p>
    </body></html>`;
    return new Response(html, { status: 500, headers: { ...corsHeaders, "Content-Type": "text/html" } });
  }
}
