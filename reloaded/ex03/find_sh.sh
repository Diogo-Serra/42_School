#!/bin/bash
find . -type f -name "*.sh" -print0 | xargs -0 -n1 basename -s .sh

