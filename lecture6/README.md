# Lecture 6: Formal Verification

This lecture begins the second half of the course!

To follow along:
- `lecture6/README.md`
- `lecture6/Slides.pdf`
- [Repo](https://github.com/DavisPL-Teaching/189C/)

We will start with some general motivational slides.
Then, we will continue with this file.

(Switch to slides)

## Summary from the slides

We know about:
- Writing code
- Writing specifications (Hypothesis and Z3)
- Proving specifications correct (Z3)

## Poll link (if you missed it)

https://forms.gle/MashpCJkwJc64teNA
https://tinyurl.com/49vatd6f

### What is formal verification?

Combination of all of the above!

### Why use formal verification?

Answer:
Formal verification is especially useful in cases where:
- **Correctness is critical**: if the software fails, some very
  serious consequence will occur
- **Security**: if the software is vulnerable to attack, you may
  not have considered all the ways it could be exploited
- **A bug is very expensive or catastrophic** for your
  company/organization

### Examples

(These were covered in the slides)

- Pentium FDIV bug: affected Intel Pentium processors in 1994.

  + recall of all defective Intel processors at the time
  + $475 million in losses!

- Therac-25: one of the most (in)famous software bugs in history.

  + radiation therapy machine (1985-1987)
  + Under seemingly random conditions it would give 100+x the intended
    radiation dose to patients, manufacturers repeatedly denied it
    was
  + 6 incidents of overdose, 3 deaths, 3 serious injuries

  + Not verified! Would verification have caught this bug?
    (One can hope)

- Low-level cryptographic libraries

  + if these are incorrect, it can take down the whole security foundation of the internet!

  + Signal messaging app: verification effort for core messaging protocol going back to 2017

  + AWS-LibCrypto: open source SSL/OpenSSL implementaiton that is proved
    using Coq, HOLLight, and other tools.
    [report](https://sos-vo.org/node/107141)

  + To cite another misc. example:
    Galois, inc. has several projects in this area including the
    [SAW](https://saw.galois.com/) verification tools and the
    [Cryptol](https://cryptol.net/) domain-specific language

- Access control bugs

  + Expose critical customer or user data to malicious actors!

  + One failure would be enough to destroy trust in an entire cloud
    provider

  + AWS is investing millions in verification tools (including using Z3 and Dafny) for AWS S3 and IAM, AWS Encryption SDK, and other
    projects

- Blockchain technology -- lots of startups, e.g.

  + [Cubist](https://cubist.dev/about) key management technology

  + [Veridise](https://veridise.org/) blockchain verification tools

## Why Dafny?

- It's modern (actively developed)
- It's used in real industry applications (Microsoft, Amazon)
- It can *cross-compile* to other languages: such as C#, Go, Python, Java, and JavaScript.
- It has a good IDE (VSCode extension)

## Verification tools for popular programming languages:

- [CMBC](https://www.cprover.org/cbmc/) for C and C++
  [CPROVER manual](https://www.cprover.org/cprover-manual/)

  C and C++ have the C Bounded Model Checker (CMBC) / CPROVER framework,
  which is widely used and deployed in practice to verify real low-level systems code,
  for example at Amazon.

  And others: [Verifast](https://github.com/verifast/verifast)

- For Python: [Deal](https://deal.readthedocs.io/basic/verification.html)
  is a precondition/postcondition framework for Python, with an experimental
  verifier built in.

- For Rust:
  [Flux](https://github.com/flux-rs/flux),
  [Verus](https://github.com/verus-lang/verus),
  [Prusti](https://github.com/viperproject/prusti-dev),
  and [Creusot](https://github.com/creusot-rs/creusot)

- [LiquidHaskell](https://ucsd-progsys.github.io/liquidhaskell/) for Haskell

- [KeY](https://www.key-project.org/) for Java

    Also: [JBMC](https://www.cprover.org/jbmc/), [JayHorn](https://github.com/jayhorn/jayhorn) and others

- Others:
    [KJS](https://github.com/kframework/javascript-semantics)
    formal semantics and verifier for JavaScript
    Experimental verifiers for [TypeScript](https://formal.land/docs/verification/typescript)
    and many others

- If you don't see your favorite programming language here, write your own! :)

## A different approach

A different appraoch is to separate the verification into two steps:

1. Verification in the verification programming language

2. Extraction to produce code in a target language

For example:
- [Coq](https://coq.inria.fr/) can be extracted to OCaml code
- [Agda](https://agda.readthedocs.io/en/v2.5.2/tools/compilers.html) can be extracted to Haskell code
- [Dafny](https://dafny.org/) can be transpiled to C#, Go, Python, Java, and JavaScript

Main idea: only write the code once and verify it within the same system!
Then integrate the transpiled code with your existing libraries
and workflow.

## Getting started: isntalling Dafny

You will need to have Dafny installed.

- If you are on Mac, see [Homework 0](https://github.com/DavisPL-Teaching/189c-hw0) for instructions:
```
brew install dotnet
brew install dafny
```
Then, in VSCode, install the Dafny extension -- link here:
https://marketplace.visualstudio.com/items?itemName=dafny-lang.ide-vscode

As with the previous homeworks, you will submit your homework through GitHub Classroom. Please see [this Piazza post](https://piazza.com/class/lt90i40zrot3ue/post/48) for further instructions.

## In a GitHub codespace?

Just install the Dafny extension in VSCode!
It should work, you may need to re-open / refresh the file
or the browser tab.

## Checking that installation worked

If you are running locally:
To double check, run `dafny --version`, you should get something like:
```
4.6.0
```

In Codespaces/vscode: Just make sure the green checkmarks are showing up.

## Resources

- [Dafny](https://dafny.org/)
- [Reference manual and user guide](https://dafny.org/latest/DafnyRef/DafnyRef)
- Textbook: *Program Proofs,* by Rustan M. Leino -- [link](https://mitpress.mit.edu/9780262546232/program-proofs/)
