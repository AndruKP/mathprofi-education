OCCUPATION_ISCO_GROUP = {
    "Pracovníci v osobných službách": 5,
    "Odborní pracovníci v oblasti práva, sociálnych vecí a kultúry a podobní pracovníci": 2,
    "Administratívni pracovníci v zákazníckych službách": 4,
    "Riadiaci pracovníci (manažéri) vo výrobe a v špecializovaných službách": 1,
    "Špecialisti v oblasti práva, sociálnych vecí a kultúry": 2,
    "Administratívni pracovníci na záznam číselných a skladových údajov": 4,
    "Predavači": 5,
    "Pracovníci pri likvidácii odpadu a ostatní nekvalifikovaní pracovníci": 9,
    "Riadiaci pracovníci (manažéri) v hotelových, reštauračných, obchodných a v ostatných službách": 1,
    "Špecialisti v oblasti vedy a techniky": 2,
    "Špecialisti v oblasti informačných a komunikačných technológií": 2,
    "Kvalifikovaní robotníci v hutníctve, strojárstve a podobní robotníci": 8,
    "Montážni robotníci": 8,
    "Vodiči a obsluha pojazdných strojných zariadení": 8,
    "Technici v oblasti informačných a komunikačných technológií": 3,
    "Elektrikári a elektronici": 7,
    "Riadiaci pracovníci (manažéri)  administratívnych, podporných a obchodných  činností": 1,
    "Špecialisti administratívnych, podporných a obchodných činností": 2,
    "Technici a odborní pracovníci v oblasti vedy a techniky": 3,
    "Odborní pracovníci v zdravotníctve": 2,
    "Odborní pracovníci administratívnych, podporných a obchodných činností": 2,
    "Pracovníci v oblasti osobnej starostlivosti": 5,
    "Spracovatelia a výrobcovia potravinárskych výrobkov, výrobkov z dreva a odevov": 7,
    "Operátori stacionárnych strojov a zariadení": 8,
    "Všeobecní administratívni pracovníci a zapisovatelia": 4,
    "Pracovníci verejnej ochrany a bezpečnostných služieb": 5,
    "Učitelia a odborní pedagogickí pracovníci": 2,
    "Ostatní pomocní administratívni pracovníci": 4,
    "Špecialisti v zdravotníctve": 2,
    "Pomocní pracovníci v ťažbe, stavebníctve, výrobe a doprave": 9,
    "Pomocní pracovníci pri príprave jedla": 9,
    "Kvalifikovaní pracovníci v poľnohospodárstve (trhovo orientovaní)": 6,
    "Zákonodarcovia, ústavní činitelia, vysokí štátni úradníci a najvyšší predstavitelia podnikov a organizácií": 1,
    "Umeleckí a ruční remeselníci a tlačiari": 7,
    "Ostatné ozbrojené sily": 0,
    "Dôstojníci ozbrojených síl": 0,
    "Upratovači a pomocníci": 9,
    "Kvalifikovaní stavební robotníci a remeselníci okrem elektrikárov": 7,
    "Pomocní pracovníci v poľnohospodárstve, lesníctve a rybárstve": 9,
    "Poddôstojníci ozbrojených síl": 0,
    "Pouliční predavači a pomocní pracovníci v podobných  službách": 5,
    "Kvalifikovaní pracovníci v lesníctve, rybárstve a poľovníctve (trhovo orientovaní)": 6,
    "Farmári, rybári, poľovníci a zberači úrody (samozásobovatelia)": 6,
}

ISCO_GROUP_NAMES = [
    "Armed forces",
    "Legislators, senior officials and managers",
    "Professionals",
    "Technicians and associate professionals",
    "Clerks",
    "Service workers and shop and market sales workers",
    "Skilled agricultural and fishery workers",
    "Craft and related trades workers",
    "Plant and machine operators and assemblers",
    "Elementary occupations",
]

# OCCUPATION_ISCO_MAP = { key: ISCO_GROUP_NAMES[value] for key, value in OCCUPATION_ISCO_GROUP.items() }
# print(OCCUPATION_ISCO_MAP)

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
}
