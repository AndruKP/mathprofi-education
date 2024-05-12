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

EDUCATION_CATEGORY_MAP = {
    "základné vzdelanie - 1. stupeň základnej školy": "primary",
    "základné vzdelanie (bližšie neuvedené)": "primary",
    "základné vzdelanie - 2. stupeň základnej školy": "primary",
    "úplné stredné vzdelanie s maturitou (bližšie neuvedené)": "secondary",
    "stredné odborné (učňovské) vzdelanie bez maturity a bez výučného listu (zaškolenie, zaučenie)": "secondary",
    "úplné stredné vzdelanie s maturitou odborné (učňovské) s výučným listom": "secondary",
    "stredné odborné (učňovské) vzdelanie bez maturity (bližšie neuvedené)": "secondary",
    "úplné stredné vzdelanie s maturitou odborné": "secondary",
    "stredné odborné (učňovské) vzdelanie bez maturity s výučným listom": "secondary",
    "stredné odborné (učňovské) vzdelanie bez maturity s vysvedčením o záverečnej skúške": "secondary",
    "úplné stredné vzdelanie s maturitou všeobecné": "secondary",
    "vyššie odborné vzdelanie vyššie odborné (absolventská skúška, absolventský diplom)": "vocational",
    "vyššie odborné vzdelanie nadstavbové (maturita absolventov učebných odborov stredných odborných škôl)": "vocational",
    "vyššie odborné vzdelanie pomaturitné (pomaturitné kvalifikačné)": "vocational",
    "vyššie odborné vzdelanie (bližšie neuvedené)": "vocational",
    "vysokoškolské vzdelanie - 1. stupeň (Bc.)": "higher",
    "vysokoškolské vzdelanie (bližšie neuvedené)": "higher",
    "vysokoškolské vzdelanie - 2. stupeň (Ing.; Mgr.; MUDr.; a i.)": "higher",
    "vysokoškolské vzdelanie - 3. stupeň (PhD.; a i.)": "higher",
    "bez ukončeného vzdelania – osoby vo veku 0-14 rokov": "without",
    "bez školského vzdelania – osoby vo veku 15 rokov a viac": "without",
    "nezistené": "unspecified",
    "dôverné": "unspecified",
}

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

def group_by_education_level(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace(EDUCATION_CATEGORY_MAP)


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
