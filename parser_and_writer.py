def parse_and_write_info(filename, gen, forms, dex):

    # i = 0
    print("Parsing data into simpler form...")
    parsed_dex = []
    size = 0
    for entry in dex:
        order = entry["id"]
        name = parse_name(entry["name"], forms)
        moves = parse_moves(entry["moves"], gen)

        if len(name) > size:
            size = len(name)

        data = {
            "order": order,
            "name": name,
            "moves": moves
        }
        parsed_dex.append(data)

        print("Parsed moves for " + name)
    print("Parsing moves complete!\n")

    file = open(filename, 'w', encoding="utf-8")
    print("Writing data to file...")
    write_header(file, size)
    for data in parsed_dex:
        write_info(data["name"], data["order"], data["moves"], file, size)

    file.close()
    print("Writing data complete!")


def parse_name(raw_name, forms):
    alt = forms["forms"]
    gender = forms["gender-based"]

    name = raw_name.replace("-", " ")
    name = name.title()
    match name:
        # Names with special characters
        case "Farfetchd":
            name = "Farfetch'd"
        case "Mr Mime":
            name = "Mr. Mime"
        case "Mime Jr":
            name = "Mime Jr."
        case "Mr Rime":
            name = "Mr. Rime"
        case "Ho Oh":
            name = "Ho-Oh"
        case "Porygon Z":
            name = "Porygon-Z"
        case "Type Null":
            name = "Type: Null"
        case "Jangmo O":
            name = "Jangmo-o"
        case "Hakamo O":
            name = "Hakamo-o"
        case "Kommo O":
            name = "Kommo-o"
        case "Ting Lu":
            name = "Ting-Lu"
        case "Chien Pao":
            name = "Chien-Pao"
        case "Wo Chien":
            name = "Wo-Chien"
        case "Chi Yu":
            name = "Chi-Yu"

        # Gendered Forms
        case "Meowstic Male":
            if gender:
                name = "Male Meowstic"
            else:
                name = "Meowstic"
        case "Meowstic Female":
            name = "Female Meowstic"
        case "Indeedee Male":
            if gender:
                name = "Male Indeedee"
            else:
                name = "Indeedee"
        case "Indeedee Female":
            name = "Female Indeedee"
        case "Basculegion Male":
            if gender:
                name = "Male Basculegion"
            else:
                name = "Basculegion"
        case "Basculegion Female":
            name = "Female Basculegion"
        case "Oinkologne":
            if gender:
                name = "Male Oinkologne"
        case "Oinkologne Female":
            name = "Female Oinkologne"

        # Pokémon with alternate forms
        case "Deoxys Normal":
            if alt:
                name = "Normal Forme Deoxys"
            else:
                name = "Deoxys"
        case "Deoxys Attack":
            name = "Attack Forme Deoxys"
        case "Deoxys Defense":
            name = "Defense Forme Deoxys"
        case "Deoxys Speed":
            name = "Speed Forme Deoxys"
        case "Wormadam Plant":
            if alt:
                name = "Plant Cloak Wormadam"
            else:
                name = "Wormadam"
        case "Wormadam Sandy":
            name = "Sandy Cloak Wormadam"
        case "Wormadam Trash":
            name = "Trash Cloak Wormadam"
        case "Rotom Heat":
            name = "Heat Rotom"
        case "Rotom Wash":
            name = "Wash Rotom"
        case "Rotom Frost":
            name = "Frost Rotom"
        case "Rotom Fan":
            name = "Fan Rotom"
        case "Rotom Mow":
            name = "Mow Rotom"
        case "Shaymin Land":
            if alt:
                name = "Land Forme Shaymin"
            else:
                name = "Shaymin"
        case "Shaymin Sky":
            name = "Sky Forme Shaymin"
        case "Basculin Red Striped":
            if alt:
                name = "Red/Blue-Striped Basculin"
            else:
                name = "Basculin"
        case "Darmanitan Standard":
            name = "Darmanitan"
        case "Tornadus Incarnate":
            name = "Tornadus"
        case "Thundurus Incarnate":
            name = "Thundurus"
        case "Landorus Incarnate":
            name = "Landorus"
        case "Kyurem White":
            name = "White Kyurem"
        case "Kyurem Black":
            name = "Black Kyurem"
        case "Keldeo Ordinary":
            name = "Keldeo"
        case "Meloetta Aria":
            name = "Meloetta"
        case "Flabebe":
            name = "Flabébé"
        case "Aegislash Shield":
            name = "Aegislash"
        case "Pumpkaboo Average":
            name = "Pumpkaboo"
        case "Gourgeist Average":
            name = "Gourgeist"
        case "Zygarde 50":
            name = "Zygarde"
        case "Hoopa":
            if alt:
                name = "Hoopa Confined"
            else:
                name = "Hoopa"
        case "Oricorio Baile":
            name = "Oricorio"
        case "Lycanroc Midday":
            if alt:
                name = "Midday Form Lycanroc"
            else:
                name = "Lycanroc"
        case "Lycanroc Midnight":
            name = "Midnight Form Lycanroc"
        case "Lycanroc Dusk":
            name = "Dusk Form Lycanroc"
        case "Wishiwashi Solo":
            name = "Wishiwashi"
        case "Minior Red Meteor":
            name = "Minior"
        case "Necrozma Dusk":
            name = "Dusk Mane Necrozma"
        case "Necrozma Dawn":
            name = "Dawn Wings Necrozma"
        case "Toxtricity Amped":
            if alt:
                name = "Amped Form Toxtricity"
            else:
                name = "Toxtricity"
        case "Toxtricity Low Key":
            name = "Low Key Form Toxtricity"
        case "Eiscue Ice":
            name = "Eiscue"
        case "Morpeko Full Belly":
            name = "Morpeko"
        case "Urshifu Single Strike":
            if alt:
                name = "Single Strike Style Urshifu"
            else:
                name = "Urshifu"
        case "Urshifu Rapid Strike":
            name = "Rapid Strike Style Urshifu"
        case "Calyrex Ice":
            name = "Ice Rider Calyrex"
        case "Calyrex Shadow":
            name = "Shadow Rider Calyrex"
        case "Enamorus Incarnate":
            name = "Enamorus"
        case "Maushold":
            name = "Maushold"

        # Alolan Forms
        case "Rattata Alola":
            name = "Alolan Rattata"
        case "Raticate Alola":
            name = "Alolan Raticate"
        case "Raichu Alola":
            name = "Alolan Raichu"
        case "Sandshrew Alola":
            name = "Alolan Sandshrew"
        case "Sandslash Alola":
            name = "Alolan Sandslash"
        case "Vulpix Alola":
            name = "Alolan Vulpix"
        case "Ninetales Alola":
            name = "Alolan Ninetales"
        case "Diglett Alola":
            name = "Alolan Diglett"
        case "Dugtrio Alola":
            name = "Alolan Dugtrio"
        case "Meowth Alola":
            name = "Alolan Meowth"
        case "Persian Alola":
            name = "Alolan Persian"
        case "Geodude Alola":
            name = "Alolan Geodude"
        case "Graveler Alola":
            name = "Alolan Graveler"
        case "Golem Alola":
            name = "Alolan Golem"
        case "Grimer Alola":
            name = "Alolan Grimer"
        case "Muk Alola":
            name = "Alolan Muk"
        case "Exeggutor Alola":
            name = "Alolan Exeggutor"
        case "Marowak Alola":
            name = "Alolan Marowak"

        # Galarian Forms
        case "Meowth Galar":
            name = "Galarian Meowth"
        case "Ponyta Galar":
            name = "Galarian Ponyta"
        case "Rapidash Galar":
            name = "Galarian Rapidash"
        case "Slowpoke Galar":
            name = "Galarian Slowpoke"
        case "Slowbro Galar":
            name = "Galarian Slowbro"
        case "Farfetchd Galar":
            name = "Galarian Farfetch'd"
        case "Weezing Galar":
            name = "Galarian Weezing"
        case "Mr Mime Galar":
            name = "Galarian Mr. Mime"
        case "Articuno Galar":
            name = "Galarian Articuno"
        case "Zapdos Galar":
            name = "Galarian Zapdos"
        case "Moltres Galar":
            name = "Galarian Moltres"
        case "Slowbro Galar":
            name = "Galarian Slowbro"
        case "Corsola Galar":
            name = "Galarian Corsola"
        case "Zigzagoon Galar":
            name = "Galarian Zigzagoon"
        case "Linoone Galar":
            name = "Galarian Linoone"
        case "Darumaka Galar":
            name = "Galarian Darumaka"
        case "Darmanitan Galar Standard":
            name = "Galarian Darmanitan"
        case "Yamask Galar":
            name = "Galarian Yamask"
        case "Stunfisk Galar":
            name = "Galarian Stunfisk"

        # Hisuian Forms
        case "Growlithe Hisui":
            name = "Hisuian Growlithe"
        case "Arcanine Hisui":
            name = "Hisuian Arcanine"
        case "Voltorb Hisui":
            name = "Hisuian Voltorb"
        case "Electrode Hisui":
            name = "Hisuian Electrode"
        case "Typhlosion Hisui":
            name = "Hisuian Typhlosion"
        case "Qwilfish Hisui":
            name = "Hisuian Qwilfish"
        case "Sneasel Hisui":
            name = "Hisuian Sneasel"
        case "Samurott Hisui":
            name = "Hisuian Samurott"
        case "Lilligant Hisui":
            name = "Hisuian Lilligant"
        case "Basculin White Striped":
            name = "White-Striped Basculin"
        case "Zorua Hisui":
            name = "Hisuian Zorua"
        case "Zoraork Hisui":
            name = "Hisuian Zoroark"
        case "Braviary Hisui":
            name = "Hisuian Braviary"
        case "Sliggoo Hisui":
            name = "Hisuian Sliggoo"
        case "Goodra Hisui":
            name = "Hisuian Goodra"
        case "Avalugg Hisui":
            name = "Hisuian Avalugg"
        case "Decidueye Hisui":
            name = "Hisuian Decidueye"

        # Paldean Forms
        case "Tauros Paldea Combat Breed":
            name = "Combat Breed Paldean Tauros"
        case "Tauros Paldea Blaze Breed":
            name = "Blaze Breed Paldean Tauros"
        case "Tauros Paldea Aqua Breed":
            name = "Aqua Breed Paldean Tauros"
        case "Wooper Paldea":
            name = "Paldean Wooper"
    return name


