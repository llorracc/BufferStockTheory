#!/bin/bash

[[ -e .latexmkrc ]] && rm .latexmkrc
ln -s .latexmkrc_build-BST-only .latexmkrc
