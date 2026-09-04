booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()
parts = booking.split(" | ")
event_code = parts[0]
username = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]
email_domain = email.split("@")[1].lower()
vip_count = vip_tag.count("VIP")
valid_event = event_code.startswith("EVT-")
valid_username = username.islower()
room_upper = room.upper()
valid_room = room_upper.startswith("ROOM-")
room_number = room.split("-")[1]
room_number_isdigit = room_number.isdigit()
valid_room = valid_room and room_number_isdigit

time_len = len(time)
time_colon = time[2]
time_hours = time[:2]
time_minutes = time[3:]
valid_time = time_len == 5 and time_colon == ":" and time_hours.isdigit() and time_minutes.isdigit()
valid_email = "@" in email and "." in email
print(f" Event code: {event_code}")
print(f"Name: {username.title()}")
print(f"Room: {room.upper()}")
print(f"Time: {time}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_count}")
print(f"Valid event code: {valid_event}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")