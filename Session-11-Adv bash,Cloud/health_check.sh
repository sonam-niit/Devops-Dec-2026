echo "Health Check Report - $(date)"

echo ""
echo "Meory Ussage"
free -h | awk '/Mem:/ {print "Used: "$3" / Total: "$2" " }'

echo ""
echo "Disk Ussage"
df -h --total | grep 'total' | awk '{print "Used: "$3" / Total: "$2" ("$5" used)"}'

echo ""
echo "CPU Load"
uptime
