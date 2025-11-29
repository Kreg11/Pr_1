from ui import print_output, root
from state import state

def run_command_line(cmd_line):
    print_output(cmd_line)
    if not cmd_line.strip():
        return

    parts = cmd_line.strip().split(maxsplit=1)
    cmd = parts[0]
    args = parts[1].strip() if len(parts) > 1 else []

    if cmd == "ls":
        if args:
            args = args.split()
            print_output(f"ls args: {' '.join(args)}")
        else:
            print_output("ls: no args")

    elif cmd == "cd":
        if args:
            print_output(f"cd args: {args}")
        else:
            print_output("cd: no args")

    elif cmd == "exit":
        root.destroy()

    else:
        print_output(f"Unknown command: {cmd}")
