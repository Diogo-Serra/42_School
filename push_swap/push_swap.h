/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/06 10:58:03 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/23 17:36:45 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft.h" 
# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

/* operations.c */
void	exec_operation(t_stack **a, t_stack **b, char *flag, int *move_count);
void	exec_reverse_operation(t_stack **a, t_stack **b, char *flag,
			int *move_count);

/* utils.c */
int		stack_is_sorted(t_stack *stack);
int		stack_has_duplicates(t_stack *stack);
long	ft_atol(const char *str);
int		is_valid_number(char *str);
void	add_number(t_stack **a, long num);

/* parsing.c */
t_stack	*parse_input(int argc, char **argv);

/* error_handling.c */
void	error_exit(t_stack **a, t_stack **b, char **split);
void	free_stack(t_stack **stack);
void	free_split(char **split);

/* radix_sort.c */
void	radix_sort(t_stack **a, t_stack **b, int *move_count);

/* sort_small.c */
void	sort_small(t_stack **a, t_stack **b, int *move_count);

#endif
