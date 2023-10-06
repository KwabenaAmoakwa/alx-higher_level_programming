#!/bin/bash

git add .
read -p "Enter commit message: " x
git commit -m "$x"
git push
