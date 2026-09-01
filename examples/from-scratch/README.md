# From-scratch example: reading log

This is a **proposal preview**, not an installed Tana schema. It demonstrates how
`create-tana-system` can begin with “I want to remember what I read and what I learned”
without imposing the workout example or assuming existing structure.

## Depth used

This compact artifact shows a **Quick Start** result. It is deliberately shallow and
does not claim full understanding. Guided Discovery would first explore triggers,
lifecycle, exceptions, habits, scale, privacy, and success criteria in short rounds.

## Desired behavior

- Add a book to a reading list from desktop or mobile.
- Mark it as planned, reading, or finished.
- Capture short takeaways linked to the book.
- Retrieve the current book and recently finished books.

## Evidence lanes

- **Observed:** no relevant structure was found in the bounded demo scope.
- **Inferred:** status and takeaways may be useful; both require confirmation.
- **Owner-confirmed:** the four behaviors above and the vocabulary `Book` and `Takeaway`.
- **Unresolved:** whether authors should be reusable records and whether ratings matter.

## Explicit assumptions

- One reading status is enough for the first version.
- Plain-text Author is acceptable until the owner has enough experience to decide.
- Mobile capture needs no additional fields in v1.

## Minimum preview

- `Book`: Title, Author (plain text initially), Reading status, Started, Finished.
- `Takeaway`: Note and a relationship to one Book.
- One `Currently reading` view and one `Recently finished` view.
- No starter records beyond one clearly labeled example approved by the owner.

## Proposed focused Skills

- `add-book` — preview a Book before creating it.
- `capture-takeaway` — link a short note to an existing Book after confirmation.
- `retrieve-reading-list` — read-only current and recently finished retrieval.

Nothing is written until the owner approves the complete preview. After creation, fresh
Tana readback—not this proposal—determines the final `TANA_SYSTEM.md`.
After using v1, the owner should run Guided Discovery to confirm lifecycle, exceptions,
retrieval needs, and whether the assumptions still hold.
