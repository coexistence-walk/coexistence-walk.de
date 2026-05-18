with open('index.html', 'r') as f:
    lines = f.readlines()

header = "".join(lines[:1706])
footer = "".join(lines[2679:])

impressum_content = """
  <section class="section" style="padding-top: 150px; min-height: 70vh;">
    <div class="container" style="max-width: 800px;">
      <p class="eyebrow">Rechtliches</p>
      <h1 class="section-title">Impressum</h1>
      <div class="divider"></div>
      
      <div style="color: #3a3a30; font-size: 1rem; line-height: 1.8;">
        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 2rem; margin-bottom: 0.5rem;">Angaben gemäß § 5 DDG</h3>
        <p>Interessengemeinschaft Coexistence Walk<br>
        Vertreten durch: Peter Nawrath<br>
        Laurentiusstraße 18<br>
        52249 Eschweiler</p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 2rem; margin-bottom: 0.5rem;">Kontakt</h3>
        <p>Telefon: +49 179 7337535<br>
        E-Mail: <a href="mailto:info@coexistence-walk.de" style="color: var(--fern); text-decoration: underline;">info@coexistence-walk.de</a></p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 2rem; margin-bottom: 0.5rem;">Verantwortlich für den Inhalt nach § 18 MStV</h3>
        <p>Peter Nawrath<br>
        Laurentiusstraße 18<br>
        52249 Eschweiler</p>
      </div>
    </div>
  </section>
"""

