from flags import alphabet
import hashlib

class CriptJulio(object):
    def __init__(self,n):
        """
        Inicia a classe, informe o numero de casas
        n: Int
        """
        self.n = n
    
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
    
    def cript(self,data):
        """
        Criptografa a string informada
        data: String
        return: String
        """
        #to lower
        data = data.lower()
        #separa todos os caracteres da string
        data_splited = list(data)
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

    @classmethod
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
        