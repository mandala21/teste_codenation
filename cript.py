from flags import alphabet, FILENAME
import hashlib
import json

class CriptJulio(object):
    filename = FILENAME
    token = '53be2661e42e33ce19f4a8aa4ff94ce2ce3ca725'

    def __init__(self,value,n):
        """
        Inicia a classe, informe o numero de casas
        n: Int
        """
        self.n = n
        self.value = value.lower()
    
    def get_order_in_alphabet(self,aim):
        """
        Recupera a posição que a letra corresponde no alfabeto
        aim: String
        return: Int
        """
        return alphabet.index(aim)
    
    def check_if_affected(self,aim):
        """
        Verifica se a letra eh afetada pelo criptografia
        aim: String
        return: Bool
        """
        return aim in alphabet
    
    def cript(self):
        """
        Criptografa a string informada
        data: String
        return: String
        """
        #separa todos os caracteres da string
        data_splited = list(self.value)
        #var que armazenara o retorno
        rs = ''
        #total do alfabeto
        total = len(alphabet)
        for letter in data_splited:
            #intera em todas as letras
            if self.check_if_affected(letter):
                #recupera a posicao e avanca as casa
                position = self.get_order_in_alphabet(letter)
                position += self.n
                #verifica se passo do tamanho total
                if position > total:
                    position = position - total
                rs += alphabet[position]
            else:
                rs += letter
        
        return rs

    def generate_sha1(self,data):
        """
        Gera um sha1 de uma string informada
        data: String
        return: String
        """
        #encode
        data = data.encode('utf-8')
        #gera a hash
        return hashlib.sha1(data).hexdigest()
    
    def dumps_file(self):
        """
        Salve o resultado em um arquivo
        method: String
        return:
        """
        decript = self.decript()
        #gera o conteudo do arquivo
        body = {
            "numero_casas": self.n,
            "token":self.token,
            "cifrado": self.value,
            "decifrado": decript,
            "resumo_criptografico": self.generate_sha1(decript)
        }
        with open(self.filename,'w') as f:
            content_file = json.dumps(body)
            f.write(content_file)
    
    def decript(self):
        """
        Descriptografa a string criptografada
        """
        #separa todos os caracteres da string
        data_splited = list(self.value)
        #var que armazenara o retorno
        rs = ''
        #total do alfabeto
        total = len(alphabet)
        for letter in data_splited:
            #intera em todas as letras
            if self.check_if_affected(letter):
                #recupera a posicao e avanca as casa
                position = self.get_order_in_alphabet(letter)
                position -= self.n
                rs += alphabet[position]
            else:
                rs += letter
        
        return rs