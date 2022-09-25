public class Queue<Item>
{
  //Protected
  protected Node first; //The first item in the queue
  protected Node last; //The last item in the queue
  protected int length; //The length of the queue

  //A node in the Queue
  protected class Node
  {
    protected Item item; //The element the node is holding
    protected Node next; //The next item in the queue

    public Node(Item new_item)
    {
      item = new_item; //Set the element that this node holds
      next = null; //Set the next node to 'null' by default
    }

    public Item get_item() { return item; }
    public void set_next(Node new_next) { next = new_next; }
    public Node get_next() { return next; }
  }

  //Public
  public boolean isEmpty() { return first == null; }
  public int length() { return length; }

  public void enqueue(Item item)
  {
    Node prev_last = last;
    last = new Node(item);

    if (isEmpty()) { first = last; }
    else { prev_last.set_next(last); }

    length ++;
  }

  public Item dequeue()
  {
    if (isEmpty())
    {
      return null;
    }
    else
    {
      Item item = first.get_item();
      first = first.get_next();
      length --;
      if (isEmpty()) { last = null; }
      return item;
    }
  }

  public static void main(String[] args)
  {
    Queue<int> q = new Queue<int>();
    while (!StdIn.isEmpty())
    {
      String item = StdIn.ReadString();
      if (!item.equals("-"))
      {
        q.enqueue(item);
      }
      else StdOut.print(q.dequeue() + " ");
    }
    StdOut.println("(" + q.length() + " left on queue)");
  }
}
