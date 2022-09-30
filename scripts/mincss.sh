#!/usr/bin/env sh

set -e

main() {
    if [ "$CI" ]; then
        echo 'Minifying all CSS'

        [ -d 'content/styles/' ] || return

        find content/styles/ -not -ipath "./node_modules/*" -type f \
            -name "*.js" ! -name "*.min.*" ! -name "vfs_fonts*" \
            -exec uglifycss --output {}.min {} \; \
            -exec rm {} \; \
            -exec mv {}.min {} \;
    else
        echo 'Not in CI mode, skipping CSS minification'
    fi
}

main "$@"
