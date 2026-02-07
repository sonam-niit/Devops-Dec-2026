names=("alex" "bob" "catty" "devid" "John")

echo "First Element: ${names[0]}" # 0 is the first Index
echo "First Element: ${names[3]}" #devid

echo "All Names: ${names[@]}" # Print All Names using @

# Access Length
echo "Total No of Names: ${#names[@]}" # # indicate count, @ indicates all

# change bob with your name
names[1]="Sonam Soni"
echo "Updated Element: ${names[1]}"

# Print all using Loop
for name in "${names[@]}"; do
    echo $name
done