#!/bin/bash
celery -A dream_cream_pastries_project worker --loglevel=debug --logfile=/dream_cream_pastries_project/logs/celery.log
