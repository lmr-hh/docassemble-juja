Liebe\*r Herr\*Frau ${ person.name.last },

vielen Dank für Ihre Anmeldung zum Landeswettbewerb Jugend Jazzt. In dieser Mail
erhalten Sie zur Bestätigung die von Ihnen angegebenen Daten sowie die Rechnung
zur Überweisung des Teilnahmebeitrags.

Bitte beachten Sie, dass Sie noch die Namen der Musiker\*innen angeben müssen.
Die Anmeldung ist erst vollständig wenn die Namen der Musiker\*innen vorliegen.
Liegen die Namen bis zum Anmeldeschluss am 26. September nicht vor, können wir
Ihre Anmeldung nicht akzeptieren.

## Angaben zum Ensemble
| Feld                  | Ihre Angabe                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------|
| Name                  | ${ensemble.name }                                                                          |
| Künstlerische Leitung | ${ ensemble.leader } ${ '<' + ensemble.leader_mail + '>' if ensemble.leader_mail else '' } |
| Größe                 | ${ ensemble.size }                                                                         |
| Homepage              | ${ ensemble.homepage }                                                                     |
| Facebook              | ${ ensemble.facebook }                                                                     |
| Twitter               | ${ ensemble.twitter }                                                                      |
| Instagram             | ${ ensemble.instagram }                                                                    |
| Sonstige Präsenzen    | ${ ensemble.presences }                                                                    |

${ ensemble.description | quote }

## Administrativer Kontakt

| Feld                 | Ihre Angabe                     |
|----------------------|---------------------------------|
| Name                 | ${ admin_contact.name }         |
| Funktion             | ${ admin_contact.role }         |
| E-Mail               | ${ admin_contact.email }        |
| Telefonnummer        | ${ admin_contact.phone_number } |
| Adresse              | ${ adresse(admin_contact) }     |
| Newsletter-Anmeldung | ${ newsletter }                 |

## Rechnungskontakt

| Feld          | Ihre Angabe                       |
|---------------|-----------------------------------|
| Name          | ${ billing_contact.name }         |
| E-Mail        | ${ billing_contact.email }        |
| Telefonnummer | ${ billing_contact.phone_number } |
| Adresse       | ${ adresse(admin_contact) }       |

Viele Grüße  
Das Jugend Jazzt Team des Landesmusikrates Hamburg
