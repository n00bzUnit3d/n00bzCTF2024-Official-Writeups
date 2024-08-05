# Plane | NoobMaster

- Description: So many plane-related challenges! Why not another one? The flag is the latitude, longitude of the place this picture is taken from, rounded upto two decimal places. Example: n00bz{55.51,-20.27}

- `plane.jpg:/attachments/plane.jpg`

# Write-up

Take a note that this is a forensics challenge and not an OSINT challenge. Running a tool like exif will show that GPS data is present. Get the lat and long (which is in degrees, minutes, and seconds), and convert to decimal degrees. Round to 2 decimal places. That is your flag!

# Flag - n00bz{13.37,-13.37}

