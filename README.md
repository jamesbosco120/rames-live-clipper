# rames-live-clipper

Lanceur public de l'outil « clips pendant le live » de la chaîne Twitch **RamesRD**.

- **Lancement automatique** : quand RamesRD passe en live (PC ou téléphone), Twitch envoie la notification officielle
  `stream.online` à un relais Cloudflare qui vérifie la signature Twitch, ignore les doublons et lance l'Action
  « Live – en direct » de ce dépôt.
- **Secours manuel** : onglet *Actions* → « Live – en direct » → *Run workflow*.
- Pendant le live, l'outil enregistre, lit le chat en lecture seule (connexion anonyme), repère les moments forts et en
  garde au plus un toutes les 45 minutes.

## Ce qui n'est PAS ici (volontairement)
Le moteur de sélection, les critères, le seuil, les statistiques, le montage et la publication restent dans un dépôt
privé, lu au moment du live avec une clé cachée (`PRIVE_TOKEN`, secret GitHub). Voir [SECURITE.md](SECURITE.md).

## Démo client (18/11/2026)
Deux autres Actions servent à démarcher des streamers : **« Démo client – veille »** (toutes les 10 min, regarde si une
chaîne à démarcher est en live) et **« Démo client – en direct »** (clips du live, rangés dans un Drive privé).
Rien n'est publié. Le nom de la chaîne n'apparaît jamais dans les journaux (masqué, repère anonyme).