def parse_moves(move_dict, gen):
    move_list = []
    for entry in move_dict:
        move = entry["move"]["name"]
        version_group_details = entry["version_group_details"]
        for group in version_group_details:
            version_group = group["version_group"]["name"]
            if is_in_gen(gen, version_group):
                name = parse_move_name(move)
                move_list.append(name)
                break

    return move_list


def is_in_gen(gen, version_group):
    match gen:
        case 1:
            match version_group:
                case "red-blue":
                    return True
                case "yellow":
                    return True
                case _:
                    return False
        case 2:
            match version_group:
                case "gold-silver":
                    return True
                case "crystal":
                    return True
                case _:
                    return False
        case 3:
            match version_group:
                case "ruby-sapphire":
                    return True
                case "emerald":
                    return True
                case "firered-leafgreen":
                    return True
                case "colosseum":
                    return True
                case "xd":
                    return True
                case _:
                    return False
        case 4:
            match version_group:
                case "diamond-pearl":
                    return True
                case "platinum":
                    return True
                case "heartgold-soulsilver":
                    return True
                case _:
                    return False
        case 5:
            match version_group:
                case "black-white":
                    return True
                case "black-2-white-2":
                    return True
                case "firered-leafgreen":
                    return True
                case _:
                    return False
        case 6:
            match version_group:
                case "x-y":
                    return True
                case "omega-ruby-alpha-sapphire":
                    return True
                case _:
                    return False
        case 7:
            match version_group:
                case "sun-moon":
                    return True
                case "ultra-sun-ultra-moon":
                    return True
                case _:
                    return False
        case 8:
            match version_group:
                case "sword-shield":
                    return True
                case "the-isle-of-armor":
                    return True
                case "the-crown-tundra":
                    return True
                case "lets-go-pikachu-lets-go-eevee":
                    return True
                case "brilliant-diamond-and-shining-pearl":
                    return True
                case "legends-arceus":
                    return True
                case _:
                    return False
        case 9:
            match version_group:
                case "scarlet-violet":
                    return True
                case "the-teal-mask":
                    return True
                case "the-indigo-disk":
                    return True
                case _:
                    return False


