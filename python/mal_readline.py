import os, sys, readline as pyreadline

history_loaded = False
histfile = os.path.expanduser("~/.mal-history")
rl = input if sys.version_info[0] >= 3 else raw_input

def readline(prompt="user> "):
    global history_loaded
    if not history_loaded:
        history_loaded = True
        try:
            with open(histfile, "r") as hf:
                for line in hf:
                    pyreadline.add_history(line.rstrip("\r\n"))
        except IOError:
            #print("Could not open %s" % histfile)
            pass

    try:
        line = rl(prompt)
        pyreadline.add_history(line)
        with open(histfile, "a") as hf:
            hf.write(line + "\n")
    except IOError:
        pass
    except EOFError:
        return None
    return line
