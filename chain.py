import time
import json
import hashlib
import logging

class Chain:
    def __init__(self):
        with open("chain.json",'r+') as file:
            try:
                file_data = json.load(file)
                self.chain = file_data
            except ValueError:
                self.chain = [] # List of Blocks
                genesis = self.createGenesisBlock(proof=1, previous_hash='0') # Creating Genesis Block
                json.dump(self.chain, file, indent = 4)

    def getChain(self):
        return self.chain

    def getLastBlock(self):
        return self.chain[-1]

    def createGenesisBlock(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(time.time()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        log = logging.getLogger("Blockchain")
        log.debug("Generated Genesis Block "+str(block["index"]) + " with Hash: " + str(self.hash(block)))
        return block
    
    def addBlock(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(time.time()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        with open("chain.json",'r+') as file:
            file_data = json.load(file)
            file_data.append(block)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        return block
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()