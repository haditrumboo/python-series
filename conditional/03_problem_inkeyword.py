post = input("enter your post: ")


comment = [
    "make a lot of money",
    "buy now",
    "click this",
    "subscribe this"]#  loop logic


if(
    "make a lot of money" in post or
    "buy now" in post or
    "click this" in post or
    "subscribe this" in post
    
):
    print("This comment is a spam.")

else:
    print("This comment is not a spam")