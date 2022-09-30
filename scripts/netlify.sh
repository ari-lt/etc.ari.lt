#!/usr/bin/env sh

set -xe

main() {
    if [ "$CI" ]; then
        echo 'Removing useless files'

        rm -rfv requirements.txt \
            runtime.txt \
            README.md \
            git.sh \
            scripts \
            .vscode \
            .github
    fi
}

main "$@"
