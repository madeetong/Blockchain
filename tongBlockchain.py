import hashlib
import datetime

time = str(datetime.datetime.now())

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chainHash = []
        self.createBlock(data='The Times 29/Sep/2022 Chancellor on brink of 3rd bailout for banks',nonce=0)

    def createBlock(self,data,nonce):
        if len(self.chain) != 0:    # กรณีไม่ใช่ genesis block
            block = {
                'index' : len(self.chain),
                'timestamp' : time,
                'data' : data,
                'nonce' : nonce,
                'previousHash' : self.chainHash[-1]
            }
            self.chain.append(block) 
            if self.proofOfWork(nonce=nonce) != False :
                blockHash = self.proofOfWork(nonce=nonce)
                self.chainHash.append(blockHash)
                return block
            else :
                self.chain.pop(-1)
            
        else :                      # กรณีเป็น genesis block
            block = {
                'index' : len(self.chain),
                'timestamp' : time,
                'data' : data,
                'nonce' : nonce,
                'previousHash' : 0
            }
            self.chain.append(block)
            blockHash = hashlib.sha256((str(self.chain[0])).encode('utf-8')).hexdigest()
            self.chainHash.append(blockHash)
            return block

    def proofOfWork(self,nonce):
        hashCalculate = hashlib.sha256((str((self.chainHash[-1]))+str(nonce)+str(self.chain[-1])).encode('utf-8')).hexdigest()
        if hashCalculate[:1] == '0':  # กำหนดเป้า automatic difficulty adjustment ที่ไม่ automatic
            return hashCalculate
        else:
            return False
            
blockchain = Blockchain() 

# จำลองเป็น miner สุ่ม nonce ใส่ data ปิด block 
blockchain.createBlock(data='Nai A send 1 coin to Nai B',nonce=875686)      # รบกวนเปลี่ยนค่า nonce จนกว่าจะเข้าเป้าด้วยครับ ขอบคุณครับ
blockchain.createBlock(data='Nai B send 0.64 coin to Nai A',nonce=45655)


# แสดงผลข้อมูล 

n=0
print('\n---------- BLOCKCHAIN DATA ----------\n')
while n< len(blockchain.chain):
    print(' Block ',n,': \n',blockchain.chain[n])
    print(' hash block ',n,': ',blockchain.chainHash[n])
    print('---------------------------------------------------------------\n')
    n+=1

