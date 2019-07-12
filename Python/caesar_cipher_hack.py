import click 
import enchant 

from tqdm import tqdm
from caesar_encryption import encrypt

@click.command()
@click.option(
    '--input_file', 
    type=click.File('r'), 
    required=True,
)

@click.option(
    '--output_file', 
    type=click.File('w'), 
    required=True,
)

def caesar_hack(input_file, output_file):
    cyphertext = input_file.read()
    eng_dictionary = enchant.Dict("en_US")
    highest_eng_words = 0  
    for key in tqdm(range(26)):
        plaintext = encrypt(cyphertext, -key)
        num_eng_words = 0
        for word in plaintext.split(' '):
            if word and eng_dictionary.check(word):
                num_eng_words += 1
        if num_eng_words > highest_eng_words:
            highest_eng_words = num_eng_words
            final_plaintext = plaintext
            final_key = key
    click.echo(final_key, final_plaintext)
    #click.echo(f'The most likely encryption key is {final_key} and original text from the user was: \n\n{final_plaintext[:1000]}...')
    #output_file.write(final_plaintext)

if __name__ == '__main__':
    caesar_hack()


