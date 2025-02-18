#! /bin/sh
#!/usr/bin/env python3.10

source ./.venv/bin/activate
clear && python main.py || deactivate

deactivate
