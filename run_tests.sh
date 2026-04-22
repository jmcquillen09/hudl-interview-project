#!/usr/bin/env bash

run_browser() {
    local browser=$1
    echo "Running tests in ${browser^}..."
    if python -m pytest --browser="$browser" "${@:2}"; then
        echo "${browser^} tests PASSED"
    else
        echo "${browser^} tests FAILED"
    fi
}

run_browser chrome "$@"
echo
run_browser firefox "$@"

if command -v safaridriver &>/dev/null; then
    echo
    run_browser safari "$@"
else
    echo
    echo "Safari skipped — safaridriver not found on this system."
fi
