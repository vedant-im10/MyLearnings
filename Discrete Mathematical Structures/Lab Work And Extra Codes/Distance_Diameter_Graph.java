//
//  Create a program to find the distance and diameter of a graph G entered by the user.
//
//  Created by VEDANT on 28/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
class Graph3
{
	private static LinkedList<Integer> adj[];
	
	@SuppressWarnings("unchecked")
	public Graph3(int v)
	{
		adj = new LinkedList[v];
		for(int i=0;i<v;i++)
		{
			adj[i] = new LinkedList<Integer>();
		}
	}
	public void addEdge(int source, int destination)
	{
		adj[source].add(destination);
		adj[destination].add(source);
	}
	public int BFS(int source, int destination)
	{
		boolean visited[] = new boolean[adj.length];
		
		int parent[] = new int[adj.length];
		
		Queue<Integer> q = new ArrayDeque<Integer>();
		
		q.add(source);
		visited[source] = true;
		parent[source] = -1;
		
		while(!q.isEmpty())
		{
			int top = q.peek();
			if(top==destination)
			{
				break;
			}
			q.poll();

			for(int neighbour: adj[top])
			{
				if(!visited[neighbour])
				{
					visited[neighbour] = true;
					q.add(neighbour);
					parent[neighbour] = top;
				}
			}
		}
		int distance = 0;
		int current = destination;
		
		while(parent[current]!=-1)
		{
			current = parent[current];
			distance++;
		}
		return distance;
	}
}

class Distance_Diameter_Graph {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int v,e;
		System.out.print("Enter the number of vertices : ");
		v = sc.nextInt();
		System.out.print("Enter the number of edges : ");
		e = sc.nextInt();
		
		Graph3 g = new Graph3(v);
		
		System.out.println("Enter "+e+" edges :");
		
		for(int i=0;i<e;i++)
		{
			int source = sc.nextInt();
			int destination = sc.nextInt();
			g.addEdge(source, destination);
		}
		
		Set<Integer> list1 = new HashSet<>();
		for(int i=0;i<v;i++)
		{
			for(int j=i+1;j<v;j++)
			{
				int distance = g.BFS(i,j);
				System.out.println("Shortest Distance from Node "+i+" to Node "+j+" is "+distance);
				list1.add(distance);
			}
		}
		Iterator<Integer> it = list1.iterator();
		int max = 0;
		while(it.hasNext())
		{
			int x = it.next();
			if(x > max)
			{
				max = x;
			}
		}
		System.out.println("Diameter of the Graph is "+max);
		sc.close();
	}
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
