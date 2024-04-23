import pandas as pd
import numpy as np

TRANSLATE_COLUMNS = {'5-ročné vekové skupiny': '5-year age groups',
                     'Ekonomické vekové skupiny': 'economical age groups',
                     'Kód kraja': 'NUTS3_CODE',
                     'Kód obce': 'LAU2_CODE',
                     'Kód oblasti': 'NUTS2_CODE',
                     'Kód okresu': 'LAU1_CODE',
                     'Kód štátu': 'NUTS1_CODE',
                     'Názov kraja': 'region name',
                     'Názov obce': 'municipality name',
                     'Názov oblasti': 'NUTS2 name',
                     'Názov okresu': 'district name',
                     'Názov štátu': 'state name',
                     'Odvetvie ekonomickej činnosti\u200b (NACE - sekcie)': 'NACE section',
                     'Pohlavie': 'sex',
                     'Súčasná ekonomická aktivita': 'current economic activity',
                     'Vek': 'age',
                     'Vzdelanie': 'education',
                     'Zamestnanie '
                     '(ISCO - triedy)': 'ISCO occupation',
                     'abs.': 'count'}


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Translates names of columns from Slovak to English
    .. note:: This function doesn't translate entries in DataFrame

    :param df: DataFrame with Slovak names of columns
    :return: DataFrame with English names of columns
    """
    return df.rename(columns=TRANSLATE_COLUMNS)


def replace_with_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces entries like "nezistené" with np.NaN
    :param df: DataFrame with string literals corresponding to NaN
    :return: DataFrame with NaN values
    """
    return df.replace(['nezistené', 'dôverné'], np.NaN)
