from clmntools import clmntools
import sys

m = clmntools.Maths()
debug = clmntools.Debuger()
decoder = clmntools.Decoder()

# 0xb8c58f3a888c8918d07e04298edeb393f962df849058704e3cc4c0ec939d09235877b60bff9914ed16f5adeab0cdf880aa84e125f436d57171015f2a168b5b8d22c3d1f40ff6455e33a8ad837431f17f3783cb0abb275aab553b9f07cfb9cd3f33d649f79ec5814be8c72355af682de27e68436c6749d7ce616c0a22c691e8ff 3 175 0x1df4e438b9b28a3be1b19c33044df52ba4cbc90f7af80e28063fabb7f1d3a8d70f759963f99f9c0bac1b9e31babab1fd68e30eff9c9d5b29c31b7d84a4ddc97de8fbeb9595b9cea554cbe6a55152d151e694e4fa19388ebaf854000b48cc079072950598e27cdc01a0a49968baa5cdef3c00ed73e918dfc61ba50478c229f7ac
# 0xb3faca5b217fb38026ea06ad314f17656f8b2f155e1709afac5fd91d5b55ae6ac09eafb8c8065065a4bee53b21143fd0b20e8245e1550b7ff5b5c5df05e25d820d469113dd64f944760ec596a4628f155a66b3bd20c8d37341155441e331832c808403b390a3f7c55ba7cae740c4dcab632dae5d50b07e2bf0bfdd12ad840107 3 90 0x458c120ce1d39f1e1acd5d7f5f8dd51d5a88ce57980cf78f9b346d48362b851dff81af3b4f9678fbcdca8e74e2262f46735d00e8c2bfb00b8fd7857c84b2816653f49657c4466996c763bb75330ed401decdef4fc86e797dc99d51e2bec3ac696c67c06960f75102f166f2a92f7ef030371ec256abe96b7e420e62971e88fdf2L
# 0xa6d410051ea8f831fe4026abbd1ed92b7bf9a300f87367b9eda19c8cec052a1284cf50907316679004aab6274c1c3479d49a30e9ade95ea049538d0ec848f217a44faf1ffdb62e5ebb591cf24cdbf26e6bd300403acc4d6c2b4e6a0fa42c5776f9e68eec2062e1a9a86e3aafec9e6ce60d4b249dc178aa70576df3ebe6722321 3 188 0x60fffcfde748be62a8fc66087d33b90c950846c49d34f74007984ea7c7f60b20199a03fc702b75d9a6f4ddbe7701bff7e1d965e6aaf5b49bd4b4785085a0be3a6c194f74696fe1725ecf879537d565a662bee8aa30f6d0cf87011922d41d2affcd5c22144665c3ca0ba920c94e8360b38f992a4d1b93308f44a0eb5f5a3c5a9dL
# 0xa04f35d80cb1d204c8d74ab48e658b081fb3250775c28c37807d4d0d669ff87f92add4ca150ab4a1fee6978cd1e26f7f5b124a2656252a6d5a8624e0ded5e508460611fa9b0034f2e35c49e2d0fbed10feda06e30102604acfc197327f5da0afe8e33cd66510693e81e838f28ab5164026dfb3dac014696b79463e65d90407eb 3 90 0x1bba15a7386dfaa8a54289adf2031979671aade84780b880149d1de7027d85b4c25f7110793873083f36e4ce300a1b1dcf1d18eeebce65f00e6e5409235a43ff435f685b8527c322b772b86d2936cc4d26b4d6578a04dc54cdeb61dc5de76a339eb00f7ef3a6dd10aa1b5afde092b028e92318049baf7c286c50e06d1a7668deL
# 0x9e1f451d0f0a9bb7ac851aa27faf0d6c75c29be4d9f62fc0b1c0635e2a2b2c90cab0d7fa8e1d9543aa157b0a484662a56b63afc3b512241b3a72e62ac4350cd7e0de065f00bc20a55df4b62bc803471f92a8febe3e4bb375ff2fa16b6370721e23c5298f1bfc5d0da207bc14ac1668a0a252ec377127a8c07dff04dbddc802d3 3 188 0x422c7f36ed7428f479655a44ac5342be85a051115d15eeb3f814539b006d1eb0be7b42d35961f24aa6734b85430250411f7d568d8c993f5487e70a2d450678e0c692452561e37a3819177e9bc56b45305bb5e8f04fed1677a5f84b820ea5d6b80a579ae223eb276646dd599609409c20169cd4dba613604da9b873f6a42528d6L

