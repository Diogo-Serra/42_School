/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/08 23:52:39 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE + 1];
	static char	*parts;
	char		*temp;
	char		*newline;
	size_t		bytes;

	parts = NULL;
	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	
	while ((bytes = read(fd, buffer, BUFFER_SIZE)) > 0)
	{
		buffer[bytes] = '\0';
		temp = parts;
		parts = ft_strjoin(parts, buffer);
		free (temp);
		newline = ft_strchr(parts, '\n');
		if (newline)
		{
			temp = ft_substr(parts, 0, newline - parts + 1);
			newline = ft_strdup(newline + 1);
			free(parts);
			parts = newline;
			return (temp);
		}
	}
	if (parts && *parts)
	{
		temp = ft_strdup(parts);
		free (parts);
		parts = NULL;
		return (temp);
	}
	free (parts);
	return (NULL);
}

int main(void)
{
    char    *out;
    int     fd;

    fd = open("test.txt", O_RDONLY);
    out = get_next_line(fd);
	printf("%s\n", out);
    free(out);
    return (0);
}

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}
