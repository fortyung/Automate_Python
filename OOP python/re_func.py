"""
closure
"""

# def logger(msg):
#     def log_msg():
#         print("log:", msg)

#     return log_msg


# log_hi = logger("hi")
# log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


prin = html_tag("h3")
prin("Hello world!")
