#----implicit conversion----
a_int = 1
b_float = 2.0
s = a_int+b_float
print(s)
print(type(s))

#binary to decimal

Binary_Number = '1001111'
Decimal_value = (1*(2^6)) + (0*(2^5)) + (0*(2^4)) + (1*(2^3)) + (1*(2^2)) + (1*(2^1)) + (1*(2^0))
print(int(Binary_Number,2))

#dec to bi
a = 10
bin_a = bin(a)
print(bin_a)
print(int(bin_a,2))

#similarly use hoct,hex to convert and use int(base(8,16))
