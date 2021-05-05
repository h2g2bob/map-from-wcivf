Ugly code which makes a beautiful map.

# Usage

Download candidates:

```
curl https://candidates.democracyclub.org.uk/media/candidates-2021-05-06.csv > candidates-2021-05-06.csv
```

And run

```
python3 parse.py
```

And you'll have some svg files

## Map:

```
https://upload.wikimedia.org/wikipedia/commons/4/4f/NUTS_1_statistical_regions_of_the_United_Kingdom_map.svg
```

## More...?

Local party contact details. Someone better would have filtered to UTLA and Unitary Authorities only, or found places without even regional party information:

```
curl "https://docs.google.com/spreadsheets/d/1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E/export?format=csv&id=1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E&gid=1210343217" > parties-district.csv
curl "https://docs.google.com/spreadsheets/d/1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E/export?format=csv&id=1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E&gid=1013163356" > parties-unitary.csv
curl "https://docs.google.com/spreadsheets/d/1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E/export?format=csv&id=1DkmKrC9pMC-3db8Ka-eoG2abSU8wr637yvBVup8467E&gid=1273833263" > parties-county.csv
```
