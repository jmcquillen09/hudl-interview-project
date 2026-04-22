@echo off

echo Running tests in Chrome...
python -m pytest --browser=chrome %*
if %ERRORLEVEL% neq 0 (
    echo Chrome tests FAILED
) else (
    echo Chrome tests PASSED
)

echo.
echo Running tests in Firefox...
python -m pytest --browser=firefox %*
if %ERRORLEVEL% neq 0 (
    echo Firefox tests FAILED
) else (
    echo Firefox tests PASSED
)

echo.
where safaridriver >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo Running tests in Safari...
    python -m pytest --browser=safari %*
    if %ERRORLEVEL% neq 0 (
        echo Safari tests FAILED
    ) else (
        echo Safari tests PASSED
    )
) else (
    echo Safari skipped -- safaridriver not found on this system.
)
