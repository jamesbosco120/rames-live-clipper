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

## Rafale et cerveau (20/11/2026)
Le forfait de minutes du dépôt privé étant épuisé, les Actions qui tournent souvent sont lancées d'ici :
**« Rafale – file »** (toutes les 10 min), **« Rafale – Facebook »** et **« Publication directe »** (toutes les heures),
**« Cerveau – copie vivante »** (toutes les heures et après chaque passage de Rafale). Même modèle que le live : le code,
la file, le journal et les réglages restent privés ; le journal affiché ici ne montre que des états généraux (« § … »).
Deux échecs de suite → notification ntfy.

## Sondages et stories Twitch (21/11/2026)
- **« Live – relais : mise en ligne »** : envoie le relais Cloudflare (passage en live + sondages Twitch en 1 touche).
- **« Stories Twitch – pack du jour »** (chaque matin) : prépare 3 à 5 vidéos courtes dans un Drive privé et programme
  3 rappels sur le téléphone. Twitch n'a pas d'API pour publier une story : rien n'est publié automatiquement.

## Tout passe par ici jusqu'au 1er décembre (22/11/2026)
Le compte GitHub est en offre gratuite : les minutes des dépôts privés de novembre sont épuisées, celles des dépôts
publics sont gratuites et sans limite. Nouveau : **« Vitrine – mise en ligne »** (à la main seulement) envoie un site de
l'Usine DEV sur Cloudflare Pages (aperçu ou vraie version). Il lit le code privé avec `PRIVE_TOKEN` et a besoin des
secrets `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` dans ce dépôt (comme « Rafale – mise en ligne de l'appli » et
« Live – relais : mise en ligne »). Aucun code de site ici, journal filtré, aucun artifact.

## Bande-annonce (22/11/2026)
**« Bande-annonce – rendu et Drive »** (à la main seulement) : refait la bande-annonce Twitch à partir du montage gardé
dans le dépôt privé (images de James, musique libre de droits) et l'envoie dans un Drive privé. Rien n'est publié.

## Sauvegarde de nuit (22/11/2026)
**« Sauvegarde de nuit »** (chaque nuit, 03 h 37 heure de France) : copie les données importantes (inscrits du giveaway,
données de Rafale, réglages) dans un Drive **privé**. Ce lanceur a la permission `id-token: write` : GitHub lui donne un
badge signé que seuls le giveaway et Rafale savent vérifier, sans aucune clé partagée. Ce badge n'est jamais donné à une
pull request ni à un fork. Journal filtré (nombres seulement), aucun artifact.
