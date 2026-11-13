import os
import tools

# The tools module can be used for mundane tasks like filtering text and converting from strings to lists

from cipher_soft import column_transpo

# The cipher_soft package contains all cipher solving programs. To use one, replace the 'example' above with
# the names of all cipher solvers you need seperated with commas. See the files for contained functions.

# U 
# Begin decoding here - please reset after use

ct = "IYCNEYGPSULAMPISBYLOTEAAOHTRKYOAHIAALSAHEYEMHPRAHATIBY"
pt = "HELLOOMGIAMSOHAPPYTHATTHISCIPHERISUNBREAKABLEYAYAYAYAY"

print(column_transpo.read_col_transpo(column_transpo.write_col_transpo("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [2,1]), [2,1]))