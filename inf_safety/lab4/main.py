from access import (
	O as Objects,
	OV as ObjectsAccessLevels,
	U as Users,
	UV as UsersAccessLevels,
	print_vector,
)

print('Objects access levels:')
print_vector(Objects, ObjectsAccessLevels)

print('\nUsers access levels:')
print_vector(Users, UsersAccessLevels)


print('\nāØ System started āØ\n')

def login():
	username = input('Enter username: ')
	userid = -1
	try:
		userid = Users.index(username)
	except:
		while userid == -1:
			print('Incorrect username: There is no user with name "{}" š„'.format(username))
			username = input('Enter username: ')
			try:
				userid = Users.index(username)
			except:
				pass

	return (username, userid)

username, userid = login()

print('\nā Success! You are welcome! š»\n')

def print_user_objects(objects, objects_access_levels, user_access_level):
	print('Available objects:')
	for i, obj in enumerate(objects):
		if user_access_level <= objects_access_levels[i]:
			print('{}. {}'.format(
				i + 1,
				obj
			))

print_user_objects(Objects, ObjectsAccessLevels, UsersAccessLevels[userid])


#
# main loop
#
while True:
	cmd = input('\nWaiting for your instructions š: ')

	if cmd == 'exit':
		print('See you soon! š¾')
		break
	elif cmd == 'quit':
		username, userid = login()
		print_user_objects(Objects, ObjectsAccessLevels, UsersAccessLevels[userid])
	elif cmd == 'request':
		obj = input('choose object (input id) š: ')

		try:
			obj = int(obj) - 1

			if obj in range(0, len(Objects)):
				if ObjectsAccessLevels[obj] >= UsersAccessLevels[userid]:
					print('ā Success!')
				else:
					print('You haven\'t enough rights for this action š„')
			else:
				print('Couldn\'t find given object š„')
		except:
			print('An invalid object id was specified')

	else:
		print('Unknown command')