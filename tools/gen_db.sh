#! /bin/bash

rm -f sawguq.db
python3 sawguq_generate.py -f sawcaux.txt sawguq.db
python3 sawguq_generate.py -f sawyimmoq1.txt sawguq.db
python3 sawguq_generate.py -f gvaefamh_1.txt sawguq.db
python3 sawguq_generate.py -f sawguq.txt sawguq.db
