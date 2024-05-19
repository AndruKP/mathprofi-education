import pandas as pd

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

ECONOMIC_SECTORS_MAP = {
    'nezistené': 'undefined',
    'Ostatné činnosti': 'other activities',
    'Poľnohospodárstvo, lesníctvo a rybolov': 'primary',
    'Ťažba a dobývanie': 'primary',
    'Stavebníctvo': 'secondary',
    'Priemyselná výroba': 'secondary',
    'Veľkoobchod a maloobchod; oprava motorových vozidiel a motocyklov': 'tertiary',
    'Doprava a skladovanie': 'tertiary',
    'Ubytovacie a stravovacie služby': 'tertiary',
    'Informácie a komunikácia': 'tertiary',
    'Činnosti v oblasti nehnuteľností': 'tertiary',
    'Odborné, vedecké a technické činnosti': 'tertiary',
    'Administratívne a podporné služby': 'tertiary',
    'Vzdelávanie': 'tertiary',
    'Umenie, zábava a rekreácia': 'tertiary',
    'Činnosti extrateritoriálnych organizácií a združení': 'tertiary',
    'Zdravotníctvo a sociálna pomoc': 'tertiary',
    'Dodávka elektriny, plynu, pary a studeného vzduchu': 'tertiary',
    'Finančné a poisťovacie činnosti': 'tertiary',
    'Dodávka vody; čistenie a odvod odpadových vôd, odpady a služby odstraňovania odpadov': 'tertiary',
    'Verejná správa a obrana; povinné sociálne zabezpečenie': 'tertiary',
    'Činnosti domácností ako zamestnávateľov; nediferencované činnosti v domácnostiach produkujúce tovary a služby na vlastné použitie': 'tertiary'
}

OCCUPATION_ISCO_MAP = {
    "Pracovníci v osobných službách": "Service workers and shop and market sales workers",
    "Odborní pracovníci v oblasti práva, sociálnych vecí a kultúry a podobní pracovníci": "Professionals",
    "Administratívni pracovníci v zákazníckych službách": "Clerks",
    "Riadiaci pracovníci (manažéri) vo výrobe a v špecializovaných službách": "Legislators, senior officials and managers",
    "Špecialisti v oblasti práva, sociálnych vecí a kultúry": "Professionals",
    "Administratívni pracovníci na záznam číselných a skladových údajov": "Clerks",
    "Predavači": "Service workers and shop and market sales workers",
    "Pracovníci pri likvidácii odpadu a ostatní nekvalifikovaní pracovníci": "Elementary occupations",
    "Riadiaci pracovníci (manažéri) v hotelových, reštauračných, obchodných a v ostatných službách": "Legislators, senior officials and managers",
    "Špecialisti v oblasti vedy a techniky": "Professionals",
    "Špecialisti v oblasti informačných a komunikačných technológií": "Professionals",
    "Kvalifikovaní robotníci v hutníctve, strojárstve a podobní robotníci": "Plant and machine operators and assemblers",
    "Montážni robotníci": "Plant and machine operators and assemblers",
    "Vodiči a obsluha pojazdných strojných zariadení": "Plant and machine operators and assemblers",
    "Technici v oblasti informačných a komunikačných technológií": "Technicians and associate professionals",
    "Elektrikári a elektronici": "Craft and related trades workers",
    "Riadiaci pracovníci (manažéri)  administratívnych, podporných a obchodných  činností": "Legislators, senior officials and managers",
    "Špecialisti administratívnych, podporných a obchodných činností": "Professionals",
    "Technici a odborní pracovníci v oblasti vedy a techniky": "Technicians and associate professionals",
    "Odborní pracovníci v zdravotníctve": "Professionals",
    "Odborní pracovníci administratívnych, podporných a obchodných činností": "Professionals",
    "Pracovníci v oblasti osobnej starostlivosti": "Service workers and shop and market sales workers",
    "Spracovatelia a výrobcovia potravinárskych výrobkov, výrobkov z dreva a odevov": "Craft and related trades workers",
    "Operátori stacionárnych strojov a zariadení": "Plant and machine operators and assemblers",
    "Všeobecní administratívni pracovníci a zapisovatelia": "Clerks",
    "Pracovníci verejnej ochrany a bezpečnostných služieb": "Service workers and shop and market sales workers",
    "Učitelia a odborní pedagogickí pracovníci": "Professionals",
    "Ostatní pomocní administratívni pracovníci": "Clerks",
    "Špecialisti v zdravotníctve": "Professionals",
    "Pomocní pracovníci v ťažbe, stavebníctve, výrobe a doprave": "Elementary occupations",
    "Pomocní pracovníci pri príprave jedla": "Elementary occupations",
    "Kvalifikovaní pracovníci v poľnohospodárstve (trhovo orientovaní)": "Skilled agricultural and fishery workers",
    "Zákonodarcovia, ústavní činitelia, vysokí štátni úradníci a najvyšší predstavitelia podnikov a organizácií": "Legislators, senior officials and managers",
    "Umeleckí a ruční remeselníci a tlačiari": "Craft and related trades workers",
    "Ostatné ozbrojené sily": "Armed forces",
    "Dôstojníci ozbrojených síl": "Armed forces",
    "Upratovači a pomocníci": "Elementary occupations",
    "Kvalifikovaní stavební robotníci a remeselníci okrem elektrikárov": "Craft and related trades workers",
    "Pomocní pracovníci v poľnohospodárstve, lesníctve a rybárstve": "Elementary occupations",
    "Poddôstojníci ozbrojených síl": "Armed forces",
    "Pouliční predavači a pomocní pracovníci v podobných  službách": "Service workers and shop and market sales workers",
    "Kvalifikovaní pracovníci v lesníctve, rybárstve a poľovníctve (trhovo orientovaní)": "Skilled agricultural and fishery workers",
    "Farmári, rybári, poľovníci a zberači úrody (samozásobovatelia)": "Skilled agricultural and fishery workers",
    "nezistené": "unspecified",
    "neaplikovateľné": "inapplicable"
}

