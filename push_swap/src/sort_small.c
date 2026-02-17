/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:21:06 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 23:19:19 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	find_min_pos(t_stack *stack)
{
	int	min;
	int	pos;
	int	min_pos;

	min = stack->value;
	pos = 0;
	min_pos = 0;
	while (stack)
	{
		if (stack->value < min)
		{
			min = stack->value;
			min_pos = pos;
		}
		pos++;
		stack = stack->next;
	}
	return (min_pos);
}

static int	find_max_value(t_stack *stack)
{
	int	max;

	max = stack->value;
	while (stack)
	{
		if (stack->value > max)
			max = stack->value;
		stack = stack->next;
	}
	return (max);
}

static void	rotate_min_to_top(t_stack **a, int *move_count)
{
	int	min_pos;
	int	size;

	size = stack_size(*a);
	min_pos = find_min_pos(*a);
	if (min_pos <= size / 2)
	{
		while (min_pos-- > 0)
			exec_operation(a, NULL, "ra", move_count);
	}
	else
	{
		while (min_pos++ < size)
			exec_reverse_operation(a, NULL, "rra", move_count);
	}
}

static void	sort_three(t_stack **a, int *move_count)
{
	int	max;

	max = find_max_value(*a);
	if ((*a)->value == max)
		exec_operation(a, NULL, "ra", move_count);
	else if ((*a)->next->value == max)
		exec_reverse_operation(a, NULL, "rra", move_count);
	if ((*a)->value > (*a)->next->value)
		exec_operation(a, NULL, "sa", move_count);
}

void	sort_small(t_stack **a, t_stack **b, int *move_count)
{
	int	size;

	size = stack_size(*a);
	if (size == 2)
	{
		if ((*a)->value > (*a)->next->value)
			exec_operation(a, NULL, "sa", move_count);
		return ;
	}
	while (size > 3)
	{
		rotate_min_to_top(a, move_count);
		exec_operation(a, b, "pb", move_count);
		size--;
	}
	sort_three(a, move_count);
	while (*b)
		exec_operation(a, b, "pa", move_count);
}
