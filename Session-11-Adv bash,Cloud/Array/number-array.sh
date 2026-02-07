nums=(1 2 3 4 5)
echo "All Nums: ${nums[@]}"

#Append
nums+=(6)
echo "After Append: ${nums[@]}"
# Append Multiple
nums+=(7 8 9 10)
echo "After Append: ${nums[@]}"
# insert at specific Index
nums[3]=-20
echo "After Insert: ${nums[@]}" # Replace
# delete
unset nums[3]
echo "After Delete: ${nums[@]}"
# if you want to insert inbetween like insert value 4 between  index 3 and 4
index=3
nums=("${nums[@]:0:${index}}" 4 "${nums[@]:${index}}")
echo "After Insert: ${nums[@]}"