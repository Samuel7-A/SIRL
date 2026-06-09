% =====================================================
% SIRL - Consultas de ejemplo para pruebas manuales
% Ejecutar: swipl -s prolog/consultas.pl
% =====================================================
:- [reglas].

:- write('=== SIRL - Pruebas de Prolog ==='), nl.
:- write('Libros de terror:'), nl,
   forall(libros_por_genero(terror, T, A, _),
          (write('  - '), write(T), write(' / '), write(A), nl)).
:- write('Recomendaciones para ciencia_ficcion:'), nl,
   forall(recomendar_por_genero(ciencia_ficcion, T, _),
          (write('  - '), write(T), nl)).
:- write('Autores similares a king:'), nl,
   forall(autor_similar(king, A), (write('  - '), write(A), nl)).
