#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "get_next_line.h"

static void	run_test(const char *path, const char *label)
{
    int		fd;
    char	*line;
    size_t	i = 0;

    fd = open(path, O_RDONLY);
    if (fd < 0)
    {
        printf("[FAIL] %s: cannot open '%s'\n", label, path);
        return ;
    }
    printf("\n==== %s (%s) ====\n", label, path);
    while (1)
    {
        line = get_next_line(fd);
        if (!line)
            break ;
        printf("[%zu] \"%s\"", i, line);
        if (line[0] && line[ft_strlen(line) - 1] != '\n')
            printf(" (EOF without newline)");
        printf("\n");
        free(line);
        i++;
    }
    close(fd);
    printf("Total lines: %zu\n", i);
}

int	main(int argc, char **argv)
{
    if (argc > 1)
    {
        for (int i = 1; i < argc; i++)
            run_test(argv[i], "ARG");
        return (0);
    }

    /* Provide your own test files:
        test_empty.txt            -> empty file
        test_only_newline.txt     -> contains just "\n"
        test_no_trailing.txt      -> last line without '\n'
        test_long_line.txt        -> one line >> BUFFER_SIZE
        test_multilines.txt       -> several mixed lines
    */
    run_test("test_empty.txt", "EMPTY");
    run_test("test_only_newline.txt", "ONLY_NEWLINE");
    run_test("test_no_trailing.txt", "NO_TRAILING_NL");
    run_test("test_long_line.txt", "LONG_LINE");
    run_test("test_multilines.txt", "MULTILINES");

    /* Sequential reads on different files (single-FD implementation). */
    run_test("test_multilines.txt", "REREAD_SAME_FILE");
    run_test("test_no_trailing.txt", "SECOND_FILE_AFTER_FIRST");

    /* Invalid FD test */
    printf("\n==== INVALID FD ====\n");
    char *line = get_next_line(-1);
    if (!line)
        printf("Correctly returned NULL for invalid fd\n");
    free(line);
    return (0);
}