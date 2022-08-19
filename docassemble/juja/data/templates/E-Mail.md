Liebe Bigbandleiter\*innen, liebe Jazzer\*innen,

vielen Dank für Ihre Anmeldung zum Landeswettbewerb Jugend Jazzt für Jazzorchester
in Hamburg 2022. Hiermit bestätigen wir Ihnen den Eingang Ihrer Anmeldung. Sie
erhalten im Folgenden eine Übersicht über die von Ihnen angegebenen Daten sowie
die Rechnung zur Überweisung des Teilnahmebeitrags.

% if Mitspielende:
Bitte beachten Sie, dass die Anmeldung erst mit Eingang des Teilnahmebeitrages vollständig ist.
Ist dies bis zum Anmeldeschluss am 26. September nicht der Fall, können wir Ihre Anmeldung nicht akzeptieren.
% else:
Bitte beachten Sie, dass Sie noch die Namen der Musiker\*innen angeben müssen.
Die Anmeldung ist erst vollständig wenn die Namen der Musiker\*innen vorliegen
und der Teilnahmebetrag überwiesen ist.
Liegen die genannten Unterlagen bis zum Anmeldeschluss am 26. September nicht vor,
können wir Ihre Anmeldung nicht akzeptieren.

[Jetzt Daten angeben](${ interview_url_action('gather_members') })
% endif

Sie können diese E-Mail bei Bedarf über die "Drucken" Funktion als PDF abspeichern.

## Ihre eingereichte Anmeldung
|Feld                  |Ihre Angabe                                                                                                 |
|----------------------|------------------------------------------------------------------------------------------------------------|
|Jazzorchester         |${ verbatim(ensemble.name) }                                                                                |
|Künstlerische Leitung |${ verbatim(ensemble.leader) } ${ '&lt;' + ensemble.leader_mail + '&gt;' if ensemble.leader_mail else '' }  |
|Größe                 |${ ensemble.size }                                                                                          |
|Homepage              |${ verbatim(ensemble.homepage) }                                                                            |
|Facebook              |${ verbatim(ensemble.facebook) }                                                                            |
|Twitter               |${ verbatim(ensemble.twitter) }                                                                             |
|Instagram             |${ verbatim(ensemble.instagram) }                                                                           |
|Sonstige Präsenzen    |${ verbatim(ensemble.presences) }                                                                           |

### Beschreibungstext

${ quote_paragraphs(ensemble.description) }

---

## Administrativer Kontakt

|Feld           |Ihre Angabe                               |
|---------------|------------------------------------------|
|Name           |${ verbatim(admin_contact.name) }         |
|Funktion       |${ verbatim(admin_contact.role) }         |
|E-Mail         |${ verbatim(admin_contact.email) }        |
|Telefonnummer  |${ verbatim(admin_contact.phone_number) } |
|Adresse        |${ adresse(admin_contact) }               |

---

## Rechnungskontakt

|Feld               |Ihre Angabe                                  |
|-------------------|---------------------------------------------|
|Rechnungsempfänger |${ verbatim(billing_contact.recipient) }     |
|Kontakt            |${ verbatim(billing_contact.name) }          |
|E-Mail             |${ verbatim(billing_contact.email) }         |
|Telefonnummer      |${ verbatim(billing_contact.phone_number) }  |
|Adresse            |${ adresse(admin_contact) }                  |

---

## Programm für das Wertungsspiel

|Titel |Komponist\*in |Arrangeur\*in |Verlag |Spieldauer |
|------|--------------|--------------|-------|-----------|
% for song in songs:
|${ song.name.text } | ${ song.composer } | ${ song.arranger } | ${ song.publisher } | ${ song.duration } |
% endfor

---
% if Mitspielende:
## Musiker\*innen

|Name |Geburtstag |Wohnort |Instrument |Position |Schüler\*in |Schule |Tätigkeit |Profi |
|-----|-----------|--------|-----------|---------|------------|-------|----------|------|
% for member in members:
|${ member.name.full() } |${ member.birthday } |${ member.address.city } |${ member.instrument } |${ member.position } |${ member.student } |${ member.school } |${ member.occupation } |${ member.professional } |
% endfor

---
% endif

## Teilnahmebedingungen und Datenschutz

Sie haben für Samstag den folgenden bevorzugten Zeitraum angegeben:  
% if preferred_times.saturday:
`${ preferred_times.saturday }`
% else:
Alle Zeiten möglich
% endif

Sie haben für Sonntag den folgenden bevorzugten Zeitraum angegeben:  
% if preferred_times.sunday:
`${ preferred_times.sunday }`
% else:
Alle Zeiten möglich
% endif

Sie haben folgenden Teilnahmebedingungen zugestimmt:

- Ich nehme zustimmend zur Kenntnis, dass meinem Ensemble vom Veranstalter ein verbindliches Zeitfenster zugewiesen wird und dass die oben angegebenen Zeitwünsche ggf. nicht berücksichtigt werden können.
- Ich habe die [Teilnahmebedingungen](https://jugendjazzt-hamburg.de/images/2022/Ausschreibung_Hamburger_Landeswettbewerb_Jugend_jazzt_2022.pdf) gelesen und bin damit einverstanden.
- Ich erkläre mich damit einverstanden, die in diesem Formular angegebenen Daten im Rahmen der Vorbereitung und Durchführung des Wettbewerbs durch den Landesmusikrat Hamburg gemäß der [Datenschutzhinweise](/packagestatic/docassemble.lmrhh/datenschutzhinweise.html) verarbeitet werden.

Viele Grüße  
Das Jugend Jazzt Team des Landesmusikrates Hamburg
