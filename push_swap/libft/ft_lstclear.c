/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 16:43:55 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/23 17:14:19 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_stack **lst, void (*del)(void*))
{
	t_stack	*cur;
	t_stack	*next;

	if (!lst || !del)
		return ;
	cur = *lst;
	while (cur)
	{
		next = cur->next;
		del((void *)(intptr_t)cur->value);
		free(cur);
		cur = next;
	}
	*lst = NULL;
}
