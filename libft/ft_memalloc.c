/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memalloc.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 14:02:05 by diserra           #+#    #+#             */
/*   Updated: 2025/09/09 21:56:11 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memalloc(size_t size)
{
	void			*p;
	unsigned char	*pc;
	size_t			i;

	p = (void *)malloc(size);
	if (!p)
		return (NULL);
	pc = p;
	i = 0;
	while (i < size)
		pc[i++] = 0;
	return (p);
}
