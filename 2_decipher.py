encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoded_1 = ""
decoded_2 = ""
decoded_3 = ""
decoded_4 = ""
decoded_5 = ""
decoded_6 = ""

i = 0
while i < len(encoded):
    if encoded[i] == "[":
        j = i + 1
        while encoded[j] != "]":
         j = j + 1
        
        content = encoded[i+1:j]
        parts = content.split("::")
        num_str = parts[0].strip()
        jumbled = parts[1].strip()
        status = parts[2].strip()
        
        if num_str.isdigit() and status == "ok":
            num = int(num_str)
            decoded_msg = ""
            for char in jumbled:
                if char in alphabet:
                    index = alphabet.find(char)
                    new_index = (index - num) % 26
                    decoded_msg = decoded_msg + alphabet[new_index]
                else:
                  decoded_msg = decoded_msg + char
            if num == 1:
                decoded_1 = decoded_msg
            elif num == 2:
                decoded_2 = decoded_msg
            elif num == 3:
                decoded_3 = decoded_msg
            elif num == 4:
                decoded_4 = decoded_msg
            elif num == 5:
                decoded_5 = decoded_msg
            elif num == 6:
                decoded_6 = decoded_msg
        
        i = j + 1
    else:
        i = i + 1
final_message = decoded_1 + decoded_2 + decoded_3 + decoded_4 + decoded_5 + decoded_6
print(final_message)