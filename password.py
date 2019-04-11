password = 'a123456'
x = 2
while x >= 0:
	input_password = input('请输入密码： ')
	if password == input_password:
		print('登入成功')
		break
	elif x > 0 and x <= 2:
		print('密码错误！ 还有', x, '次机会')
		x = x - 1
	else:
		print('登录失败')
		break


