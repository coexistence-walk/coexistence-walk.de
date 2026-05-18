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
