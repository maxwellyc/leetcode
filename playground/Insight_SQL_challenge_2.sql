CREATE PROCEDURE bookLibrary()
BEGIN
    /* Write your SQL here. Terminate each statement with a semicolon. */

    /* ranked by book count for each author */
  SELECT author, book FROM
    SELECT book_library.author, book_library.book
    rank_4.author_tot_cnt, rank_4.author_total_days,
    rank_4.days_left
    FROM
    (
    SELECT rank_1.book_id, rank_1.author_tot_cnt,
    rank_3.days_left, rank_3.author_total_days
    FROM
        (
        SELECT book_library.book_id, author_tot_cnt
        FROM
            (
            /* count number of books for each author
            has [author, author_tot_cnt] columns
            */
            SELECT author, COUNT(book) AS author_tot_cnt
            FROM book_library
            GROUP BY author
            ORDER BY author_tot_cnt DESC
            ) AS rank_tot_books
        LEFT OUTER JOIN
            book_library
        ON rank_tot_books.author = book_library.author
        ) AS rank_1
    LEFT OUTER JOIN
        (
        /* min number of days for each book and total number for the author  */
        SELECT book_id, author, days_left,
        SUM(days_left) AS author_total_days
        FROM
            (
            /* min number of days for each book  */
            SELECT book_id, author,
            (total_number_of_pages - pages_read ) / speed AS days_left
            FROM book_library
            ) AS rank_2
        GROUP BY author
        ) AS rank_3
    ON rank_3.book_id=rank_1.book_id
    ) AS rank_4
    LEFT OUTER JOIN book_library
    ON rank_4.book_id = book_library.book_id
    ORDER BY rank_4.author_tot_cnt, rank_4.author_total_days, rank_4.days_left, book_library.book


    ;
END
