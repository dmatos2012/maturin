from subprocess import check_output, run
import os


def main():

   # /home/david/oss/maturin/test-crates/venvs/develop-hello-world-cpython/bin
    # run(["pip", "install", "uv"])
    # lst = check_output(["uv", "pip", "list"]).decode("utf-8").strip().split("\n")
    # print(lst)
    # print("\n")
    # print(os.environ["PATH"])
    output = check_output(["hello-world"]).decode("utf-8").strip()
    if not output == "Hello, world!":
        raise Exception(output)

    # get pip list command
    # run pip install uv
    output = check_output(["foo"]).decode("utf-8").strip()
    if not output == "🦀 Hello, world! 🦀":
        raise Exception(output)
    print("SUCCESS")


if __name__ == "__main__":
    main()
