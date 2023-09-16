# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithemtic_arranger
from unittest import main


print(arithemtic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(module='test_module', exit=False)