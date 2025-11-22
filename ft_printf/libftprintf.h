/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libftprintf.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 05:57:35 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 07:33:03 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFTPRINTF_H
# define LIBFTPRINTF_H

# define UPPER_HEX "0123456789ABCDEF"
# define LOWER_HEX "0123456789abcdef"

# include <stdarg.h>
# include <unistd.h>

size_t	ft_strlen(const char *s);
int		ft_printf(const char *src, ...);
void	*ft_calloc(size_t nmemb, size_t size);
void	*ft_memcpy(void *dst, const void *src, size_t n);
char	*ft_itoa_base(long n, int base, const char *digits);

#endif /* LIBFTPRINTF_H */