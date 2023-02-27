# PuReGoMe scripts

PuReGoMe scripts contains the python and bash scripts of the 
[PuReGoMe project](https://research-software-directory.org/projects/puregome)
of the Netherlands eScience Center and the University of Utrecht,
except for the script involving querying the data based on content, 
those are available in a separate repository 
[PuReGoMe queries](https://github.com/puregome/queries).

The most important script is 
[text-unique.py](https://github.com/puregome/scripts/blob/master/src/puregome_scripts/text_unique.py)
which is being used for removing duplicate tweets from the data.

## Installation

- `pip install -r requirements.txt`
- `pip install .`

## Testing

- `pytest tests`

## Contact

Erik Tjong Kim Sang `e.tjongkimsang@esciencecenter.nl`
