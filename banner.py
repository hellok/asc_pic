from text import color
import time,random
import log

banner = ''

Logos ={
    1:'wake-up-neo.txt',
    2:'cow-head.txt',
    3:'r7-metasploit.txt',
    4:'figlet.txt',
    5:'i-heart-shells.txt',
    6:'branded-longhorn.txt',
    7:'cowsay.txt',
    8:'3kom-superhack.txt',
    9:'missile-command.txt',
    10:'null-pointer-deref.txt',
    11:'metasploit-shield.txt',
    12:'ninja.txt',
    13:'workflow.txt',
    14:'global.txt',
    15:'1.txt',
    16:'blue.txt'
  }

#data=open(random.choice(Logos)).read()
data=open('global.txt').read()
_lines = data.split('\n')


def splash():
    log.trace('\x1b[G\x1b[?25l')
    for l in range(1):
     for c in range(2):#time
        for line in _lines:
            log.trace(color(c % 8, line) + '\n')
            time.sleep(0.01)
        for _ in _lines:
            log.trace('\x1b[F')
     for line in _lines:
        log.trace(line + '\n')
     log.trace('\x1b[?25h')

splash()

_lines = banner.split('\n')

splash()
