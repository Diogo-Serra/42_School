/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_realloc.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 09:58:12 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/10 10:17:51 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_realloc(void *ptr, size_t new_size)
{
	size_t	old_size;
	void	*new_pointer;

	if (!ptr)
		ptr = malloc(new_size);
	if (new_size == 0)
	{
		free(ptr);
		return (NULL);
	}
	old_size = *((size_t *)ptr - 1);
	new_pointer = malloc(new_size);
	if (!new_pointer)
		return (NULL);
	if (old_size < new_size)
	{
		ft_memcpy(new_pointer, ptr, old_size);
	}
	else
	{
		ft_memcpy(new_pointer, ptr, new_size);
	}
	free(ptr);
	return (new_pointer);
}
