/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 20:00:00 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 22:54:09 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	assign_index(t_stack *stack)
{
	t_stack	*current;
	t_stack	*compare;
	int		rank;

	current = stack;
	while (current)
	{
		rank = 0;
		compare = stack;
		while (compare)
		{
			if (compare->value < current->value)
				rank++;
			compare = compare->next;
		}
		current->index = rank;
		current = current->next;
	}
}

static int	get_max_bits(int size)
{
	int	bits;

	bits = 0;
	while ((size - 1) >> bits)
		bits++;
	return (bits);
}

void	radix_sort(t_stack **a, t_stack **b, int *move_count)
{
	int	size;
	int	max_bits;
	int	i;
	int	j;

	assign_index(*a);
	size = stack_size(*a);
	max_bits = get_max_bits(size);
	i = 0;
	while (i < max_bits)
	{
		j = 0;
		while (j < size)
		{
			if ((((*a)->index >> i) & 1) == 0)
				exec_operation(a, b, "pb", move_count);
			else
				exec_operation(a, b, "ra", move_count);
			j++;
		}
		while (*b)
			exec_operation(a, b, "pa", move_count);
		i++;
	}
}
