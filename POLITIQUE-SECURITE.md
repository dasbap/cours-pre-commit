# Politique de sécurisation — NOVA SERVICES

## Contrôles et blocages

Tous les dépôts doivent vérifier les espaces, fins de fichiers, gros fichiers, YAML et secrets. Les dépôts Python ajoutent Bandit, tests rapides et audit des dépendances. Ces contrôles sont obligatoires localement et sont rejoués sur tous les fichiers en CI. Un échec bloque le commit local ou la CI ; une indisponibilité du service d'audit n'est pas assimilée à un résultat sans vulnérabilité.

Les suites longues, tests d'intégration et scans d'images peuvent être réservés à la CI. Les revues humaines restent nécessaires. La branche principale doit exiger une pull request, une revue et la réussite des vérifications côté serveur. Cette politique décrit les règles visées ; leur activation doit être vérifiée sur l'hébergement utilisé.

## Faux positifs et exceptions

Chaque exception porte une référence de ticket, le fichier ou la règle exacte, une justification, un propriétaire et une date d'expiration de 30 jours maximum. Le référent sécurité approuve et réexamine l'exception ; l'auteur ne l'approuve pas seul. Il faut vérifier l'origine et l'usage d'une valeur avant de l'ajouter à une baseline. Ne pas exclure globalement un dossier pour faire disparaître une détection.

Un secret réel doit être retiré puis révoqué ou renouvelé ; traiter son historique si nécessaire. Une dépendance vulnérable sans correctif impose de qualifier l'exposition, limiter ou désactiver la fonctionnalité, rechercher une alternative et obtenir une exception temporaire avec mesures compensatoires. Sans exception approuvée, le contrôle reste bloquant.

## Responsabilités et mises à jour

Le responsable de chaque dépôt entretient les versions des hooks et dépendances ; le référent sécurité valide les exceptions et suit les vulnérabilités. Chaque mois et à chaque alerte critique, proposer une mise à jour par pull request (`pre-commit autoupdate`), consulter les changements, rejouer les contrôles et faire relire avant fusion. Les versions restent épinglées.

La clôture d'une correction exige un diff ou commit identifiable, des tests de non-régression et une nouvelle exécution réussie du contrôle concerné. Conserver les journaux avec date et référence du commit, sans secret. Les exceptions restent traçables dans les tickets et revues.

## Trois indicateurs

| Indicateur et calcul | Source | Propriétaire / fréquence | Seuil et action |
| --- | --- | --- | --- |
| Couverture : dépôts avec configuration versionnée et CI active / dépôts concernés × 100 | Inventaire et configurations CI | Responsable développement / mensuel | Moins de 100 % : affecter l'intégration des dépôts manquants |
| Réussite : exécutions CI terminées avec succès / exécutions terminées × 100, erreurs techniques distinguées | Historique CI | Responsable de dépôt / hebdomadaire | Moins de 95 % : analyser les causes ; toute CI rouge bloque la fusion |
| Délai médian : jours entre détection et correction vérifiée pour les constats clôturés | Tickets, commits et nouvelles analyses | Référent sécurité / mensuel | Dépassement des cibles : relance ; cible proposée de 2 jours critique, 7 élevée, 30 moyenne |

Sans historique ou dénominateur, afficher « non mesuré » ou « non applicable ». Aucun résultat métier n'est inventé à partir du seul TP. Une hausse des détections peut venir d'une meilleure couverture.
