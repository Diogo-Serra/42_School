/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:21:06 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 19:08:56 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

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

static int	find_min_position(t_stack *stack)
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

static void	sort_three(t_stack **a, int *move_count)
{
	int	max;

	max = find_max_value(*a);
	if ((*a)->value == max)
	{
		exec_operation(a, NULL, "ra", move_count);
		if ((*a)->value > (*a)->next->value)
			exec_operation(a, NULL, "sa", move_count);
	}
	else if ((*a)->next->value == max)
	{
		exec_reverse_operation(a, NULL, "rra", move_count);
		if ((*a)->value > (*a)->next->value)
			exec_operation(a, NULL, "sa", move_count);
	}
	else if ((*a)->value > (*a)->next->value)
		exec_operation(a, NULL, "sa", move_count);
}

static void	push_min_to_b(t_stack **a, t_stack **b, int *move_count)
{
	int	min_pos;
	int	size;

	size = stack_size(*a);
	min_pos = find_min_position(*a);
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
	exec_operation(a, b, "pb", move_count);
}

void	sort_small(t_stack **a, t_stack **b, int *move_count)
{
	int	size;

	size = stack_size(*a);
	if (size == 2)
	{
		if ((*a)->value > (*a)->next->value)
			exec_operation(a, NULL, "sa", move_count);
	}
	else if (size == 3)
		sort_three(a, move_count);
	else if (size == 4)
	{
		push_min_to_b(a, b, move_count);
		sort_three(a, move_count);
		exec_operation(a, b, "pa", move_count);
	}
	else if (size == 5)
	{
		push_min_to_b(a, b, move_count);
		push_min_to_b(a, b, move_count);
		sort_three(a, move_count);
		exec_operation(a, b, "pa", move_count);
		exec_operation(a, b, "pa", move_count);
	}
}
