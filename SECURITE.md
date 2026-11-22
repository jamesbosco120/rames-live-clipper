# Sécurité (dépôt public)

1. **Clés** : uniquement dans *Settings → Secrets and variables → Actions* (`PRIVE_TOKEN`, `BRAIN_TOKEN`, `FUSION_TOKEN` (facultatif), et pour les démos clients
   `RAMES_DRIVE_RELAY_URL` / `RAMES_DRIVE_RELAY_KEY`, pour les mises en ligne Cloudflare `CLOUDFLARE_API_TOKEN` /
   `CLOUDFLARE_ACCOUNT_ID`). Jamais dans le code.
2. **Qui peut lancer** : `workflow_dispatch` (propriétaire du dépôt ou relais avec son jeton) et l'horloge de GitHub
   (« Démo client – veille », toutes les 10 min ; « Fusion auto – PR de Claude », toutes les 5 min).
   Aucune pull request, aucun « fork » ne déclenche quoi que ce soit.
3. **Journaux propres** : l'outil tourne en mode public (`LIVE_PUBLIC=1`) ; le journal complet est écrit dans un fichier
   effacé à la fin, seules les lignes « § … » (états généraux) sont affichées. Jamais de score, critère, phrase,
   pseudo du chat, lien privé ou clé. GitHub masque en plus automatiquement les secrets.
4. **Aucune vidéo stockée ici** : pas d'*artifacts*. Les moments choisis sont envoyés au dépôt privé, qui monte le
   clip et le publie (Drive → Rafale, reel d'essai Instagram). La machine de GitHub est effacée après chaque lancement.
5. **Contrôle** : `python3 outils/verifier_journal.py <journal|dossier>` cherche clés, liens privés et critères.
