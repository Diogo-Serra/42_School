/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_abs.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:17:27 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/23 15:53:30 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_ABS_H
# define FT_ABS_H

static inline int ft_abs(int digit)
{
	if (digit < 0)
		return (-digit);
	return (digit);
}

#endif /* FT_ABS_H */
