import java.nio.file.Files
import java.nio.file.Paths

fun main() {
    val graphs: List<List<Int>> = Files.readAllLines(Paths.get("inputs/day10.txt")).map { it.trim().map { char -> char.toString().toInt() } }
    val n = graphs.size
    val m = graphs[0].size


    fun part1(graphs: List<List<Int>>): Int {
        val prev = mutableMapOf<Pair<Int, Int>, MutableSet<Pair<Int, Int>>>()
        val queue = ArrayDeque<Pair<Int, Int>>()
        var res = 0

        for (i in 0 until n) {
            for (j in 0 until m) {
                if (graphs[i][j] == 0) {
                    queue.add(Pair(i, j))
                    prev[Pair(i, j)] = mutableSetOf(Pair(i, j))
                }
            }
        }

        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            if(graphs[x][y] == 9) {
                res += prev[Pair(x, y)]?.size ?: 0
                continue
            }
            for (dx in -1..1) {
                for (dy in -1..1) {
                    if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) continue
                    val nx = x + dx
                    val ny = y + dy
                    if ((nx in 0 until n) && (ny in 0 until m) && (graphs[nx][ny] == 1 + graphs[x][y])) {
                        if (!prev.containsKey(Pair(nx, ny))) {
                            queue.addLast(Pair(nx, ny))
                            prev[Pair(nx, ny)] = mutableSetOf()
                        }
                        prev[Pair(nx, ny)]?.addAll(prev[Pair(x, y)] ?: emptySet())
                    }
                }
            }
        }
        return res
    }

    fun part2(graphs: List<List<Int>>): Int {
        val cnt = mutableMapOf<Pair<Int, Int>, Int>()
        val queue = ArrayDeque<Pair<Int, Int>>()
        var res = 0

        for (i in 0 until n) {
            for (j in 0 until m) {
                if (graphs[i][j] == 0) {
                    queue.add(Pair(i, j))
                    cnt[Pair(i, j)] = 1
                }
            }
        }

        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            if(graphs[x][y] == 9) {
                res += cnt[Pair(x, y)] ?: 0
                continue
            }
            for (dx in -1..1) {
                for (dy in -1..1) {
                    if ((dx == 0 && dy == 0) || (dx != 0 && dy != 0)) continue
                    val nx = x + dx
                    val ny = y + dy
                    if ((nx in 0 until n) && (ny in 0 until m) && (graphs[nx][ny] == 1 + graphs[x][y])) {
                        if (!cnt.containsKey(Pair(nx, ny))) {
                            queue.addLast(Pair(nx, ny))
                        }
                        cnt[Pair(nx, ny)] = (cnt[Pair(nx, ny)] ?: 0) + cnt[Pair(x, y)]!!
                    }
                }
            }
        }
        return res
    }

    println(part1(graphs))
    println(part2(graphs))
}