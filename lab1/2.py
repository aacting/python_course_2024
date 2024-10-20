# TODO Найдите количество книг, которое можно разместить на дискете
KILOBYTES_IN_MEGABYTE = 1024
BYTES_IN_KILOBYTE = 1024

weight_of_one_symbol_in_bytes = 4
count_of_symbols_per_string = 25
count_of_string_per_page = 50
count_of_pages_in_book = 100
disk_size_in_Mb = 1.44

disk_size_in_bytes = disk_size_in_Mb * KILOBYTES_IN_MEGABYTE * BYTES_IN_KILOBYTE
weight_of_one_book_in_bytes = weight_of_one_symbol_in_bytes * count_of_symbols_per_string \
                              * count_of_string_per_page * count_of_pages_in_book
count_of_books = int(disk_size_in_bytes // weight_of_one_symbol_in_bytes)

print("Количество книг, помещающихся на дискету:", count_of_books)
