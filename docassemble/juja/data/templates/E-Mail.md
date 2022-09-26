Liebe Bigbandleiter\*innen, liebe Jazzer\*innen,

vielen Dank für Ihre Anmeldung zum Landeswettbewerb Jugend Jazzt für Jazzorchester
in Hamburg 2022. Hiermit bestätigen wir Ihnen den Eingang Ihrer Anmeldung. Sie
erhalten im Folgenden eine Übersicht über die von Ihnen angegebenen Daten sowie
die Rechnung zur Überweisung des Teilnahmebeitrags.

Damit Ihre Anmeldung vollständig ist, benötigen wir von Ihnen noch folgende Daten:

- Ein vollständige Liste der teilnehmenden Musiker\*innen (exkl. Bandleader).
  Für jede Person brauchen wir folgende Angaben: Vorname, Nachname, Geburtstag,
  Wohnort, Instrument, Position (1. Trompete, ...), bei Schülern eine Angabe,
  welche Schule besucht wird, ansonsten eine Angabe der aktuellen Tätigkeit.
  Wenn Profi-Musiker\*innen dabei sind, sollten diese entsprechend gekennzeichnet
  werden.
- Eine Angabe des Programms, das gespielt wird. Für jedes der Stücke benötigen
  wir folgende Angaben: Titel, Komponist\*in, ggf. Arrangeur\*in, Verlag,
  ungefähre Spieldauer.

Beachten Sie außerdem, dass der Teilnahmebeitrag rechtzeitig überwiesen werden muss.
Liegen die genannten Unterlagen bis zum Anmeldeschluss am 3. Oktober nicht vor,
können wir Ihre Anmeldung nicht akzeptieren.

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
