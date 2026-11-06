# NOVA SERVICES — Contrôles avant commit

Le calculateur accepte uniquement addition, soustraction, multiplication et division. Aucun `eval` n'est utilisé. La configuration charge `APP_PASSWORD` depuis l'environnement et refuse une valeur absente ou vide sans la journaliser.

## Installation reproductible

Python 3.14 et Git sont utilisés. Depuis ce dossier sous PowerShell :

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
# Renseigner APP_PASSWORD localement, sans committer .env.
python -m pre_commit install
python -m pre_commit run --all-files
python -m pytest -q
python -m pip_audit -r requirements.txt
```

Sous Linux : `source .venv/bin/activate`. Les versions des outils sont épinglées dans `requirements-dev.txt`. Les hooks locaux pytest et pip-audit utilisent le Python de l'environnement actif. `.env` est ignoré ; `.env.example` ne contient pas de secret. La baseline de detect-secrets ne contient aucun résultat à ignorer.

Les preuves datées sont dans `preuves/`. La politique et les trois indicateurs se trouvent dans [POLITIQUE-SECURITE.md](POLITIQUE-SECURITE.md). GitHub Actions reprend les mêmes hooks sur chaque push et pull request.

## Deux problèmes corrigés

| Problème de départ | Risque | Correction | Vérification |
| --- | --- | --- | --- |
| `eval()` sur une saisie utilisateur | Exécution arbitraire de code | Liste fermée des quatre opérations | Tests des résultats et du refus des opérations inconnues |
| Mot de passe en dur | Divulgation via le dépôt et son historique | Variable d'environnement, `.env` ignoré, exemple vide | Tests valeur configurée, absente et vide ; detect-secrets |

Un véritable secret déjà exposé devrait être révoqué, même après suppression du code. Les valeurs de test du TP sont fictives.

## Réponses de compréhension

1. Un hook pre-commit exécute des contrôles avant la création d'un commit et peut le bloquer.
2. Un contrôle local aide le développeur ; la CI rejoue les règles sur le serveur, indépendamment des hooks installés localement.
3. Versionner la configuration partage les règles et leur évolution entre développeurs et CI.
4. Un motif ressemblant à un secret peut être une donnée fictive ou une référence : toute détection doit être qualifiée.
5. Une baseline inventorie des éléments examinés ; elle ne doit jamais transformer un secret réel en exception silencieuse.
6. `eval()` peut exécuter le code choisi par l'utilisateur avec les droits du processus.
7. `.env` doit rester hors du dépôt pour ne pas publier sa configuration sensible.
8. Les variables d'environnement ne gèrent pas à elles seules rotation, droits, fuites dans les logs ni historique ; un gestionnaire de secrets est préférable en production.
9. Bandit analyse des pratiques de code ; pip-audit compare les dépendances à des vulnérabilités connues.
10. Les hooks peuvent être absents ou contournés ; les tests doivent donc être rejoués en CI.
11. Les pushes directs sont interdits par les règles de protection de branche du serveur, avec revue et vérifications obligatoires.
12. Couverture des dépôts, taux de contrôles réussis et délai de correction permettent de piloter le dispositif ; leurs définitions figurent dans la politique.
