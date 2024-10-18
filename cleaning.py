def remove_eng (infile, ofile) :
    with open (infile, "r", encoding="utf-8" ) as f:

        text = f.read ()

    text_clean = "".join ( che for che in text if ord (che) > 127 )

    with open(ofile, 'w', encoding='utf-8') as outfile:
        outfile.write(text_clean)

y = 'dictionary_converted.txt' 
x = 'cleaned_dictionary.txt'  
remove_eng ( y, x)
print (f'all characters in dictionary have removed "{y}" and  save to "{x}.')


