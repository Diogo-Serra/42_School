/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:21:06 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 17:55:17 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_small(t_stack **a, int *move_count)
{
	t_stack *tmp;
	t_stack	*current;

	current = *a;
	while (current && current->next)
	{
		if (current->value > current->next->value)
		{
			tmp = current->value;
			current->value = current->next->value;
			current->next->value = tmp;
			current = *a;
			break ;
		}
		current = current->next;
	}
}
