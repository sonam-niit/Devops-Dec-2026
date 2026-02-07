read -rp "Enter IP: " data
# pattern='^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' 
pattern='^[0-2]{1}[1-5]{1}[0-5]{1}\.{3}[0-2]{1}[1-5]{1}[0-5]{1}$' #more clear with 0-255
if [[ $data =~ $pattern ]]; then
    echo "Valid"
else
    echo "Not Valid"
fi