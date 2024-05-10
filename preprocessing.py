import pandas as pd
import numpy as np

TRANSLATE_COLUMNS = {'5-ročné vekové skupiny': 'year_5_age_groups',
                     'Ekonomické vekové skupiny': 'economical_age_groups',
                     'Kód kraja': 'NUTS3_CODE',
                     'Kód obce': 'LAU2_CODE',
                     'Kód oblasti': 'NUTS2_CODE',
                     'Kód okresu': 'LAU1_CODE',
                     'Kód štátu': 'NUTS1_CODE',
                     'Názov kraja': 'region_name',
                     'Názov obce': 'municipality_name',
                     'Názov oblasti': 'NUTS2_name',
                     'Názov okresu': 'district_name',
                     'Názov štátu': 'state_name',
                     'Odvetvie ekonomickej činnosti\u200b (NACE - sekcie)': 'NACE_section',
                     'Pohlavie': 'sex',
                     'Súčasná ekonomická aktivita': 'current_economic_activity',
                     'Vek': 'age',
                     'Vzdelanie': 'education',
                     'Zamestnanie '
                     '(ISCO - triedy)': 'ISCO_occupation',
                     'abs.': 'count'}

TRANSLATE_SEX = {
    'muž': 'male',
    'žena': 'female'
}


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


def age_preprocess(age_string: str):
    """
    Preprocesses age string to integer
    .. note:: Preprocesses age string (90+ age transforms into 90)
    """
    if age_string == '90 a viac rokov':
        return 90
    return int(age_string)


def translate_sex(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace(TRANSLATE_SEX)
