import json
import requests


def read_api(gen, start, end, forms):
    dex = []

    print("Gathering data...")
    for x in range(start, end + 1):
        i = str(x)
        dex = create_request(i, gen, forms, dex)
        print("Gathered data for Pokémon #" + i)

    print("Gathering data complete!\n")
    return dex


def create_request(i, gen, forms, dex):
    alt = forms["forms"]
    gender = forms["gender-based"]
    regional = forms["regional variant"]
    
    dex.append(get_response(i, i))
    match i:  # Go through each Pokémon in National Dex order
        case "19":
            if regional and gen >= 7:
                dex.append(get_response(i, "rattata-alola"))
        case "20":
            if regional and gen >= 7:
                dex.append(get_response(i, "raticate-alola"))
        case "26":
            if regional and gen >= 7:
                dex.append(get_response(i, "raichu-alola"))
        case "27":
            if regional and gen >= 7:
                dex.append(get_response(i, "sandshrew-alola"))
        case "28":
            if regional and gen >= 7:
                dex.append(get_response(i, "sandslash-alola"))
        case "37":
            if regional and gen >= 7:
                dex.append(get_response(i, "vulpix-alola"))
        case "38":
            if regional and gen >= 7:
                dex.append(get_response(i, "ninetales-alola"))
        case "50":
            if regional and gen >= 7:
                dex.append(get_response(i, "diglett-alola"))
        case "51":
            if regional and gen >= 7:
                dex.append(get_response(i, "dugtrio-alola"))
        case "52":
            if regional and gen >= 7:
                dex.append(get_response(i, "meowth-alola"))
            if regional and gen >= 8:
                dex.append(get_response(i, "meowth-galar"))
        case "53":
            if regional and gen >= 7:
                dex.append(get_response(i, "persian-alola"))
        case "58":
            if regional and gen >= 8:
                dex.append(get_response(i, "growlithe-hisui"))
        case "59":
            if regional and gen >= 8:
                dex.append(get_response(i, "arcanine-hisui"))
        case "74":
            if regional and gen >= 7:
                dex.append(get_response(i, "geodude-alola"))
        case "75":
            if regional and gen >= 7:
                dex.append(get_response(i, "graveler-alola"))
        case "76":
            if regional and gen >= 7:
                dex.append(get_response(i, "golem-alola"))
        case "77":
            if regional and gen >= 8:
                dex.append(get_response(i, "ponyta-galar"))
        case "78":
            if regional and gen >= 8:
                dex.append(get_response(i, "rapidash-galar"))
        case "79":
            if regional and gen >= 8:
                dex.append(get_response(i, "slowpoke-galar"))
        case "80":
            if regional and gen >= 8:
                dex.append(get_response(i, "slowbro-galar"))
        case "83":
            if regional and gen >= 8:
                dex.append(get_response(i, "farfetchd-galar"))
        case "88":
            if regional and gen >= 7:
                dex.append(get_response(i, "grimer-alola"))
        case "89":
            if regional and gen >= 7:
                dex.append(get_response(i, "muk-alola"))
        case "100":
            if regional and gen >= 8:
                dex.append(get_response(i, "voltorb-hisui"))
        case "101":
            if regional and gen >= 8:
                dex.append(get_response(i, "electrode-hisui"))
        case "103":
            if regional and gen >= 7:
                dex.append(get_response(i, "exeggutor-alola"))
        case "105":
            if regional and gen >= 7:
                dex.append(get_response(i, "marowak-alola"))
        case "110":
            if regional and gen >= 8:
                dex.append(get_response(i, "weezing-galar"))
        case "122":
            if regional and gen >= 8:
                dex.append(get_response(i, "mr-mime-galar"))
        case "128":
            if regional and gen >= 9:
                dex.append(get_response(i, "tauros-paldea-combat-breed"))
                dex.append(get_response(i, "tauros-paldea-blaze-breed"))
                dex.append(get_response(i, "tauros-paldea-aqua-breed"))
        case "144":
            if regional and gen >= 8:
                dex.append(get_response(i, "articuno-galar"))
        case "145":
            if regional and gen >= 8:
                dex.append(get_response(i, "zapdos-galar"))
        case "146":
            if regional and gen >= 8:
                dex.append(get_response(i, "moltres-galar"))

        case "157":
            if regional and gen >= 8:
                dex.append(get_response(i, "typhlosion-hisui"))
        case "194":
            if regional and gen >= 9:
                dex.append(get_response(i, "wooper-paldea"))
        case "199":
            if regional and gen >= 8:
                dex.append(get_response(i, "slowking-galar"))
        case "211":
            if regional and gen >= 8:
                dex.append(get_response(i, "qwilfish-hisui"))
        case "215":
            if regional and gen >= 8:
                dex.append(get_response(i, "sneasel-hisui"))
        case "222":
            if regional and gen >= 8:
                dex.append(get_response(i, "corsola-galar"))

        case "263":
            if regional and gen >= 8:
                dex.append(get_response(i, "zigzagoon-galar"))
        case "264":
            if regional and gen >= 8:
                dex.append(get_response(i, "linoone-galar"))
        case "386":
            if alt:
                dex.append(get_response(i, "deoxys-attack"))
                dex.append(get_response(i, "deoxys-defense"))
                dex.append(get_response(i, "deoxys-speed"))

        case "413":
            if alt:
                dex.append(get_response(i, "wormadam-sandy"))
                dex.append(get_response(i, "wormadam-trash"))
        case "479":
            if alt:
                dex.append(get_response(i, "rotom-heat"))
                dex.append(get_response(i, "rotom-wash"))
                dex.append(get_response(i, "rotom-frost"))
                dex.append(get_response(i, "rotom-fan"))
                dex.append(get_response(i, "rotom-mow"))
        case "492":
            if alt:
                dex.append(get_response(i, "shaymin-sky"))

        case "502":
            if regional and gen >= 8:
                dex.append(get_response(i, "samurott-hisui"))
        case "549":
            if regional and gen >= 8:
                dex.append(get_response(i, "lilligant-hisui"))
        case "550":
            if regional and gen >= 8:
                dex.append(get_response(i, "basculin-white-striped"))
        case "554":
            if regional and gen >= 8:
                dex.append(get_response(i, "darumaka-galar"))
        case "555":
            if regional and gen >= 8:
                dex.append(get_response(i, "darmanitan-galar-standard"))
        case "562":
            if regional and gen >= 8:
                dex.append(get_response(i, "yamask-galar"))
        case "570":
            if regional and gen >= 8:
                dex.append(get_response(i, "zorua-hisui"))
        case "571":
            if regional and gen >= 8:
                dex.append(get_response(i, "zoroark-hisui"))
        case "618":
            if regional and gen >= 8:
                dex.append(get_response(i, "stunfisk-galar"))
        case "628":
            if regional and gen >= 8:
                dex.append(get_response(i, "braviary-hisui"))
        case "646":
            if alt:
                dex.append(get_response(i, "kyurem-white"))
                dex.append(get_response(i, "kyurem-black"))

        case "678":
            if gender:
                dex.append(get_response(i, "meowstic-female"))
        case "705":
            if regional and gen >= 8:
                dex.append(get_response(i, "sliggoo-hisui"))
        case "706":
            if regional and gen >= 8:
                dex.append(get_response(i, "goodra-hisui"))
        case "713":
            if regional and gen >= 8:
                dex.append(get_response(i, "avalugg-hisui"))
        case "720":
            if alt:
                dex.append(get_response(i, "hoopa-unbound"))

        case "724":
            if regional and gen >= 8:
                dex.append(get_response(i, "decidueye-hisui"))
        case "745":
            if alt:
                dex.append(get_response(i, "lycanroc-midnight"))
                dex.append(get_response(i, "lycanroc-dusk"))
        case "800":
            if alt:
                dex.append(get_response(i, "necrozma-dusk"))
                dex.append(get_response(i, "necrozma-dawn"))
                dex.append(get_response(i, "necrozma-ultra"))

        case "849":
            if alt:
                dex.append(get_response(i, "toxtricity-low-key"))
        case "876":
            if gender:
                dex.append(get_response(i, "indeedee-female"))
        case "892":
            if alt:
                dex.append(get_response(i, "urshifu-rapid-strike"))
        case "898":
            if alt:
                dex.append(get_response(i, "calyrex-ice"))
                dex.append(get_response(i, "calyrex-shadow"))
        case "902":
            if gender:
                dex.append(get_response(i, "basculegion-female"))

        case "916":
            if gender:
                dex.append(get_response(i, "oinkologne-female"))

    return dex


def get_response(index, name):
    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(base_url + name + '/')
    entry = json.loads(response.text)
    entry["id"] = index
    return entry
