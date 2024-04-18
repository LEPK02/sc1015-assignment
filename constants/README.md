FULL_COLUMNS_DICT structure:
```python
{
    'meta': {
        'aggregated': [list of aggregated meta cols from teams + scores],
        'unaggregated': [list of unaggregated meta cols from teams + scores]
    },
    'attack': {
        'aggregated': [list of aggregated attack cols from teams + scores],
        'unaggregated': [list of unaggregated attack cols from teams + scores]
    },
    ...
}
```

FULL_AGG_COLUMNS_DICT structure:
``` python
{
    'meta': [list of updated aggregated cols],
    'squad': [list of updated aggregated cols],
    ...
}
```

AGG_COL_TO_CAT_DICT structure:
```python
{
    'gk_pens_saved_per90': 'gk',
    'tackles_won_per90': 'defence'
    ...
}
```
