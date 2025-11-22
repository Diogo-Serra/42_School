/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libftprintf.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 05:57:35 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 07:46:06 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFTPRINTF_H
# define LIBFTPRINTF_H

# define UPPER_HEX "0123456789ABCDEF"
# define LOWER_HEX "0123456789abcdef"

# include <stdarg.h>
# include <unistd.h>
# include <stdint.h>

size_t	ft_strlen(const char *s);
int		ft_printf(const char *src, ...);
int		ft_putnbr_base(long n, int base, const char *digits);

#endif /* LIBFTPRINTF_H */