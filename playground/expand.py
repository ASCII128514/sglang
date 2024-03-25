from sglang import function, system, user, assistant, gen, set_default_backend, RuntimeEndpoint


from helper import readfile
import time
import argparse

@function
def expansion(s, sentence, max_tokens):
    s += system("You are a helpful writer that keeps writing text. Do not stop early. Here are the text that you need to expand on: ")
    s += user(sentence)
    s += assistant(gen("answer", max_tokens=max_tokens))

@function
def multi_turn_question(s, question_1, question_2):
    s += system("You are a helpful assistant.")
    s += user(question_1)
    s += assistant(gen("answer_1", max_tokens=256))
    s += user(question_2)
    s += assistant(gen("answer_2", max_tokens=256))

set_default_backend(RuntimeEndpoint("http://localhost:30000"))

# state = multi_turn_question.run(
#     question_1="What is the capital of the United States?",
#     question_2="List two local attractions.",
# )

# for m in state.messages():
#     print(m["role"], ":", m["content"])

# print(state["answer_1"])


parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('--pos', type=int,default=0)

parser.add_argument('--max_new_tokens', type=int,default=2)

args = parser.parse_args()

for _ in range(20):
    t1 = time.time()
    state = expansion.run(
        sentence=readfile(start_pos=args.pos, length=3000),
        max_tokens=args.max_new_tokens
    )

    for m in state.messages():
        print(m["role"], ":", m["content"])

    print(state["answer"])
    t2 = time.time()

    print(f"time: {(t2-t1)*1000}")