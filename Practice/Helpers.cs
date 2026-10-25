using System.Text.Json;
using System.Text.Json.Serialization;

// LeetCode's standard node types. The commented-out copies at the top of each
// Solution.cs stub are NOT needed: these are provided here.

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) {
        this.val = val;
        this.next = next;
    }
}

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

// JSON <-> node conversion so tests.json can describe lists and trees as plain arrays
// ([1,2,3] for lists, LeetCode level-order [1,null,2,3] for trees).

public class ListNodeConverter : JsonConverter<ListNode> {
    public override ListNode Read(ref Utf8JsonReader reader, Type t, JsonSerializerOptions o) {
        if (reader.TokenType == JsonTokenType.Null) return null;
        var vals = JsonSerializer.Deserialize<List<int>>(ref reader, o);
        ListNode head = null, tail = null;
        foreach (var v in vals) {
            var n = new ListNode(v);
            if (head == null) head = tail = n; else { tail.next = n; tail = n; }
        }
        return head;
    }

    public override void Write(Utf8JsonWriter w, ListNode value, JsonSerializerOptions o) {
        w.WriteStartArray();
        int guard = 0;
        for (var n = value; n != null && guard++ < 1_000_000; n = n.next) w.WriteNumberValue(n.val);
        w.WriteEndArray();
    }
}

public class TreeNodeConverter : JsonConverter<TreeNode> {
    public override TreeNode Read(ref Utf8JsonReader reader, Type t, JsonSerializerOptions o) {
        if (reader.TokenType == JsonTokenType.Null) return null;
        var vals = JsonSerializer.Deserialize<List<int?>>(ref reader, o);
        if (vals.Count == 0 || vals[0] == null) return null;
        var root = new TreeNode(vals[0].Value);
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        int i = 1;
        while (q.Count > 0 && i < vals.Count) {
            var cur = q.Dequeue();
            if (i < vals.Count && vals[i] != null) { cur.left = new TreeNode(vals[i].Value); q.Enqueue(cur.left); }
            i++;
            if (i < vals.Count && vals[i] != null) { cur.right = new TreeNode(vals[i].Value); q.Enqueue(cur.right); }
            i++;
        }
        return root;
    }

    public override void Write(Utf8JsonWriter w, TreeNode value, JsonSerializerOptions o) {
        var outList = new List<int?>();
        var q = new Queue<TreeNode>();
        q.Enqueue(value);
        while (q.Count > 0) {
            var n = q.Dequeue();
            if (n == null) { outList.Add(null); continue; }
            outList.Add(n.val);
            q.Enqueue(n.left);
            q.Enqueue(n.right);
        }
        while (outList.Count > 0 && outList[^1] == null) outList.RemoveAt(outList.Count - 1);
        JsonSerializer.Serialize(w, outList, o);
    }
}
