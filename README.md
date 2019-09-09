# Fys3150_Projekt_1
Computational physics project 1.

Hensikten med dette projektet er å få erfaring med å skrive vitenskaplige atrikler, utvikle gode vaner når det kommer til struktur og gjennomføring av projekter generelt. I tillegg ønsker jeg å få god kjenskap til algoritmene og metodene, slik at disse kan brukes siden.

Forsøket er en simulering av potensialet fra en ladning fra en gitt avstand fra ladningen. Jeg har sett på potensialet fra ladningen opptill en meters avstand, for å simulere potensialet har vi brukt Poissons ligning til å finne annenderiverte av potensialet. Deretter brukte jeg annenderivertes diskritisering til lage et linjært ligningsystem.

Ligningssytemet har jeg løst ved hjelp av en agumentert matrise, ved bruk av enten Thomas algoriothmen og en baklengst substutisjon eller ved hjelp av LU Decomposisjon. Så har jeg sett på hvordan potensialet ser ut sammenlignet med en analytsik løsning.

Jeg har sett på hvordan nøyaktigheten til resultatene er avhengige av å ha en liten som mulig stegstørrelse, og hvordan stegstørrelsen påvirker tiden påkrevd til å gjennomføre simulasjonen. Jeg har også sett på hvor effektive de forskjellige algoritmene oppfører seg for forskjellige n, både i tidsforbruk og minne bruk.

Ved siden av simulasjonene og sammenligningen har jeg laget unittester, unit testene er designet slik at de skal finne feil hvis koden ikke fungerer slik den skal. Dette medfører at når koden blir skrevet om og nye funksjoner blir implementert så vil koden beholde funksjonalitet.

Sist men ikke minst har jeg laget et GitHub reposetory som inneholder kildekoden jeg har utviklet i dette projektet, i tillegg til et par håndplukkede resultater som skal forsøke å vise at koden virker som den skal. GitHub reposetoryet skal også vise en ganske detaljert logg av utviklingen av koden.
