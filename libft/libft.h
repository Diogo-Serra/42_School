/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/04 18:05:58 by diserra           #+#    #+#             */
/*   Updated: 2025/09/05 01:09:47 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <stdlib.h>

size_t	ft_strlen(const char *s);
char	*ft_strcpy(char *dest, const char *src);
char	*ft_strncpy(char *dest, const char *src, size_t n);
char	*ft_strdup(const char *s);
char	*ft_strcat(char *dest, const char *src);
char	*ft_strncat(char *dest, const char *src, size_t n);
int		ft_strcmp(const char *s1, const char *s2);

#endif /* LIBFT_H */

/* Tests

int	main(int argc, char **argv)
{
	int	result;

	if (argc == 2)
	{
		result = ft_strlen(argv[1]);
		printf("strlen: %d\n", result);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	char	*ptr;
	char	dest[20];

	if (argc == 2)
	{
		ptr = ft_strcpy(dest, argv[1]);
		printf("strcpy: %s\n", ptr);
	}
	return (0);
}
	
int	main(int argc, char **argv)
{
	char	*ptr;
	char	dest[20] = "Hello ";

	if (argc == 2)
	{
		ptr = ft_strcat(dest, argv[1]);
		printf("strcat: %s\n", ptr);
	}
	return (0);
}*/
