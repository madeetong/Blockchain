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
                'previousHash' : self.chainHash[len(self.chainHash)-1]
            }
            blockHash = self.proofOfWork(nonce=nonce)
            if self.proofOfWork(nonce=nonce) != False :
                self.chain.append(block)
                self.chainHash.append(blockHash)
                return block
            
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

    def previousBlock(self):
        self.chain[-1]
        return self.chain[-1]

    def blockHash(self,block):
        hashEndodeBlock = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
        return hashEndodeBlock

    def proofOfWork(self,nonce):
        hashCalculate = hashlib.sha256((str((self.chainHash[len(self.chainHash)-1]))+str(nonce)).encode('utf-8')).hexdigest()
        if hashCalculate[:1] == '0':  # กำหนดเป้า automatic difficulty adjustment ที่ไม่ automatic
            return hashCalculate
        else:
            return False
            
blockchain = Blockchain() 

# จำลองเป็น miner สุ่ม nonce ใส่ data ปิด block 
blockchain.createBlock(data='Nai A send 1 coin to Nai B',nonce=875686)      # รบกวนเปลี่ยนค่า nonce จนกว่าจะเข้าเป้าด้วยครับ ขอบคุณครับ



# แสดงผลข้อมูล 

n=0
print('\n---------- BLOCKCHAIN DATA ----------\n')
while n< len(blockchain.chain):
    print(' Block ',n,': \n',blockchain.chain[n])
    print(' hash block ',n,': ',blockchain.chainHash[n])
    print('---------------------------------------------------------------\n')
    n+=1

