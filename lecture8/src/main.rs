/*
    Main file

    main.rs is the default entrypoint for a Rust program.
*/

// Just for this lecture: allowing warnings, since we wrote a lot of
// illustrative / playground code
#![allow(dead_code, unused_variables)]
#![allow(
    clippy::unused_unit,
    clippy::unnecessary_cast,
    clippy::needless_return,
    clippy::vec_init_then_push
)]

/*
    Modules

    In most cases, these correspond directly to
    .rs files in your src/ folder.
*/
pub mod intro;
pub mod syntax;

/*
    Main function

    The easiest way to run your program: include a file
        src/main.rs
    and a function
        fn main()
*/
fn main() {
    println!("Hello, ECS 189C!");

    // Call into functions in syntax.rs

    // syntax::machine_types();

    // println!("2 + 2 = {}", syntax::add_two_integers(2, 2));
    // println!("2 + 3 = {}", syntax::add_two_integers(2, 3));
    // println!("2 + -2 = {}", syntax::add_two_integers(2, -2));

    // syntax::array();

    // syntax::slices();

    // syntax::strings();
}
