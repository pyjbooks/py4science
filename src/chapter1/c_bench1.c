#include <stdio.h>
#include <windows.h>
#include <stdlib.h>

const int N = 10000;
const int M = 1000;
const int L = 10000;

int main(int argc, char** argv)
{
    int i, j, k;
    double a[M], S[N][L], x[N][M], y[M][L];
    LARGE_INTEGER start_pc, end_pc, freq_pc;

    /* ① 配列に値を設定 */
    srand(1);
    double rnd_max = (double) RAND_MAX;
    for (i=0; i<M; i++) {
        a[i] = (rnd_max*0.5 - rand()) / rnd_max;
    }
    for (i=0; i<N; i++) {
        for (j=0; j<M; j++) {
            x[i][j] = (rnd_max*0.5 - rand()) / rnd_max;
        }
    }
    for (i=0; i<M; i++) {
        for (j=0; j<L; j++) {
            y[i][j] = (rnd_max*0.5 - rand()) / rnd_max;
        }
    }
    for (i=0; i<N; i++) {
        for (j=0; j<L; j++) {
            S[i][j] = 0.0;
        }
    }
    
    /* ② 処理開始時の時間を計測 */
    QueryPerformanceFrequency( &freq_pc );
    QueryPerformanceCounter( &start_pc );

    /* ③ 行列演算処理(処理時間計測対象) 式(1-1)の処理 */
    for (i=0; i<N; i++) {
        for (j=0; j<L; j++) {
            for (k=0; k<M; k++) {
                S[i][j] += a[k]*x[i][k]*y[k][j];
            }
        }
    }
    
    /* ④ 処理終了時の時間を計測*/
    QueryPerformanceCounter( &end_pc );
    double sec_pc = (end_pc.QuadPart - start_pc.QuadPart) / (double)freq_pc.QuadPart;
    printf("計算時間 = %.3lf[ms]\n", sec_pc * 1000);

    /* ⑤ 最適化によりSの計算が省略されないように、計算後にランダム参照 */
    i = (int) (start_pc.QuadPart % N);
    j = (int) (end_pc.QuadPart % L);
    printf("S[%d][%d] = %.3lf\n", i, j, S[i][j]);

    return 0;
}

