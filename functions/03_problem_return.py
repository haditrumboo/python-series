
def greet(name, ending):
    return f"Hello {name} {ending}"

message = greet("Wahid", "thanks")
print(message)


# ==============================
def greet(name, ending):
    print(f"hello {name}", end="")
    print(ending )


greet("wahid", "thnaks")