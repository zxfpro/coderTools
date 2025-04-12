#!/bin/bash

#pytest-html

#uv run pytest test/test_packager.py::test_process_github_repo

project="codertools"
uv run pytest --html=$test_html_path/$project.html
