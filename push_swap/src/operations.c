/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 19:10:34 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 19:10:37 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

/* Swap the first two elements of a stack */
static void	swap(t_stack *stack)
{
	int	tmp;

	if (!stack || !stack->next)
		return ;
	tmp = stack->value;
	stack->value = stack->next->value;
	stack->next->value = tmp;
}

/* Push top of src to top of dst */
static void	push(t_stack **dst, t_stack **src)
{
	t_stack	*top;

	if (!*src)
		return ;
	top = *src;
	*src = (*src)->next;
	top->next = *dst;
	*dst = top;
}

/* Rotate: first element becomes last */
static void	rotate(t_stack **stack, int is_reverse)
{
	t_stack	*node;
	t_stack	*prev;

	if (!*stack || !(*stack)->next)
		return ;
	node = *stack;
	prev = NULL;
	while (node->next)
	{
		prev = node;
		node = node->next;
	}
	if (is_reverse)
	{
		prev->next = NULL;
		node->next = *stack;
		*stack = node;
	}
	else
	{
		node->next = *stack;
		*stack = (*stack)->next;
		node->next->next = NULL;
	}
}

/* Execute normal operations: sa, sb, ss, pa, pb, ra, rb, rr */
void	exec_operation(t_stack **a, t_stack **b, char *flag, int *move_count)
{
	if (flag[0] == 's' && flag[1] == 'a')
		swap(*a);
	else if (flag[0] == 's' && flag[1] == 'b')
		swap(*b);
	else if (flag[0] == 's')
	{
		swap(*a);
		swap(*b);
	}
	else if (flag[0] == 'p' && flag[1] == 'a')
		push(a, b);
	else if (flag[0] == 'p')
		push(b, a);
	else if (flag[1] == 'a')
		rotate(a, 0);
	else if (flag[1] == 'b')
		rotate(b, 0);
	else
	{
		rotate(a, 0);
		rotate(b, 0);
	}
	ft_putendl_fd(flag, 1);
	if (move_count)
		(*move_count)++;
}

/* Execute reverse operations: rra, rrb, rrr */
void	exec_reverse_operation(t_stack **a, t_stack **b, char *flag,
			int *move_count)
{
	if (flag[2] == 'a')
		rotate(a, 1);
	else if (flag[2] == 'b')
		rotate(b, 1);
	else
	{
		rotate(a, 1);
		rotate(b, 1);
	}
	ft_putendl_fd(flag, 1);
	if (move_count)
		(*move_count)++;
}
