/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:29:33 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:29:37 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memalloc(size_t size)
{
	void			*p;
	unsigned char	*pc;

	p = (void *)malloc(size);
	if (!p)
		return (NULL);
	pc = p;
	while (size--)
		*pc++ = 0;
	return (p);
}
