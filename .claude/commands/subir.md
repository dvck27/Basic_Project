---
description: Publica los cambios locales en GitHub (validación + stage + commit + push)
---

Publica los cambios actuales del repositorio en GitHub (`origin`, rama `main`).

Pasos:
1. Ejecuta `git status` y revisa el diff para ver exactamente qué cambió. Detente ante cambios ajenos o secretos.
2. Stagea todo: `git add -A` (respeta `.gitignore`) y valida con `git diff --cached --check` y
   `git diff --cached --stat`.
3. Crea el commit con un mensaje conciso en español, en modo imperativo, que resuma los cambios.
   Si el usuario pasó un mensaje en `$ARGUMENTS`, úsalo como mensaje del commit.
4. Ejecuta `git push origin main`; si la rama aún no tiene upstream, usa `git push -u origin main`.
5. Verifica con `git branch -vv` y `git log origin/main..HEAD`, que debe quedar vacío.
6. Confirma al usuario qué se commiteó y que se publicó en GitHub.

Nunca pidas ni muestres contraseñas/tokens. Si Git Credential Manager solicita autenticación,
indica al usuario que la complete en su diálogo seguro, no en el chat ni en archivos versionados.
