#!/bin/bash

# =============================================
# Bash Script: Automated Rover Mission Tasks
# =============================================

# Task 1: Create 'rover_mission' directory and navigate into it
echo "1) Creating 'rover_mission' directory..."
mkdir -p rover_mission && cd rover_mission || exit

# Task 2: Create empty log files (log1.txt, log2.txt, log3.txt)
echo "2) Creating log files..."
touch log1.txt log2.txt log3.txt

# Task 3: Rename log1.txt to mission_log.txt
echo "3) Renaming log1.txt to mission_log.txt..."
mv log1.txt mission_log.txt

# Task 4: Find all files with .log extension (none expected, just demonstrating)
echo "4) Finding .log files (none expected)..."
find . -name "*.log"

# Task 5: Display contents of mission_log.txt (empty unless modified)
echo "5) Contents of mission_log.txt:"
cat mission_log.txt

# Task 6: Find lines containing "ERROR" in mission_log.txt (add demo content first)
echo "6) Adding demo content to mission_log.txt..."
echo "This is an ERROR message." >> mission_log.txt
echo "This is normal log data." >> mission_log.txt
echo "Another ERROR occurred." >> mission_log.txt
echo "Lines containing 'ERROR':"
grep "ERROR" mission_log.txt

# Task 7: Count lines in mission_log.txt
echo "7) Line count in mission_log.txt:"
wc -l mission_log.txt

# Task 8: Show system date and time
echo "8) Current date and time:"
date

# Task 9: Display CPU usage (top for 3 seconds)
echo "9) CPU usage (sampling for 3 seconds)..."
top -b -n 1 | head -n 12  # Shows summary (Ctrl+C to exit if interactive)

# Task 10: Schedule shutdown in 10 minutes (commented out for safety)
echo "10) [SAFETY NOTE] Uncomment to schedule shutdown in 10 minutes:"
echo "# sudo shutdown -h +10"
echo "--> Actual command is commented out to prevent accidental shutdown."

# Completion message
echo "Script completed! Check outputs above."
