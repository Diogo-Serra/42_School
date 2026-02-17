/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 17:18:11 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 19:15:14 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void push_swap(t_stack **a, t_stack **b, int *move_count)
{
	int	size;

	if (stack_is_sorted(*a))
		return ;
	size = stack_size(*a);
	if (size <= 5)
		sort_small(a, b, move_count);
	else
		sort_small(a, b, move_count);
}

int main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;
	int		move_count;

	a = NULL;
	b = NULL;
	move_count = 0;
	
	if (argc < 2)
		return (0);
	a = parse_input(argc, argv);
	if (!a)
		return (1);
	if (stack_has_duplicates(a))
	{
		error_exit(&a, &b);
		return (1);
	}
	push_swap(&a, &b, &move_count);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
