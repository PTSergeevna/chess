in = readline(in)
exp_out = readline(out)
out = chess(in)
if (out == exp_out):
	return 0
else:
	print("FAIL! expected %s, got %s", exp_out, out)
	return 1
