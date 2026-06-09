% =====================================================
% SIRL - Sistema Inteligente de Recomendación de Libros
% Archivo: reglas.pl
% Rol: Inferencia lógica pura.
%   Prolog razona sobre el conocimiento de hechos.pl
%   para deducir recomendaciones. Sin código Python.
%   Sin lógica de negocio. Solo razonamiento declarativo.
% =====================================================

:- [hechos].

% -------------------------------------------------------
% REGLA 1: Por género directo
% -------------------------------------------------------
recomendar_por_genero(Genero, Titulo) :-
    libro(_, Titulo, Genero, _).

% -------------------------------------------------------
% REGLA 2: Por género relacionado
% -------------------------------------------------------
recomendar_por_genero_relacionado(Genero, Titulo) :-
    genero_relacionado(Genero, GeneroSimilar),
    libro(_, Titulo, GeneroSimilar, _).

% -------------------------------------------------------
% REGLA 3: Por autor directo
% -------------------------------------------------------
recomendar_por_autor(Autor, Titulo) :-
    libro(_, Titulo, _, Autor).

% -------------------------------------------------------
% REGLA 4: Por autor similar
% -------------------------------------------------------
recomendar_por_autor_similar(Autor, Titulo) :-
    autor_similar(Autor, AutorSimilar),
    libro(_, Titulo, _, AutorSimilar).

% -------------------------------------------------------
% PREDICADOS DE BÚSQUEDA (para el menú del sistema)
% -------------------------------------------------------

% Buscar todos los libros de un género
libros_por_genero(Genero, Titulo, Autor) :-
    libro(_, Titulo, Genero, Autor).

% Buscar todos los libros de un autor
libros_por_autor(Autor, Titulo, Genero) :-
    libro(_, Titulo, Genero, Autor).

% Buscar un libro por título (búsqueda exacta)
buscar_libro(Titulo, Genero, Autor) :-
    libro(_, Titulo, Genero, Autor).

% Contar libros por género
total_por_genero(Genero, Total) :-
    aggregate_all(count, libro(_, _, Genero, _), Total).

% Obtener todos los géneros únicos disponibles
genero_disponible(Genero) :-
    libro(_, _, Genero, _).

% Obtener todos los autores únicos disponibles
autor_disponible(Autor) :-
    libro(_, _, _, Autor).

% -------------------------------------------------------
% REGLA PRINCIPAL DE RECOMENDACIÓN
% recomendar(Genero, Autor, Titulo)
% -------------------------------------------------------
recomendar(Genero, _, Titulo) :-
    recomendar_por_genero(Genero, Titulo).

recomendar(Genero, _, Titulo) :-
    recomendar_por_genero_relacionado(Genero, Titulo).

recomendar(_, Autor, Titulo) :-
    Autor \= ninguno,
    recomendar_por_autor(Autor, Titulo).

recomendar(_, Autor, Titulo) :-
    Autor \= ninguno,
    recomendar_por_autor_similar(Autor, Titulo).
