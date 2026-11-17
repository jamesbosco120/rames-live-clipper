#!/usr/bin/env python3
"""Contrôle de sécurité : rien de privé dans un journal d'Action ou dans le code de ce dépôt public.

  python3 outils/verifier_journal.py <journal.txt | dossier> [--mots-prives fichier]
Cherche : clés (GitHub, Cloudflare, Twitch, Google…), liens Drive / Docs, liens d'Apps Script, scores et critères
(« score », « seuil », « facteurs », « pourquoi », « contexte : »), et les mots d'une liste privée facultative
(ex. les listes ✅ / ❌ fournies au moment du test, jamais rangées ici). Code 1 au moindre doute.
"""
import re, sys
from pathlib import Path

MOTIFS = {
    "jeton GitHub": r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}",
    "jeton Cloudflare/Twitch (long secret)": r"(?i)(secret|token|cle|key)\s*[=:]\s*[A-Za-z0-9_\-]{20,}",
    "lien Drive / Docs": r"drive\.google\.com/|docs\.google\.com/",
    "relais Apps Script": r"script\.google\.com/macros",
    "lien HLS signé": r"usher\.ttvnw\.net|ttvnw\.net/.+sig=",
    "score ou critère": r"(?i)\bscore\b\s*[:=]?\s*\d|\bseuil\b\s*[:=]?\s*\d|facteurs|pourquoi|contexte\s*:|mots_emotion|mots_contexte|eliminatoires|\+\d+(\.\d)? dB",
}


def verifier(texte: str, mots: list[str]) -> list[str]:
    pb = [f"{nom} : « {m.group(0)[:40]} »" for nom, rx in MOTIFS.items() for m in [re.search(rx, texte)] if m]
    low = texte.lower()
    pb += [f"mot privé : « {w} »" for w in mots if w and re.search(rf"(?<!\w){re.escape(w.lower())}(?!\w)", low)]
    return pb


if __name__ == "__main__":
    cible = Path(sys.argv[1])
    mots = []
    if "--mots-prives" in sys.argv:
        mots = [l.strip() for l in Path(sys.argv[sys.argv.index("--mots-prives") + 1]).read_text().splitlines() if l.strip()]
    fichiers = [cible] if cible.is_file() else [f for f in cible.rglob("*") if f.is_file() and ".git" not in f.parts]
    total = 0
    for f in fichiers:
        if f.resolve() == Path(__file__).resolve():
            continue                       # ce fichier contient les motifs eux-mêmes
        for p in verifier(f.read_text(errors="ignore"), mots):
            print(f"❌ {f} : {p}")
            total += 1
    print("✅ Rien de privé trouvé." if not total else f"❌ {total} problème(s).")
    sys.exit(1 if total else 0)
