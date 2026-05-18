export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // 1. CMS schickt uns zum Login
    if (url.pathname === "/auth") {
      const redirectUrl = `https://github.com/login/oauth/authorize?client_id=${env.GITHUB_CLIENT_ID}&scope=repo,user`;
      return Response.redirect(redirectUrl, 302);
    }

    // 2. GitHub schickt uns nach Login zurück
    if (url.pathname === "/callback") {
      const code = url.searchParams.get("code");
      if (!code) return new Response("Missing code", { status: 400 });

      const response = await fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "User-Agent": "Cloudflare-Worker"
        },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code: code
        })
      });

      const data = await response.json();
      const token = data.access_token;

      if (!token) return new Response("Fehler beim Token-Abruf", { status: 500 });

      const html = `
        <!DOCTYPE html>
        <html>
        <body>
          <script>
            window.opener.postMessage(
              'authorization:github:success:' + JSON.stringify({token: '${token}', provider: 'github'}),
              '*'
            );
            window.close();
          </script>
        </body>
        </html>
      `;
      return new Response(html, { headers: { "Content-Type": "text/html" } });
    }

    // 3. WICHTIG: Wenn es nicht um den Login geht, lade deine normale Webseite!
    return env.ASSETS.fetch(request);
  }
};
