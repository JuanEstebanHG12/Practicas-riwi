            
def validate_inputs(input_type, prompt, extra_validation = None):
    errors_messages = {
        int : "Enter a number greater than 0",
        float: "Enter a number greater than 0",
        str: "Do not enter empty text."
    }
    while True:
        try:
            validated_input = input_type(input(f"{prompt}"))
            if extra_validation and not extra_validation(validated_input):
                print(f"\033[31m{errors_messages[input_type]}\033[0m")
                continue
            return validated_input
        except ValueError:
            print(f"\033[31m{errors_messages[input_type]}\033[0m")