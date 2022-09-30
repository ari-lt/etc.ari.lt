#!/usr/bin/env sh

set -e

main() {
    git diff >/tmp/ari-web-etc.diff

    git add -A
    git commit -sa
    git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
}

main "$@"
