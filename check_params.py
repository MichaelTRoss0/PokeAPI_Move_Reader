import sys

limit = 1010


def verify(params):
    li = ["output", "generation", "start", "end", "forms"]
    for s in li:
        if s not in params:
            msg = "Variable {} is missing or misnamed in parameters.".format(s)
            sys.exit(msg)


def validate(output_file, gen, start, end, forms):
    if not output_file.endswith(".txt"):
        msg = output_file + " is not a valid filename to write to. " \
                            "It must end in '.txt'."
        sys.exit(msg)

    check_gen(gen, start, end)

    if start < 1 or start >= limit:
        msg = "{} is not a valid value for 'start'. " \
              "It must be at least 1 and at most 1 less than {}." \
            .format(str(start), str(limit))
        sys.exit(msg)

    if end < start or end > limit:
        msg = "{} is not a valid value for 'end'. " \
              "It must be at least 1 more than 'start' and at most {}." \
            .format(str(end), str(limit))
        sys.exit(msg)

    check_forms(forms)


def check_gen(gen, start, end):
    if gen < 1 or gen > 9:
        msg = "{} is not a valid value for 'generation'. " \
              "It must be a number from 1 to 9." \
            .format(str(gen))
        sys.exit(msg)

    match gen:
        case 1:
            if start > 151:
                msg = "There were only 151 Pokémon in Generation 1. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 151:
                msg = "There were only 151 Pokémon in Generation 1. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 2:
            if start > 251:
                msg = "There were only 251 Pokémon in Generation 2. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 251:
                msg = "There were only 251 Pokémon in Generation 2. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 3:
            if start > 386:
                msg = "There were only 386 Pokémon in Generation 3. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 386:
                msg = "There were only 386 Pokémon in Generation 3. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 4:
            if start > 493:
                msg = "There were only 493 Pokémon in Generation 4. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 493:
                msg = "There were only 493 Pokémon in Generation 4. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 5:
            if start > 649:
                msg = "There were only 649 Pokémon in Generation 5. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 649:
                msg = "There were only 649 Pokémon in Generation 5. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 6:
            if start > 721:
                msg = "There were only 721 Pokémon in Generation 6. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 721:
                msg = "There were only 721 Pokémon in Generation 6. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 7:
            if start > 809:
                msg = "There were only 809 Pokémon in Generation 7. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 809:
                msg = "There were only 809 Pokémon in Generation 7. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
        case 8:
            if start > 905:
                msg = "There were only 905 Pokémon in Generation 8. " \
                      "{} is not a valid value for 'start'." \
                    .format(str(start))
                sys.exit(msg)
            elif end > 905:
                msg = "There were only 905 Pokémon in Generation 8. " \
                      "{} is not a valid value for 'end'." \
                    .format(str(end))
                sys.exit(msg)
            elif start < 810:
                msg = "Not all Pokémon from previous Generations are available in Generation 8. " \
                      "If no Generation 8 data exists for a Pokémon, " \
                      "then the list of moves will be blank.\n"
                print(msg)
        case 9:
            if start < 810:
                msg = "Not all Pokémon from previous Generations are available in Generation 9. " \
                      "If no Generation 9 data exists for a Pokémon, " \
                      "then the list of moves will be blank.\n"
                print(msg)


def check_forms(forms):
    li = ["forms", "gender-based", "regional variant"]
    for s in li:
        if s not in forms:
            msg = "Variable '{}' is missing or misnamed in forms.".format(s)
            sys.exit(msg)
        if not isinstance(forms[s], bool):
            msg = "Variable '{}' must be either 'true' or 'false'.".format(s)
            sys.exit(msg)
