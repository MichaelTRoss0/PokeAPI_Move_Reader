import api_reader
import check_params
import json_reader
import parser_and_writer

input_file = "params.json"

params = json_reader.read_json(input_file)
check_params.verify(params)
output_file = params["output"]
gen = params["generation"]
start = params["start"]
end = params["end"]
forms = params["forms"]
check_params.validate(output_file, gen, start, end, forms)

print("Will now write move data of Pokémon #{} to #{} in generation {} to the file {}.\n"
      .format(str(start), str(end), str(gen), output_file))

dex = api_reader.read_api(gen, start, end, forms)
parser_and_writer.parse_and_write_info(output_file, gen, forms, dex,)
