# Node Template

To stop having to faff about with Prettier, Linting, Typescript setup etc. 

## Usage

* `npm run dev`: watches TS files for changes (make sure in /src), rebuilds and runs Node again. 
* `npm run prettier-format`: run prettier and fix, default config except tabs = 2 spaces, single quotes.
* `npm run lint`: run ESLint with default config.
* `npm run compile`: compile to /dist 
* Pre-commit hook setup to check prettier and linting, but without changing anything.
