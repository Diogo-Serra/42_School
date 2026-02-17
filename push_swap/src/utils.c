/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:21:09 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 19:04:25 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*stack_new(int value)
{
	t_stack	*new;

	new = malloc(sizeof(t_stack));
	if (!new)
		return (NULL);
	new->value = value;
	new->next = NULL;
	return (new);
}

void	stack_add_back(t_stack **stack, t_stack *new_node)
{
	t_stack	*last;

	if (!*stack)
	{
		*stack = new_node;
		return ;
	}
	last = *stack;
	while (last->next)
		last = last->next;
	last->next = new_node;
}

int	stack_size(t_stack *stack)
{
	int	size;

	size = 0;
	while (stack)
	{
		size++;
		stack = stack->next;
	}
	return (size);
}

int	stack_is_sorted(t_stack *stack)
{
	while (stack && stack->next)
	{
		if (stack->value > stack->next->value)
			return (0);
		stack = stack->next;
	}
	return (1);
}

int	stack_has_duplicates(t_stack *stack)
{
	t_stack	*curr;
	t_stack	*check;

	curr = stack;
	while (curr)
	{
		check = curr->next;
		while (check)
		{
			if (curr->value == check->value)
				return (1);
			check = check->next;
		}
		curr = curr->next;
	}
	return (0);
}