datenschutz_content = """
  <section class="section" style="padding-top: 150px; min-height: 70vh;">
    <div class="container" style="max-width: 800px;">
      <p class="eyebrow">Rechtliches</p>
      <h1 class="section-title">Datenschutzerklärung</h1>
      <div class="divider"></div>
      
      <div style="color: #3a3a30; font-size: 1rem; line-height: 1.8;">
        <h2 style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 600; color: var(--bark); margin-top: 2.5rem; margin-bottom: 1rem;">1. Datenschutz auf einen Blick</h2>
        
        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Wer ist verantwortlich für die Datenerfassung auf dieser Website?</h3>
        <p>Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Dessen Kontaktdaten lauten:</p>
        <p>Peter Nawrath<br>
        Laurentiusstraße 18<br>
        52249 Eschweiler<br>
        Telefon: +49 179 7337535<br>
        E-Mail: <a href="mailto:info@coexistence-walk.de" style="color: var(--fern); text-decoration: underline;">info@coexistence-walk.de</a></p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Wie erfassen wir deine Daten?</h3>
        <p>Deine Daten werden zum einen dadurch erhoben, dass du uns diese mitteilst. Hierbei kann es sich z. B. um Daten handeln, die du in ein Kontaktformular eingibst. Andere Daten werden automatisch oder nach deiner Einwilligung beim Besuch der Website durch unsere IT-Systeme erfasst. Das sind vor allem technische Daten (z. B. Internetbrowser, Betriebssystem oder Uhrzeit des Seitenaufrufs).</p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Welche Rechte hast du bezüglich deiner Daten?</h3>
        <p>Du hast jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck deiner gespeicherten personenbezogenen Daten zu erhalten. Du hast außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen. Hierzu sowie zu weiteren Fragen zum Thema Datenschutz kannst du dich jederzeit an uns wenden. Des Weiteren steht dir ein Beschwerderecht bei der zuständigen Aufsichtsbehörde zu.</p>

        <h2 style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 600; color: var(--bark); margin-top: 2.5rem; margin-bottom: 1rem;">2. Datenerfassung auf dieser Website</h2>
        
        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Kontakt- und Anmeldeformulare (Formspree)</h3>
        <p>Wenn du uns per Kontakt- oder Anmeldeformular Anfragen zukommen lässt, werden deine Angaben aus dem Formular inklusive der von dir dort angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall von Anschlussfragen bei uns gespeichert. Diese Daten geben wir nicht ohne deine Einwilligung weiter.</p>
        <p>Für die technische Abwicklung unserer Formulare nutzen wir den Dienst Formspree (Formspree, Inc., USA). Wenn du das Formular absendest, werden deine eingegebenen Daten an die Server von Formspree übertragen und dort verarbeitet. Weitere Informationen zum Umgang mit Nutzerdaten findest du in der Datenschutzerklärung von Formspree: <a href="https://formspree.io/legal/privacy-policy/" target="_blank" rel="noopener noreferrer" style="color: var(--fern); text-decoration: underline;">https://formspree.io/legal/privacy-policy/</a></p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Server-Log-Dateien</h3>
        <p>Der Provider der Seiten erhebt und speichert automatisch Informationen in so genannten Server-Log-Dateien, die dein Browser automatisch an uns übermittelt. Dies sind:</p>
        <ul style="margin-left: 20px; margin-bottom: 1rem;">
          <li>Browsertyp und Browserversion</li>
          <li>verwendetes Betriebssystem</li>
          <li>Referrer URL</li>
          <li>Hostname des zugreifenden Rechners</li>
          <li>Uhrzeit der Serveranfrage</li>
          <li>IP-Adresse</li>
        </ul>
        <p>Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen.</p>

        <h2 style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 600; color: var(--bark); margin-top: 2.5rem; margin-bottom: 1rem;">3. Plugins und externe Dienste</h2>
        <p>Um unsere Website ansprechend und funktional zu gestalten, binden wir Dienste von Drittanbietern ein. Bei der Nutzung dieser Dienste wird deine IP-Adresse an die Server der jeweiligen Anbieter übertragen.</p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Google Maps</h3>
        <p>Diese Seite nutzt über eine API den Kartendienst Google Maps, um dir die Route des Walks visuell darzustellen. Anbieter ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland.</p>
        <p>Zur Nutzung der Funktionen von Google Maps ist es notwendig, deine IP-Adresse zu speichern. Diese Informationen werden in der Regel an einen Server von Google in den USA übertragen und dort gespeichert. Wir haben keinen Einfluss auf diese Datenübertragung.</p>
        <p>Mehr Informationen zum Umgang mit Nutzerdaten findest du in der Datenschutzerklärung von Google: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" style="color: var(--fern); text-decoration: underline;">https://policies.google.com/privacy</a></p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Google Web Fonts</h3>
        <p>Diese Seite nutzt zur einheitlichen Darstellung von Schriftarten so genannte Web Fonts, die von Google bereitgestellt werden. Beim Aufruf einer Seite lädt dein Browser die benötigten Web Fonts in deinen Browsercache, um Texte und Schriftarten korrekt anzuzeigen. Wenn dein Browser Web Fonts nicht unterstützt, wird eine Standardschrift von deinem Computer genutzt.</p>
        <p>Weitere Informationen zu Google Web Fonts findest du unter <a href="https://developers.google.com/fonts/faq" target="_blank" rel="noopener noreferrer" style="color: var(--fern); text-decoration: underline;">https://developers.google.com/fonts/faq</a> und in der Datenschutzerklärung von Google: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" style="color: var(--fern); text-decoration: underline;">https://policies.google.com/privacy</a></p>

        <h3 style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 600; color: var(--bark); margin-top: 1.5rem; margin-bottom: 0.5rem;">Imgix (Content Delivery Network)</h3>
        <p>Wir nutzen das Content Delivery Network (CDN) Imgix, um Bilder (z. B. Logos und Team-Fotos) auf unserer Website schnell und geräteübergreifend optimiert auszuliefern. Ein CDN ist ein Netzwerk regional verteilter und über das Internet verbundener Server. Durch die Nutzung werden technische Daten, wie deine IP-Adresse, an Server von Imgix übertragen. Anbieter ist die Zebrafish Labs, Inc. (Imgix), 423 Washington St, San Francisco, CA 94111, USA.</p>
        <p>Weitere Informationen findest du in der Datenschutzerklärung von Imgix: <a href="https://imgix.com/privacy" target="_blank" rel="noopener noreferrer" style="color: var(--fern); text-decoration: underline;">https://imgix.com/privacy</a></p>

        <p style="margin-top: 2rem; font-style: italic; color: rgba(244, 239, 228, 0.7); background: var(--bark); padding: 1rem; border-radius: 4px;">Wenn du auf Nummer sicher gehen möchtest, kannst du bezüglich der US-Dienste (Google, Formspree, Imgix) zusätzlich ein sogenanntes Cookie-Banner (Consent-Tool) auf deiner Seite einrichten. Damit holst du dir aktiv die Zustimmung der Nutzer ein, bevor Google Maps oder die externen Bilder geladen werden.</p>
      </div>
    </div>
  </section>
"""

with open('impressum.html', 'w') as f:
    f.write(header + impressum_content + footer)

with open('datenschutz.html', 'w') as f:
    f.write(header + datenschutz_content + footer)
