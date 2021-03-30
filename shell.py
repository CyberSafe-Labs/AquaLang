# Copyright (c) 2021 CyberSafe Labs, Inc.
# This Software is Protected by the GPL-3.0 License
# Violation of the license could lead to possible legal action

import core

print("Aqua Lang v1.0.0 by Aditya Patil, Source Code released under the GPL-3.0 License. See License for more information.")
print("Shell Version: 1.0.0")
print("Copyright (c) 2021 CyberSafe Labs, Inc.")

while True:
	text = input('AquaLang > ')
	if text.strip() == "": continue
	result, error = core.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
