/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 13:09:16 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/20 13:23:14 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stdlib.h>
# include <stddef.h>
# include <unistd.h>

/* =========================================================*/
/* 1) C-string length, duplication, and copy                */
/* =========================================================*/
size_t	ft_strlen(const char *s);
char	*ft_strdup(const char *s);

/* =========================================================*/
/* 2) Concatenation                                         */
/* =========================================================*/
size_t	ft_strlcat(char *dst, const char *src, size_t size);

/* =========================================================*/
/* 3) Comparison                                            */
/* =========================================================*/
int		ft_strncmp(const char *s1, const char *s2, size_t n);

/* =========================================================*/
/* 4) Search                                                */
/* =========================================================*/
char	*ft_strchr(const char *s, int c);
char	*ft_strnstr(const char *haystack, const char *needle, size_t len);
char	*ft_strrchr(const char *s, int c);

/* =========================================================*/
/* 5) Character tests & case conversion                     */
/* =========================================================*/
int		ft_isalnum(int c);
int		ft_isalpha(int c);
int		ft_isascii(int c);
int		ft_isdigit(int c);
int		ft_isprint(int c);
int		ft_tolower(int c);
int		ft_toupper(int c);

/* =========================================================*/
/* 6) Numeric conversion                                    */
/* =========================================================*/
int		ft_atoi(const char *s);

/* =========================================================*/
/* 7) Raw memory primitives                                 */
/* =========================================================*/
void	*ft_memchr(const void *s, int c, size_t n);
int		ft_memcmp(const void *s1, const void *s2, size_t n);
void	*ft_memcpy(void *dst, const void *src, size_t n);
void	*ft_memmove(void *dst, const void *src, size_t n);
void	*ft_memset(void *s, int c, size_t n);
void	ft_bzero(void *s, size_t n);

/* =========================================================*/
/* 9) String functional utilities                           */
/* =========================================================*/
char	*ft_itoa(int n);
void	ft_striteri(char *s, void (*f)(unsigned int, char *));
char	*ft_strjoin(char const *s1, char const *s2);
char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));

/* =========================================================*/
/* 10) I/O (stdout convenience)                             */
/* =========================================================*/
void	ft_putendl(char const *s);

/* =========================================================*/
/* 11) I/O (file descriptor variants)                       */
/* =========================================================*/
void	ft_putchar_fd(char c, int fd);
void	ft_putnbr_fd(int n, int fd);
void	ft_putstr_fd(char const *s, int fd);

#endif /* LIBFT_H */
