import sys

file_path = '/home/kevin/Downloads/coexistence-walk_webseite/index.html'

with open(file_path, 'r') as f:
    lines = f.readlines()

new_form = """          <form action="https://formspree.io/f/xgorblbb" method="POST">
            <input type="hidden" name="_subject" value="Neue Anmeldung – Coexistence Walk" />
            <input type="hidden" name="_redirect" value="https://www.coexistence-walk.de/danke.html" />
            <input type="hidden" name="_captcha" value="false" />

            <div class="form-row">
              <div class="form-group">
                <label>Vorname & Nachname</label>
                <input type="text" name="name" placeholder="Max Mustermann" required />
              </div>
              <div class="form-group">
                <label>E-Mail-Adresse</label>
                <input type="email" name="email" placeholder="deine@email.de" required />
              </div>
            </div>

            <div class="form-group">
              <label>Telefonnummer (für Notfälle vor Ort)</label>
              <input type="tel" name="telefon" placeholder="+49 ..." required />
            </div>

            <div class="form-group">
              <label>Ich möchte teilnehmen am:</label>
              <div style="display:flex; flex-direction:column; gap:0.5rem; margin-top:0.5rem;">
                <label style="font-weight:normal; display:flex; align-items:center; gap:0.5rem; cursor:pointer;">
                  <input type="radio" name="teilnahme" value="Gesamter Zeitraum (29.05. – 06.06.2026)" required />
                  <span>Gesamter Zeitraum (29.05. – 06.06.2026)</span>
                </label>
                <label style="font-weight:normal; display:flex; align-items:center; gap:0.5rem; cursor:pointer;">
                  <input type="radio" name="teilnahme" value="Einzelne Etappen" id="einzelneEtappenRadio" required />
                  <span>Einzelne Etappen</span>
                </label>
                <input type="text" name="einzelne_etappen_datum" placeholder="Bitte Datum angeben (z.B. 30.05. - 31.05.)"
                  style="margin-top:0.25rem; display:none;" id="einzelneEtappenInput" />
              </div>
            </div>

            <div class="form-group">
              <label>Logistik & Sicherheit</label>
              <div style="display:flex; flex-direction:column; gap:1rem; margin-top:0.5rem; background:rgba(255,255,255,0.4); padding:1.25rem; border-radius:6px; border:1px solid rgba(0,0,0,0.05);">
                <div>
                  <span style="font-size:0.9rem; color:var(--bark); font-weight:500;">Wandert ein Hund mit?</span>
                  <div style="display:flex; gap:1.5rem; margin-top:0.5rem;">
                    <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
                      <input type="radio" name="hund" value="Ja" required /> Ja
                    </label>
                    <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
                      <input type="radio" name="hund" value="Nein" required /> Nein
                    </label>
                  </div>
                </div>
                <hr style="border:none; border-top:1px solid rgba(0,0,0,0.06); margin:0;"/>
                <div>
                  <span style="font-size:0.9rem; color:var(--bark); font-weight:500;">Benötigen Sie einen Gepäcktransfer?</span>
                  <div style="display:flex; gap:1.5rem; margin-top:0.5rem;">
                    <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
                      <input type="radio" name="gepaeck" value="Ja" required /> Ja
                    </label>
                    <label style="font-weight:normal; display:flex; align-items:center; gap:0.4rem; cursor:pointer;">
                      <input type="radio" name="gepaeck" value="Nein" required /> Nein
                    </label>
                  </div>
                </div>
                <div style="font-size:0.85rem; color:var(--sand); margin-top:0.2rem; display:flex; align-items:center; gap:0.4rem;">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                  Beachte: Selbstverpflegung!
                </div>
              </div>
            </div>

            <div class="form-group">
              <label>Rechtliches</label>
              <div style="display:flex; flex-direction:column; gap:0.8rem; margin-top:0.5rem; background:rgba(255,255,255,0.4); padding:1.25rem; border-radius:6px; border:1px solid rgba(0,0,0,0.05);">
                <label style="font-weight:normal; display:flex; align-items:flex-start; gap:0.6rem; font-size:0.85rem; line-height:1.4; cursor:pointer;">
                  <input type="checkbox" name="privat_exkursion" required style="margin-top:0.15rem; flex-shrink:0;" />
                  <span>Ich habe zur Kenntnis genommen, dass es sich um eine private Exkursion (Interessengemeinschaft) und nicht um eine Demonstration handelt.</span>
                </label>
                <label style="font-weight:normal; display:flex; align-items:flex-start; gap:0.6rem; font-size:0.85rem; line-height:1.4; cursor:pointer;">
                  <input type="checkbox" name="unterkunft_selbstbuchung" required style="margin-top:0.15rem; flex-shrink:0;" />
                  <span>Mir ist bewusst, dass Hotelzimmer oder sonstige Unterkünfte selbstständig und separat nach eigenen Wünschen gebucht werden müssen.</span>
                </label>
                <label style="font-weight:normal; display:flex; align-items:flex-start; gap:0.6rem; font-size:0.85rem; line-height:1.4; cursor:pointer;">
                  <input type="checkbox" name="agb" required style="margin-top:0.15rem; flex-shrink:0;" />
                  <span>Ich akzeptiere die <a href="teilnahmebedingungen.html" target="_blank" style="color:var(--fern); text-decoration:underline; text-underline-offset:2px;">Teilnahmebedingungen</a> und den Haftungsausschluss.</span>
                </label>
              </div>
            </div>

            <button type="submit" class="btn btn-primary" style="width:100%; justify-content:center; margin-top:0.5rem;">Anmeldung absenden</button>
          </form>
"""

# The form starts at line 2727 (index 2726) and the duplicated garbage ends at line 2879 (index 2878).
# So we keep lines up to index 2726, add our new form, and append from index 2879.
new_lines = lines[:2726] + [new_form] + lines[2879:]

with open(file_path, 'w') as f:
    f.writelines(new_lines)
