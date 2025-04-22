#nome do arquivo de entrada
input_file = "compilador_macaco_v13.gals"

#####################################################

#nome do arquivo de saída
output_file = input_file.rsplit('.', 1)[0] + '.gals'

# Evitar sobrescrever o arquivo de entrada
if input_file == output_file:
    output_file = input_file.rsplit('.', 1)[0] + '_processed.gals'

def process_text_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        modified_lines = []
        for line in lines:
            modified_line = ''
            inside_quotes = False
            
            for char in line:
                if char == '"':
                    inside_quotes = not inside_quotes
                    modified_line += char
                elif inside_quotes and char.isalpha():
                    modified_line += char.lower()
                else:
                    modified_line += char
            
            modified_lines.append(modified_line)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)
            
        print(f"Arquivo processado com sucesso! Resultado salvo em: {output_file}")
        
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {str(e)}")

# Exemplo de uso
process_text_file(input_file, output_file)