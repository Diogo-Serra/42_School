/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 05:57:35 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/24 21:32:14 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# define UPPER_HEX "0123456789ABCDEF"
# define LOWER_HEX "0123456789abcdef"
# define DECIMAL "0123456789"

# include <stdarg.h>
# include <unistd.h>
# include <stdint.h>

size_t	ft_strlen(const char *s);
int		ft_printf(const char *src, ...);
int		ft_putnbr_base(long n, const char *digits, int base);

#endif /* FT_PRINTF_H */