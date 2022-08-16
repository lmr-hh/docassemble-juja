Liebe Jazzer\*innen,

vielen Dank für Ihre Anmeldung zum Landeswettbewerb Jugend Jazzt. In dieser Mail
erhalten Sie zur Bestätigung die von Ihnen angegebenen Daten sowie die Rechnung
zur Überweisung des Teilnahmebeitrags.

Bitte beachten Sie, dass Sie noch die Namen der Musiker\*innen angeben müssen.
Die Anmeldung ist erst vollständig wenn die Namen der Musiker\*innen vorliegen.
Liegen die Namen bis zum Anmeldeschluss am 26. September nicht vor, können wir
Ihre Anmeldung nicht akzeptieren.

## Angaben zum Ensemble
|Feld                  |Ihre Angabe                                                                                                 |
|----------------------|------------------------------------------------------------------------------------------------------------|
|Name                  |${ verbatim(ensemble.name) }                                                                                |
|Künstlerische Leitung |${ verbatim(ensemble.leader) } ${ '&lt;' + ensemble.leader_mail + '&gt;' if ensemble.leader_mail else '' }  |
|Größe                 |${ ensemble.size }                                                                                          |
|Homepage              |${ verbatim(ensemble.homepage) }                                                                            |
|Facebook              |${ verbatim(ensemble.facebook) }                                                                            |
|Twitter               |${ verbatim(ensemble.twitter) }                                                                             |
|Instagram             |${ verbatim(ensemble.instagram) }                                                                           |
|Sonstige Präsenzen    |${ verbatim(ensemble.presences) }                                                                           |

### Beschreibungstext

${ quote_paragraphs(ensemble.description) }

## Administrativer Kontakt

|Feld           |Ihre Angabe                               |
|---------------|------------------------------------------|
|Name           |${ verbatim(admin_contact.name) }         |
|Funktion       |${ verbatim(admin_contact.role) }         |
|E-Mail         |${ verbatim(admin_contact.email) }        |
|Telefonnummer  |${ verbatim(admin_contact.phone_number) } |
|Adresse        |${ adresse(admin_contact) }               |

## Rechnungskontakt

|Feld          |Ihre Angabe                                 |
|--------------|--------------------------------------------|
|Name          |${ verbatim(billing_contact.name) }         |
|E-Mail        |${ verbatim(billing_contact.email) }        |
|Telefonnummer |${ verbatim(billing_contact.phone_number) } |
|Adresse       |${ adresse(admin_contact) }                 |

Viele Grüße  
Das Jugend Jazzt Team des Landesmusikrates Hamburg