REQURED_EDUCATION_MAP = {
    "Pracovníci v osobných službách": "without",
    "Odborní pracovníci v oblasti práva, sociálnych vecí a kultúry a podobní pracovníci": "higher",
    "Administratívni pracovníci v zákazníckych službách": "secondary",
    "Riadiaci pracovníci (manažéri) vo výrobe a v špecializovaných službách": "higher",
    "Špecialisti v oblasti práva, sociálnych vecí a kultúry": "higher",
    "Administratívni pracovníci na záznam číselných a skladových údajov": "secondary",
    "Predavači": "without",
    "Pracovníci pri likvidácii odpadu a ostatní nekvalifikovaní pracovníci": "without",
    "Riadiaci pracovníci (manažéri) v hotelových, reštauračných, obchodných a v ostatných službách": "higher",
    "Špecialisti v oblasti vedy a techniky": "higher",
    "Špecialisti v oblasti informačných a komunikačných technológií": "higher",
    "Kvalifikovaní robotníci v hutníctve, strojárstve a podobní robotníci": "vocational",
    "Montážni robotníci": "vocational",
    "Vodiči a obsluha pojazdných strojných zariadení": "vocational",
    "Technici v oblasti informačných a komunikačných technológií": "higher",
    "Elektrikári a elektronici": "vocational",
    "Riadiaci pracovníci (manažéri) administratívnych, podporných a obchodných činností": "higher",
    "Špecialisti administratívnych, podporných a obchodných činností": "higher",
    "Technici a odborní pracovníci v oblasti vedy a techniky": "higher",
    "Odborní pracovníci v zdravotníctve": "higher",
    "Odborní pracovníci administratívnych, podporných a obchodných činností": "higher",
    "Pracovníci v oblasti osobnej starostlivosti": "vocational",
    "Spracovatelia a výrobcovia potravinárskych výrobkov, výrobkov z dreva a odevov": "vocational",
    "Operátori stacionárnych strojov a zariadení": "vocational",
    "Všeobecní administratívni pracovníci a zapisovatelia": "secondary",
    "Pracovníci verejnej ochrany a bezpečnostných služieb": "vocational",
    "Učitelia a odborní pedagogickí pracovníci": "higher",
    "Ostatní pomocní administratívni pracovníci": "secondary",
    "Špecialisti v zdravotníctve": "higher",
    "Pomocní pracovníci v ťažbe, stavebníctve, výrobe a doprave": "without",
    "Pomocní pracovníci pri príprave jedla": "without",
    "Kvalifikovaní pracovníci v poľnohospodárstve (trhovo orientovaní)": "vocational",
    "Zákonodarcovia, ústavní činitelia, vysokí štátni úradníci a najvyšší predstavitelia podnikov a organizácií": "higher",
    "Umeleckí a ruční remeselníci a tlačiari": "vocational",
    "Ostatné ozbrojené sily": "inapplicable",
    "Dôstojníci ozbrojených síl": "inapplicable",
    "Upratovači a pomocníci": "without",
    "Kvalifikovaní stavební robotníci a remeselníci okrem elektrikárov": "vocational",
    "Pomocní pracovníci v poľnohospodárstve, lesníctve a rybárstve": "without",
    "Poddôstojníci ozbrojených síl": "inapplicable",
    "Pouliční predavači a pomocní pracovníci v podobných službách": "without",
    "Kvalifikovaní pracovníci v lesníctve, rybárstve a poľovníctve (trhovo orientovaní)": "vocational",
    "Farmári, rybári, poľovníci a zberači úrody (samozásobovatelia)": "without",
}

