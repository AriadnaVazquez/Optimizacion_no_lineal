import sympy as sp
import re

def arreglar_entrada(texto):
    
    texto = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', texto)
    texto = texto.replace(')(', ')*(')
    return texto.replace('^', '**').lower()

def programa_calculadora():
    x = sp.symbols('x')
    
    while True:
        print("\n" + " " * 60)
        print("   CALCULADORA")
        print(" " * 60)
        
        entrada_usuario = input("Introduce f(x): ")
        
        try:
            expresion = arreglar_entrada(entrada_usuario)
            f = sp.sympify(expresion)
            
            # PASO 1: Derivada y Puntos Críticos
            f1 = sp.factor(sp.simplify(sp.diff(f, x)))
            print(f"\nf'(x) = {f1}")
            
            puntos = sp.solve(f1, x)
            
            p_reales = [p for p in puntos if p.is_real]
            
            print(f"\nPuntos críticos: {p_reales}")
            
            if not p_reales:
                print("No se encontraron puntos críticos reales.")
            else:
                # PASO 2: Evaluación
                for c in p_reales:
                    print(f"\n" + "-"*45)
                    print(f" ANALIZANDO PUNTO: x = {c}")
                    print("-"*45)
                    
                    hallado = False
                    for n in range(2, 11):
                        raw_der = sp.diff(f, x, n)
                        df_n = sp.factor(sp.simplify(raw_der))
                        
                        val = df_n.subs(x, c)
                        
                        print(f"Orden {n}: f^({n})(x) = {df_n}")
                        print(f"Evaluación: f^({n})({c}) = {val.evalf():.6f}")
                        
                        if val != 0:
                            if n % 2 == 0:
                                tipo = "Mínimo Local" if val > 0 else "Máximo Local"
                                print(f"\n>> {tipo} en x = {c}")
                            else:
                                print(f"\n>> Punto de inflexión en x = {c}")
                            
                            hallado = True
                            break
                        else:
                            print("Comentario: f=0, derivando de nuevo.")
                    
                    if not hallado:
                        print("No se obtuvo conclusión tras la décima derivada.")

        except Exception as e:
            print(f"\nERROR: Revisa la expresión. {e}")
        
        print("\n" + "="*60)
        if input("¿Quieres analizar otra función? (s/n): ").lower().strip() != 's':
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    programa_calculadora()