import chain
import node
import logging
import os

def start():
    clear = lambda: os.system('clear')
    clear()

    log = logging.getLogger("Blockchain")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    blockchain = chain.Chain()

    miner = node.Node()
    valid = miner.validateChain(blockchain.getChain())
    if(valid):
        log.debug("Chain validated successfully.")
    else:
        log.error("Chain is broken")
        quit()
    
    while(True):
        mined_proof = miner.mineBlock(blockchain.getLastBlock()["proof"])
        blockchain.addBlock(mined_proof, miner.hash(blockchain.getLastBlock()))
        log.debug("Mined Block "+str(blockchain.getLastBlock()["index"])+" with Hash: " + str(miner.hash(blockchain.getLastBlock())))

start()