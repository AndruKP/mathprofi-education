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


def categorize_education(data):
    education_levels = set(data["Vzdelanie"].unique())
    primary = [x for x in education_levels if "základné" in x]
    education_levels -= set(primary)  # for quering purposes
    secondary = [x for x in education_levels if "stredné" in x]
    education_levels -= set(secondary)
    vocational = [x for x in education_levels if "vyššie" in x]
    education_levels -= set(vocational)
    higher = [x for x in education_levels if "vysokoškolské" in x]
    education_levels -= set(higher)
    without = [x for x in education_levels if "bez" in x]
    education_levels -= set(without)
    unspecified = ["nezistené", "dôverné"]
    education_levels -= set(unspecified)
    assert (
        len(education_levels) == 0
    ), f"{education_levels} do not correspond to any category"

    education_category_map = dict(
        [
            (level, category)
            for category, levels in zip(
                [
                    "primary",
                    "secondary",
                    "vocational",
                    "higher",
                    "without",
                    "unspecified",
                ],
                [primary, secondary, vocational, higher, without, unspecified],
            )
            for level in levels
        ]
    )
    return education_category_map
