def col_transpo_shift(text: str, key: list) -> str: 
    block_size = len(key)

    # Create a function to sort text into lists

    def create_lists(text):
        # Setup lists

        full_text_list = []
        useful_text_list = []
        excess_text_list = []
        all_lists = [full_text_list, useful_text_list, excess_text_list]

        # Setup cipher text in three lists

        for i in text:
            full_text_list.append(i)

        # Check how far block length is from 7

        offset_from_block_length = len(full_text_list) % block_size
        for i in range(0, len(text) - offset_from_block_length):
            useful_text_list.append(full_text_list[i])

        if offset_from_block_length != 0:
            for i in range(0, offset_from_block_length):
                excess_text_list.append(full_text_list[len(useful_text_list) + i])

        return all_lists

    # Create a function to fully decode text

    def decode_text(list):
        useful_text_list = list[1]
        decoded_list = []
        decoded_text = ""
        number_of_blocks = int(len(useful_text_list) / block_size)

        for i in range(1, number_of_blocks + 1):
            current_list = []

            for j in range(0, block_size):
                current_list.append(useful_text_list[(block_size * (i - 1)) + j])

            for k in range(0, block_size):
                decoded_list.append(current_list[int(key[k]) - 1])

        for l in decoded_list:
            decoded_text += l

        return decoded_text

    return decode_text(create_lists(text))

def read_col_transpo(cipher_text: str, key: list) -> str:
    row_length = len(key)
    column_height = round(len(cipher_text) / row_length)


    # Filter the cipher text into a list of rows

    rows = []
    block = ""
    
    for char in cipher_text:
        block += char
        if len(block) == column_height:
            rows.append(block)
            block = ""

    intermediate_step = ""

    for index in range(0, column_height):
        for row in rows:
            intermediate_step += row[index]

    plain_text = col_transpo_shift(intermediate_step, key)

    return plain_text

def write_col_transpo(plain_text: str, key: list) -> str:
    intermediate_step = col_transpo_shift(plain_text, key)

    rows = []
    current_row = []

    for char in intermediate_step:
        current_row.append(char)

        if len(current_row) == len(key):
            rows.append(current_row)
            current_row = []

    cipher_text = ""

    for index in range(0, len(key)):
        for row in rows:
            cipher_text += row[index]

    return cipher_text