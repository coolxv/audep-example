def start(vme, *args, **kwargs):
    # print(f"cd {args[0]}")
    # vme.run(f"cd {args[0]}")
    # result = vme.value.run(f"pwd")
    # print(result.stdout)
    result1 = vme.run(f"cd {args[0]} && ./redis-server ./conf/redis.conf")
    print("redis run result", result1)
    return 0


