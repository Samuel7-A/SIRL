% =====================================================
% SIRL - Sistema Inteligente de Recomendación de Libros
% Archivo: hechos.pl
% Descripción: Base de conocimiento con libros disponibles
% =====================================================

% libro(ID, Titulo, Genero, Autor).
libro(1, 'Clean Code', programacion, martin).
libro(2, 'The Pragmatic Programmer', programacion, hunt).
libro(3, 'Design Patterns', programacion, gamma).
libro(4, 'Introduction to Algorithms', algoritmos, cormen).
libro(5, 'Artificial Intelligence: A Modern Approach', inteligencia_artificial, russell).
libro(6, 'Dune', ciencia_ficcion, herbert).
libro(7, '1984', distopia, orwell).
libro(8, 'Brave New World', distopia, huxley).
libro(9, 'It', terror, king).
libro(10, 'The Shining', terror, king).
libro(11, 'The Lord of the Rings', fantasia, tolkien).
libro(12, 'Harry Potter', fantasia, rowling).
libro(13, 'Sapiens', historia, harari).
libro(14, 'A Brief History of Time', ciencia, hawking).
libro(15, 'The Great Gatsby', clasico, fitzgerald).

% genero_relacionado(Genero1, Genero2).
% Define géneros que se consideran similares entre sí
genero_relacionado(programacion, algoritmos).
genero_relacionado(algoritmos, programacion).
genero_relacionado(distopia, ciencia_ficcion).
genero_relacionado(ciencia_ficcion, distopia).
genero_relacionado(terror, fantasia).
genero_relacionado(fantasia, terror).
genero_relacionado(historia, ciencia).
genero_relacionado(ciencia, historia).

% autor_popular(Autor, Genero).
% Autores conocidos en un género
autor_popular(king, terror).
autor_popular(tolkien, fantasia).
autor_popular(orwell, distopia).
autor_popular(martin, programacion).
autor_popular(harari, historia).
