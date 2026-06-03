% =====================================================
% SIRL - Sistema Inteligente de Recomendación de Libros
% Archivo: reglas.pl
% Descripción: Reglas de inferencia para recomendación
% =====================================================

:- [hechos].

% -------------------------------------------------------
% REGLA 1: Recomendar por género favorito directo
% Si al usuario le gusta un género, recomendar libros de ese género
% -------------------------------------------------------
recomendar_por_genero(GeneroFavorito, Titulo) :-
    libro(_, Titulo, GeneroFavorito, _).

% -------------------------------------------------------
% REGLA 2: Recomendar por género relacionado
% Si al usuario le gusta un género, también puede gustarle uno similar
% -------------------------------------------------------
recomendar_por_genero_relacionado(GeneroFavorito, Titulo) :-
    genero_relacionado(GeneroFavorito, GeneroSimilar),
    libro(_, Titulo, GeneroSimilar, _).

% -------------------------------------------------------
% REGLA 3: Recomendar por autor favorito
% Si al usuario le gusta un autor, recomendar otros libros del mismo autor
% -------------------------------------------------------
recomendar_por_autor(AutorFavorito, Titulo) :-
    libro(_, Titulo, _, AutorFavorito).

% -------------------------------------------------------
% REGLA 4: Recomendación combinada (género + autor popular)
% Recomienda libros de autores populares en el género favorito del usuario
% -------------------------------------------------------
recomendar_autor_popular(GeneroFavorito, Titulo) :-
    autor_popular(Autor, GeneroFavorito),
    libro(_, Titulo, _, Autor).

% -------------------------------------------------------
% REGLA PRINCIPAL: recomendar/3
% Reúne todas las reglas anteriores en una sola consulta
% Parámetros: Genero, Autor, Libro recomendado
% -------------------------------------------------------
recomendar(Genero, _, Titulo) :-
    recomendar_por_genero(Genero, Titulo).

recomendar(Genero, _, Titulo) :-
    recomendar_por_genero_relacionado(Genero, Titulo).

recomendar(_, Autor, Titulo) :-
    Autor \= ninguno,
    recomendar_por_autor(Autor, Titulo).

recomendar(Genero, _, Titulo) :-
    recomendar_autor_popular(Genero, Titulo).
