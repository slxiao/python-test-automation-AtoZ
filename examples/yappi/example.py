import yappi


def a():
    for i in range(10000000): pass

yappi.start()

a()

yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()