TRANSLATE_SEX = {
    'muž': 'male',
    'žena': 'female'
}


def rename_columns(df: pd.DataFrame) -> None:
    """
    Translates names of columns from Slovak to English
    .. note:: This function doesn't translate entries in DataFrame

    :param df: DataFrame with Slovak names of columns
    :return: DataFrame with English names of columns
    """
    df.rename(columns=TRANSLATE_COLUMNS, inplace=True)


def group_by_education_level(df: pd.DataFrame) -> None:
    """
    Creates new column with grouping by education level
    Primary, secondary, higher, vocational and without
    """
    df['education_category'] = df['education'].map(EDUCATION_CATEGORY_MAP).astype('category')


def group_by_isco(df: pd.DataFrame) -> None:
    """
    Creates new column with grouping by ISCO classification
    See https://isco-ilo.netlify.app/en/isco-08/ ((c) 2024 International Labour Organization (ILO)) for more details
    """
    df['ISCO_group'] = df['ISCO_occupation'].map(OCCUPATION_ISCO_MAP).astype('category')


def group_by_sector(df: pd.DataFrame) -> None:
    """
    Creates new column with grouping by economic sector
    Primary, secondary, tertiary, other activities and undefined
    """
    df['NACE_group'] = df['NACE_section'].map(ECONOMIC_SECTORS_MAP).astype('category')


def age_preprocess(age_string: str) -> int:
    """
    Preprocesses age string to integer
    .. note:: Preprocesses age string (90+ age transforms into 90)

    :param age_string: string with age literal
    :return: int in [0; 90]
    """
    if age_string == '90 a viac rokov':
        return 90
    return int(age_string)


def translate_sex(df: pd.DataFrame) -> None:
    df.replace(TRANSLATE_SEX, inplace=True)


def preprocess(df: pd.DataFrame) -> None:
    """
    Combination of all preprocessing functions
    """
    rename_columns(df)
    translate_sex(df)

    if 'age' in df.columns:
        df['age'] = df['age'].apply(age_preprocess)

    if 'education' in df.columns:
        group_by_education_level(df)

    if 'ISCO_occupation' in df.columns:
        group_by_isco(df)

    if 'NACE_section' in df.columns:
        group_by_sector(df)
