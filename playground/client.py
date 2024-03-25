from sglang import function, system, user, assistant, gen, set_default_backend, RuntimeEndpoint


from helper import readfile
import time
import argparse
import random

@function
def expansion(s, sentence, max_tokens):
    s += system("You are a helpful writer that keeps writing text. Do not stop early. Here are the text that you need to expand on: ")
    s += user(sentence)
    s += assistant(gen("answer", max_tokens=max_tokens, ignore_eos=True))



set_default_backend(RuntimeEndpoint("http://localhost:30000"))

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('--pos', type=int,default=0)

parser.add_argument('--input_length', type=int,default=512)

parser.add_argument('--max_new_tokens', type=int,default=128)

parser.add_argument('--n', type=int,default=20)

parser.add_argument('--interval', type=float,default=0.3)



args = parser.parse_args()

for _ in range(args.n):
    time.sleep(random.uniform(0, args.interval))
    t1 = time.time()
    state = expansion.run(
        sentence=readfile(start_pos=args.pos, length=args.input_length),
        max_tokens=args.max_new_tokens
    )

    for m in state.messages():
        print(m["role"], ":", m["content"])

    print(state["answer"])
    t2 = time.time()

    print(f"#####\ntime: {(t2-t1)*1000}\n#####")