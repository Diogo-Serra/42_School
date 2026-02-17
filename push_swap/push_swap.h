/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/06 10:58:03 by diosoare          #+#    #+#             */
/*   Updated: 2026/02/17 17:48:43 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft.h" 
# include <stdlib.h>
# include <unistd.h>
# include <limits.h>
# include <stdio.h>

typedef struct s_stack
{
	int				value;
	int				index;
	struct s_stack	*next;
}					t_stack;

/* operations.c */
void	exec_operation(t_stack **a, t_stack **b, char *flag, int *move_count);
void	exec_reverse_operation(t_stack **a, t_stack **b, char *flag,
			int *move_count);

/* utils.c */
t_stack	*stack_new(int value);
void	stack_add_back(t_stack **stack, t_stack *new_node);
int		stack_size(t_stack *stack);
int		stack_is_sorted(t_stack *stack);
int		stack_has_duplicates(t_stack *stack);

/* parsing.c */
t_stack	*parse_input(int argc, char **argv);
void	validate_and_add(t_stack **a, char *str);
void	process_split(t_stack **a, char **split);

/* parsing_utils.c */
long	ft_atol(const char *str);
int		is_valid_number(char *str);
void	add_number(t_stack **a, long num);

/* error_handling.c */
void	error_exit(t_stack **a, t_stack **b);
void	free_stack(t_stack **stack);
void	free_split(char **split);

/* sort_small.c */
void	sort_small(t_stack **a, int *move_count);

#endif
