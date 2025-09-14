/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 14:02:05 by diserra           #+#    #+#             */
/*   Updated: 2025/09/14 21:05:33 by diserra          ###   ########.fr       */
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