# Important definitions to keep in mind
* Python is an 'interpreted' language, and not a compiled language.
* Compiled languages like C or C++ require that the source code is compiled into machine code by the system's compiler (i.e. gcc, clangd).
* Python source code does not require compilation and therefore is interpreted by the python interpreter and passed to the computer.
* This allows python to be more dynamically typed and edited, making it more responsive.
* This is why from here on out we will refer to passing things to the interpreter.

# Some things to keep in mind
* Python syntax has a few style points that are preferred.
* Since the language was designed to be more readable to humans, making your code readable by others is the best thing you can do. Often you will share your code with others and having code that is clear, readable, and modular is helpful for others to get read, understand, and apply your code.
## Ways to make your code readable by others:
* Make sure that variables are named in a way that is unique (prevents over-writing in scripts) and is related to its output (easier to call later).
* Make sure to include comments where needed, and not too many comments to take up space.
* When possible, store things in variables, classes, or functions instead of repeating inputs. The key focus is to make things succinct, but modular so that people will not need to import your entire scripts to get a subset of its functionality.
* When writing a script with `if __name__ == "__main__":`, it is nicer to run only a single `main()` after, and to define your `main()` function before the statement.
* You can also check on the python website to see what the current PEP (Python Enhancement Proposals) for best practices (i.e. x=4*2*4^2 would be easier to read with spacing between operators [This is not always universally applied and may not matter to most people. Also your code editor may come with some Language Server Protocol (LSP) that will automatically format or recommend formatting for your code.])
* Often times, the simple approach is clearer, faster, and easier to optimize.
