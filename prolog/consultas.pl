% =====================================================
% SIRL - Sistema Inteligente de Recomendación de Libros
% Archivo: consultas.pl
% Descripción: Consultas de ejemplo para probar el sistema
% =====================================================

:- [reglas].

% -------------------------------------------------------
% Para probar manualmente en SWI-Prolog, ejecutar:
%   swipl -s consultas.pl
% Y luego escribir las consultas abajo
% -------------------------------------------------------

% CONSULTA 1: ¿Qué libros hay del género programacion?
%   ?- libro(_, Titulo, programacion, _).

% CONSULTA 2: ¿Qué se recomienda si me gusta ciencia_ficcion y no tengo autor favorito?
%   ?- recomendar(ciencia_ficcion, ninguno, Libro).

% CONSULTA 3: ¿Qué se recomienda si me gusta terror y mi autor favorito es king?
%   ?- recomendar(terror, king, Libro).

% CONSULTA 4: ¿Qué géneros están relacionados con distopia?
%   ?- genero_relacionado(distopia, Relacionado).

% CONSULTA 5: ¿Cuáles son los autores populares en fantasia?
%   ?- autor_popular(Autor, fantasia).

% -------------------------------------------------------
% Consulta automática de demostración al cargar el archivo
% -------------------------------------------------------
:- write('=== SIRL: Consultas de Ejemplo ==='), nl.
:- write('Libros de programacion:'), nl,
   forall(libro(_, T, programacion, _), (write('  - '), write(T), nl)).
:- write('Recomendaciones para genero terror:'), nl,
   forall(recomendar_por_genero(terror, T), (write('  - '), write(T), nl)).
