#!/bin/bash

# =============================================
# Rover Pre-Mission System Check
# =============================================

# Generate random battery percentage (0-100)
battery_level=$(( RANDOM % 101 ))

echo "Battery Level: $battery_level%"

# Check battery level
if [ "$battery_level" -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi

# Check network connectivity by pinging google.com
echo "Checking network connectivity..."
if ping -c 1 google.com &> /dev/null; then
    echo "Network: OK"
else
    echo "Communication failure!"
    exit 1
fi

# If both checks pass
echo "All systems operational!"
exit 0
