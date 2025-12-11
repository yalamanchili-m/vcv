# Prime Number
echo "Enter a number:"
read n
flag=0
if [ $n -le 1 ]; then
    flag=1
else
    for ((i=2; i*i<=n; i++))
    do
        if [ $((n%i)) -eq 0 ]; then
            flag=1
            break
        fi
    done
fi
if [ $flag -eq 0 ]; then
    echo "$n is a Prime Number"
else
    echo "$n is NOT a Prime Number"
fi

# Palindrome Number
echo "Enter a number:"
read n
temp=$n
rev=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    rev=$((rev * 10 + digit))
    n=$((n / 10))
done
if [ $rev -eq $temp ]; then
    echo "$temp is a Palindrome"
else
    echo "$temp is NOT a Palindrome"
fi

# Armstrong Number
echo "Enter a number:"
read n
temp=$n
sum=0
while [ $n -gt 0 ]
do
    digit=$((n % 10))
    sum=$((sum + digit*digit*digit))
    n=$((n / 10))
done
if [ $sum -eq $temp ]; then
    echo "$temp is an Armstrong Number"
else
    echo "$temp is NOT an Armstrong Number"
fi

# Decimal to Binary
echo "Enter a decimal number:"
read n
binary=""
while [ $n -gt 0 ]
do
    r=$((n % 2))
    binary="$r$binary"
    n=$((n / 2))
done
echo "Binary: $binary"

# Binary to Decimal
echo "Enter a binary number:"
read bin
len=${#bin}
decimal=0
power=1
for ((i=len-1; i>=0; i--))
do
    digit=${bin:$i:1}
    decimal=$((decimal + digit * power))
    power=$((power * 2))
done
echo "Decimal: $decimal"