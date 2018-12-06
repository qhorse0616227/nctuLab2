#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
	def build(self):
		#Add 9 switches to a topology
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		
		#Add 6 hosts to a topology
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		
		#Add 14 bidirectional link to a topology
		self.addLink(s7, s9, bw=40, delay='5ms', loss=2)
		self.addLink(s8, s9, bw=50, delay='4ms', loss=3)
		self.addLink(h1, s1, bw=10, delay='50us', loss=12)
		self.addLink(s1, s7, bw=23, delay='1ms', loss=8)
		self.addLink(h2, s2, bw=5, delay='2ms', loss=3)
		self.addLink(s2, s7, bw=18, delay='2ms', loss=9)
		self.addLink(h3, s3, bw=7, delay='63us', loss=9)
		self.addLink(s3, s7, bw=15, delay='3ms', loss=5)
		self.addLink(h4, s4, bw=12, delay='40us', loss=14)
		self.addLink(s4, s8, bw=19, delay='80us', loss=7)
		self.addLink(h5, s5, bw=15, delay='30us', loss=18)
		self.addLink(s5, s8, bw=30, delay='95us', loss=2)
		self.addLink(h6, s6, bw=3, delay='5ms', loss=2)
		self.addLink(s6, s8, bw=20, delay='60us', loss=6)

def simpleTest():
	topo = SingleSwitchTopo()
	net = Mininet(topo=topo, controller=OVSController, link=TCLink)
	net.start()
	print("Testing network connectivity")
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)
	net.pingAll()
	CLI(net)

if __name__ == '__main__':
	setLogLevel('info')
	simpleTest()
