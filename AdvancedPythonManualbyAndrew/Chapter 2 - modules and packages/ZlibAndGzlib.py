# import gzip
# import zlib
# with gzip.open("C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\Chapter 2 - modules and packages\\csvtest.csv.gz", "rb") as f:
#     file_content = f.read()
#     print("1. ", file_content)
#     print("2. ", zlib.decompress(file_content))
#     print("3. ", gzip.decompress(file_content))
#     print("4. ",gzip.decompress(zlib.decompress(file_content)))
#     print("5. ",zlib.decompress(gzip.decompress(file_content)))
#     print("6. ",zlib.decompress(gzip.decompress(zlib.decompress(file_content))))
#     print("7. ",gzip.decompress(zlib.decompress(gzip.decompress(file_content))))
#     print("8. ",gzip.decompress(zlib.decompress(gzip.decompress(zlib.decompress(file_content)))))
#     print("9. ",zlib.decompress(gzip.decompress(zlib.decompress(gzip.decompress(file_content)))))
#     print("10. ",zlib.decompress(gzip.decompress(zlib.decompress(gzip.decompress(zlib.decompress(file_content))))))
#     print("11. ",gzip.decompress(zlib.decompress(gzip.decompress(zlib.decompress(gzip.decompress(file_content))))))
#     print("12. ",gzip.decompress(zlib.decompress(gzip.decompress(zlib.decompress(gzip.decompress(zlib.decompress(file_content)))))))

import gzip
import zlib

# Open the file using the 'with' statement to ensure it's properly closed afterward
with gzip.open("C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\Chapter 2 - modules and packages\\csvtest.csv.gz", "rb") as f:
    file_content = f.read()
    print("1. ", file_content)
    print("2. ", zlib.decompress(file_content))
    print("3. ", gzip.decompress(file_content))
    # Add the rest of your print statements as needed
