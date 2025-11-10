/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_realloc.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 09:58:12 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/10 10:46:08 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_realloc(void *ptr, size_t old_size, size_t new_size)
{
	void	*new_pointer;
	size_t	to_copy;

	if (new_size == 0)
	{
		free(ptr);
		return (NULL);
	}
	if (!ptr)
		return (malloc(new_size));
	new_pointer = malloc(new_size);
	if (!new_pointer)
		return (NULL);
	if (old_size < new_size)
	{
		to_copy = old_size;
	}
	else
	{
		to_copy = new_size;
	}
	if (to_copy)
		ft_memcpy(new_pointer, ptr, to_copy);
	free(ptr);
	return (new_pointer);
}
