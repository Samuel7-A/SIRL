% =====================================================
% SIRL - Sistema Inteligente de Recomendación de Libros
% Archivo: hechos.pl
% Rol de Prolog: SOLO contiene conocimiento puro.
%   - Relaciones entre géneros
%   - Relaciones entre autores
%   - Datos de libros con enlace de compra
% Los libros son la "base de datos" que Prolog maneja.
% Python se encarga de la integración y el JSON.
% =====================================================

% --- RELACIONES ENTRE GÉNEROS ---
% genero_relacionado(G1, G2): si te gusta G1, también puede gustarte G2
genero_relacionado(ciencia_ficcion,    distopia).
genero_relacionado(distopia,           ciencia_ficcion).

genero_relacionado(programacion,       algoritmos).
genero_relacionado(algoritmos,         programacion).

genero_relacionado(historia,           ciencia).
genero_relacionado(ciencia,            historia).

genero_relacionado(ciencia_ficcion,    fantasia).
genero_relacionado(fantasia,           ciencia_ficcion).

genero_relacionado(algoritmos,         inteligencia_artificial).
genero_relacionado(inteligencia_artificial, algoritmos).

% --- RELACIONES ENTRE AUTORES ---
% autor_similar(A1, A2): si te gusta A1, también puede gustarte A2
autor_similar(herbert,   asimov).
autor_similar(asimov,    clarke).
autor_similar(clarke,    herbert).
autor_similar(king,      straub).
autor_similar(tolkien,   rowling).
autor_similar(rowling,   tolkien).
autor_similar(orwell,    huxley).
autor_similar(huxley,    orwell).
autor_similar(martin,    hunt).

% --- BASE DE LIBROS ---
% libro(ID, Titulo, Genero, Autor)

libro(1,  'Clean Code',                             programacion,            martin).
libro(2,  'The Pragmatic Programmer',               programacion,            hunt).
libro(3,  'Design Patterns',                        programacion,            gamma).
libro(4,  'Introduction to Algorithms',             algoritmos,              cormen).
libro(5,  'Artificial Intelligence Modern Approach',inteligencia_artificial, russell).
libro(6,  'Dune',                                   ciencia_ficcion,         herbert).
libro(7,  'Foundation',                             ciencia_ficcion,         asimov).
libro(8,  'Rendezvous with Rama',                   ciencia_ficcion,         clarke).
libro(9,  '1984',                                   distopia,                orwell).
libro(10, 'Brave New World',                        distopia,                huxley).
libro(11, 'It',                                     terror,                  king).
libro(12, 'The Shining',                            terror,                  king).
libro(13, 'The Lord of the Rings',                  fantasia,                tolkien).
libro(14, 'Harry Potter',                           fantasia,                rowling).
libro(15, 'Sapiens',                                historia,                harari).
libro(16, 'A Brief History of Time',                ciencia,                 hawking).
libro(17, 'The Great Gatsby',                       clasico,                 fitzgerald).
libro(18, 'Neuromancer',                            ciencia_ficcion,         gibson).
libro(19, 'Hyperion',                               ciencia_ficcion,         simmons).
libro(20, 'The Haunting of Hill House',             terror,                  jackson).
