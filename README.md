# Ivy-Compiler

## Welcome to Ivy
This is the compiler for my Ivy project. A small toy programming language that I hope to grow one day! The language is called Ivy because much like the Ivy plant, when given the proper attention, I think this language can really grow to encompass great things!

To create this compiler, I am taking advantage of the PLY module which provides Lex and Yacc functionality in Python :) Back in college, I had the pleasure (and anguish) of writing a compiler using Flex and Bison using C/C++. I'm a couple years removed from that course now and have finally recovered (yes, I'm sort of joking) enough to tackle writing a compiler again!

If you come across this project, feel free to shoot me an email at nabab47@gmail.com to inquire more about it! I'd love others to contribute! :)

Cheers,

Animesh

## Usage Instructions

To run the Ivy compiler, run:
python ivy.py <input>
Ex: python ivy.py test.py

## Dependencies

This project does require that the `ply` module be installed. `pip install ply` should do the trick, or `python -m pip install ply` if your're working in a virtual python environment.
