<div>

<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/cover-libft-bonus.png" alt="Banner">
</p>

---

# 42 Project - Libft

**Goal**: Reimplement key C standard library functions + bonus linked list utilities.

---

## Mandatory Functions

**Character testing**  
`ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`  
`ft_toupper`, `ft_tolower`

**String handling**  
`ft_strlen`, `ft_strchr`, `ft_strrchr`, `ft_strncmp`  
`ft_strlcpy`, `ft_strlcat`, `ft_strnstr`, `ft_strdup`

**Memory**  
`ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`  
`ft_memccpy`, `ft_memchr`, `ft_memcmp`

**Conversion & allocation**  
`ft_atoi`, `ft_itoa`, `ft_calloc`

**Output**  
`ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`

---

## Bonus Functions (Linked List)

```c
typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}                   t_list;
ft_lstnew, ft_lstadd_front, ft_lstsize, ft_lstlast
ft_lstadd_back, ft_lstdelone, ft_lstclear, ft_lstiter, ft_lstmap
```
Makefile Rules
```c
all → build libft.a
```

</div>
bonus → add list functions
clean → remove .o
fclean → remove libft.a
re → rebuild all
```

Full libft with bonus, clean Makefile, no globals, no main in sources.
