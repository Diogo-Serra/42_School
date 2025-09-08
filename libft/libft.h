/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 18:05:58 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 20:00:13 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stdlib.h>
# include <stddef.h>

/* =========================================================*/
/* 1) C-string length, duplication, and copy                */
/* =========================================================*/
size_t	ft_strlen(const char *s);
char	*ft_strdup(const char *s);
char	*ft_strcpy(char *dst, const char *src);
char	*ft_strncpy(char *dst, const char *src, size_t n);

/* =========================================================*/
/* 2) Concatenation                                         */
/* =========================================================*/
char	*ft_strcat(char *dst, const char *src);
char	*ft_strncat(char *dst, const char *src, size_t n);
size_t	ft_strlcat(char *dst, const char *src, size_t size);

/* =========================================================*/
/* 3) Comparison                                            */
/* =========================================================*/
int		ft_strcmp(const char *s1, const char *s2);
int		ft_strncmp(const char *s1, const char *s2, size_t n);

/* =========================================================*/
/* 4) Search                                                */
/* =========================================================*/
char	*ft_strstr(const char *haystack, const char *needle);
char	*ft_strnstr(const char *haystack, const char *needle, size_t len);
char	*ft_strchr(const char *s, int c);
char    *ft_strrchr(const char *s, int c);

/* =========================================================*/
/* 5) Character tests & case conversion                     */
/* =========================================================*/
int		ft_isalpha(int c);
int		ft_isdigit(int c);
int		ft_isalnum(int c);
int		ft_tolower(int c);
int		ft_toupper(int c);
int     ft_isascii(int c);
int     ft_isprint(int c);

/* =========================================================*/
/* 6) Numeric conversion                                    */
/* =========================================================*/
int		ft_atoi(const char *s);

/* =========================================================*/
/* 7) Raw memory primitives                                 */
/* =========================================================*/
void	*ft_memset(void *s, int c, size_t n);
void	ft_bzero(void *s, size_t n);
void	*ft_memcpy(void *dst, const void *src, size_t n);
void	*ft_memccpy(void *dst, const void *src, int c, size_t n);
void	*ft_memmove(void *dst, const void *src, size_t n);
void    *ft_memchr(const void *s, int c, size_t n);
int     ft_memcmp(const void *s1, const void *s2, size_t n);

/* =========================================================*/
/* 8) Allocation & lifecycle helpers                        */
/* =========================================================*/
void	*ft_memalloc(size_t size);
void	ft_memdel(void **ap);
char	*ft_strnew(size_t size);
void	ft_strdel(char **as);
void	ft_strclr(char *s);

/* =========================================================*/
/* 9) String functional utilities                           */
/* =========================================================*/
void	ft_striter(char *s, void (*f)(char *));
void	ft_striteri(char *s, void (*f)(unsigned int, char *));
int		ft_strequ(char const *s1, char const *s2);
char	*ft_strsub(char const *s, unsigned int start, size_t len);
char	*ft_strjoin(char const *s1, char const *s2);
char	**ft_strsplit(char const *s, char c);
char	*ft_strtrim(char const *s);
char	*ft_itoa(int n);

/* =========================================================*/
/* 10) I/O (stdout convenience)                             */
/* =========================================================*/
void	ft_putchar(char c);
void	ft_putnbr(int n);
void	ft_putstr(char const *s);
void	ft_putendl(char const *s);

/* =========================================================*/
/* 11) I/O (file descriptor variants)                       */
/* =========================================================*/
void	ft_putchar_fd(char c, int fd);
void	ft_putstr_fd(char const *s, int fd);
void	ft_putendl_fd(char const *s, int fd);
void	ft_putnbr_fd(int n, int fd);

#endif /* LIBFT_H */