def parse_move_name(move):
    name = move.replace("-", " ")
    name = name.title()
    match name:
        case "Baby Doll Eyes":
            name = "Baby-Doll Eyes"
        case "Double Edge":
            name = "Double-Edge"
        case "Freeze Dry":
            name = "Freeze-Dry"
        case "Lock On":
            name = "Lock-On"
        case "Mud Slap":
            name = "Mud-Slap"
        case "Multi Attack":
            name = "Multi-Attack"
        case "Power Up Punch":
            name = "Power-Up Punch"
        case "Self Destruct":
            name = "Self-Destruct"
        case "Soft Boiled":
            name = "Soft-Boiled"
        case "Topsy Turvy":
            name = "Topsy-Turvy"
        case "Trick Or Treat":
            name = "Trick-or-Trear"
        case "U Turn":
            name = "U-turn"
        case "V Create":
            name = "V-create"
        case "Wake Up Slap":
            name = "Wake-Up Slap"
        case "Will O Wisp":
            name = "Will-O-Wisp"
        case "X Scissor":
            name = "X-Scissor"

    return name


def write_header(file, size):
    header = "{:>4} || {:>{size}} || Moves\n".format("ID#", "Name", size=size)

    length = len(header)
    separator = ""
    for i in range(length):
        separator += "="
        pass
    separator += "\n"

    file.write(header)
    file.write(separator)


def write_info(name, id_number, moves, file, size):
    info1 = "{:>4} || {:>{size}} || ".format(id_number, name, size=size)
    info2 = list_moves(moves) + "\n"

    info_line = info1 + info2

    file.write(info_line)


def list_moves(move_list):
    length = len(move_list)

    if length == 0:
        return ""

    line = move_list[0]
    for i in range(1, length):
        line += ", "
        line += move_list[i]
    
    return line