pk1  = 0xfd2adfc8f9e88d3f31941e82bef75f6f9afcbba4ba2fc19e71aab2bf5eb3dbbfb1ff3e84b6a4900f472cc9450205d2062fa6e532530938ffb9e144e4f9307d8a2ebd01ae578fd10699475491218709cfa0aa1bfbd7f2ebc5151ce9c7e7256f14915a52d235625342c7d052de0521341e00db5748bcad592b82423c556f1c1051 
e1   = 3
u1 = 37
c1   = 0x81579ec88d73deaf602426946939f0339fed44be1b318305e1ab8d4d77a8e1dd7c67ea9cbac059ef06dd7bb91648314924d65165ec66065f4af96f7b4ce53f8edac10775e0d82660aa98ca62125699f7809dac8cf1fc8d44a09cc44f0d04ee318fb0015e5d7dcd7a23f6a5d3b1dbbdf8aab207245edf079d71c6ef5b3fc04416L

pk2  = 0xfd2adfc8f9e88d3f31941e82bef75f6f9afcbba4ba2fc19e71aab2bf5eb3dbbfb1ff3e84b6a4900f472cc9450205d2062fa6e532530938ffb9e144e4f9307d8a2ebd01ae578fd10699475491218709cfa0aa1bfbd7f2ebc5151ce9c7e7256f14915a52d235625342c7d052de0521341e00db5748bcad592b82423c556f1c1051 
e2   = 3 
u2 = 52
c2   = 0x1348effb7ff42372122f372020b9b22c8e053e048c72258ba7a2606c82129d1688ae6e0df7d4fb97b1009e7a3215aca9089a4dfd6e81351d81b3f4e1b358504f024892302cd72f51000f1664b2de9578fbb284427b04ef0a38135751864541515eada61b4c72e57382cf901922094b3fe0b5ebbdbac16dc572c392f6c9fbd01eL

assert( pk1 == pk2 )
n = pk1

u11 = m.modinv(u1**3,n)
u22 = m.modinv(u2**3,n)

c11 = ((c1*u11)%n)
c22 = ((c2*u22)%n)

'''
    m1' = m + u1
    m2' = m + u2
    
    m1' = m2' + (u1 - u2)
    
    a = 1
    b = u2 - u1
    
    haut = b*(c2 + 2c1 - b**3)
    bas  = (c2 - c1 + 2*(b**3))
'''

a = 1
b = u2 - u1

haut = b*(c22 + 2*c11 - b**3)
bas  = (c22 - c11 + 2*(b**3))

bas2 = m.modinv(bas, n)

x = ((haut*bas2)%n)
print decoder.hexdecode(hex(x-u1)[2:-1])

# m1 = uid1 * m + (uid1**2)
# m2 = uid2 * m + (uid2**2)

# m2 = uid2/uid1 * (uid1 * m) + (uid2**2) + (uid2)(uid1**2)/(uid1) - uid2 * uid1
# m2 = uid2/uid1 * (uid1 * m + uid1**2) + uid2**2 - uid1*uid2
# m2 = uid2/uid1 * m1 + (uid2 * (uid2 - uid1))

# m2 = (( u1*(u2-u1) )*( (u1**3)*c2 + 2*(u2**3)*c1 + (u1**3)*(u2**3)*((u2-u1)**3) )/( (u1**3)*c2 - (u2**3)*c1 + 2*(u1**3)*(u2**3)*((u2-u1)**3) ) % pk1)
# m1 = (( u2*(u1-u2) )*( (u2**3)*c1 + 2*(u1**3)*c2 + (u2**3)*(u1**3)*((u1-u2)**3) )/( (u2**3)*c1 - (u1**3)*c2 + 2*(u2**3)*(u1**3)*((u1-u2)**3) ) % pk1)

# a = ( u2*(u1-u2) )*( (u2**3)*c1 + 2*(u1**3)*c2 + (u2**3)*(u1**3)*((u1-u2)**3) )
# b = ( (u2**3)*c1 - (u1**3)*c2 + 2*(u2**3)*(u1**3)*((u1-u2)**3) )

# c = m.modinv(b,pk1)

# x = (a*c) % pk1
# print hex(x)
# print x % u1


# d = (( u1*(u2-u1) )*( (u1**3)*c2 + 2*(u2**3)*c1 + (u1**3)*(u2**3)*((u2-u1)**3) ))
# e = ( (u1**3)*c2 - (u2**3)*c1 + 2*(u1**3)*(u2**3)*((u2-u1)**3) )

# f = m.modinv(e,pk1)

# y = (d*f) % pk1
# print hex(y)
# print y % u2

# z = m.gcd(x,y)
# print hex(z)
# print hex(z%pk1)
# print hex(z%u2)

# i = 0
# print i

# def monitor(*o):
    # print o

# def handler():
    # debug.log('i = %d' % i)
    # debug.log('m = %s' % hex(m))
        
# debug.debug()
# debug.setLevel(3)
# debug.max = 5
# debug.add_handle(handler)

# monitor(i)

# while True:
    # tmp = pk1*i + x
    # if (tmp % u1) == 0:
        # m = tmp / u1 - u1
        # if ((len(hex(m).strip("L")[2:]) % 2) == 0) and decoder.printable(m):
            # print d.hexdecode(hex(m)[2:-1])
            # print 
    # if (i % 100000) == 0:
        # print i
    # i += 1