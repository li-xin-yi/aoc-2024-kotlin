import java.nio.file.Files
import java.nio.file.Paths


fun main() {
    val nums: MutableList<Int> = Files.readAllLines(Paths.get("inputs/day09.txt")).first().map { it.toString().toInt()}.toMutableList()

    var cur = 0
    var res = 0L
    var last: Int = nums.size/2 * 2
    println(last)

    for ((i, num) in nums.withIndex()) {
        if (i % 2 == 0) {
            if (num == 0) break
            res += 1L * (i/2) * ((2* cur + num -1 ) * num / 2)
        } else {
            for (j in 0..<num) {
               while (last > i && nums[last] == 0) {
                   last -= 2
               }
                if (last <= i) break
                res += 1L * (cur + j) * (last / 2)
                nums[last] -= 1
        }
    }
    cur += num
    }

    println(res)
}
