import java.util.Scanner


fun main() {
    val scanner = Scanner(System.`in`)
    val input: List<Long> = scanner.nextLine().split(" ").map{ it.toLong() }
    var cnt: Map<Long, Long> = input.groupingBy { it }.eachCount().mapValues { it.value.toLong() }

    val t = 75

    for (i in 0 until t) {
        val temp = mutableMapOf<Long, Long>()
        for ((k, v) in cnt) {
            if (k == 0L) temp[1] = temp.getOrDefault(1, 0) + v
            else if ( k.toString().length % 2 == 0) {
                val n = k.toString().length / 2
                val left = k.toString().substring(0, n).toLong()
                val right = k.toString().substring(n).toLong()
                temp[left] = temp.getOrDefault(left, 0L) + v
                temp[right] = temp.getOrDefault(right, 0L) + v
            } else {
                temp[k * 2024L] = temp.getOrDefault(k * 2024L, 0L) + v
            }
        }
        cnt = temp
    }
    println(cnt.values.sum())
}