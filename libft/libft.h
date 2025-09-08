/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 18:05:58 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 17:32:27 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdlib.h>
# include <string.h>

/* ========================================================================= */
/* 1) C-string length, duplication, and copy                                  */
/*    - Basic null-terminated string utilities                                */
/* ========================================================================= */
size_t  ft_strlen(const char *s);                          /* length of s (no NUL) */
char    *ft_strdup(const char *s);                         /* malloc copy of s */
char    *ft_strcpy(char *dst, const char *src);            /* copy src -> dst */
char    *ft_strncpy(char *dst, const char *src, size_t n); /* copy up to n bytes */

/* ========================================================================= */
/* 2) Concatenation                                                           */
/*    - Append src to dst variants (ensure enough space for dst variants)     */
/* ========================================================================= */
char    *ft_strcat(char *dst, const char *src);            /* append src -> dst */
char    *ft_strncat(char *dst, const char *src, size_t n); /* append up to n */
size_t  ft_strlcat(char *dst, const char *src, size_t size);/* like BSD strlcat */

/* ========================================================================= */
/* 3) Comparison                                                               */
/* ========================================================================= */
int     ft_strcmp(const char *s1, const char *s2);         /* lexicographic cmp */
int     ft_strncmp(const char *s1, const char *s2, size_t n); /* cmp up to n */

/* ========================================================================= */
/* 4) Search                                                                   */
/* ========================================================================= */
char    *ft_strstr(const char *haystack, const char *needle);     /* first needle */
char    *ft_strnstr(const char *haystack, const char *needle, size_t len); /* within len */
char    *ft_strchr(const char *s, int c);                   /* first c in s (incl. '\0') */

/* ========================================================================= */
/* 5) Character tests & case conversion                                        */
/* ========================================================================= */
int     ft_isalpha(int c);
int     ft_isdigit(int c);
int     ft_isalnum(int c);
int     ft_tolower(int c);
int     ft_toupper(int c);

/* ========================================================================= */
/* 6) Numeric conversion                                                       */
/* ========================================================================= */
int     ft_atoi(const char *s);                             /* ASCII -> int */

/* ========================================================================= */
/* 7) Raw memory primitives                                                    */
/* ========================================================================= */
void    *ft_memset(void *s, int c, size_t n);              /* fill n bytes with c */
void    ft_bzero(void *s, size_t n);                       /* set n bytes to 0 */
void    *ft_memcpy(void *dst, const void *src, size_t n);  /* copy n bytes */
void    *ft_memccpy(void *dst, const void *src, int c, size_t n); /* stop after c */
void    *ft_memmove(void *dst, const void *src, size_t n); /* safe overlap copy */

/* ========================================================================= */
/* 8) Allocation & lifecycle helpers                                           */
/* ========================================================================= */
void    *ft_memalloc(size_t size);                         /* malloc + zeroed */
void    ft_memdel(void **ap);                              /* free + NULL */
char    *ft_strnew(size_t size);                           /* new zeroed char[] */
void    ft_strdel(char **as);                              /* free + NULL for char* */
void    ft_strclr(char *s);                                /* set all chars to '\0' */

/* ========================================================================= */
/* 9) String functional utilities                                              */
/* ========================================================================= */
void    ft_striter(char *s, void (*f)(char *));            /* apply f to each char */
void    ft_striteri(char *s, void (*f)(unsigned int, char *)); /* with index */
int     ft_strequ(char const *s1, char const *s2);         /* boolean equality */
char    *ft_strsub(char const *s, unsigned int start, size_t len); /* substring */
char    *ft_strjoin(char const *s1, char const *s2);       /* concat into new str */

/* ========================================================================= */
/* 10) I/O (stdout convenience)                                                */
/* ========================================================================= */
void    ft_putchar(char c);
void    ft_putnbr(int n);
void    ft_putstr(char const *s);
void    ft_putendl(char const *s);

/* ========================================================================= */
/* 11) I/O (file descriptor variants)                                          */
/* ========================================================================= */
void    ft_putchar_fd(char c, int fd);
void    ft_putstr_fd(char const *s, int fd);
void    ft_putendl_fd(char const *s, int fd);

#endif /* LIBFT_H */
